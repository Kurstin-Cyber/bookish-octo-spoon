from flask import Flask, request

app = Flask(__name__)


@app.route('/test')
def hello():
    print('Hi, the hello() function is being executed')
    return "Hello Kurstin"


users = {
    "Kurstin": {
        "mobile_phone": "555-567-1234",
        "todos": [
            {
                "description": "get email address",
                "completed": False
            }
        ]
    },
    "Matthew": {
        "mobile_phone": "555-567-1236",
        "todos": [
            {
                "description": "get email address",
                "completed": False
            }
        ]
    }
}


@app.route('/users')
def get_all_users():
    my_users = []
    for key in users:
        user = {
            "username": key,
            "mobile_phone": users[key]['mobile_phone'],
            "todos": users[key]['todos']
        }
        my_users.append(user)
    return {
               "users": my_users
    }, 200


@app.route("/users/<username>")
def get_user_by_username(username):
    if username in users:
        return{
            "username": username,
            "mobile_phone": users[username]['mobile_phone'],
            "todos": users[username]['todos']
    }
    else:
        return {
            "message": f"User with username {username} does not exist!"

        }, 404






app.run(port=8080)
