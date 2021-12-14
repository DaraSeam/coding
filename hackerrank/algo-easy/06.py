# convert 12hour format to 24hour format HH-MM-SSPM/AM
def timeConversion(s):
    a = ''
    format = s[-2:]
    hour = s[:2]
    min_sec = s[2:8]
    if format == "AM":
        if hour == "12":
            a = "00" + min_sec
        else:
            a = s[:-2]
    else: # if format is PM instead
        if hour == "12":
            a = s[:-2]
        else:
            a = str(int(hour)+12) + min_sec

    # print(str(int(hour)+12))
    # print(type("00" + min_sec))
    # print(s[:-2])
    print(type(a))

s = "07:05:45PM"
timeConversion(s)