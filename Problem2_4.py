"""
Problem 2_4:
random.random() generates pseudo-random real numbers between 0 and 1. But what
if you needed other random reals? Write a program to use random.random() but
generate list of random reals between 30 and 35. This is a simple matter of 
multiplication and addition. Print out the list (in list form).
"""
#%%
import random

def problem2_4():
    """ Make a list of 10 random reals between 30 and 35 """
    random.seed(70)
    num_lis = []
    for i in range(10):
        n = (random.random() * 5 + 30)
        num_lis.append(n)
    print(num_lis)

#%%
