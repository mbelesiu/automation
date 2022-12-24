def isPhoneNumbe(text):
    if len(text) != 12:
        return False
    for i in range(0,3):
        if not text.isdecimal():
            return False