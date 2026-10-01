import sys

print("=== Command Quest ===")
print(f"Program name: {sys.argv[0]}")
args = sys.argv[1:]
if not args:
    print("No arguments provided!")
else:
    print(f"Arguments received: {len(args)}")
    i = 1
    for arg in args:
        print(f"Argument {i}: {arg}")
        i += 1
print(f"Total arguments: {len(sys.argv)}")
