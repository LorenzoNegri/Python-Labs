```python
a=0
while a>=0:
    if a==1000: break
    a+=1
print(a)
```

    1000



```python
a=0
while a>=0 and a<1000:
    a+=1
print(a)
```

    1000



```python
x=0
if x>0:
    pass
else:
    x=5
x
```




    5




```python
x=[1.0,2.0,3.0]
for n in x:
    print(len(x)-n+1)
```

    3.0
    2.0
    1.0



```python
# To print all the index position of negative values
x=[1,3,-8,5,4,-5,2]
for i in range(len(x)):
    if x[i] < 0:
        print("negative number at index ", i)
```

    negative number at index  2
    negative number at index  5



```python
# Range can be used on cycles of iteration of big dimension data
# without without occupying a lot of memory
```


```python
# we can specify upper and lower boundaries of range
list(range(3, 7))
```




    [3, 4, 5, 6]




```python
# we can specify the steps, forward or backwards boundaries of range
list(range(0, 10, 2))
```




    [0, 2, 4, 6, 8]




```python
list(range(10, 0, -1))
```




    [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]




```python
# for loop with tuple with ops
tlist = [(1,2), (3,7), (9,5)]
result = 0

for x,y in tlist:
    result += (x*y)

print(result)
# the result is resutl= tlist[(x1*y1)+(x2*y2)+(x3*y3)]
```

    68



```python
# for loop with tuple with ops
tlist = [('a',2), ('a',7), ('b',5), ('c',12), ('c',1)]
result = 0

for x,y in tlist:
    if x=="a":
        pass
    else:
        result += (y)

print(result)
# the result is if tuple element "a" we skip count 
# otherwise: result= tlist[(y1)+(y2)+...+(yn)]
```

    5



```python
# merge two list into one listed tuple with ZIP func
x = ['a','b','c','d']
y = [2, 7, 5, 12, 11, 1]
z = zip(x, y)
list(z)
```




    [('a', 2), ('b', 7), ('c', 5), ('d', 12)]




```python
# comprehesion examples
x = [1,2,3,4,5]
x_squared = [item*item for item in x]
x_squared
```




    [1, 4, 9, 16, 25]




```python
# comprehesion with if
x = [1,2,3,4,5]
x_squared = [item*item for item in x if item > 2]
x_squared
```




    [9, 16, 25]




```python
# comprehesion dictionary creation
x = [1,2,3,4,5]
x_squared_dict = {item: item*item for item in x if item > 2}
x_squared_dict
```




    {3: 9, 4: 16, 5: 25}




```python
# generative that does not use so much memory
x = [1,2,3,4,5]
x_squared_gen = (item*item for item in x)
x_squared_gen
```




    <generator object <genexpr> at 0x7fdaeced94c0>




```python
# retrive result from the previus generative object
for square in x_squared_gen:
    print(square,)
```

    1
    4
    9
    16
    25



```python

```
