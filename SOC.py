import math

def soc(x, n):    
    d = round(math.log2(n) + 1) 
    c = list(range(1, n+1))
    print ('Множество ',n)
    print('загадано число ', x)
    print('максимально возможное кол-во оперций не более ',(d))
    search(x, c)

def search(y,c, num = 0):        
    x = y 
    a = c     
    num += 1
    if x == 1:            
        result(num, x)
        return
    s = int((( len(a) ) / 2) + 0.5)        
    if x < a[s]:
        f = a[:(s)]        
        search(x , f, num)
    elif x > a[s]:
        f = a[s:]        
        search(x , f, num)
    elif x == a[s]:                 
        result(num, a[s])
   
def result(num, x):
    print('выполнено операций ', num)
    print ('искомое число ', x)
    return

if __name__ == "__main__":
    
    first_num = int(input('введите искомое число: '))
    sec_num = int(input('введите дапозон: '))    
    if (first_num <= sec_num) and (isinstance(first_num, int)) and (isinstance(sec_num,int)):
        soc(first_num, sec_num)
    else:
        print ("""Искомое число должно быть меньше диапозона""")
    