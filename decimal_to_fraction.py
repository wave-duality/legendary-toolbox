'''
Given a decimal d, search for rational numbers that would round to d. Only print fully reduced fractions.
'''

from math import *

def relprime(i, j):
  return gcd(i, j) == 1
  
def ratl(d, num):
  #generate num instances of fractions
  denom = 1 
  found = 0
  suitable = []
  add = floor(d)
  d = d-add
  acc = len(str(d).split(".")[1])
  while found != num:
    for i in range(0, denom):
      if abs(i/denom - d) <= 5/10**(acc+1) and relprime(i, denom):
        suitable.append([i+add*denom, denom])
        found += 1
    denom += 1
  return suitable

def display(suitable):
  for i in suitable:
    print(str(i[0]) + "/" + str(i[1]))
  
