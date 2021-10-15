# File          : pythonproject.py
# Author        : Snehal Khairnar
# Version       : v1.0
# Created Date  : 08/10/2021
# Description   : Testing the functionality of List, Tuples
# Licensing     : Snehal Khairnar, LYIT
# ----------------------------------
import pprint

courses = ['Development and operation', 'Cyber security', 'cloud computing', 'artificial intelligence']
codes = ('Devops', 'cyber sec', 'cloud comp', 'ai')
course_codes = {'devops' : 1, 'cyber security' : 2, 'cloud computing' :3, 'artificial intelligence' : 4}
course = input("enter the course name ")
code = input("enter course code")

pp = pprint.PrettyPrinter(indent=4)
pp.pprint(course)

if 'cyber' in course or 'ai' in course or 'devops' in course or 'cloud' in course:
    print("exist")
else:
    print("not exist")


