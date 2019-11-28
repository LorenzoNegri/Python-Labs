```python
# dictionaries
```


```python
english_to_italian =  {'red':'rosso', 'blue':'blu', 'green':'verde'}
print("this dictionary has",len(english_to_italian), "words")
print("red in italian is", english_to_italian['red'])
print(list(english_to_italian.keys()))
print(list(english_to_italian.values()))
print(list(english_to_italian.items()))
```

    this dictionary has 3 words
    red in italian is rosso
    ['red', 'blue', 'green']
    ['rosso', 'blu', 'verde']
    [('red', 'rosso'), ('blue', 'blu'), ('green', 'verde')]



```python
# get function to return a specific value or saying that it is not there
print(english_to_italian.get('red', 'no translation available'))
print(english_to_italian.get('yellow', 'no translation available for yellow'))
print(english_to_italian.get('brown'))
```

    rosso
    no translation available for yellow
    None



```python
# setdefault to give a specific return on that value
print(english_to_italian.setdefault('brown','NA'))
```

    NA



```python
z = {'red':1, 'blue':2, 'green':3}
x = {'red':2, 'blue':1, 'green':5}
x.update(z)
x
```




    {'red': 1, 'blue': 2, 'green': 3}




```python
# counting words with dictionaries
_string="To be, or not to be, that is the question"
occurences = {}
for word in _string.split():
    occurences[word] = occurences.get(word, 0) + 1
    
for word in occurences:
    print("the word", word, "occurs", occurences[word], \
            "times in the string")
```

    the word To occurs 1 times in the string
    the word be, occurs 2 times in the string
    the word or occurs 1 times in the string
    the word not occurs 1 times in the string
    the word to occurs 1 times in the string
    the word that occurs 1 times in the string
    the word is occurs 1 times in the string
    the word the occurs 1 times in the string
    the word question occurs 1 times in the string



```python

```
