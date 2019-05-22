def find_longest(s):
    n = len(s)
    stack = [-1]
    ret = 0
    for i in range(n):
        if s[i] == '(':
            stack.append(i)
        else:
            stack.pop()

            if len(stack) != 0:
                ret = max(ret, i - stack[len(stack) - 1])
            else:
                stack.append(i)
    return ret