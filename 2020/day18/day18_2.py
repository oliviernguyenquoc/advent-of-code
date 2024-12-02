def evaluate(nb1: int, op: str, nb2: int) -> int:
    if op == "+":
        res = nb1 + nb2
    elif op == "*":
        res = nb1 * nb2

    return res


def calculate_plus(op: str) -> int:
    res_stack = []
    op_stack = []
    i = 0
    len_op = len(op)

    while True:
        if op[i].isdigit():
            if len(op_stack) > 0 and len(res_stack) > 0:
                if op_stack[-1] == "+":
                    res = evaluate(
                        res_stack.pop(len(res_stack) - 1),
                        op_stack.pop(len(op_stack) - 1),
                        int(op[i]),
                    )
                    res_stack.append(res)
                else:
                    res_stack.append(int(op[i]))
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
            if res_stack and op_stack and op_stack[len(op_stack) - 1] == "+":
                res = evaluate(
                    res_stack.pop(len(res_stack) - 1),
                    op_stack.pop(len(op_stack) - 1),
                    calculate_plus(op[i + 1 : i + j + 1]),
                )
            else:
                res = calculate_plus(op[i + 1 : i + j + 1])
            res_stack.append(res)
            i += j + 2

        if i == len_op:
            for _ in range(len(op_stack)):
                res = evaluate(res_stack.pop(0), op_stack.pop(0), res_stack.pop(0))
                res_stack = [res] + res_stack
            break

    return res_stack[0]


f = open("./day18/input.txt")

op_list = "".join(f.readlines()).split("\n")
op_list = [op.replace(" ", "") for op in op_list]

results = []

for op in op_list:
    print("op: ", op)
    res = calculate_plus(op)
    print("res", res)
    results.append(res)

print(results)
print(sum(results))

f.close()