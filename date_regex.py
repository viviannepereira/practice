import re
def find_year(string):
    dates = re.findall(r"(\d{2})/{1}(\d{2})/{1}(\d{2,4})", string)
    print(dates)
find_year("Hello my name is vivianne and my birthday is 11/12/2008. my friends birthday is 01/01/1995")