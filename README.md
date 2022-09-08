# fibpy
the python code which calculates n-th Fibonacci number in O(log n)!!! 
#Basic consept
This code can calculate n-th Fibonacci number!
#How to run
Just run fib.py and input n.
The value will be displayed.
#Ristriction
Initially the n is ristricted upto 1000000000000000.
And the answer is displayed as mod 998244353.
More precisely, the maximam limititation is defined by the number of bit of n.
If you want to change the maximum, you should change the value of the default argument of fib(), maxBit.
#Order of run time
Be proportional to the maxBit. (O(maxBit))
If you choose the appropreate value, the run time will be O(log n).
