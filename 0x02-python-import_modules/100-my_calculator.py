#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    import calculator_1 as cal

    argc = len(sys.argv)
    if argc != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)

    a = int(sys.argv[1])
    op = sys.argv[2]
    b = int(sys.argv[3])

    if op == "+":
        print("{} + {} = {}".format(a, b, cal.add(a, b)))
    elif op == "-":
        print("{} - {} = {}".format(a, b, cal.sub(a, b)))
    elif op == "*":
        print("{} * {} = {}".format(a, b, cal.mul(a, b)))
    elif op == "/":
        print("{} / {} = {}".format(a, b, cal.div(a, b)))
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
