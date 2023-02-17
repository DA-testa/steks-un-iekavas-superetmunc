def is_balanced(s):
    stack = []
    opening = set('({[')
    pairs = set([ ('(',')'), ('{','}'), ('[',']') ])
    for char in s:
        if char in opening:
            stack.append(char)
        else:
            if len(stack) == 0:
                return False
            last_open = stack.pop()
            if (last_open, char) not in pairs:
                return False
    return len(stack) == 0


if __name__ == '__main__':
    import sys
    if len(sys.argv) > 1:
        filename = sys.argv[1]
        with open(filename) as f:
            for line in f:
                line = line.strip()
                print('Success' if is_balanced(line) else 'Failure')
    else:
        s = input().strip()
        print('Success' if is_balanced(s) else 'Failure')
