command = input()
book = {}

while command != "Lumpawaroo":
    is_user = False
    if " | " in command:
        force_side, force_user = command.split(" | ")
        if force_user not in book:
            book[force_user] = force_side
    elif " -> " in command:
        force_user, force_side = command.split(" -> ")
        if force_user in book:
            del(book[force_user])
        book[force_user] = force_side
        print(f"{force_user} joins the {force_side} side!")

    command = input()

members = [x for x in book.values()]
sides = []
for i in members:
    if i not in sides:
        sides.append(i)
        users = "\n! ".join([x for x in book if book[x] == i])
        print(f"Side: {i}, Members: {members.count(i)}")
        print(f"! {users}")

#invert the dictionary
# users = [x for x in book.keys()]
# bookz = {}
# for j in range(len(members)):
#     if members[j] not in bookz:
#         bookz[members[j]] = []
#     bookz[members[j]].append(users[j])
#
# for k, v in bookz.items():
#     joined = "\n! ".join(v)
#     print(f"Side: {k}, Members: {len(v)}")
#     print(f"! {joined}")