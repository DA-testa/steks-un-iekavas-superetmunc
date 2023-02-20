# 221RDC037 Edmunds Fiļipovs 18.grupa
from collections import namedtuple

Bracket = namedtuple("Bracket", ["char", "position"])


def are_matching(left, right):
    return (left + right) in ["()", "[]", "{}"]


def find_mismatch(text):
    opening_brackets_stack = []
    for i, next in enumerate(text):
        if next in "([{":
            opening_brackets_stack.append(Bracket(next, i))

        if next in ")]}":
            if not opening_brackets_stack or not are_matching(opening_brackets_stack.pop().char, next):
             return i + 1


def main():
    choice = input()
    if "I" in choice:
        text = input()
    mismatch = find_mismatch(text)
    if mismatch is not None:
     print(mismatch)
    else:
     print("Success")


if __name__ == "__main__":
    main()
    
