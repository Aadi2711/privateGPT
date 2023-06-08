import os
from PIL import Image
import pytesseract
from PyPDF2 import PdfWriter, PdfReader

pdf_path = "inpath/6891-000-27-45-J314_0.pdf"
temp_dir = "image_path/"

from pdf2image import convert_from_path

images = convert_from_path(pdf_path)

image_files = []
for i, image in enumerate(images):
    image_path = os.path.join(temp_dir, f"page_{i+1}.png")
    image.save(image_path, "PNG")
    image_files.append(image_path)

extracted_texts = []
for image_file in image_files:
    image = Image.open(image_file)
    text = pytesseract.image_to_string(image)
    extracted_texts.append(text)



file = open('source_documents/model1.txt','w')
for text in extracted_texts:
    file.write(text+"\n")
file.close()
# pdf_writer = PdfWriter()

# for i, image_file in enumerate(image_files):
#     image = Image.open(image_file)
#     text = pytesseract.image_to_string(image)
#     # Create a new PDF page
#     if str(b'%%EOF') in text:
#         break
#     pdf_page = PdfReader(image_file)
#     # Add the PDF page to the PDF document
#     pdf_writer.addPage(pdf_page.getPage(0))

# output_pdf_path = "source_documents/B224-TENDER_DOC-B224-000-81-41-CP-T-8102_A_RenditionFile.pdf"
# with open(output_pdf_path, "wb") as output_pdf:
#     pdf_writer.write(output_pdf)

for image_file in image_files:
    os.remove(image_file)

print("PDF generation complete!")
