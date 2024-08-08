import win32com.client


def open_file(filename):
    catia = win32com.client.Dispatch("CATIA.Application")
    # catia.Documents.Open(filename)
    doc = catia.ActiveDocument
    window = catia.ActiveWindow

    print([type(i).__name__ for i in catia.Documents])
    # 当前文件名
    print(doc.FullName)
    print(doc.DrawingRoot)


if __name__ == '__main__':
    filename = r'E:\develop\CatiaDimTools\test.CATDrawing'
    open_file(filename)
