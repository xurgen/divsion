"""
除法程序(可求除数和余数)

Version: 2。0
Author: 金淼
Date: 2020-08-22
"""
def wordtest(chart):
    '''输入字符正确与否的测试程序,输入正确返回输入的字符与False，否则返回True'''
    character = ("1","2","3","4","5","6","7","8","9","0",".","-")
    for i in chart:
        if i not in character:
            if i in ("q","Q","e","E"):
                exit()
            print("输入的数字不符合要求")
            return True,chart
    return False,chart
        
def main(): 
    while True:
        '''输入第一个数'''       
        temp = True
        while temp:
            num1 = input("请输入第一个数: ")
            (temp,a) = wordtest(num1)
        num1 = eval(a)
        '''输入第二个数'''
        temp = True
        while temp:
            num2 = input("请输入第二个数: ")
            (temp,b) = wordtest(num2)
            if eval(b) == 0:
                print("除数不能为零，请重新输入！")
                temp = True
        num2 = eval(b)
        '''计算后输入表达式'''
        if  abs(num1)//abs(num2) == 0:
            quotient = num1/num2
            print("{} / {} = {}".format(num1,num2,quotient))
            print("==================")
        elif  abs(num1)/abs(num2) == abs(num1)//abs(num2):                    #判断是否能整除（能整除）
            quotient = num1/num2
            print("{} / {} = {}".format(num1,num2,quotient))
            print("==================")
        else:
            quotient = int(num1/num2)                     #不能整除
            remainder =num1-quotient*num2
            print("{} / {} = {} 余 {}".format(num1,num2,quotient,remainder))
            print("==================")
    


if __name__ == "__main__":
    main()
