import pandas as pd

pd.set_option("display.max_rows", 5)

linked = pd.read_csv('C:\\Users\\arnol\\OneDrive\\Desktop\\Kaggle-Data-Analysis\\src\\linkdin_Job_data.csv')
print(linked.head())
print("____________")
print()

#Selecting a specific column.
id = linked.job_ID
print(id.head())
print("____________")
print()

#Selecting the first value from the job id column.
print("A single Id")
first = linked.job_ID[0]
print(first)
print("____________")
print()

#Selecting the first row.
print("Selecting the first row")
first_row = linked.iloc[0]
print(first_row)
print()

print("Selecting the first 10 items in the entire first column")
top = linked.iloc[:10, 0]
print(top)
print()

print("Selecting items based on certain indices.")
ind = linked.iloc[[2, 4, 5, 6],:]
print(ind)
print()

#for index 23, 45, 56 56, display data for : - location, company_id, company_name
ind = linked.loc[[23, 45, 56, 67], ['location', 'company_name', 'work_type']]
print(ind)
print()