import re

def is_phone_number(phone_number):
    numbers = re.findall(r"\(?\d{3}\)?[-, ]?\d{3}[-, ]?\d{4}", phone_number)
    return numbers
        
print(is_phone_number("Hello my name is vivianne and my phone number is 333-232-3403. my friends phone number is (333) 232 3403"))