from typing import Final
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
import logging
from handlers import pdf_handler, image_handler



TELEGRAM_TOKEN: Final = '8115249055:AAHCEHdCP-9Q4T2RRRAbzznz4BzyaJQ2f6s'
BOT_USERNAME: Final = '@upsc_test_bot'


# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',level=logging.INFO)
logger = logging.getLogger(__name__)


# Commands
async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f'Hello there, I am Upsc bot')

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f'How can I help you?')

async def custom_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f'This is a custom command')

async def image_upload_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f'Please upload an image')


# Handle Responses
def handle_response(text: str) -> str:
    processed: str = text.lower()

    if 'hello' in processed:
        return 'Hello there!'
    
    if 'bye' in processed:
        return 'Goodbye!'
    
    if 'thank you' in processed:
        return 'You are welcome!'

    return 'I am sorry, I did not understand that'


async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message_type: str = update.message.chat.type
    text: str = update.message.text

    print(f'User ({update.message.chat.id}) in {message_type}: "{text}"')
    if message_type == 'group':
        if BOT_USERNAME in text:
            new_text: str = text.replace(BOT_USERNAME, '').strip()
            response: str = handle_response(new_text)
        else:
            return
    else:
        response: str = handle_response(text)

    print('Bot said: ', response)
    await update.message.reply_text(response)

async def error(update: Update, context: ContextTypes.DEFAULT_TYPE):
    logger.warning(f'Update {update.message.text} caused error {context.error}')


def main():
    return 'main hello'




if __name__ == '__main__':
    print('Starting the bot.....')
    app = Application.builder().token(TELEGRAM_TOKEN).build()


    # Commands
    app.add_handler(CommandHandler('start', start_command))
    app.add_handler(CommandHandler('help', help_command))
    app.add_handler(CommandHandler('custom', custom_command))


    # Messages
    app.add_handler(MessageHandler(filters.TEXT, handle_message))
    app.add_handler(MessageHandler(filters.PHOTO, image_handler))
    app.add_handler(MessageHandler(filters.Document.MimeType("application/pdf"), pdf_handler))

    # Error
    app.add_error_handler(error)


    # Polling
    print("Polling......")
    app.run_polling(poll_interval=3)