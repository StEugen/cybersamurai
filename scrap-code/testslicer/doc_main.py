from docx2python import docx2python

def extract_text(paragraph):
    if isinstance(paragraph, list):
        return ''.join(sub_paragraph['text'] for sub_paragraph in paragraph if isinstance(sub_paragraph, dict))
    else:
        return paragraph['text']

def split_docx(docx_file, start_page, end_page, output_file_prefix):
    doc_result = docx2python(docx_file)

    total_pages = len(doc_result.body)
    if start_page < 1:
        start_page = 1
    if end_page > total_pages:
        end_page = total_pages

    extracted_text = ""
    for page_num in range(start_page - 1, end_page):
        for paragraph in doc_result.body[page_num]:
            extracted_text += extract_text(paragraph)


    with open(f"{output_file_prefix}_pages_{start_page}_to_{end_page}.txt", "w") as output_file:
        output_file.write(extracted_text)

split_docx("input.docx", 2, 5, "output")


