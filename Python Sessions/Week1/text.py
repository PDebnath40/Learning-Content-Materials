# This is simple interest for given values of p, r , t
def SI(p,r,t):
    si = p*r*t/100
    return si

'''
compund interest
'''

def CI(p,r,t):
    ci = p*(1 + r/100)**t
    return ci



# Create the following set of the functions:
# SUM(a,b), SUB(a,b), MULT(a,b), POW(a,b)
# Qroots(a,b,c), F_grav(m1,m2,r)
# the open a new jupyter note book and call this text file in jupyter notebook and perform
# hint: import text 

def SUM(a,b):
   s=a+b
   return s

def SUB(a,b):
   s=a-b
   return s

def MULT(a,b):
   s=a*b
   return s

def POW(a,b):
   s=a**b
   return s

def qroot(a,b,c):
  x1= (-b+(b**2-4*a*c)**0.5)/2*a
  x2= (-b-(b**2-4*a*c)**0.5)/2*a
  return x1, x2

def F_grav(m1,m2,r):
  f=6.67*10**(-27)*m1*m2/r**2
  return f
    