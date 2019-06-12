def num_calculate(str_number):    
    even, ood = [], []
    for i in str_number:
        if int(i) % 2 == 0:
            even.append(i)        
        else:
            ood.append(i)
    str_list = "".join([str(len(even)), str(len(ood)), str(len(even)+len(ood))])
    return str_list
     
def BlackHole(str_number):    
    i = 0
    number = num_calculate(str_number)    
    while True:      
        i += 1  
        print('重复第{}次:{}'.format(i, number)) 
        number = num_calculate(number)
        if int(number) == 123:
            i += 1
            print('重复第{}次:{}'.format(i, number))
            break
 
if __name__ == '__main__':
     BlackHole(input("输入一个数字: "))
