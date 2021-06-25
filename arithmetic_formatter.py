def arithmetic_arranger(problems, show=False):
    # Limit problems to five
    if len(problems) > 5:
        return "Error: Too many problems."

    # create empty list
    first = []
    second = []
    lens = []
    operator = []
    
    # Split problem into seperate variable and limits input to numbers
    for problem in problems:
        a, b, c = problem.split()
        if not a.isnumeric() or not c.isnumeric():
            return "Error: Numbers must only contain digits."

        # adds number to list
        first.append(a)
        second.append(c)
        operator.append(b)
        lens.append(max(map(len, [a, c])))  # adds maximum digits for the problem
        #print(lens)

        # Limits problem to 4 digits
    for i in lens:
        if i > 4:
            return "Error: Numbers cannot be more than four digits."
            
        # Check for operator in problems
    if "*" in operator or "/" in operator:
        return "Error: Operator must be '+' or '-'."

    # Printing first line
    ret ="    ".join([
        first[i].rjust(lens[i] + 2) for i in range(len(first))
                        ]) + "\n"

    # Printing second line
    ret += "    ".join([
        operator[i] + " " + second[i].rjust(lens[i]) for i in range(len(second))
                         ]) + "\n"

    # Printing separation line
    ret += "    ".join([
        ("-" * (lens[i] + 2)).rjust(lens[i]) for i in range(len(second))
        ])

    # Printing the answer
    if show:
        ret += "\n" + "    ".join([
            str(eval(problems[i])).rjust(lens[i]+2) for i in range(len(second))
            ])

    print(ret)
    return ret
# test
arithmetic_arranger(["3 + 855","3801 - 2", "45 + 43", "123 + 49"])

# This code passed the test.
