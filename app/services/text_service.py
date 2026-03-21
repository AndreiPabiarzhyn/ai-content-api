def correct_text_logic(text: str) -> str:
    original = text

    text = text.lower()

    text = text.replace("i ", "I ")
    text = text.replace("has", "have")
    text = text.replace("a apple", "an apple")

    text = text.capitalize()

    return text
