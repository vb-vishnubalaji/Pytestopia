import requests

db = {
    1: "Alice",
    2: "Bob",
    3: "John"
}


def get_data_from_db(user_id):
    return db.get(user_id)


def get_data_from_requests():
    res = requests.get("https://jsonplaceholder.typicode.com/users")
    if res.status_code == 200:
        return res.json()

    raise requests.HTTPError