import sys

def takesinput():

    i = 1
    argnumber = (len(sys.argv))
    print("=== Command Quest ===")
    print(f"Program name : {sys.argv[0]}")
    if argnumber == 1:
        print("No arguments provided!")
    else:
        print(f"Arguments received: {argnumber - 1}")
    while argnumber > i:
        print(f"Argument {i}: {sys.argv[i]}")
        i += 1
    print(f"Total argumengts {argnumber}")

def main():
    takesinput()

if __name__ == "__main__":
    main()