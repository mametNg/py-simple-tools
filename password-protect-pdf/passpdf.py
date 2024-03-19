from PyPDF2 import PdfWriter, PdfReader
import getpass

# Making an instance of the PdfFileWriter class and storing it in a variable
writer = PdfWriter()


# Explicitly ask the user what the name of the original file is
pdf_name = input('Pleast type in the name of the pdf file suffixed with its extention: ')

# Making an instance of the PdfFileReader class with the original file as an argument
original_file = PdfReader(pdf_name)

# Copies the content of the original file to the writer variable
for page in range(len(original_file.pages)):
    writer.add_page(original_file.pages[page])

# Retrieve a preferred password from the user 
password = getpass.getpass(prompt = "Set a Password: ")

# Encrypt the copy of the original file
writer.encrypt(password)

# Opens a new pdf (write brinary permission) and writes the content of the 'writer' into it
with open('sample-secured.pdf', 'wb') as f:
    writer.write(f)
    f.close()
