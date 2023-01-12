import json

FILENAME = "users.json"

def load_data():
    with open(FILENAME, 'r') as file:
        users = json.load(file)
    return users

def add_entry(username, movie, seats):
    users = load_data()
    if username not in users:
        users[username] = {}
        users[username]['history'] = {}
        print("New account", username, "was created")

    users[username]['history'][movie] = seats
    print("Ticket booking was saved")
    save(users)


def save(users):
    with open(FILENAME, 'w') as file:
        file.write(json.dumps(users, indent=4))

if __name__ == '__main__':
    main()
