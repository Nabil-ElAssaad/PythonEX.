word = input("Please enter a word\t")
# print("Character present at even position : " , word[0:len(word):2])
# print("Character present at even position : " , word[1:len(word):2])

index = 0
while index < len(word):
    print("Character present at even position : ", word[index], " at index ", index , end=" ")
    index = index + 2
    print()

index1 = 1
while index1 < len(word):
    print("Character present at odd position  : ", word[index1], " at index ", index1 , end="")
    index1 = index1 + 2
    print()
