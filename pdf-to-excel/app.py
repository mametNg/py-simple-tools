import aspose.pdf as ap

input_pdf = "sample.pdf"
output_pdf =  "result.xlsx"

document = ap.Document(input_pdf)
save_option = ap.ExcelSaveOptions()
document.save(output_pdf, save_option)

# =================================================================================
# # Import the required Module
# import tabula
# # Read a PDF File
# df = tabula.read_pdf("cc0b4132-d4e6-49d3-9cea-735219c30457.pdf", pages='all')[0]
# # convert PDF into CSV
# tabula.convert_into("cc0b4132-d4e6-49d3-9cea-735219c30457.pdf", "iplmatch.xlsx", output_format="xlsx", pages='all')
# print(df)
# =================================================================================
# import tabula
# import pandas as pd


# def pdf_to_excel(pdf_file_path, excel_file_path):
#     # Read PDF file
#     tables = tabula.read_pdf(pdf_file_path, pages='all')

#     # Write each table to a separate sheet in the Excel file
#     with pd.ExcelWriter(excel_file_path) as writer:
#         for i, table in enumerate(tables):
#             table.to_excel(writer, sheet_name=f'Sheet{i+1}')


# pdf_to_excel('cc0b4132-d4e6-49d3-9cea-735219c30457.pdf', 'path_to_excel_file.xlsx')