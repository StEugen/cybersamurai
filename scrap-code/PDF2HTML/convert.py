from pdf2html import pdf2htmlEX

def convert_pdf_to_html(pdf_path, output_dir):
    pdf2htmlEX(pdf_path, output_dir)

# Replace 'input.pdf' with the path to your PDF file
pdf_path = 'input.pdf'

# Replace 'output_dir' with the directory where you want to save the HTML files
output_dir = 'output/'

convert_pdf_to_html(pdf_path, output_dir)
