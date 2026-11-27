
# MediVaani

## Medicine Information and Kannada Translator

MediVaani is a medicine information system designed to help users understand medicine information in Kannada.

The system aims to extract text from medicine images, identify the medicine, retrieve its information, translate it into Kannada, and provide voice output.

## Project Objectives

- Extract text from medicine images using OCR.
- Identify medicine names from extracted text.
- Provide medicine information in simple language.
- Translate medicine information into Kannada.
- Provide Kannada voice output.

## Technologies Used

- Python
- FastAPI
- Uvicorn
- Pillow
- Tesseract OCR
- Pytesseract

## Current Progress

- FastAPI backend setup
- Home endpoint
- Health-check endpoint
- Medicine image upload endpoint
- OCR text extraction from medicine images

## How to Run

1. Install Python.
2. Install the required Python packages:

   ```bash
   python -m pip install -r requirements.txt
   ```

3. Install Tesseract OCR separately.

4. Run the backend:

   ```bash
   python -m uvicorn main:app --reload
   ```

5. Open the API documentation:

   http://127.0.0.1:8000/docs

## Team Project

MediVaani is a college mini-project developed using Python and FastAPI.

## Disclaimer

MediVaani is intended to help users understand medicine information. It is not a substitute for professional medical advice.
