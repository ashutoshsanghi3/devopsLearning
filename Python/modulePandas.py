#Create a venv for pandas and pip install pandas in that
import pandas as pd 
data = {'name':['ashutosh','vilas','raghav'],'subject':['python','java','sql'],'marks':[80,50,70]}

df=pd.DataFrame(data)
# print("Data")
# print(df)

# for index,row in df.iterrows():
#     print(f'{index}')
#     print(f'{row['name']}')

# A list of date strings
date_list = ['2025-02-01', '2025-02-02', '2025-02-03', '2025-02-04']

# Convert to a DatetimeIndex (Pandas handles conversion)
dates = pd.to_datetime(date_list)
print(dates)