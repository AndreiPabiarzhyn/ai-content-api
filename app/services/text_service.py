def correct_text_logic(text: str) -> str:
    original = text

    text = text.lower()

    text = text.replace("i ", "I ")
    text = text.replace("has", "have")
    text = text.replace("a apple", "an apple")

    text = text.capitalize()

    return text


def simplify_text_logic(text: str) -> str:
    simplified = text

    simplified = simplified.replace("would like to", "want to")
    simplified = simplified.replace("purchase", "buy")
    simplified = simplified.replace("do not", "don't")

    return simplified
