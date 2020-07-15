#!/usr/bin/env python
#_*_ coding: utf8 _*_
import math
from colorama import *
import time
#tamaño
n = 14
init()
for y in range(n, -n, -1):
	for x in range(-n, n):
		#ecuación
		if ((x**2) + ((5*y/4) - math.sqrt(4*abs(x)))**2) <= n**2:
			time.sleep(0.001)
			print(Fore.RED + "0", end=" ")
		else:
			print(Fore.WHITE + "1", end=" ")
	print("")
