train = [0] * int(input())

command = input()

while command != "End":
    command = command.split()
    action = command[0]
    if action == "add":
        people = int(command[1])
        train[-1] += people
    elif action == "insert":
        index = int(command[1])
        people = int(command[2])
        train[index] += people
    elif action == "leave":
        index = int(command[1])
        people = int(command[2])
        train[index] -= people

    command = input()

print(train)
