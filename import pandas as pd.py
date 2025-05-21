import re

def validate_string_format(data_list, pattern):
    """
    Validates if each string in a list matches a given regular expression pattern.

    Args:
        data_list (list): A list of strings to validate.
        pattern (str): The regular expression pattern to match.

    Returns:
        list: A list of booleans, where True indicates the string matches the pattern,
              and False otherwise.
    """
    validation_results = []
    for item in data_list:
        if isinstance(item, str) and re.fullmatch(pattern, item):
            validation_results.append(True)
        else:
            validation_results.append(False)
    return validation_results

# Example Usage:
# Validate email addresses
email_data = ["test@example.com", "user.name@sub.domain.co", "invalid-email", "another@.com", 123]
email_pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
email_validation = validate_string_format(email_data, email_pattern)
print(f"Email Validation Results: {email_validation}")

# Validate phone numbers (e.g., XXX-XXX-XXXX)
phone_data = ["123-456-7890", "987.654.3210", "abc-def-ghi", "1234567890"]
phone_pattern = r"^\d{3}-\d{3}-\d{4}$"
phone_validation = validate_string_format(phone_data, phone_pattern)
print(f"Phone Validation Results: {phone_validation}")

# Validate alphanumeric strings (e.g., contains only letters and numbers)
alphanum_data = ["abc123", "ABCDEF", "12345", "a b c", "special!"]
alphanum_pattern = r"^[a-zA-Z0-9]+$"
alphanum_validation = validate_string_format(alphanum_data, alphanum_pattern)
print(f"Alphanumeric Validation Results: {alphanum_validation}")