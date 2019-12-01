```python
# factorial calculation
def fact(n):
    """Return the factorial of the given number."""
    r = 1
    while n>0:
        r = r*n
        n -= 1
    return r

print(fact.__doc__)
fact(4)
```

    Return the factorial of the given number.





    24




```python
# find maximum number
def maximum(*numbers): # (*)this to include more than one 
    if len(numbers) == 0:
        return None
    else:
        maxnum = numbers[0]
        for n in numbers[1:]:
            if n > maxnum:
                maxnum = n
        return maxnum
        
print(maximum(3,2,18))
print(maximum(3,2,8,-3,6,41,23,84,-6,-8,-25,5,56,-65))
```

    18
    84



```python
# how to sum parameters included in computing but not defined in this sum function
def example_sumf(x, y, **other):
    print("x: {0}, y: {1}, keys in 'other': {2}".format(x, y, list(other.keys())))
    other_tot = 0
    for k in other.keys(): # the loop will add the numbers for the ones we do not know yet the value
        other_tot += other[k]
    print("The total of values for the 'other' is {0}".format(other_tot))
    print("The total sum of values is {0}".format(other_tot+x+y))

example_sumf(2, y=1, rat=3, bar=4)
example_sumf(2, y=1, rat=3, bar=4, z=20, a=8)
```

    x: 2, y: 1, keys in 'other': ['rat', 'bar']
    The total of values for the 'other' is 7
    The total sum of values is 10
    x: 2, y: 1, keys in 'other': ['rat', 'bar', 'z', 'a']
    The total of values for the 'other' is 35
    The total sum of values is 38



```python
# fahrenheit to celsius conversion functions
def f_to_celsius(degrees_f):
    return (degrees_f - 32) * 5/9
def c_to_farenheit(degrees_c):
    return (degrees_c * 9/5) + 32

#we can use a dictionary to use them with data
t = {'F_to_C': f_to_celsius, 'C_to_F': c_to_farenheit}
print(t['C_to_F'](27))
print(t['F_to_C'](-10))
```

    80.6
    -23.333333333333332



```python
# fahrenheit to celsius conversion with lambda expression
t = {'F_to_C': lambda deg_f: (deg_f - 32) * 5/9, 
     'C_to_F': lambda deg_c: (deg_c * 9/5) + 32}
# inside a dictionary
# and testing
print(t['C_to_F'](27))
print(t['F_to_C'](-10))
```

    80.6
    -23.333333333333332



```python

```
