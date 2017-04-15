from model.documentation import Documentation
from pdf import PDF

bdd = Documentation('example')
pdf = PDF(bdd)
pdf.output('tuto2.pdf', 'F')
pass
