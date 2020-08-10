"""
除法程序(可求除数和余数)

Version: 1.1
Author: 金淼
Date: 2020-08-10
"""
# -*- coding: utf-8 -*- 

import division3

dv = division3.div()  #实例化一个类对象

def inputstr1():
    '''判断输入的第一个是数据还是退出字符'''
    
    while True:
        inpstr1 = input("请输入一个被除数： ")
        divnum1 = dv.num_word(inpstr1)
        if type(divnum1) ==str:
            if len(divnum1) > 1:
                print(f"你输入的数不符合要求，请重新输入！{divnum1}")
            elif len(divnum1) == 1:
                if divnum1 == "q" or divnum1 == "Q" or divnum1 == "e" or divnum1 == "E":
                    #print(f"你要求退出程序")
                    break
        else:
            divnum1 = eval(inpstr1)
            #print(f"你输入的是一个正确的数{divnum1}")
            break
    return divnum1

def inputstr2():
    '''判断输入的第二个是数据是否为“0”，还是退出字符'''

    while True:
        inpstr2 = input("请输入一个除数： ")
        divnum2 = dv.num_word(inpstr2)
        if type(divnum2) ==str:
            if len(divnum2) > 1:
                print(f"你输入的数不符合要求，请重新输入！{divnum2}")
            elif len(divnum2) == 1:
                if divnum2 == "q" or divnum2 == "Q" or divnum2 == "e" or divnum2 == "E":
                    print(f"你要求已退出程序！")
                    break
        else:
            divnum2 = eval(inpstr2)
            if divnum2 != 0:
                #print(f"你输入的是一个正确的数{divnum2}")
                break
            else:
                print(f"除数不能为{divnum2}")
    return divnum2

def main():          #执行主函数
    while True:
        div1 = inputstr1()  #调用输入函数输入被除数
        if div1 == "q" or div1 == "Q" or div1 == "e" or div1 == "E":
            print("你已经退出程序,谢谢使用,请再次光临！")                   #返回退出信息
            break
        else:
            div2 = inputstr2() #调用输入函数输入除数
            if div2 == "q" or div2 == "Q" or div2 == "e" or div2 == "E":
                print("你已经退出程序,谢谢使用,请再次光临！")        #返回退出信息
                break   #程序中断退出
            else:             
                dv.divjs(div1,div2)     #调用计算除法函数
                


if __name__ == "__main__":
    main()


