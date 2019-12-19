---
title: Home
---

## Lorenzo Negri Programming

Here you can view my programming laboratories and experiments coding in Data Science field with Python; starting from some [basic operations](https://lorenzonegri.github.io/Python-Labs/basics) but still interesting coding, to some **advanced** hacking, tricks and tips on [data science fundamentals](https://lorenzonegri.github.io/Python-Labs/) coding with python.

The list of topics:
 - [Basic Operations](https://github.com/LorenzoNegri/Python-Labs/tree/master/Basics): Notes, Experiments and Discovering new things.
 - [Analyzing Data with Python](https://github.com/LorenzoNegri/Python-Labs/tree/master/Analyzing%20Data%20with%20Python): From simple to Pro.
 - [Visiualizing Data with Python](https://lorenzonegri.github.io/Python-Labs/): .
 - [Data Science Fundamentals](https://lorenzonegri.github.io/Python-Labs/): From simple to Pro.

Next, below, I showcase some coding of what you can find the links above.

### Import shelve 

It's a useful module to manage and create simple dictionaries/databases on the fly and to deal with massive dictionaries. It could be to slow for some real big data. A simple example of shelve use where we can easely create and maintain a clients address book:

```python
# shelve can be used with massive datasets
import shelve
mass = shelve.open("clients") # creates or writes a file

mass['ferri'] = ('barley', '565-589-3656', '123 Milan') # add all the data we need
mass['black'] = ('alexy', '333-219-2587', '398 London') # add all the data we need

mass.close()

# simple method
with shelve.open('clients') as db:
    db['bianchi'] = ('alexy', '333-219-2587', '398 London')

# reading data from the file created above
import shelve
mass = shelve.open("clients")

# read content
print(mass['ferri'])
mass.close()
```
Output:
```markdown
('barley', '565-589-3656', '123 Milan')
```

For more details about other basics coding like this one above go to my [basic operations link](https://github.com/LorenzoNegri/Python-Labs/tree/master/Basics).

### Jekyll Themes

Your Pages site will use the layout and styles from the Jekyll theme you have selected in your [repository settings](https://github.com/LorenzoNegri/Python-Labs/settings). The name of this theme is saved in the Jekyll `_config.yml` configuration file.

### Support or Contact

Having trouble with Pages? Check out our [documentation](https://help.github.com/categories/github-pages-basics/) or [contact support](https://github.com/contact) and we’ll help you sort it out.
