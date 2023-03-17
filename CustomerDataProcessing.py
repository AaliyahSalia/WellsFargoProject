# Wells Fargo Customer Data Processing

# Import required libraries
import pandas as pd
import requests
import json

# QA and clean data
def clean_data(df):
    df = df.dropna()
    df = df[df['account_balance'] >= 0] 
    df['zip_code'] = df['zip_code'].astype(str).str[:5]
    return df

# Manipulate the shape of data for a business purpose
def manipulate_data(df):
    df['age'] = 2023 - df['birth_year'] 
    df['is_active'] = df['account_balance'] > 0 
    df['credit_score_category'] = pd.cut(df['credit_score'], [0, 579, 669, 739, 799, 850], labels=['Poor', 'Fair', 'Good', 'Very Good', 'Exceptional'])
    return df

# Move data between two systems
def move_data(df):
    url = "https://api.wellsfargo.com/data"
    payload = json.dumps(df.to_dict())
    headers = {'Content-Type': 'application/json'}
    response = requests.post(url, headers=headers, data=payload)
    if response.status_code == 200:
        print("Data successfully transferred to remote system.")
    else:
        print("Error transferring data to remote system.")

# Load data
df = pd.read_csv("customer_data.csv")

# Clean data
df = clean_data(df)

# Manipulate data
df = manipulate_data(df)

# Move data
move_data(df)
