ids = 0
while True:
    user_id = input("enter the user id")
    ids += 1
    if ids == 5:
        break
scores = 0
while True:
    top_scores = int(input("enter the scores"))
    scores +=1
    if scores == 5:
        break
grid = [[ "x" for cols in range(4)] for rows in range(6)]
