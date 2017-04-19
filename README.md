# Bddocs

EN: Create end-user readable docs in Pythonic way

PT: Crie documentos legíveis para o usuário final de forma Pythonica


## Installation

To install Bddocs, simply:

```bash

    $ pip install bddocs
    
    ✨🍰✨
    
```
Satisfaction, guaranteed.


## How to start ##

To use, simply:

```python
>>> from bddocs import Documentation  # to retrieve bdd information
>>> from bddocs import PDF  # to get PDF output
>>> from bddocs import HTML  # to get it HTML output
>>> bdd = Document('example')  # pass the path of .feature documents
>>> PDF(bdd).output('document.pdf')  # retrieve BDD info in a PDF file
>>> HTML(bdd).output('document.html')  # retrieve BDD info in a HTML file
```


## Documentation

[We are still documenting](https://github.com/yurireeis/bddocs/issues/14).


## How to Contribute

Before opening any issues or proposing any pull requests, please read our 
[Contributor's Guide](CONTRIBUTING.md).

