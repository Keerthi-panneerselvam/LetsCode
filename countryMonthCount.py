import pandas as pd
import calendar

lines = ['123 456 /country=sg/ date=20200731',
         '123 456 /country=sg/ date=20200730',
         '123 456 /country=sg/ date=20200631',
         '123 456 /country=tw/ date=20200731',
         '123 456 /country=tw/ date=20200730',
         '123 456 /country=tw/ date=20200631',
         '123 456 /country=cn/ date=20200731',
         '123 456 /country=cn/ date=20200730',
         '123 456 /country=cn/ date=20200631',
         '123 456 /country=cn/ date=20200931',
         '123 456 /country=cn/ date=20201331',
         '123 456 /country=cn/ date=20201731',
         '123 459 /country=sg/ date=20201431',]

country_month_dict = {}
month_mapping = {str(i).zfill(2): month for i, month in enumerate(calendar.month_name) if i != 0}

# Iterate through each line and extract country, month, and value
for line in lines:
    words = line.split()
    country = None
    date = None
    value = None
    
    # Find the country, date, and value in the list of words
    for word in words:
        if word.startswith('/country='):
            country = word[9:-1]  # Extract the country code
        elif word.startswith('date='):
            date = word[5:]  # Extract the date part
        elif word.isnumeric():
            value = int(word)  # Assuming the value is numeric
    
    # Extract the month and add to the dictionary
    if country and date and value is not None:
        month = month_mapping.get(date[4:6], "invalid")  # Extract the month part
        invalid_month =  month is "invalid"

        if invalid_month:
            if country in country_month_dict:
                if "invalid" in country_month_dict[country]:
                    country_month_dict[country]["invalid"] = country_month_dict[country]["invalid"] + "|" + line
                else:
                    country_month_dict[country]["invalid"] = line
            else:
                country_month_dict[country] = {"invalid": line}
        else:
            # Check if the country exists in the dictionary
            if country in country_month_dict:
                # Check if the month exists for the country
                if month in country_month_dict[country]:
                    count = country_month_dict[country][month]
                    # Add the month and value to the dictionary
                    country_month_dict[country][month] = count + value
                else:
                    # If month is not present, set the value to 0
                    country_month_dict[country][month] = value
            else:
                # If country is not present, add it to the dictionary with the specified month and value of 0
                country_month_dict[country] = {month: value}

# Convert the dictionary to a DataFrame
df = pd.DataFrame.from_dict(country_month_dict, orient='index')
df.index.name = 'Country'

# Reset the index to have 'Country' as a regular column
df.reset_index(inplace=True)

# Write the DataFrame to a CSV file
df.to_csv('output.csv', index=False)
