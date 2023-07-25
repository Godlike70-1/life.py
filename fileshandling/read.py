# r = opens a file if exists, throws a error if doesnt exists
# w = opens a file for writing, creates a file if doesnt exists 
# x = creates a specified file, throws error if it already exists
# a = opens a file to add something, creates a file if doesnt exists
# t = string value or texts
# b = images or other binary values

current_score = 1001
high_score = 0
if current_score>high_score:
    f = open("score.txt","w")
    print(f.write(f"highscore = {current_score}"))
    f.close()
else:
    print("the highscore is still unbeatable")
