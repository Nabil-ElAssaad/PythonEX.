class Movie:
    """ This app has been developed by Nabil El Assaad  """

    def __init__(self, title, hero, heroine):
        self.title = title
        self.hero = hero
        self.heroine = heroine

    def info(self):
        print("Movie name is  : ", self.title)
        print("hera hero is  : ", self.hero)
        print("Movie heroine is  : ", self.heroine)


list_of_Movie = []
while True:
    title = input(" Enter Movie Name ")
    hero = input(" Enter Hero Name ")
    Heroine = input(" Enter heroine Name ")
    m = Movie(title, hero, Heroine)  # Create a Movie object with dynamic data
    list_of_Movie.append(m)
    print("Movie added too the list successfully")
    option = input("Do yo want to add more Movie [ Yes | No ]")
    if option.lower().strip() == "yes":
        continue
    elif option.lower().strip() == "no":
        break

print("All Movies Information")
for movie in list_of_Movie:
    print("-" * 25)
    movie.info()
