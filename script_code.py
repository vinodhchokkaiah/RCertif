import os
import xlwt
import xlrd
from xlutils.copy import copy

excel_sheet = xlwt.Workbook(encoding="utf-8")
sheet1 = excel_sheet.add_sheet("Test Case Details")
sheet1.write(0, 0, "File Name")
sheet1.write(0, 1, "Requirement ID")
sheet1.write(0, 2, "Description")
sheet1.write(0, 3, "Status")


def read_req_from_test_files(test_case_files_path):

    i = 1

    for dir, folder, filenames in os.walk(test_case_files_path):
        for filename in filenames:
            if ".py" in filename:
                with open(test_case_files_path + filename, 'r') as file_read:
                    list2 = file_read.readlines()
                    for n in list2:
                        if "@Requirement Text:" in n:
                            sheet1.write(i, 0, filename)
                            sheet1.write(i, 1, n.split(":")[1])
                            sheet1.write(i, 2, n.split(":")[2])
                            i = i + 1

    excel_sheet.save("Report.xls")


def compare(path_to_reqs, path_to_test_reqs):

    read_req_from_test_files(test_case_files_path = "D:\\Mini_Project\\RCertif\\Test Files\\")

    req_data = []
    req_book = xlrd.open_workbook(path_to_reqs)
    p = req_book.sheet_names()
    for y in p:
       sh = req_book.sheet_by_name(y)
       for rownum in xrange(sh.nrows):
          req_data.append((sh.row_values(rownum)))

    test_req_data = []
    test_book = xlrd.open_workbook(path_to_test_reqs)
    p = test_book.sheet_names()
    for y in p:
       sh = test_book.sheet_by_name(y)
       for rownum in xrange(sh.nrows):
          test_req_data.append((sh.row_values(rownum)))

    row = 1
    rb = xlrd.open_workbook(path_to_test_reqs)
    wb = copy(rb)
    s = wb.get_sheet(0)
    for j in test_req_data:
        for i in req_data:
            if j[1] == i[0]:
                if j[2].rstrip() == i[1].rstrip():
                    s.write(row,3,'Same')
                    row = row + 1

                elif j[2].rstrip() != i[1].rstrip():
                    s.write(row,3,'Suspected')
                    row = row + 1

    wb.save(path_to_test_reqs)

if __name__ == "__main__":

    compare(path_to_reqs = "D:\\Mini_Project\\RCertif\\Requirements\\SRD_ECG.xlsx",
            path_to_test_reqs="D:\\Mini_Project\\RCertif\\Report.xls")
