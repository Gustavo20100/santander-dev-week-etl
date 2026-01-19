import pandas as pd

def extract_users(path="SDW2023.csv"):
    users = pd.read_csv(path).to_dict(orient="records")
    for user in users:
        user["news"] = []
    return users
