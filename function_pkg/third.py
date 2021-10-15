# File          : week4_tut.py
# Author        : Snehal Khairnar
# Version       : v3.0
# Created Date  : 15/10/2021
# Description   : function exercise 2
# Licensing     : Snehal Khairnar, LYIT
# ----------------------------------
import pprint
def option():
    print("Option 1 : LYIT courses and course code")
    print("Option 2 : edit course name")
    print("Option 3 : Pretty print data ")
    print("option 4 : Check if course name has comman in code")
option()
select = int(input("enter the option"))
print(select)

while select != 0:
    if select == 1:
        print("Bsc in Cyber security", "Msc in Devops", "Msc in Cyber security", "Msc in cloud computing", "Msc in data science")
        break

    elif select == 2:
        new_course_name = int(input("enter the course name"))
        print(new_course_name)
        break

    elif select == 3:
        print("Bsc in Cyber security and",
              "Msc in Devops and",
              "Msc in Cyber security and ",
              "Msc in cloud computing and",
              "Msc in data science")
        break










