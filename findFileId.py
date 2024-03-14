import pandas as pd
import json
import re

# Sample JSON inputs
# json_inputs = [
#     {'path': '/external/datasource/nca/cobt_cn_20240229.csv', 'action': 'upload'},
#     {'path': '/external/datasource/mot_ilms/ilms_20240229.csv', 'action': 'upload'},
#     {'path': '/external/datasource/mot_ds_ap/ds_ap_20240229.csv', 'action': 'upload'},
#     {'path':'/external/datasource/nca/cobt_ae_20240229.csv', 'action': 'upload'}
# ]

# JSON dump
json_input_dump = '{"path": "/external/datasource/nca/cobt_cn_20240229.csv", "action": "upload"}'

# Convert JSON dump to Python dictionary
json_input = json.loads(json_input_dump)

# Sample pandas DataFrame
data = {
    'file_id': [1, 2, 3],
    'app_code': ['cobt_cn', 'ilms', 'ds_ap'],
    'lobt': ['nca', 'mot', 'mot']
}

df = pd.DataFrame(data)

# Function to extract file name before date from path
def extract_filename(path):
    return re.search(r'([^/]+)_\d{8}\.csv', path).group(1)

# Function to find corresponding file_id
def find_file_id(path, master_df):
    filename = extract_filename(path)
    row = master_df[master_df['app_code'] == filename]
    if not row.empty:
        return row
    else:
        return None

# Extracting file_ids
if  json_input['action'].lower() == 'upload':
    master_input = find_file_id(json_input['path'], master_df=df)
    if master_input is not None:
        print(master_input, type(master_input))