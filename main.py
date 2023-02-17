import os
from collections import namedtuple

Bracket = namedtuple("Bracket", ["char", "position"])


def are_matching(left, right):
    return (left + right) in ["()", "[]", "{}"]


def find_mismatch(text):
    opening_brackets_stack = []
    for i, next in enumerate(text):
        if next in "([{":
            opening_brackets_stack.append(Bracket(next, i))
        elif next in ")]}":
            if not opening_brackets_stack:
                return i + 1
            top = opening_brackets_stack.pop()
            if not are_matching(top.char, next):
                return i + 1
    if opening_brackets_stack:
        return opening_brackets_stack[0].position + 1
    else:
        return "Success"


def main():
    choice = input("Enter 'F' to input a file, or 'I' to input brackets: ")
    if choice == "F":
        filename = input("Enter the filename: ")
        if not os.path.exists(filename):
            print(f"File '{filename}' does not exist.")
            return
        with open(filename) as f:
            text = f.read()
    elif choice == "I":
        text = input("Enter the brackets: ")
    else:
        print("Invalid choice")
        return

    mismatch = find_mismatch(text)
    print(mismatch)


if __name__ == "__main__":
    main()
