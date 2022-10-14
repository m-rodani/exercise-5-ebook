scores_and_id = [
    ["AAA01",135],
    ["BBB01",72],
    ["CCC01",34],
    ["DDD01",65]
]

for grid in scores_and_id:
    print(grid)

user_id = str(input("enter the id"))
for i in range(0,len(scores_and_id)):
    if user_id == i:
        print("valid")
    elif i != user_id:
        print("invalid")
        scores_and_id.append(user_id)

