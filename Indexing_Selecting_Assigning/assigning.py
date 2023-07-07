import pandas as pd

linked = pd.read_csv('C:\\Users\\arnol\\OneDrive\\Desktop\\Kaggle-Data-Analysis\\src\\linkdin_Job_data.csv')

rec = pd.DataFrame(linked.loc[(linked.no_of_application < 500) & (linked.job == 'Data Analyst')])
print(rec)