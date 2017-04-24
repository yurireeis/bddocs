from bddocs.model.documentation import Documentation
from bddocs.src.pdf.pdf import PDF

bdd = Documentation('bddocs/example')
pdf = PDF(bdd)
pdf.output('example.pdf')
