import re

def capture_url(string):
    urls = re.findall(r"w{,3}\.{,1}[^\.][\w\d_.]+[^\.]\.{1}[\w\d]+", string)
    return urls

print(capture_url("www.abc.com is  a cool website, cool_website.tv is also a cool website"))