

from win32com.client import Dispatch

from catia.base.constants import ToleranceType

caa = Dispatch('CATIA.Application')

doc = caa.ActiveDocument

drawing_sheets = doc.Sheets

for drawing_sheet in drawing_sheets:
    print(f'----------------{drawing_sheet.Name}----------------')
    drawing_views = drawing_sheet.Views
    for drawing_view in drawing_views:
        if drawing_view.Name in ['Main View', 'Background View']:
            continue

        print(f'----------------{drawing_view.Name}----------------')
        GDTs = drawing_view.GDTs
        idx = 0
        while idx < GDTs.Count:
            GDT = GDTs.Item(idx + 1)
            print(GDT.GetTextRange(1, 0).Text, GDT.RowNumber)
            idx += 1


if __name__ == '__main__':
    pass
