s = "AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC"

countA = 0
countT = 0
countC = 0
countG = 0
for char in s:
    if char == "A":
        countA += 1
    if char == "T":
        countT += 1
    if char == "C":
        countC += 1
    if char == "G":
        countG += 1
print(countA, countC, countG, countT)