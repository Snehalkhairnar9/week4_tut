# File          : week4_tut.py
# Author        : Snehal Khairnar
# Version       : v1.0
# Created Date  : 15/10/2021
# Description   : function exercise 1
# Licensing     : Snehal Khairnar, LYIT
# ----------------------------------

import platform

p = platform.uname()

print("machine :", p.machine)
print("system :", p.system)
print("node :", p.node)
print("version :", p.version)
print("processor :", p.processor)
print("release :", p.release)
