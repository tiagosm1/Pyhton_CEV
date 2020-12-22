import urllib
import urllib.request

try:
    site = urllib.request.urlopen('http://www.google.com')
except urllib.error.URLError:
    print('O GOOGLE não está acessível!')
else:
    print('O GOOGLE está acessível!!!')
print(site.read)


