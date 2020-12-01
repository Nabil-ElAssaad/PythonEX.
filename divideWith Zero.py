numbers = [10.20,30,0,40,50]
for x in numbers:
    if x==0:
        print("We cant divide with Zero")
        continue
    print("100/{}={:.2F}".format(x,100/x))
