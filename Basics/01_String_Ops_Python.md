---
nav: true
--- 

```python
"0123456".find('1')
```




    1




```python
"789 10 11 12".find(' ')
```




    3




```python
x = 'abc\n'
print(x,end="")
```

    abc



```python
"".join(["hgd", "cat", "hkd", "bbe", "HH"])
```




    'hgdcathkdbbeHH'




```python
x="You can have any  space or tab   long or short"
a=x.split()
print(a)
"_".join(a)
```

    ['You', 'can', 'have', 'any', 'space', 'or', 'tab', 'long', 'or', 'short']





    'You_can_have_any_space_or_tab_long_or_short'




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




```python
# transform binary string into number
int("101", 2)
```




    5




```python
x="www.python.org"
x.strip("www")
```




    '.python.org'




```python
x="www.python.org"
x.strip(".gorw") # discards . g o r and all the w
```




    'python'




```python
x="(name, date),\n"
x.strip("\n)(,")
```




    'name, date'




```python
x="mississipi"
x.replace("ss","DD")
```




    'miDDiDDipi'




```python
# use RE module with .maketrans and .translate to use better replace techniques
x = "§x ^ (y % Z)"
table = x.maketrans("§^()", "!&[]")
x.translate(table)
```




    '!x & [y % Z]'




```python
x = "1"
print(x.zfill(3))
```

    001



```python
x="a,s.d;f:"
table=x.maketrans(",.;:","    ")
x.translate(table)
```




    'a s d f '




```python
# find the last s position in the text: Mississipi Burning
x="Mississipi Burning"
x.rfind("s")
```




    6




```python
# delete everything after the last s in the text: Mississipi Burning
x="Mississipi Burning"
s=x.rfind("s")
wordlist=list(x)
wordlist[s::]=[]
x="".join(wordlist)
print(x)
```

    Missis



```python

```
