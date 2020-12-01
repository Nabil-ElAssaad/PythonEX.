fWord = input("Please enter a first word\t")
sWord = input("Please enter a 2nd word\t")
output = ""
i = 0
while i < len(fWord):
    output = output + fWord[i]
    if i < len(sWord):
        output = output + sWord[i]
    i = i + 1
print(output)

# Program to merge characters of 2 strings into a single string by taking characters alternatively.
