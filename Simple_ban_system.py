# coding=gbk
import functools
import datetime
balance = 1000
operation_log = []

def menu():
    menu = """
操作菜单如下：
0：退出
1：存款
2：取款
3：查看操作记录
"""
    print(menu)

def valiadte(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        amount = args[0]
        amount_str = str(args[0])
        if amount < 0:
            print("金额有误，不应该是负数")
        elif len(amount_str) - amount_str.index(".") - 1 > 2:
            print("金额有误，最多保留两位")
        else:
            func(*args, **kwargs)
    return wrapper

@valiadte
def deposit(amount):
    global balance
    balance += amount
    write_log(amount, "存款")

def withdral(amount):
    global balance
    if amount > balance:
        print("账户余额不足")
    else:
        balance -= amount
    write_log(amount, "取款")

def write_log(amount, type):
    global operation_log
    nowTime = datetime.datetime.now()
    createTime = nowTime.strftime("%Y-%m-%d %H:%M:%S")
    operation_log.append([createTime, amount, type, f'{balance:.2f}'])

def print_log():
    for i in operation_log:
        print(i)


while True:
    menu()
    choice = int(input("请输入操作："))
    if choice == 1:
        print("存款操作")
        amount = float(input("请输入存款金额："))
        deposit(amount)
        print(f"您当前的余额是：{balance:.2f}元。")
    elif choice == 2:
        print("取款操作")
        amount = float(input("请输入取款金额："))
        withdral(amount)
        print(f"您当前的余额是：{balance:.2f}元。")
    elif choice == 3:
        print("打印操作流水")
        print_log()
    elif choice == 0:
        print("您已退出系统")
        break
    else:
        print("您的输入有误")
