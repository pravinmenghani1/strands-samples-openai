#!/usr/bin/env python3

import os
import io
import json
import base64
from openai import OpenAI
from PIL import Image
from pypdf import PdfReader
from strands import tool

@tool
def process_document(file_path: str) -> str:
    """
    Process a medical document (PDF or image) and extract its content using an OpenAI model.
    
    Args:
        file_path: Path to the document file (PDF or image)
        
    Returns:
        Extracted text content from the document
    """
    if not os.path.exists(file_path):
        return json.dumps({"error": f"File not found: {file_path}"})
    
    file_extension = os.path.splitext(file_path)[1].lower()
    
    try:
        # Use the LLM for all document types
        if file_extension == '.pdf':
            # For PDFs, try the LLM first, then fall back to traditional PDF extraction
            try:
                return _use_llm_for_document(file_path)
            except Exception as e:
                print(f"LLM processing failed, falling back to PDF extraction: {str(e)}")
                return _process_pdf_traditional(file_path)
        
        # Process image files with the LLM
        elif file_extension in ['.jpg', '.jpeg', '.png', '.tiff', '.bmp']:
            return _use_llm_for_document(file_path)
        
        else:
            return json.dumps({"error": f"Unsupported file format: {file_extension}"})
            
    except Exception as e:
        return json.dumps({"error": f"Error processing document: {str(e)}"})

def _process_pdf_traditional(file_path: str) -> str:
    """Extract text from a PDF file using PyPDF."""
    try:
        # Extract text directly from PDF
        reader = PdfReader(file_path)
        text = ""
        for page in reader.pages:
            text += page.extract_text() + "\n"
        
        # If text extraction yields meaningful content, return it
        if len(text.strip()) > 50:
            return text
        
        # If minimal text was extracted, the PDF might be scanned/image-based
        # In this case, we can't extract text using traditional methods
        return json.dumps({"error": "PDF appears to be image-based and requires an LLM for processing"})
        
    except Exception as e:
        return json.dumps({"error": f"Error processing PDF: {str(e)}"})

def _use_llm_for_document(file_path: str) -> str:
    """Use an OpenAI model for document processing."""
    try:
        client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])
        
        # Read file as base64
        with open(file_path, 'rb') as file:
            file_bytes = file.read()
        
        # Build the document part based on file extension
        file_extension = os.path.splitext(file_path)[1].lower()
        if file_extension == '.pdf':
            base64_data = base64.b64encode(file_bytes).decode('utf-8')
            document_part = {
                "type": "file",
                "file": {
                    "filename": os.path.basename(file_path),
                    "file_data": f"data:application/pdf;base64,{base64_data}"
                }
            }
        else:
            if file_extension in ['.jpg', '.jpeg']:
                media_type = 'image/jpeg'
            else:
                # OpenAI accepts PNG/JPEG, so convert other image formats (TIFF, BMP) to PNG
                if file_extension != '.png':
                    buffer = io.BytesIO()
                    Image.open(io.BytesIO(file_bytes)).save(buffer, format='PNG')
                    file_bytes = buffer.getvalue()
                media_type = 'image/png'
            base64_data = base64.b64encode(file_bytes).decode('utf-8')
            document_part = {
                "type": "image_url",
                "image_url": {"url": f"data:{media_type};base64,{base64_data}"}
            }
        
        response = client.chat.completions.create(
            model=os.getenv("OPENAI_MODEL_ID", "gpt-5-mini"),
            max_completion_tokens=16384,  # includes reasoning tokens
            messages=[
                {
                    "role": "user",
                    "content": [
                        document_part,
                        {
                            "type": "text",
                            "text": "Extract all text content from this medical document. Preserve the formatting as much as possible. Include all medical terms, diagnoses, medications, and treatments. Be thorough and capture all details from the document."
                        }
                    ]
                }
            ]
        )
        
        return response.choices[0].message.content
        
    except Exception as e:
        raise Exception(f"Error using the LLM for document processing: {str(e)}")
