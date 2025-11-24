import re

def find_price(string):
    prices = re.findall(r"(?:\${1}\d+\.?\d+)", string)
    return prices

print(find_price("sir, that big mac will cost you about $1.25. no sir, you cant negotiate a big mac... i cant sell it to you for $0.50"))