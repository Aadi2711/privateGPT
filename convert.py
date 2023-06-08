import cv2
import pytesseract

input_dir = "image_path"
img = cv2.imread(input_dir,1)
result = pytesseract.image_to_pdf_or_hocr(img, lang-"eng", config-tessdata_dir_config)
f = open ("source_documents/searchabiePDF.pdf","w+b")
f.write(bytearray(result))
f. close ()