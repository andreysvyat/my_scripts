import sys

from PyPDF2 import \
    PdfFileReader as pdf_reader, \
    PdfFileWriter as pdf_writer

SRC_FILE_PATH = sys.argv[1]
DES_FILE_PATH = sys.argv[2] if len(sys.argv) > 2 else "./new_file.pdf"


def copy_two_pages(pdf_path):
    with open(pdf_path, 'rb') as src_file, open(DES_FILE_PATH, 'wb') as dest_file:
        src_pdf = pdf_reader(src_file)

        dest_pdf = pdf_writer()
        dest_pdf.add_page(src_pdf.getPage(0))
        dest_pdf.add_page(src_pdf.getPage(1))
        dest_pdf.write(dest_file)


print(copy_two_pages(SRC_FILE_PATH))
