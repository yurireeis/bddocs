from model.documentation import Documentation
from src.pdf.pdf import PDF

bdd = Documentation('example')
pdf = PDF(bdd)
pdf.output('example.pdf')
pass
