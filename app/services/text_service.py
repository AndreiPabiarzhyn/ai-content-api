import re


def correct_text_logic(text: str) -> str:
    text = text.lower()

    text = re.sub(r"\bi\b", "I", text)
    text = re.sub(r"\bhas\b", "have", text)
    text = re.sub(r"\ba apple\b", "an apple", text)

    text = text.capitalize()

    return text


def simplify_text_logic(text: str) -> str:
    simplified = text

    simplified = simplified.replace("would like to", "want to")
    simplified = simplified.replace("purchase", "buy")
    simplified = simplified.replace("do not", "don't")

    return simplified
