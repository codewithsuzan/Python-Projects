email = input("Enter your email address: ")  # Example: s@g.np, sujan@gmail.com
has_space = False
has_uppercase = False
has_invalid_char = False

if len(email) >= 6:
    if email[0].isalpha():  # First character must be alphabetic
        if "@" in email and email.count("@") == 1:  # Only one '@' is allowed
            if email.endswith(".com") or email.endswith(".net") or email.endswith(".org") or email[-3] == "." or email[-4] == ".":  # Valid domain
                for char in email:
                    if char.isspace():  # No spaces allowed
                        has_space = True
                    elif char.isalpha() and char.isupper():  # No uppercase letters allowed
                        has_uppercase = True
                    elif not (char.isalnum() or char in "_@."):  # Invalid characters
                        has_invalid_char = True
                
                if has_space or has_uppercase or has_invalid_char:
                    print("Invalid email address: Contains spaces, uppercase letters, or invalid characters.")
                else:
                    print("Valid email address!")
            else:
                print("Invalid email address: Incorrect domain.")
        else:
            print("Invalid email address: Must contain exactly one '@'.")
    else:
        print("Invalid email address: Must start with a letter.")
else:
    print("Invalid email address: Must be at least 6 characters long.")
