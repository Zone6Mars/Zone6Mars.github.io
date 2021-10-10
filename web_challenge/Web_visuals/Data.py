import pandas as pd

# Read the csv file in
df = pd.read_csv('Resources/Clean_City_List_Info.csv')

# Save to file
df.to_html('data.html', index=False)

# Assign to string
table = df.to_html()
print(table)