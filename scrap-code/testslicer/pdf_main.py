import os
from tempfile import TemporaryDirectory
from pdf2image import convert_from_path

def split_document(input_path, output_dir, page_ranges):
    split_documents = []

    images = convert_from_path(input_path)

    for i, (start, end) in enumerate(page_ranges, start=1):
        output_path = os.path.join(output_dir, f"split_{i}.pdf")
        selected_pages = images[start-1:end]
        selected_pages[0].save(output_path, save_all=True, append_images=selected_pages[1:], quality=100)
        split_documents.append(output_path)

    return split_documents

if __name__ == "__main__":
    input_document_path = "input.pdf"
    output_directory = "output"
    page_ranges = [(1, 3), (4, 6)]

    os.makedirs(output_directory, exist_ok=True)

    split_documents = split_document(input_document_path, output_directory, page_ranges)

    print("Split documents:")
    for document in split_documents:
        print(document)
