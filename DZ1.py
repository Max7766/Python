palindrom=range(0,2019)
for x in palindrom:
    w=str(x)
    if w[0:]==w[::-1]:
        print(w)
    
