# -*- coding: utf-8 -*-

div1 = 0
div2 = 0
while True:
    temp = input("请输入一个被除数： ")
    if temp == "q" or temp == "Q" or temp == "e" or temp == "E":
        break  # 收到退出信息，中断程序运行
        # exit()
        # quit()
    else:
        div1 = eval(temp)
        temp = input("请输入一个除数： ")
        div2 = eval(temp)
        while div1 < div2:
            if temp == "q" or temp == "Q" or temp == "e" or temp == "E":
                break  # 收到退出信息，中断程序运行
            else:
                print("除数大于被除数，请从新输入！")
                temp = input("请输入一个被除数： ")
                div1 = eval(temp)
                temp = input("请输入一个除数： ")
                div2 = eval(temp)
        if div1 / div2 == div1 // div2:  # 判断是否能整除（能整除）
            quotient = div1 / div2
            print("{} / {} = {}".format(div1, div2, quotient))
        else:
            quotient = div1 // div2  # 不能整除
            remainder = div1 % div2
            print("{} / {} = {} 余 {}".format(div1, div2, quotient, remainder))
