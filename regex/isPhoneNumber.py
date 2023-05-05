import re

phoneNumRegex = re.compile(r'(\d\d\d)?-?(\d\d\d-\d\d\d\d)')
mo = phoneNumRegex.search('My number is 503-550-7997')
mo2 = phoneNumRegex.search('My number is 550-7997')
print('Phone number found: ' + mo.group())
print(mo.group(1))
print(mo.group(2))
print(mo.group(0))
print(mo.group())
areaCode, mainNumber = mo.groups()
print(areaCode)
print(mainNumber)
print("Mo2: " + mo2.group())