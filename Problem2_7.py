"""
Problem 2_7:
Heron's formula for computing the area of a triangle with sides a, b, and c is
as follows. Let s = .5(a + b + c) --- that is, 1/2 of the perimeter of the 
triangle. Then the area is the square root of s(s-a)(s-b)(s-c). You can compute
the square root of x by x**.5 (raise x to the 1/2 power). Use an input 
statement to get the length of the sides. Don't forget to convert this input 
to a real number using float(). Adjust your output to be just like what you
see below. Here is a run of my program:
problem2_7()
enter length of side one:3
enter length of side two:4
enter length of side three:5
Area of a triangle with sides 3.0 4.0 5.0 is 6.0
 
"""
#%%

def problem2_7():
    """ computes area of triangle using Heron's formula. """
    a = float(input("enter length of side one:"))
    b = float(input("enter length of side two:"))
    c = float(input("enter length of side three:"))
    s = ((.5)*(a+b+c))
    area = ((s*(s-a)*(s-b)*(s-c))**.5)
    print("Area of a triangle with sides",a,b,c,"is",area)
    
#%%
