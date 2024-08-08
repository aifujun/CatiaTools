import math

from pycatia import catia


def calc_text_pos(x1, y1, x2, y2, offset: float = 7, reverse: bool = False):
    """
    计算A，B两点延长线上相距A或B距离offset点坐标
    :param x1: A点x坐标
    :param y1: A点y坐标
    :param x2: B点x坐标
    :param y2: B点y坐标
    :param offset: 所求点距A或B点距离
    :param reverse: true: 所求点在BA延长线上； false: 所求点在AB延长线上
    :return:
    """
    x12 = x2 - x1
    y12 = y2 - y1
    distance = math.sqrt(x12 ** 2 + y12 ** 2)
    offset_x = x12 * offset / distance
    offset_y = y12 * offset / distance
    if reverse:
        return x1 - offset_x, y1 - offset_y
    return offset_x + x2, offset_y + y2


if __name__ == '__main__':
    print(calc_text_pos(0, 0, 1, 1, math.sqrt(2)))
    print(calc_text_pos(1, 1, 0, 0, math.sqrt(2)))
    # print(calc_text_pos(0, 0, 1, -1, math.sqrt(2)))
    # print(calc_text_pos(0, 0, -1, 1, math.sqrt(2)))
    # print(calc_text_pos(0, 0, -1, -1, math.sqrt(2)))
    # caa = catia()
    # print(caa.active_document)
