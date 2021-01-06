def permutations(string):
    #your code here
    from itertools import permutations as per
    a=per(string,len(string))
    lista=[]
    string=''
    lista=[string.join(i) for i in a if string.join(i) not in lista]
    
    return set(lista)
