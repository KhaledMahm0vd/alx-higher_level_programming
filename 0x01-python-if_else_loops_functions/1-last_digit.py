#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
sn = str(number)
last_num = int(sn[-1])
str_last = "Last digit of "
str_six = " and is less than 6 and not 0"
if last_num > 5:
    print("{}{} is {} and is greater than 5".format(str_last, number, sn[-1]))
elif last_num < 6 and last_num != 0:
    print("{}{} is {}{}".format(str_last, number, sn[-1], str_six))
else:
    print("{}{} is {} and is 0".format(str_last, number, sn[-1]))
