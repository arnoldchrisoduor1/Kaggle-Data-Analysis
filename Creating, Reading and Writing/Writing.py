import pandas as pd

animals = pd.DataFrame({
    'Goats' : 56,
    'Sheep' : 87,
    'Cows' : 78
}, index = ["Year 2000", "Year 2001", "Year 2002"])

filename = 'animals.csv'
animals.to_csv(filename, index = True)
print("Data Successfully written to CSV")