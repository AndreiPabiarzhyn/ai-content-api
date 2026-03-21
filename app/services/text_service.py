def correct_text_logic(text: str) -> str:
    corrected = text.replace("i ", "I ")
    corrected = corrected.replace("has", "have")
    corrected = corrected.replace("a apple", "an apple")

    return corrected
