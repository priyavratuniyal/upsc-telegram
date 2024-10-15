from gradio_client import Client, handle_file
import ast
import logging

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',level=logging.INFO)
logger = logging.getLogger(__name__)


def get_text_from_image(file_path:str)->str:
    logger.info("Processing the image to text in Gradio......\n")
    logger.info(f'File Path: {file_path}')
    client = Client("gokaygokay/Florence-2")
    result = client.predict(
            image=handle_file(file_path),
            task_prompt="OCR",
            text_input=None,
            model_id="microsoft/Florence-2-large",
            api_name="/process_image"
    )
    return result


def extract_text_from_image(file_path:str)->str:
    return "TEST text from IMAGE"

# print(HUGGING_FACE_KEY)
# print(get_text_from_image('AgACAgUAAxkBAANPZw2HDFYyDAdbvadgTshimWznzuoAAgrAMRvLY3BU9ZPxGqVvhFkBAAMCAAN5AAM2BA.jpg'))