import math

sim_dic = {'add': '+', 'sub': '-', 'mul': '*', 'div': '/', 'mod': '%', 'pow': '**'}
sci_op = ['sin', 'cos', 'tan', 'log', 'sqrt']


def simple(n1, n2, op):
    if op == '+':
        return n1 + n2
    elif op == '-':
        return n1 - n2
    elif op == '*':
        return n1 * n2
    elif op == '/':
        return n1 / n2
    elif op == '%':
        return n1 % n2
    else:
        return n1 ** n2


def scientific(n, op):
    if op == "sin":
        return math.sin(n)
    elif op == "cos":
        return math.cos(n)
    elif op == "tan":
        return math.tan(n)
    elif op == "sqrt":
        return math.sqrt(n)
    else:
        return math.log(n, 10)


def calc():
    cal = int(input("Enter \"0\" for simple calculator:\n Enter \"1\" for scientific calculator:"))
    if cal == 0:
        print("The operations we have are:")
        for x in sim_dic:
            print(x)
        ope = input("\nEnter the operation to perform:")
        a = int(input("\nEnter the 1st number:"))
        b = int(input("\nEnter the 2nd number:"))
        ans = simple(a, b, sim_dic[ope])
        print("\nThe answer is:", ans)
    else:
        print("The operations we have are:", sci_op[:])
        ope = input("\nEnter the operation to perform:")
        a = int(input("\nEnter the number:"))
        ans = scientific(a, ope)
        print("\nThe answer is:", ans)


calc()
while True:
    if input("Press 1 to continue or 0 to exit") == "1":
        calc()
    else:
        break
