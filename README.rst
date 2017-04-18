Bddocs
--------

## How to start ##

To use simply do::

>>> from bddocs import Documentation  # to retrieve bdd information
>>> from bddocs import PDF  # to get PDF output
>>> from bddocs import HTML  # to get it HTML output
>>> bdd = Document('example')  # pass the path of .feature documents
>>> PDF(bdd).output('document.pdf')  # retrieve BDD info in a PDF file
>>> HTML(bdd).output('document.html')  # retrieve BDD info in a HTML file
