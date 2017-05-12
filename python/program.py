import sys
import request

# pega o link passado e mostra o condigo-fonte
a = sys.argv

l = request.get(a[1])

print(l.text)
