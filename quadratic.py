import math
import re
def lineaar(a,b):
    #ax+b=0
    return -b/a

def quadratic(a,b,c):
    if a == 0:
        return linear(b,c)
    delta = math.pow(b,2)-4*a*c
    if delta >= 0:
        x = (round((-b+math.sqrt(delta))/(2*a),3),round((-b-math.sqrt(delta))/(2*a),3))
        return x
    

# def input_processor():
#     pattern = r'\d*|\.'
#     a,b,c = input('a='),input('\nb='),input('\nc=')
#     new_ls = []
#     for item in [a,b,c]:
#         if re.match(pattern,item):#判断部分
#             item = eval(item)
#             new_ls.append(item)
#         else:
#             print("输入错误，请输入数字，程序退出")
#             break

#     return tuple(new_ls)

# print(a,b,c)

def input_judging(a,b,c):
    pattern = r'\d*|\.'
    new_ls = []
    for item in [a,b,c]:
        if re.match(pattern,item):#判断部分
            pass
        else:
            print("输入错误，请输入数字")
            return 0
            break
    return 1

def main():
        a,b,c = input('a='),input('\nb='),input('\nc=')
        if input_judging(a,b,c):
            a = eval(a)
            b = eval(b)
            c = eval(c)
            x = quadratic(a,b,c)
            print(f"二次方程{a}x^2+{b}x+{c}=0在实数域上的解是：{x}")


if __name__=='__main__':
    main()