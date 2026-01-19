def transform(users):
    for user in users:
        user["news"].append({
            "icon": "credit.svg",
            "description": f"{user['name']}, invista hoje para garantir seu futuro financeiro."
        })
    return users
