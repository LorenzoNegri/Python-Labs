```python
# how to count lines of a massive file without going out of memory
file_obj = open("myfile", 'r')
count = 0
for line in file_obj:
    count += 1
print(count)
file_obj.close()
```


```python
# binary mode of reading a file
input_file = open("myfile", 'rb') # opens file as binary by 'rb'
header = input_file.read(4) # read the first 4 byte (header string)
data = input_file.read() # rest of file
input_file.close()
```


```python
# how to use pickle to store anything you want inside a file and use it later
import pickle
a = {'a':[1,2,3,4],'b':[5,6,7,8],'c':[9,10,11,12]}
b = {1:['a','a','a','a'], 2:['b','b','b','b'], 3:['c','c','c','c']}
c = {'a':[11,12,13,14],15:['e','e','e','e'],16:[17,18,19,20]}

file = open("state", 'wb') # create or writes the file
pickle.dump(a, file)
pickle.dump(b, file)
pickle.dump(c, file)
file.close()
```


```python
# read the file saved with pickle
import pickle

file = open("state", 'rb') # read the pickle file
a = pickle.load(file)
b = pickle.load(file)
c = pickle.load(file)
file.close()

print(a)
print(b)
print(c)
```

    {'a': [1, 2, 3, 4], 'b': [5, 6, 7, 8], 'c': [9, 10, 11, 12]}
    {1: ['a', 'a', 'a', 'a'], 2: ['b', 'b', 'b', 'b'], 3: ['c', 'c', 'c', 'c']}
    {'a': [11, 12, 13, 14], 15: ['e', 'e', 'e', 'e'], 16: [17, 18, 19, 20]}



```python
# shelve to use for massive data
import shelve
mass = shelve.open("clients") # creates or writes a file

mass['ferri'] = ('barley', '565-589-3656', '123 Milan') # add all the data we need
mass['black'] = ('alexy', '333-219-2587', '398 London') # add all the data we need

mass.close()
```


```python
# reading data from the file created above
import shelve
mass = shelve.open("clients")

# read content
print(mass['ferri'])
```

    ('barley', '565-589-3656', '123 Milan')



```python
# simple read a file
with open("clients.bak", 'r') as f:
    file = f.read()
print(file)
```

    'ferri', (0, 54)
    'black', (512, 54)
    



```python
# simple write and read the file
with open("clients_b", 'w') as f:
        f.write("Hello, Earth\nand Moon")
with open("clients_b", 'r') as f:
    file = f.read()
print(file)
```

    Hello, Earth
    and Moon



```python

```
