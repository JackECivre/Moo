import pandas as pd

df = pd.read_csv('results.csv')
df.drop_duplicates(inplace=True)
df.to_csv('results.csv', index=False)

