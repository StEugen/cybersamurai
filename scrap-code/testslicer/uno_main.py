import subprocess

def split_docx(input_file, start_page, end_page, output_file):
    pdf_file = input_file.replace('.docx', '.pdf')
    subprocess.run(['unoconv', '-f', 'pdf', input_file])

    subprocess.run(['pdftk', pdf_file, 'cat', f'{start_page}-{end_page}', 'output', output_file])

    subprocess.run(['rm', pdf_file])

if __name__ == "__main__":
    input_file = 'input.docx'
    start_page = 1
    end_page = 5
    output_file = 'output.docx'
    split_docx(input_file, start_page, end_page, output_file)
