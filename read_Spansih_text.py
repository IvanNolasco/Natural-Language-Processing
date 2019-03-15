from bs4   import BeautifulSoup

f=open('e960401.html', encoding='latin-1')
t=f.read()
f.close()

soup = BeautifulSoup(t, 'lxml')
tS = soup.get_text()
tS = tS.replace('\x97', ' ')

print(tS)

f=open('e960401.txt', 'w')
f.write(tS)
f.close()
