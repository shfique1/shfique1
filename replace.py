import pandas as pd
df=pd.read_csv('Jcpenney_Men_Data.csv')
#df = pd.read_csv('data.csv')  # Replace 'data.csv' with the name of your CSV file

# Rename the 'description' column to 'material'
df.rename(columns={'Description': 'Material'}, inplace=True)

# Save the updated DataFrame to the same CSV file
df.to_csv('Jcpenney_Men_data1.csv', index=False)