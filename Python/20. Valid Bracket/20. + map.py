def isvalid(s):
    stack = []
    maps = {
        "{": "}",
        "[": "]",
        "(": ")"
    }
    for x in s:
        if x in maps:
            stack.append(maps[x])
        else:
            if len(stack) != 0:
                top_element = stack.pop()
                if x != top_element:
                    return False
                else:
                    continue
            else:
                return False
    return len(stack) == 0


isvalid('}')
