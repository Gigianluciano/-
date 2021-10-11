#括号
import sys
import random
from fractions import Fraction
e = open("Exercise.txt", "a+")          #打开exercise文件
a = open("Answer.txt", "a+")          #打开answer文件

list1 = []      #空列表
list2 = []      #存放二数运算值
yunsuanfu =[]   #存放运算符
yunsuanfu2=[]   #存放运算符2（我知道很笨 但是不这样弄括号添加部分搞不定了
#产生数字
def create_num(n):
    num = random.randint(2, 3)   #生成2,3个数
    # 运算符计数
    global j
    j = 0
    while j < num:       #循环生成随机数
        i = random.choice(['整', '分'])
        if i == '整':
            num1 = random.randint(1, n)
            num_int = Fraction(num1, 1)
            list1.append(num_int)             #出整数
        elif i == '分':
            num1 = random.randint(1, n)       #分子
            num2 = random.randint(1, n)       #分母
            # 判断max公约数
            mi = max(num1, num2)
            ni = min(num1, num2)
            r = mi % ni
            while r != 0:
                mi = ni
                ni = r
                r = mi % ni
                if ni != 1:
                    num1 //= ni
                    num2 //= ni
            if num2 == 0 or num1 % num2 == 0:
                continue
            if num1 >= num2:
                create_fakefrac(num1, num2)
            num_frac = Fraction(num1, num2)          #出真分数
            list1.append(num_frac)
        j += 1
    list1.sort(reverse=True)
    # 调试用 列出随机生成的数字及个数
    # print(list1)
    # print(f"num:{j}")

#真分数print
def create_fakefrac(x, y):
    num_inte = x//y        #商
    num_fra = x%y       #余数
    if num_fra == 0:
        return Fraction(x,y)
    else:
        if num_inte == 0:
            return Fraction(x,y)
        else:
            str = f"{num_inte}'{num_fra}/{y}"
        return str

#随机选择符号
def create_fuhao():
    fuhao=[1, 2, 3, 4]
    fu=random.choice(fuhao)
    return fu

#switch运算
def calculate(x,y,z):
    # 单运算符逻辑部分
    def add(x, y):
        result = x + y
        return result

    def minus(x, y):
        result = x - y
        return result

    def mult(x, y):
        result = x * y
        return result

    def divi(x, y):
        result = x / y
        return result

    numbers = {
        1 : add(x, y),
        2 : minus(x, y),
        3 : mult(x, y),
        4 : divi(x, y),
    }

    return numbers[z]

#switch输出算式函数
def output_string(x,y):

    def add1():
        #判断假分数
        if (x.numerator > x.denominator):
            res1 = create_fakefrac(x.numerator, x.denominator)
        else:
            res1=x
        if (y.numerator > y.denominator):
            res2 = create_fakefrac(y.numerator, y.denominator)
        else:
            res2=y

        #括号判别
        if j==3 and yunsuanfu2[-1]>=3:
            e.write(("(%s + %s)" % (res1, res2)))
        if j==3 and yunsuanfu2[-1]<3:
            e.write(("%s + %s" % (res1, res2)))
        if j == 2:
            e.write(("%s + %s" % (res1, res2)) + ("\n"))

    def minus1():
        if (x.numerator > x.denominator):
            res1 = create_fakefrac(x.numerator, x.denominator)
        else:
            res1 = x
        if (y.numerator > y.denominator):
            res2 = create_fakefrac(y.numerator, y.denominator)
        else:
            res2 = y
        #括号判别
        if j==3 and yunsuanfu2[-1]>=3:
            e.write(("(%s - %s)" % (res1, res2)))
        if j==3 and yunsuanfu2[-1]<3:
            e.write(("%s - %s" % (res1, res2)))
        if j==2:
            e.write(("%s - %s" % (res1, res2)) + ("\n"))

    def mult1():
        if (x.numerator > x.denominator):
            res1 = create_fakefrac(x.numerator, x.denominator)
        else:
            res1 = x
        if (y.numerator > y.denominator):
            res2 = create_fakefrac(y.numerator, y.denominator)
        else:
            res2 = y

        #括号判别
        if j==3 and yunsuanfu2[-1]>=3:
            e.write(("%s * %s" % (res1, res2)))
        if j==3 and yunsuanfu2[-1]<3:
            e.write(("%s * %s" % (res1, res2)))
        if j == 2:
            e.write(("%s * %s" % (res1, res2)) + ("\n"))

    def divi1():
        if (x.numerator > x.denominator):
            res1 = create_fakefrac(x.numerator, x.denominator)
        else:
            res1 = x
        if (y.numerator > y.denominator):
            res2 = create_fakefrac(y.numerator, y.denominator)
        else:
            res2 = y

        #括号判别
        if j==3 and yunsuanfu2[-1]>=3:
            e.write(("%s ÷ %s" % (res1, res2)))
        if j==3 and yunsuanfu2[-1]<3:
            e.write(("%s ÷ %s" % (res1, res2)))
        if j == 2:
            e.write(("%s ÷ %s" % (res1, res2)) + ("\n"))

    switch = {
        1 :add1,
        2 :minus1,
        3 :mult1,
        4 :divi1
    }

    return switch[yunsuanfu[-1]]()

#若两个运算符 则只输出后半部分
def output_string_2(y):

    def add2():

        if (y.numerator > y.denominator):
            res3 = create_fakefrac(y.numerator, y.denominator)

        else:
            res3 = y

        e.write(("+ %s" % res3) + "\n")

    def minus2():

        if (y.numerator > y.denominator):
            res3 = create_fakefrac(y.numerator, y.denominator)

        else:
            res3 = y

        e.write(("- %s" % res3) + "\n")

    def mult2():

        if (y.numerator > y.denominator):
            res3 = create_fakefrac(y.numerator, y.denominator)

        else:
            res3 = y

        e.write(("* %s" % res3) + "\n")

    def divi2():

        if (y.numerator > y.denominator):
            res3 = create_fakefrac(y.numerator, y.denominator)

        else:
            res3 = y

        e.write(("÷ %s" % res3) + "\n")

    switch = {
        1 :add2,
        2 :minus2,
        3 :mult2,
        4 :divi2
    }

    return switch[yunsuanfu2[-1]]()

print("\n请先在文件路径下创建‘Exercise.txt’和‘Answer.txt'文件夹，否则将无法运行")
n=int(input("请输入题目个数:"))
r = int(input("请输入随机数取值的最大值（最大值为十）："))
global timu
timu=1
if r<0 or r>10:
    print("输入错误，请按照要求输入，即将关闭程序")
    sys.exit(1)

while n>0:
    create_num(r)   #产生数字和j
    yunsuanfu.append(create_fuhao())    #产生运算符1
    list2.append(calculate(list1[0],list1[1],yunsuanfu[-1]))        #结果存放
    if j==3:
        yunsuanfu2.append(create_fuhao())  # 随机第二个运算符以判断是否需要加括号
    e.write("四则运算题目%s:" %timu)
    output_string(list1[0],list1[1])    #输出两数式子，若第需要加括号则添加

    #判断运算符个数
    if j>2:
        output_string_2(list1[2])
        list2.append(calculate(list2[0], list1[2],yunsuanfu2[-1]))
    # 转换答案
    global answer
    answer = create_fakefrac(list2[-1].numerator, list2[-1].denominator)
    #清空每次运算的保存数据
    list1.clear()
    list2.clear()
    yunsuanfu.clear()
    yunsuanfu2.clear()
    a.write("答案%s:" %timu + str(answer) + "\n")
    timu+=1
    n=n-1


print("\n创建完毕，请打开对应文件夹查看")