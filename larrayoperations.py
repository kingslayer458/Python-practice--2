# Initialize an empty list
arr = []

# Take the number of commands
N = int(input("Enter number of commands: "))

# Loop through N commands
for _ in range(N):
    # Read the command and split it into parts
    command = input().split()
    cmd = command[0]

    # Handle each command
    if cmd == "print":
        print(arr)

    elif cmd == "insert":
        arr.insert(int(command[1]), int(command[2]))

    elif cmd == "remove":
        arr.remove(int(command[1]))

    elif cmd == "append":
        arr.append(int(command[1]))

    elif cmd == "sort":
        arr.sort()

    elif cmd == "pop":
        arr.pop()

    elif cmd == "reverse":
        arr.reverse()
