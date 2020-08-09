'''判断输入的是数字还是字符串'''



def num_word(numword):

	'''判断输入的是数字还是字符串'''
    c = 0
    for i in a:
        if ord(i) >= 48 and ord(i)<=57 or ord(i)==46:  
            c=c+1
            if c>=len(a):
                print(f"这是一个数字{a}")
        else:
            print(f"这是一个字符{a}")
            break
    return numword

    
while True:
    a = input("请输入一个数： ")
    num = num_word(a)
    print(num)
    
    

