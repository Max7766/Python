def sort(*h):
    if not h:
        print('No')
    if len(h)==1:
        return h
    else:
        dic={}
        for x in h:
            if type(x)not in dic.keys():#если переменная типа не находиться в словаре
                dic[type(x)]=1
            else:
                dic[type(x)]+=1    
                return dic
t=sort(23,'Max',False,934,34,{'age':'32'}) 
print(t)




