f=open('test.html', encoding='UTF8')
text=f.read()
print(type(text))
print(len(text))

print(text)


f.close()