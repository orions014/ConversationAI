__author__ = 'Mitu'
from perspective import Perspective
from googletrans import Translator
import pandas as pd
from langdetect import detect
from sklearn.metrics import precision_recall_curve
from sklearn.metrics import average_precision_score


p = Perspective("AIzaSyDA41FbGVbRgcjnkzx_YjwoDa1qkxRpoA8")
translator = Translator()

dfs = pd.read_excel('comment.xlsx')

commentColumn = [column for column in dfs['comment']]

y_score = [column for column in dfs['score']]

y_perspective_score =[]

index = 0
for comment in commentColumn:


    # print("index {} {}".format(index,comment))

    if detect(comment) != "en":
        try:
            comment = translator.translate(comment)
            comment = comment.text
        except:
            print("something occurred while converting to english. ")
    try:
        score = p.score(comment, tests=["TOXICITY"])
        score = score["TOXICITY"].score

        if score >= 0 and score <= 0.3:
            y_perspective_score.append(0)

        else:
            y_perspective_score.append(1)

    except:
        print("something occurred while calculating perspective score ")
        y_perspective_score.append(0)

    # print("my_give score {}, perspective score {}".format(y_score[index],y_perspective_score[index]))
    # print("/n")
    index+=1



# print("y_score length",len(y_score))
# print("y_perspective_score length",len(y_perspective_score))


# Precision P = TP/(TP+ FP)
# Recall R = TP/(TP + FN)

tp = 0
fp = 0
fn = 0

for i in range(len(y_score)):
    if y_score[i] == y_perspective_score[i]:
        tp += 1
    elif y_score[i] == 0 and y_perspective_score[i] == 1:
        fp += 1
    elif y_score[i] == 1 and y_perspective_score[i] == 0:
        fn += 1

print("True positive {}".format(tp))
print("False positive {}".format(fp))
print("False negative {}".format(fn))
precision = tp / (tp+fp)

print("Precision {}".format(precision))


recall = tp / (tp+fn)

print("Recall {}".format(recall))






