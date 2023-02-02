import pandas as pd

#raise
# Create a 3x3 pandas DataFrame ??
data = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
df = pd.DataFrame(data, columns=['A', 'B', 'C'])

# Save the DataFrame to a .csv file
df.to_csv('a.csv', index=False)

#%%



