import sys


def command_quest():
    args = sys.argv
    args_len = len(sys.argv)
    if (args_len == 1):
        print("=== Command Quest ===")
        print("No arguments provided!")
        print(f"Program name: {args[0]}")
        print(f"Total arguments: {args_len}\n")
    else:
        print("=== Command Quest ===")
        print(f"Program name: {args[0]}")
        print(f"Arguments received: {args_len - 1}")
        count = 0
        for arg in args:
            if (count):
                print(f"Argument {count}: {arg}")
            count += 1
        print(f"Total arguments: {args_len}\n")


command_quest()
