import json
from typing import List

from data_models import MisleadingTag, Post
from note_writer.llm_util import get_gemini_response


def get_misleading_why_tags(post_text: str):
    """
    Given a post's text, returns a list of reasons why the post may be misleading.
    """
    misleading_why_tags_prompt = f"""
    A post on X says:
    {post_text}
    
    Why might this post be misleading?
    Your response must be a JSON list of strings.
    """.strip()

    gemini_response_str = get_gemini_response(misleading_why_tags_prompt)

    try:
        misleading_why_tags = json.loads(gemini_response_str)["misleading_tags"]
        return [MisleadingTag(tag) for tag in misleading_why_tags]
    except json.JSONDecodeError:
        print(f"Could not parse JSON from response: {gemini_response_str}")
    return []
