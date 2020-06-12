import re

def caan_extractor(string):
    #returns list of strings of four digit numbers and only four digit numbers
    regex = r'\b\d{4}\b'
    return(re.findall(regex, string))


testString = input('Test String:')
if testString == "":
    testString = "1234, 12345, 0099 112233445566 67 77, "
print(caan_extractor(testString))
