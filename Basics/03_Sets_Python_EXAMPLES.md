```python
# & only the elements in common by the sets
set_1=set([1,2,3,8,9])
set_2=set([1,2,5,6,7])
set_3=set_1 & set_2
set_3
```




    {1, 2}




```python
# union of elements of sets
set_1 | set_2
```




    {1, 2, 3, 5, 6, 7, 8, 9}




```python
# check if alla elements of a set are inside the other
set_2.issubset(set_1)
```




    False




```python
# symmetrical difference
# all elements that are unique in the sets
set_1 ^ set_2
```




    {3, 5, 6, 7, 8, 9}




```python
set_1.add(7)
set_1
```




    {1, 2, 3, 7, 8, 9}




```python
set_1.remove(7)
7 in set_1
```




    False




```python

```
