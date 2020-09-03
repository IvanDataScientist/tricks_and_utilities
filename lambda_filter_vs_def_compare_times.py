
import timeit

#Example filter + lambda

#List 1000 first numbers
comprobar = range(1000)

start=(time.time())
#Var + filter() + lambda
filt = filter(lambda x: x % 2 == 0, comprobar)
#Result to list 
pares = list(filt)
#Show list if filter is True
print(pares[1:5],time.time()-start)
#OUTPUT [2, 4, 6, 8....]


start=(time.time())
#Example only def
def function(comprobar):
    """
    """
    par=[]
    for x in comprobar:
        if x % 2 == 0:
            par.append(x)
    return(par)
print(function(comprobar)[1:5],(time.time()-start))
#OUTPUT [2, 4, 6, 8....]