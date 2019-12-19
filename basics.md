---
title: Basic Operations
nav: true
--- 

## Content:
 - [On Strings](#01-id)
 - [Lists and Tuples](#02-id)
 - [Sets](#03-id)
 
### <a name="01-id"></a> String Operations

**How to count number of spaces in a string?**
```python
"789 10 11 12".find(' ')
```
    3

**If you need to join text?**
```python
x="You can have any  space or tab   long or short"
a=x.split()
print(a)
"_".join(a) #in this case joined with _
```
```markdown
    ['You', 'can', 'have', 'any', 'space', 'or', 'tab', 'long', 'or', 'short']
    'You_can_have_any_space_or_tab_long_or_short'
```


Another way:



```python
x="Mississipi"
a=x.split("ss")
"::".join(a)
```
```markdown
    'Mi::i::ipi'
```
```python
x="Mississipi"
b=x.split("ss",1) # here I split only on the first pair of  "ss"
"zz".join(b)
```
```markdown
    'Mizzissipi'
```
    
    
**If there is a binary string, how can I convert it to integer?**



```python
# transform binary string into number
int("101", 2)
```
```markdown
    5
```

**How can I strip the name of a website from an URL?**

```python
x="www.python.org"
x.strip(".gorw") # discards . g o r and all the w
```
```markdown
    'python'
```

**How to replace specific characters from a string?**

With `.maketrans()` and `.translate()`

```python
# use RE module with .maketrans and .translate to use better replace techniques
x = "§x ^ (y % Z)"
table = x.maketrans("§^()", "!&[]")
x.translate(table)
```
```markdown
    '!x & [y % Z]'
```

**I have a string with text and other disturbing characters, how can I remove them?**

```python
x="a,s.d;f:"
table=x.maketrans(",.;:","    ")
x.translate(table)
```
```markdown
    'a s d f '
```

### <a name="02-id"></a> Lists and Tuples

**How to append a list to a list?**

```python
# adding a list to the end of a list
x=[1,2,3,4]
x[len(x):]=[5,6,7]
x
```
```markdown
    [1, 2, 3, 4, 5, 6, 7]
```

**Adding a list before a list?**

```python
# adding a list at the start of a list
x[:0]=[-1,0]
x
```
```markdown
    [-1, 0, 1, 2, 3, 4, 5, 6, 7]
```

**Removing elements from a list**

```python
# remove elements from a list
x[1:-1]=[] # removes elements from position 1 to "6" -1 position form end
x
```
```markdown
    [-1, 7]
```

**Append a string to a list**

```python
x=[1,2,3]
x.append("four")
x
```
```markdown
    [1, 2, 3, 'four']
```

**Appending lists to a list**

```python
# append lists
y=[5,6,7]
x.extend(y)
x
```
```markdown
    [1, 2, 3, 'four', 5, 6, 7]
```

**Inserting a value in a list in a certain position**

```python
x.insert(4, 4)
x
```
```markdown
    [1, 2, 3, 'four', 4, 5, 6, 7]
```

The first value in `.insert()` is the position.

```python
x.insert(0, 'start')
x
```
```markdown
    ['start', 1, 2, 3, 'four', 4, 5, 6, 7]
```

**Fast functions to sort a list by lenght of words**

```python
# function to sort by lenght of words
def compare_num_of_chars(x):
    return len(x)
x.sort(key=compare_num_of_chars)
print(x)
```
```markdown
    ['A', 'W', 'Beta', 'Kakkazza', 'Zuzzorellone']
```

**Another way of appendind lists**

```python
z=y + x
z
```
```markdown
    [7, 6, 5, 4, 3, 2, 'A', 'W', 'Beta', 'Kakkazza', 'Zuzzorellone']
```

**Creating a sequence in Tuples**

```python
# Tuples
x=3
y=2
t=(x+y,x*y,x/y)
tuple=t+(t*3)
tuple
```
```markdown
    (5, 6, 1.5, 5, 6, 1.5, 5, 6, 1.5, 5, 6, 1.5)
```

**Trick to split text into letters and make a list**

```python
# nice to split text
list("zuzzurelone, yes")
```
```markdown
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
```

### <a name="03-id"></a> Sets

![]("https://upload.wikimedia.org/wikipedia/commons/thumb/9/99/Venn0001.svg/384px-Venn0001.svg.png")

**With `&` it finds the elements in common by the sets

```python
# & only the elements in common by the sets
set_1=set([1,2,3,8,9])
set_2=set([1,2,5,6,7])
set_3=set_1 & set_2
set_3
```
```markdown
    {1, 2}
```


Next, below, I showcase some coding of what you can find the links above.
