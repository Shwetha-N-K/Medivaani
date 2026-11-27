
from fastapi import FastAPI, UploadFile, File, HTTPException
from PIL import Image
import pytesseract
import re
from io import BytesIO

app = FastAPI(title="MediVaani API")

# Tesseract installation path
pytesseract.pytesseract.tesseract_cmd = (
    r"C:\Program Files\Tesseract-OCR\tesseract.exe"
)

@app.get("/")
def home():
    return {"message": "Welcome to MediVaani"}

@app.get("/health")
def health():
    return {"status": "Backend is running"}

def identify_medicine_name(text):
    lines = text.splitlines()

    for line in lines:
        # Find a line containing medicine strength
        if re.search(r"\d+\s*(mg|mcg|ml|g)\b", line, re.IGNORECASE):

            # Remove common medicine words
            name = re.sub(
                r"\b(tablets?|capsules?|syrup|injection|IP|USP|BP)\b",
                " ",
                line,
                flags=re.IGNORECASE
            )

            # Remove medicine strength
            name = re.sub(
                r"\d+\s*(mg|mcg|ml|g)\b",
                " ",
                name,
                flags=re.IGNORECASE
            )

            # Remove unwanted symbols
            name = re.sub(r"[^A-Za-z0-9 -]", " ", name)

            # Remove extra spaces
            name = re.sub(r"\s+", " ", name).strip()

            if name:
                return name

    return None


@app.post("/upload-medicine")
async def upload_medicine(file: UploadFile = File(...)):

    # Read uploaded image
    image_data = await file.read()

    try:
        # Convert uploaded bytes into an image
        image = Image.open(BytesIO(image_data))

        # Extract text using OCR
        extracted_text = pytesseract.image_to_string(image)
        medicine_name = identify_medicine_name(text)

    except Exception as e:
        raise HTTPException(
            status_code=400,
            detail="Unable to process the uploaded image"
        )

    return {
    "filename": file.filename,
    "extracted_text": text,
    "medicine_name": medicine_name,
    "message": "Medicine text extracted successfully"
}