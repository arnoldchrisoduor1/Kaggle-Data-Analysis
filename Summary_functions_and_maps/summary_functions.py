import pandas as pd

linked = pd.read_csv('C:\\Users\\arnol\\OneDrive\\Desktop\\Kaggle-Data-Analysis\\src\\linkdin_Job_data.csv')

#Finding the mean of values
m = linked.points.mean()

#Finding the median
ma = linked.points. median()

#Checking for unique values
un = linked.country.unique()

#Counting the unique values
cu = linked.country.value_counts()

#Subtrating the prices from the mean price.
meanp = linked.points.mean()
def change(points):
    linked.points - meanp
    return points

linked.apply(change, axis='columns')

#Getting the wine with the best price to point ratio.
wine_idx = (linked.points / linked.price).idxmax()
name = linked.loc[wine_idx, 'title']
