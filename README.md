## Lorenzo Negri Programming

Here you can view my programming laboratories and experiments coding in Data Science field with Python; starting from some [basic](https://lorenzonegri.github.io/Python-Labs/) operations and interesting coding to some advanced tricks and tips on [DataSscience Fundamentals](https://lorenzonegri.github.io/Python-Labs/) coding with python.

Whenever you commit to this repository, GitHub Pages will run [basic](https://lorenzonegri.github.io/Python-Labs/) to rebuild the pages in your site, from the content in your Markdown files.

### Shelve

It's a useful way to manage or create simple dictionaries/databases on the fly and to deal with massive dictionaries. It could be to slow for some real big data. A simple example of shelve use:

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
```markdown
('barley', '565-589-3656', '123 Milan')
```

For more details see [GitHub Flavored Markdown](https://guides.github.com/features/mastering-markdown/).

### Jekyll Themes

Your Pages site will use the layout and styles from the Jekyll theme you have selected in your [repository settings](https://github.com/LorenzoNegri/Python-Labs/settings). The name of this theme is saved in the Jekyll `_config.yml` configuration file.

### Support or Contact

Having trouble with Pages? Check out our [documentation](https://help.github.com/categories/github-pages-basics/) or [contact support](https://github.com/contact) and we’ll help you sort it out.
