word = input("please enter a word\n")
subString = input("please enter a subString\n")
l = len(word)
i = word.find(subString) # Return -1 if word doesnt contain subString
count = 0
if i == -1:
    print("this {} is not found in {} ".format(subString, word))
while i != -1:
    count = count + 1
    print("this {} present in {} at index {} ".format(subString, word,i))
    i = word.find(subString,i+len(subString),l)

print("The number of occurrences is " , count  )

