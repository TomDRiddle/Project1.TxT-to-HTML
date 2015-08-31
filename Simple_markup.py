import sys,re,util
file=open(input("input txt path:"),'r')
html=open('output.html','w')
html.write('<html><head><title>...</title><body>')
title=True
for block in util.blocks(file):
    block=re.sub(r'\*(.+?)\*',r'<em>\1</em>',block)
    if title:
        html.write('<h1>')
        html.write(block)
        html.write('</h1>')
        title=False
    else:
        html.write('<p>')
        html.write(block)
        html.write('</p>')
        html.write('</body></html>')
html.close()