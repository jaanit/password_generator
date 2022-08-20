import random

lower = "abcdefghijklmnopqrstuvwxyz"
upper = lower.upper()
sym = "@!#_=-"
number = "0123456789"
passe =  lower  + sym + number + upper
len_passe = 8
passeword = "".join(random.sample(passe,len_passe))
print("ur passe is :", passeword)