text = input("Enter text you want mirrored: ")
tlen = len(text)
mirrored = ""
while tlen > 0:
    tlen -= 1
    mirrored += text[tlen]
print(mirrored)