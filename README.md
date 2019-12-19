## Lorenzo Negri Programming

Here you can view my programming laboratories and experiments coding in Data Science field with Python; starting from some basic operations and interesting coding [editor on GitHub](https://github.com/LorenzoNegri/Python-Labs/edit/master/README.md) to some advanced tricks and tips.

Whenever you commit to this repository, GitHub Pages will run [Jekyll](https://jekyllrb.com/) to rebuild the pages in your site, from the content in your Markdown files.

### Markdown

Markdown is a lightweight and easy-to-use syntax for styling your writing. It includes conventions for

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

('barley', '565-589-3656', '123 Milan')
```

For more details see [GitHub Flavored Markdown](https://guides.github.com/features/mastering-markdown/).

### Jekyll Themes

Your Pages site will use the layout and styles from the Jekyll theme you have selected in your [repository settings](https://github.com/LorenzoNegri/Python-Labs/settings). The name of this theme is saved in the Jekyll `_config.yml` configuration file.

### Support or Contact

Having trouble with Pages? Check out our [documentation](https://help.github.com/categories/github-pages-basics/) or [contact support](https://github.com/contact) and we’ll help you sort it out.
