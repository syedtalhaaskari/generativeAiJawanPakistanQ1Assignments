# Write a function called is_valid_email  that takes an email address as an argument and returns True/False depending on whether it is a valid email address.
# Check rules:
# Must contain at least 1 character before the at symbol
# Must contain an @ symbol
# Must have at-least 1 character after the @ symbol and before the period(.)
# Must contain at least 1 character after the last period(.).
# Maximum 256 characters
# Must start with a letter or a number

# hint: use if statement 6 times to check each rule. if any one rule failed return false

def is_valid_email(email):
    try:
        email_length = len(email)
        split_at = email.split('@')
        split_period = email.split('.')
        
        if len(split_at[0]) > 0 and len(split_at) > 1 and split_at[1][0] != '.' and len(split_period) > 1 and len(split_period[-1]) > 0 and email_length < 256 and email[0].isalnum():
            return True
        return False
    except:
        return False

while True:
    email = input('Enter something but not "0": ')
    if email == '0':
        break
    print(is_valid_email(email))
    

