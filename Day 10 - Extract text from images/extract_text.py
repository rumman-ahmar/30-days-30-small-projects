from PIL import Image
from pytesseract import pytesseract

# include the following two lines if you haven't configured the environment variable
tesseract_path = r"C:\Program Files\Tesseract-OCR\tesseract.exe"  # location where you installed it
pytesseract.tesseract_cmd = tesseract_path

# open the image
image = Image.open("python-is-love.png")

# extract the text from the image
text = pytesseract.image_to_string(image)

# print extracted text
print(text)
