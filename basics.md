---
title: Basic Operations
nav: true
--- 

## Content:
 - [On Strings](#some-id)
 
### <a name="some-id"></a> String Operations

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
    ['You', 'can', 'have', 'any', 'space', 'or', 'tab', 'long', 'or', 'short']
    'You_can_have_any_space_or_tab_long_or_short'
Another way:
```python
x="Mississipi"
a=x.split("ss")
"::".join(a)
```
    'Mi::i::ipi'
```python
x="Mississipi"
b=x.split("ss",1)
"zz".join(b)
```
    'Mizzissipi'
**If we have a binary string, how can I convert it to integer?**
```python
# transform binary string into number
int("101", 2)
```
    5
**How can I strip the name of a website from an URL?**
```python
x="www.python.org"
x.strip(".gorw") # discards . g o r and all the w
```
    'python'
**how to replace specific characters from a string?**
With .maketrans and .translate
```python
# use RE module with .maketrans and .translate to use better replace techniques
x = "§x ^ (y % Z)"
table = x.maketrans("§^()", "!&[]")
x.translate(table)
```
    '!x & [y % Z]'
**I have a string with text and other disturbing characters, how can I remove them?**
```python
x="a,s.d;f:"
table=x.maketrans(",.;:","    ")
x.translate(table)
```
    'a s d f '







Next, below, I showcase some coding of what you can find the links above.














Next, below, I showcase some coding of what you can find the links above.
