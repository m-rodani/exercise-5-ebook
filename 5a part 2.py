scores_and_id = ["AAA01","BBB01","CCC01","DDD01"] , ["135","87","188","10"]
list(scores_and_id)
for grid in scores_and_id:
    print(grid)
user_id = input("enter your id")
for i in scores_and_id:
    if i == user_id:
        print("valid")
    elif i != user_id:
        scores_and_id.__add__(user_id)
        scores_and_id.__add__(0)
for grid in scores_and_id:
    print(grid)
