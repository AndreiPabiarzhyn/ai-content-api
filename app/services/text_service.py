import re


CORRECTION_RULES = [
    (r"\bi\b", "I"),
    (r"\bhas\b", "have"),
    (r"\ba apple\b", "an apple"),
    (r"\bdo not\b", "don't"),
]

SIMPLIFY_RULES = [
    (r"\bwould like to\b", "want to"),
    (r"\bpurchase\b", "buy"),
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

    for pattern, replacement in SIMPLIFY_RULES:
        simplified = re.sub(pattern, replacement, simplified, flags=re.IGNORECASE)

    return simplified

def generate_text_logic(prompt: str) -> str:
    return f"Here is a short content idea about {prompt}. It can be useful and engaging for readers."