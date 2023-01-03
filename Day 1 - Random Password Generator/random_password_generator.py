import string  # library to get letters, numbers, and special_chars
import random  # library to choose random characters


def password_generator(pwd_length=24):
    """
    Function to generate random password
    Args:
        pwd_length (int, optional): decides the password length.
        Defaults to 24.

    Returns:
        string: random string(password)
    """

    # get all the english alphabets
    letters = string.ascii_letters

    # get the digits from 0-9
    digits = string.digits

    # get all the special chars
    special_chars = string.punctuation

    # combine them together
    combined_text = letters + digits + special_chars

    # generate a random string(password)
    password = "".join(random.sample(combined_text, pwd_length))
    return password


if __name__ == "__main__":
    print(password_generator())
    # randomly generated password: _f$.#;38mKIHhQ-P?kTs=*+U
