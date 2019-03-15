tokens=['1', '2', '3', '4', '5', '6', '7', '8', '9']
w='5'
windowSize=12

context1=[]
for i in range(len(tokens)):
    if tokens[i]==w:
        try:
            for j in range(i-int(windowSize/2), i): #left context
                context1.append(tokens[j])
        except IndexError:
            pass
        try:
            for j in range(i+1, i+(int(windowSize/2+1))): #right context
                context1.append(tokens[j])
        except IndexError:
            pass
       
print('Contexto:', context1)


context2=[]
for i in range(len(tokens)):
    if tokens[i]==w:
        for j in range(i-1, i-int(windowSize/2)-1, -1): #left context
            if j >=0: 
                context2.append(tokens[j])
        try:
            for j in range(i+1, i+(int(windowSize/2+1))): #right context
                context2.append(tokens[j])
        except IndexError:
            pass

print('Contexto:', context2)
   
