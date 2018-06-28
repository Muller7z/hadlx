
import math
import xlrd,xlsxwriter
from weifubo import cycle


def read_xlsx(filename):
    # 打开工作表
    workbook = xlrd.open_workbook(filename)
    sheetname = workbook.sheet_names
    print(sheetname)
    # 打开第一个sheet
    worlsheet = workbook.sheet_by_index(0)
    # 从sheet中获取数据：列col 行row
    col_B = worlsheet.col_values(0)
    col_C = worlsheet.col_values(2)
    # 切片：得到有用的数据
    return col_B[1:],col_C[1:]


def write_xlsx(rlist):
    workbook = xlsxwriter.Workbook("result.xlsx")
    worksheet = workbook.add_worksheet("newsheet")
    worksheet.write(1,1,"L")
    for i in range(len(rlist)):
        worksheet.write(i+2,1,rlist[i])
        print("写入第%s行数据"%i)
    workbook.close


if __name__ == "__main__":
    print("文件.xlsx必须在当前目录下，结果在result.xlsx中")
    filename = input("filename:")
    r = read_xlsx(filename)
    print(r)
    Tlist = r[0]
    hlist = r[1]
    Llist = []
    for i in range(len(Tlist)):
        T = Tlist[i]
        h = hlist[i]
        Llist.append(cycle(T,h))
    write_xlsx(Llist)
    
    


    



