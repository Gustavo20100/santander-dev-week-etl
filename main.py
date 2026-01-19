from extract import extract_users
from transform import transform
from load import load

def main():
    users = extract_users()
    users = transform(users)
    load(users)

if __name__ == "__main__":
    main()
