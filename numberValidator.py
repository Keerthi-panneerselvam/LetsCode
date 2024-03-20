import pandas as pd

# Sample dataframe
data = {'strings': ['100', '001', '007', '099', '870']}
df = pd.DataFrame(data)

# Check if the dataframe contains a specific value
def dataframe_contains_value(df, value):
    for string in df['strings']:
        if int(string) == value:
            return True
    return False

# Check if the dataframe contains the specified value
contains_value = dataframe_contains_value(df, 7)

print(f"{contains_value}")
