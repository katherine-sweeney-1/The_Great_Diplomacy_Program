import math

# Check whether some values are NaN or not
print (math.isnan (56), type(56))
print (math.isnan (-45.34), type(-45.34))
print (math.isnan (+45.34))
print (math.isnan (math.inf))
print (math.isnan (float("nan")), type(float("nan")))
print (math.isnan (float("inf")))
print (math.isnan (float("-inf")))
print (math.isnan (math.nan))