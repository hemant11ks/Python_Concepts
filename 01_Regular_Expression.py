import re


def validate_phone_number(phone_number):
    """
    Validate a phone number.

    Args:
    phone_number (str): The phone number to validate.

    Returns:
    bool: True if the phone number is valid, False otherwise.
    """
    pattern = r"^\d{3}-\d{3}-\d{4}$"
    if re.match(pattern, phone_number):
        return True
    else:
        return False


def extract_urls(text):
    """
    Extract URLs from a string.

    Args:
    text (str): The text to extract URLs from.

    Returns:
    list: A list of extracted URLs.
    """
    pattern = r"https?://\S+"
    urls = re.findall(pattern, text)
    return urls


def replace_special_characters(text):
    """
    Replace special characters with spaces.

    Args:
    text (str): The text to replace special characters in.

    Returns:
    str: The text with special characters replaced.
    """
    pattern = r"[^a-zA-Z0-9\s]"
    new_text = re.sub(pattern, " ", text)
    return new_text


def validate_email(email):
    """
    Validate an email address.

    Args:
    email (str): The email address to validate.

    Returns:
    bool: True if the email address is valid, False otherwise.
    """
    pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
    if re.match(pattern, email):
        return True
    else:
        return False


def search_pattern(text, pattern):
    """
    Search for a pattern in a string.

    Args:
    text (str): The text to search in.
    pattern (str): The pattern to search for.

    Returns:
    bool: True if the pattern is found, False otherwise.
    """
    if re.search(pattern, text):
        return True
    else:
        return False


def validate_email_address(email):
    """
    Validate an email address.

    Args:
    email (str): The email address to validate.

    Returns:
    None
    """
    pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
    if re.match(pattern, email):
        print("Email is valid")
    else:
        print("Email is invalid")


def extract_numbers(text):
    """
    Extract all numbers from a string.

    Args:
    text (str): The text to extract numbers from.

    Returns:
    None
    """
    pattern = r"\d+"
    numbers = re.findall(pattern, text)
    print("Numbers:", numbers)


def replace_pattern(text, pattern, repl):
    """
    Replace all occurrences of a pattern in a string.

    Args:
    text (str): The text to replace the pattern in.
    pattern (str): The pattern to replace.
    repl (str): The replacement string.

    Returns:
    None
    """
    new_string = re.sub(pattern, repl, text)
    print("New string:", new_string)


def main():
    print("Example 1: Validate phone number")
    phone_number = "123-456-7890"
    print(f"Phone number: {phone_number}, Valid: {validate_phone_number(phone_number)}")

    print("\nExample 2: Extract URLs")
    text = "Visit https://www.google.com for more information. You can also check out http://www.example.com."
    print(f"Text: {text}")
    print(f"Extracted URLs: {extract_urls(text)}")

    print("\nExample 3: Replace special characters")
    text = "Hello, world! This is a test."
    print(f"Text: {text}")
    print(f"Text with special characters replaced: {replace_special_characters(text)}")

    print("\nExample 4: Validate email")
    email = "example@example.com"
    print(f"Email: {email}, Valid: {validate_email(email)}")

    print("\nExample 5: Search pattern")
    text = "Hello, world!"
    pattern = "world"
    print(f"Text: {text}, Pattern: {pattern}, Found: {search_pattern(text, pattern)}")

    print("\nExample 6: Validate email address")
    email = "example@example.com"
    validate_email_address(email)

    print("\nExample 7: Extract numbers")
    text = "The numbers are 1, 2, and 3"
    extract_numbers(text)

    print("\nExample 8: Replace pattern")
    text = "Hello, world! Goodbye, world!"
    pattern = "world"
    repl = "earth"
    replace_pattern(text, pattern, repl)


if __name__ == "__main__":
    main()