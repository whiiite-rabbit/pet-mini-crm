def clean_text(text: str):
    """
    Clean a given text string by:
    - removing leading/trailing whitespace
    - filtering out unwanted characters
    - converting to lowercase
    - capitalizing the first letter

    :param text: Raw input string
    :return: Cleaned and normalized string
    """
    stripped_text = text.strip()
    unwanted_chars = "!@#*%<>/|№"
    cleaned_text = "".join([c for c in stripped_text if c not in unwanted_chars])
    normalized_text = cleaned_text.lower().capitalize()
    return normalized_text


if __name__ == "__main__":
    raw_text = "   ПРИВЕТ@, КАК# ДЕЛА!  "
    cleaned_text = clean_text(raw_text)
    print(cleaned_text)
