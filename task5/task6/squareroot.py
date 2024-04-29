import json
 json.open()

"""
    approx_sqrrt = x/2
    closer_approx_sqrrt = (approx_sqrrt + x/approx_sqrrt)/2
    while closer_approx_sqrrt != approx_sqrrt:
        approx_sqrrt = closer_approx_sqrrt
        closer_approx_sqrrt = (approx_sqrrt + x/approx_sqrrt)/2
    return approx_sqrrt
"""

square_root_x = square_root(x)
#print (f"The squareroot of {x} when calculated from the newton's equation is {square_root_x}")



"""
    approx = n/2
    closer = (approx + n/approx)/2
    while closer != approx:
        approx = closer
        closer = (approx + n/approx)/2
    return approx

    f(x)= 0 # step 1 is finding where the squareroot of x == 0
    f′(x0) #value of y when f == 0

    x1 = x0 – f(x0)/f'(x0)  # Newton's eqa

   #where x0 is the intial guess
   # This needs f′(x0) ≠ 0  in order for this to work
     
x0 is the initial value of x,
f(x0) is the value of the equation at initial value, and
f'(x0) is the value of the first order derivative of the equation or function at the initial value x0.
    
    guess is used

 def mySqrt(n):
newGuess=n/2
for i in range(50):
    newGuess=0.5*(newGuess + (n/newGuess))
return newGuess
"""




