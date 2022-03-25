import img2pdf
from PIL import Image
import os

img_path = 'C:/Users/Harsh/Downloads/result.jpg'

pdf_path = 'C:/Users/Harsh/Downloads/RESULT.pdf'

img2pdf = os.system("img2pdf C:/Users/Harsh/Downloads/result.jpg")

pdf_bytes = img2pdf.convert(img2pdf.filename)

file = open(pdf_path, "wb")

file.write(pdf_bytes)

img2pdf.close()

file.close()

print("SUCCESSFULLY MADE PDF FILE.")