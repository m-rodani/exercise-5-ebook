grid = [["empty" for cols in range(2) for rows in range(5)]]
for row in grid:
    print(row)
while True:
    user_id = input("enter the user id")
    if user_id == "xxx":
        break
    for i in range(4):
        for x in range(1):
            grid[x][i] = user_id
for row in grid:
    print(row)