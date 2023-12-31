import pandas as pd

linked = pd.read_csv('C:\\Users\\arnol\\OneDrive\\Desktop\\Kaggle-Data-Analysis\\src\\linkdin_Job_data.csv')

analysts = pd.DataFrame(linked.loc[linked.job == 'Data Analyst'])
print(analysts)

#selecting all the data analyst jobs from recruiters that have less than 500 linked in followers.

rec = pd.DataFrame(linked.loc[(linked.no_of_application < 500) & (linked.job == 'Data Analyst')])
print(rec)