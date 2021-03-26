import pandas as pd
# https://www.kaggle.com/kaggle/kaggle-survey-2018

raw = pd.read_csv("./raw_data/multipleChoiceResponses.csv")

q21 = "Q21_Part_"
q21_list = []
for i in range(1, 14):
	q21_list.append(q21 + str(i))

column_list = ['Q6','Q8','Q9','Q22']
column_list.extend(q21_list)

processed = raw[column_list]
processed.to_json("./data.json")


print(len(processed.Q6.unique()))
# There are 23 unique job titles in the dataset; need to narrow down to most common titles
