import logging
logging.basicConfig(filename='example.txt' , level=logging.DEBUG)
logging.info("A new process came ")
try:
    x = int(input("please enter a number  "))
    y = int(input("please enter a number  "))
    z = x / y
    print("Result is " , z)
except ZeroDivisionError as msg:
    print("Cannot divide with Zero ")
    logging.exception(msg)
except ValueError as msg1:
    print("Please enter int value only")
    logging.exception(msg1)
logging.info("Request process done")

