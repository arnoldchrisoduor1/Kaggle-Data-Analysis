import pandas as pd

fruits = pd.DataFrame({
    'Apples' : [23, 45, 76],
    'Oranges' : [56, 23, 89],
    'Mangoes' : [56, 76, 98]
}, index = ["Year 2004", "Year 2006", "Year 2009"])

print(fruits)
print("__________________________")