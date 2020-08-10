"""
除法程序(可求除数和余数)

Version: 0.5
Author: 金淼
Date: 2020-08-08
"""
# -*- coding: utf-8 -*- 

class div(object):

    def num_word(self,numword):
        '''判断输入的字符是数字还是字符串'''
        c = 0
        for i in numword:
            if ord(i) >= 48 and ord(i)<=57 or ord(i)==46 or ord(i)==45:
                c=c+1
                if c>=len(numword):
                    num = eval(numword)
                    return num
            else:
                word = numword
                break
        return word


    def divinput(self):  #数据输入函数
        '''输入二个数，输入大小写“q”或"e"退出函数调用。 '''
        temp1=""
        temp2=""
        temp1 = input("请输入第一个数： ")
        if temp1 == "q" or temp1 == "Q" or temp1 == "e" or temp1 == "E":
            return temp1,temp2            #返回退出信息
        temp2 = input("请输入第二个数： ")
        if temp2 == "q" or temp2 == "Q" or temp2 == "e" or temp2 == "E":
            return temp1,temp2            #返回退出信息
        else:
            _div1 = eval(temp1)
            _div2 = eval(temp2)
            return  _div1,_div2           #返回输入的数据



    def divjs(self,div1,div2):       #数据计算函数
        '''求二个数的除法函数。'''
        # if div1 < div2:
        #     print("除数大于被除数，请从新输入！")
        #     print("=================")
        #     return 
        if  div1/div2 == div1//div2 or abs(div1)<abs(div2):     #判断是否能整除（能整除）
            quotient = div1/div2
            print("{} / {} = {}".format(div1,div2,quotient))
            print("=================")
        else:                            #不能整除
            quotient = div1//div2
            remainder = (div1)%div2
            print("{} / {} = {} 余 {}".format(div1,div2,quotient,remainder))
            print("=================")
        return

def main():          #执行主函数
    dv = div()       #实例化一个对象
    while True:
        (div1,div2) = dv.divinput()     #调用输入函数
        if div1 == "q" or div1 == "Q" or div1 == "e" or div1 == "E" or div2 == "q" or div2 == "Q" or div2 == "e" or div2 == "E":
            print("你已经退出程序,谢谢使用,请再次光临！")                   #返回退出信息
            break               #程序中断退出

        dv.divjs(div1,div2)     #调用计算除法函数

if __name__ == "__main__":
    main()           #调用子函数

