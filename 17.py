def calculate(expression):
    def apply_op(a, b, op):
        if op == "+":
            return a + b
        elif op == "-":
            return a - b
        elif op == "*":
            return a * b
        return a/b

    values = []
    operations = []
    priority = {"+": 1, "-": 1, "*": 2, '/': 2}

    i = 0
    while i < len(expression):
        if expression[i].isdigit():
            val = 0
            while i < len(expression) and expression[i].isdigit():
                val = 10 * val + int(expression[i])
                i += 1

            i -= 1
            values.append(val)

        elif expression[i] == " ":
            i += 1
            continue

        elif expression[i] == "(":
            operations.append("(")

        elif expression[i] == ")":
            while operations and operations[-1] != "(":
                val1 = values.pop()
                val2 = values.pop()
                op = operations.pop()
                values.append(apply_op(val2, val1, op))
            # get rid of "("
            operations.pop()

        else:
            while len(operations) > 0 and operations[-1] != "(" and\
                        priority[operations[-1]] >= priority[expression[i]]:
                val1 = values.pop()
                val2 = values.pop()
                op = operations.pop()
                values.append(apply_op(val2, val1, op))
            operations.append(expression[i])
        i += 1

    while len(operations) > 0:
        val1 = values.pop()
        val2 = values.pop()
        op = operations.pop()
        values.append(apply_op(val2, val1, op))
    return values[0]


text = input("Введите выражение: ")
result = calculate(text)
print("Результат:", result)
