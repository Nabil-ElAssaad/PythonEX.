Quantity =int(input("Enter number of students: "))
rec={}
i = 1
while i <= Quantity:
    name = input("Please enter a name \t")
    mark = input("Please enter a mark \t")
    rec[name] = mark
    i = i + 1

print("Name of Student", "\t", "% of marks")
for x,t in rec.items():
    print("\t", x, "\t\t\t", t)