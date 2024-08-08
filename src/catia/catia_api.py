import json
import math

import pywintypes
from win32com.client import Dispatch

from catia.base.constants import CatTextFrameType, ToleranceType
from pycatia import catia
from pycatia.drafting_interfaces.drawing_document import DrawingDocument


class CatiaApi:

    def __init__(self):
        self._caa = Dispatch('Catia.Application')
        self.caa = catia(self._caa)

        self.dim_idx = 1

    def extract_data(self):
        pass

    def mark_dimension(self):
        dim_info = []
        doc: DrawingDocument = self.caa.active_document

        # 图纸sheet Collection
        drawing = doc.sheets

        # 窗口tab | sheet（图纸.1  图纸.2  ...）
        for sheet in drawing:
            views = sheet.views
            # 所有视图 （正视图  剖视图  ...）
            for view in views:
                for text in view.texts:
                    if text.name == 'TitleBlock_Text_DrawingNumber':
                        print(f'图号: ', text.text)
                    if text.name == 'TitleBlock_Text_RevisionNum':
                        print('检验计划版次: ', text.text)
                texts_obj = view.texts
                dimension = view.dimensions
                for idx, dimension in enumerate(dimension):
                    tol_info = dimension.get_tolerances()
                    value_obj = dimension.get_value()
                    # 尺寸标注的边界坐标（左下, 右下, 左上, 右上）
                    border = dimension.get_boundary_box()
                    pos_x, pos_y = self.calc_text_pos(*border)

                    # 在尺寸旁边插入标注文字气泡
                    _text = texts_obj.add(f'{self.dim_idx}', pos_x, pos_y)
                    _text.frame_type = CatTextFrameType.catCircle.value
                    self.dim_idx += 1

                    dim_info.append({
                        'name': dimension.name,  # 尺寸对象名称
                        'value': value_obj.value,  # 绘图尺寸的值（理论值）
                        'dimension_type': dimension.dim_type,  # 尺寸标注类型（Enum: CatDimType）
                        'value_frame': dimension.value_frame,  # 尺寸边框类型（Enum: CatDimFrame）
                        'boundary_pso': border,  # 尺寸边界坐标（根据坐标标记确定气泡位置）
                        'around_text': value_obj.get_bault_text(1),  # 尺寸标注四周环绕的文本信息（位置: 前、后、上、下）
                        'display_unit': value_obj.get_display_unit(1),  # 图纸显示单位
                        'format_unit': value_obj.get_format_unit(1),  # 格式化单位
                        'precision': value_obj.get_format_precision(1),  # 尺寸值的精度
                        'tolerance': {
                            'type': tol_info[0],  # 公差类型
                            'name': tol_info[1],  # 公差名称
                            'up_tolerance': tol_info[2],  # 上公差（字母数字类型）
                            'low_tolerance': tol_info[3],  # 下公差（字母数字类型）
                            'up_tolerance_value': tol_info[4],  # 上公差（数值类型）
                            'low_tolerance_value': tol_info[5],  # 下公差（数值类型）
                            'display_mode': tol_info[6],  # 公差显示模式
                        },
                    })
        print(json.dumps(dim_info, indent=4, ensure_ascii=False))
        return dim_info

    def mark_geometric_tolerance(self):
        doc: DrawingDocument = self.caa.active_document
        # 图纸sheet Collection
        drawing = doc.sheets

        # 窗口tab | sheet（图纸.1  图纸.2  ...）
        for sheet in drawing:
            views = sheet.views
            # 所有视图 （正视图  剖视图  ...）
            for view in views:
                if view.name in ['Main View', 'Background View']:
                    continue
                texts_obj = view.texts
                # for text in texts_obj:
                #     print(text)
                #     print(text.text)

                gdts = view.gdts
                for idx, gdt in enumerate(gdts):
                    row_number = gdt.row_number
                    # 上文本
                    upper_text = gdt.get_text_range(0, 0).text
                    # 下文本
                    lower_text = gdt.get_text_range(0, 1).text
                    # 公差类型
                    tolerance_type = ToleranceType(gdt.get_tolerance_type(row_number))
                    # 公差值
                    tolerance_value = gdt.get_text_range(row_number, 0).text
                    # 公差参考
                    symbol_a = gdt.get_text_range(row_number, 1).text
                    symbol_b = gdt.get_text_range(row_number, 2).text if symbol_a else ''
                    symbol_c = gdt.get_text_range(row_number, 3).text if symbol_b else ''
                    # 位置(标注左边中心点)
                    pos_x = gdt.x
                    pos_y = gdt.y

                    # 在尺寸旁边插入标注文字气泡
                    _text = texts_obj.add(f'{self.dim_idx}', pos_x, pos_y)
                    _text.frame_type = CatTextFrameType.catCircle.value
                    self.dim_idx += 1

                    print(f'公差上下文本值, 上文本: {upper_text}, 下文本: {lower_text}')
                    print(f'{tolerance_type} | {tolerance_value} | {symbol_a} | {symbol_b} | {symbol_c}')
                    print(gdt.get_reference_number(row_number))
                    print('--------------------------------')

    def mark_roughness(self):
        self.caa.display_file_alerts = False
        doc: DrawingDocument = self.caa.active_document
        # 图纸sheet Collection
        drawing = doc.sheets

        # 窗口tab | sheet（图纸.1  图纸.2  ...）
        for sheet in drawing:
            views = sheet.views
            # 所有视图 （正视图  剖视图  ...）
            for view in views:
                print(view)
                if view.name in ['Main View', 'Background View']:
                    continue
                # components = view.components
                # print(components, components.count)
                # for idx, component in enumerate(components):
                #     print(idx, component)

    @staticmethod
    def calc_text_pos(lbx, lby, rbx, rby, ltx, lty, rtx, rty, offset: float = 7):
        """
        Calculate the position of the text bounding box
        :param lbx: left bottom position x
        :param lby: left bottom position y
        :param rbx: right bottom position x
        :param rby: right bottom position y
        :param ltx: left top position x
        :param lty: left top position y
        :param rtx: right top position x
        :param rty: right top position y
        :param offset: offset of the text bounding box
        :return:
        """
        x1 = (rbx + lbx) / 2.0
        y1 = (rby + lby) / 2.0
        x2 = (ltx + rtx) / 2.0
        y2 = (lty + rty) / 2.0
        distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
        offset_x = (x2 - x1) * offset / distance
        offset_y = (y2 - y1) * offset / distance
        return offset_x + x2, offset_y + y2


if __name__ == '__main__':
    CatiaApi().mark_roughness()
