def evaluate(nb1: int, op: str, nb2: int) -> int:
    if op == "+":
        res = nb1 + nb2
    elif op == "*":
        res = nb1 * nb2

    return res


def calculate(op: str) -> int:
    res_stack = []
    op_stack = []
    i = 0

    len_op = len(op)

    while True:
        # print(i, op, op[i], res_stack, op_stack)
        if op[i].isdigit():
            if len(op_stack) > 0 and len(res_stack) > 0:
                res = evaluate(res_stack.pop(0), op_stack.pop(0), int(op[i]))
                res_stack.append(res)
            else:
                res_stack.append(int(op[i]))
            i += 1
        elif op[i] in ["*", "+"]:
            op_stack.append(op[i])
            i += 1

        elif op[i] == "(":
            nb_parenthesis = 1
            for j, char in enumerate(op[i + 1 :]):
                if char == "(":
                    nb_parenthesis += 1
                elif char == ")":
                    nb_parenthesis -= 1

                if nb_parenthesis == 0:
                    break
            if res_stack and op_stack:
                res = evaluate(
                    res_stack.pop(0), op_stack.pop(0), calculate(op[i + 1 : i + j + 1])
                )
            else:
                res = calculate(op[i + 1 : i + j + 1])
            res_stack.append(res)
            i += j + 2

        if i == len_op:
            break

    return res_stack[0]


f = open("./day18/input.txt")

op_list = "".join(f.readlines()).split("\n")
op_list = [op.replace(" ", "") for op in op_list]

results = []

for op in op_list:
    print("op: ", op)
    res = calculate(op)
    results.append(res)

print(results)
print(sum(results))

f.close()