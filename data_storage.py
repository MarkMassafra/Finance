from openpyxl import workbook

def export_to_excel(data, filename):

    workbook = Workbook()
    sheet  = workbook.active

    headers = data[0].keys
    sheet.append(headers)

    for row in data:
        sheet.append(list(row.values()))

    workbook.save(filename)