import os
from telegram import File
import ast
import logging

UPLOAD_DIR = './user_data/uploads'
os.makedirs(UPLOAD_DIR, exist_ok=True)

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',level=logging.INFO)
logger = logging.getLogger(__name__)

async def save_file(file:File) -> str:
    """Save file from Telegram to local disk"""
    
    file_path = os.path.join(UPLOAD_DIR, file.file_id+ '.' + file.file_path.split('.')[-1])
    await file.download_to_drive(custom_path=file_path)
    return file_path

def format_text_result_from_gradio(text:str)->str:
    """Extract the final result from the text obtained from gradio"""

    ocr_output = ast.literal_eval(text[-2])
    # Access the value associated with the '<OCR>' key
    extracted_text = ocr_output['<OCR>']
    print(f'Extracted text: {extracted_text}')
    return extracted_text

def delete_image(file_path:str)->None:
    logger.info(f'Deleting the image at : {file_path}')
    os.remove(file_path)