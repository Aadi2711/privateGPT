import os
import io
from pdfminer.converter import TextConverter
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.pdfpage import PDFPage
from pdfminer.layout import LAParams

# Function to extract text from a PDF and store it in a text file
def extract_text_from_pdf(input_pdf_path, output_txt_folder):

    output_txt_path = os.path.join(output_txt_folder, "output.txt")

    with open(input_pdf_path, 'rb') as pdf_file:
        resource_manager = PDFResourceManager()
        fake_file_handle = io.StringIO()
        converter = TextConverter(resource_manager, fake_file_handle, laparams=LAParams(all_texts=True))
        page_interpreter = PDFPageInterpreter(resource_manager, converter)

        with open(output_txt_path, "w", encoding="utf-8") as output_file:
            for page in PDFPage.get_pages(pdf_file):
                page_interpreter.process_page(page)

            text = fake_file_handle.getvalue()
            text = text.replace('\n\n', '\n')
            output_file.write(text)

        # Close the resources
        converter.close()
        fake_file_handle.close()

def main():
    # Path to the input PDF
    input_pdf_path = "image_path/Pro.pdf"

    # Folder to store the output text file
    output_txt_folder = "source_documents"
    extract_text_from_pdf(input_pdf_path, output_txt_folder)

if __name__ == "__main__":
    main()
