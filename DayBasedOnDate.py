import datetime

my_date = datetime.datetime (2015 , 6 , 23)
my_Birthday = " my birthday in {0:%B %d,%Y} fell on {0:%A}".format(my_date)
print(my_Birthday)