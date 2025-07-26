import os

import dotenv
import google.generativeai as genai


def _make_request(
    prompt: str, temperature: float = 0.8, model: str = "gemini-2.5-flash-lite"
):
    """
    Currently extremely simple and includes no retry logic.
    """
    # 1. Configure the library with your API key
    genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

    # 2. Select the Gemini model
    model = genai.GenerativeModel(model)

    # 3. Send the prompt and get a response
    response = model.generate_content(
        prompt, generation_config={"temperature": temperature}
    )

    # 4. Return the text content of the response
    return response.text


def get_gemini_response(
    prompt: str, temperature: float = 0.8, model: str = "gemini-2.5-flash-lite"
):
    return _make_request(prompt, temperature, model)


def gemini_describe_image(
    image_url: str, temperature: float = 0.01, model: str = "gemini-2.5-flash-lite"
):
    """
    Currently just describe image on its own. There are many possible
    improvements to consider making, e.g. passing in the post text or
    other context and describing the image and post text together.
    """
    # Gemini does not support image URLs directly, so we need to download the image first
    # and then upload it to the API. This is a placeholder for that functionality.
    # For now, we will just return a dummy response.
    return "This is a placeholder for the image description."


if __name__ == "__main__":
    dotenv.load_dotenv()
    print(
        get_gemini_response(
            "Provide me a digest of world news in the last 2 hours. Please respond with links to each source next to the claims that the source supports."
        )
    )
