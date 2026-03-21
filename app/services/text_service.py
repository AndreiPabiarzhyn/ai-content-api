import re


CORRECTION_RULES = [
    (r"\bi\b", "I"),
    (r"\bhas\b", "have"),
    (r"\ba apple\b", "an apple"),
    (r"\bdo not\b", "don't"),
]


def correct_text_logic(text: str) -> str:
    text = text.lower()

    for pattern, replacement in CORRECTION_RULES:
        text = re.sub(pattern, replacement, text)

    text = text.capitalize()

    return text

def simplify_text_logic(text: str) -> str:
    simplified = text

    simplified = simplified.replace("would like to", "want to")
    simplified = simplified.replace("purchase", "buy")
    simplified = simplified.replace("do not", "don't")

    return simplified
