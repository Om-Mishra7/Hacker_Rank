def breakingRecords(scores):
    
    # Setting flags
    Broke_Min_Score = 0
    Broke_Max_Score = 0

    # Setting initial values as the first score
    Min_Score = scores[0]
    Max_Score = scores[0]

    # Looping through the scores list and checking if the score is higher or lower than the current max or min score
    for i in range(0,len(scores)):
        if scores[i] < Min_Score:
            Min_Score = scores[i]
            Broke_Min_Score += 1
        elif scores[i] > Max_Score:
            Max_Score = scores[i]
            Broke_Max_Score += 1
    
    return[Broke_Max_Score,Broke_Min_Score]


scores = [10, 5, 20, 20, 4, 5, 2, 25, 1]

print(breakingRecords(scores))