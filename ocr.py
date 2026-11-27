
from PIL import Image
import pytesseract

# Tesseract installation path
pytesseract.pytesseract.tesseract_cmd = (
    r"C:\Program Files\Tesseract-OCR\tesseract.exe"
)

# Open medicine image from project folder
image = Image.open("medicine.jpg")

# Extract text from image
text = pytesseract.image_to_string(image)

# Display extracted text
print("Extracted Medicine Information:")
print(text)
