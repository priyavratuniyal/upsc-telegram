from telegram import Update
from telegram.ext import CallbackContext
from utils import save_file, format_text_result_from_gradio, delete_image
from processors.image_to_text import get_text_from_image
from processors.pdf_to_text import extract_text_from_pdf


async def image_handler(update:Update, context:CallbackContext) -> None:
    """Handle image messages from user"""

    await update.message.reply_text('Thank you for uplodaing the image')
    await update.message.reply_text('Processing........')

    file = await update.message.photo[-1].get_file()

    file_path = await save_file(file)
    extracted_text = get_text_from_image(file_path)
    processed_text = format_text_result_from_gradio(extracted_text)
    delete_image(file_path)

    # await update.message.reply_text(file_path)
    await update.message.reply_text(f'Extracted text:\n{processed_text}')


async def pdf_handler(update:Update, context:CallbackContext) -> None:
    """Handle image messages from user"""

    await update.message.reply_text('Thank you for uplodaing the image')
    await update.message.reply_text('Processing........')
    file = await update.message.document.get_file()
    
    file_path= await save_file(file)
    extracted_text = extract_text_from_pdf(file_path)

    await update.message.reply_text(f'Extracted text:\n{extracted_text}')
    
