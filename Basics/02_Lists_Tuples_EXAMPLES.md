```python
x=[[1,2,[3,4],5],6]
len(x)
# only the two elemetns have been detected and not the nested ones
```




    2




```python
x[-2]
```




    [1, 2, [3, 4], 5]




```python
x[1]
```




    6




```python
x[1:2]
```




    [6]




```python
# adding a list to the end of a list
x=[1,2,3,4]
x[len(x):]=[5,6,7]
x
```




    [1, 2, 3, 4, 5, 6, 7]




```python
# adding a list at the start of a list
x[:0]=[-1,0]
x
```




    [-1, 0, 1, 2, 3, 4, 5, 6, 7]




```python
# remove elements from a list
x[1:-1]=[] # removes elements from position 1 to "6" -1 position form end
x
```




    [-1, 7]




```python
x=[1,2,3]
x.append("four")
x
```




    [1, 2, 3, 'four']




```python
# append lists
y=[5,6,7]
x.extend(y)
x
```




    [1, 2, 3, 'four', 5, 6, 7]




```python
x.insert(4, 4)
x
```




    [1, 2, 3, 'four', 4, 5, 6, 7]




```python
x.insert(0, 'start')
x
```




    ['start', 1, 2, 3, 'four', 4, 5, 6, 7]




```python
del x[0]
x
```




    [2, 3, 'four', 4, 5, 6, 7]




```python
x.remove('four')
x
```




    [2, 3, 4, 5, 6, 7]




```python
x.reverse()
x
```




    [7, 6, 5, 4, 3, 2]




```python
x.sort()
x
```




    [2, 3, 4, 5, 6, 7]




```python
y=x[:] # clone a list
y.reverse()
y
```




    [7, 6, 5, 4, 3, 2]




```python
x
```




    [2, 3, 4, 5, 6, 7]




```python
x=["A", "Zuzzorellone", "Beta", "W", "Kakkazza"]
x.sort()
x
```




    ['A', 'Beta', 'Kakkazza', 'W', 'Zuzzorellone']




```python
# function to sort by lenght of words
def compare_num_of_chars(x):
    return len(x)
x.sort(key=compare_num_of_chars)
print(x)
```

    ['A', 'W', 'Beta', 'Kakkazza', 'Zuzzorellone']



```python
z=y + x
z
```




    [7, 6, 5, 4, 3, 2, 'A', 'W', 'Beta', 'Kakkazza', 'Zuzzorellone']




```python
z = ['null']*4
z
```




    ['null', 'null', 'null', 'null']




```python
z = [1,2,3]*6
z
```




    [1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3]




```python
min(x)
```




    'A'




```python
max(x)
```




    'Zuzzorellone'




```python
x=[[1,2],[3,4],[5,6]]
x[0]
```




    [1, 2]




```python
x[0][1]
```




    2




```python
x[1]
```




    [3, 4]




```python
# Tuples
x=3
y=2
t=(x+y,x*y,x/y)
tuple=t+(t*3)
tuple
```




    (5, 6, 1.5, 5, 6, 1.5, 5, 6, 1.5, 5, 6, 1.5)




```python
# list
x=3
y=2
t=[x+y,x*y,x/y]
t
```




    [5, 6, 1.5]




```python
x, y, z, t = 1, 2, 3, 4
print(x,y,y*z,z/t)
```

    1 2 6 0.75



```python
# nice to split text
list("zuzzurelone, yes")
```




    ['z',
     'u',
     'z',
     'z',
     'u',
     'r',
     'e',
     'l',
     'o',
     'n',
     'e',
     ',',
     ' ',
     'y',
     'e',
     's']




```python
sorted(tuple)
```




    [1.5, 1.5, 1.5, 1.5, 5, 5, 5, 5, 6, 6, 6, 6]




```python

```
