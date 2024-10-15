from gradio_client import Client, handle_file
import ast


def get_text_from_image(file:str)->str:
    client = Client("gokaygokay/Florence-2")
    result = client.predict(
            image=handle_file('small.jpg'),
            task_prompt="OCR",
            text_input=None,
            model_id="microsoft/Florence-2-large",
            api_name="/process_image"
    )
    return result