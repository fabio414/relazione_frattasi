s = input("Stringa: ")
s = s + "$"

rotazioni = []

for i in range(len(s)):
    rotazioni.append(s[i:] + s[:i])

for i in range(len(rotazioni)):
    for j in range(len(rotazioni) - 1):
        if rotazioni[j] > rotazioni[j + 1]:
            temp = rotazioni[j]
            rotazioni[j] = rotazioni[j + 1]
            rotazioni[j + 1] = temp