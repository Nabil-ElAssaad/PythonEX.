city = input("please enter a city name\n")
sCity = city.strip()
listOfCities =["Amestrdam" , "Dubai" , "London" ,"Boston"]
while True:
 if sCity in listOfCities:
       print("{} in the list".format(city))
 else:
       print("{} not in the list, Please try again".format(city))
