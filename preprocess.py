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


# Find out which columns to use from Q6 (job titles)
print(len(processed.Q6.unique()))
# There are 23 unique job titles in the dataset; need to narrow down to most common titles
proportion_jobs = {}
total_jobs = processed.shape[0] - processed['Q6'].isna().sum() # total rows without NaN for Q22

for job in processed.Q6.unique():
	count = processed.loc[processed.Q6 == job, 'Q22'].count()
	proportion_jobs[job] = count/total_jobs * 100

proportion_jobs = {k: v for k, v in sorted(proportion_jobs.items(), reverse=True, key=lambda x: x[1])}
print(proportion_jobs)

# Data Scientist > Software Engineer > Data Analyst > Research Scientist > Consultant > Data Engineer > Business Analyst 


# Find out which columns to use from Q21 (visualization tools)
proportion = {}
total = processed.shape[0] - processed['Q22'].isna().sum() # total rows without NaN for Q22

for tool in processed.Q22.unique():
	count = processed.loc[processed.Q22 == tool, 'Q22'].count()
	proportion[tool] = count/total * 100

proportion = {k: v for k, v in sorted(proportion.items(), reverse=True, key=lambda x: x[1])}
print(proportion)

# The top 5 responses: Matplotlib, ggplot2, Seaborn, Plotly, D3, take up 96% of the responses; should only include these 


