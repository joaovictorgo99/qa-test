from flask import Flask, request, jsonify
import jwt
import datetime as dt

# Config
app = Flask(__name__)
SECRET_KEY = "super-secret-key"

# Database (in memory)
tasks = []
task_id_control = 1

# Admin user
USER = {"username": "admin", "password": "123"}

# Auth
@app.route("/login", methods=["POST"])
def login():
    data = request.get_json()

    if data.get("username") == USER["username"] and data.get("password") == USER["password"]:
        token = jwt.encode(
            {
                "user": USER["username"],
                "exp": dt.datetime.now(dt.UTC) + dt.timedelta(minutes=10)
            },
            SECRET_KEY,
            algorithm="HS256"
        )

        return jsonify({"token": token})

    return jsonify({"error": "Invalid credentials"}), 401

def token_required(f):
    def wrapper(*args, **kwargs):
        auth = request.headers.get("Authorization", "")

        if not auth.startswith("Bearer "):
            return jsonify({"error": "Missing token"}), 401

        token = auth.split(" ")[1]

        try:
            jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
        except jwt.ExpiredSignatureError:
            return jsonify({"error": "Expired token"}), 401
        except jwt.InvalidTokenError:
            return jsonify({"error": "Invalid token"}), 401
        return f(*args, **kwargs)

    wrapper.__name__ = f.__name__

    return wrapper

# Tasks
@app.route("/tasks", methods=["GET"])
@token_required
def get_tasks():
    return jsonify(tasks)

@app.route("/tasks", methods=["POST"])
@token_required
def create_task():
    global task_id_control
    data = request.get_json()

    if "title" not in data:
        return jsonify({"error": "The 'title' is required"}), 400

    task = {"id": task_id_control,
            "title": data["title"],
            "description": data.get("description", ""),
            "status": "pending"}
    tasks.append(task)
    task_id_control += 1

    return jsonify(task), 201

@app.route("/tasks/<int:task_id>", methods=["GET"])
@token_required
def get_task(task_id):
    task = next((t for t in tasks if t["id"] == task_id), None)

    if not task:
        return jsonify({"error": "Task not found"}), 404

    return jsonify(task)

@app.route("/tasks/<int:task_id>", methods=["PUT"])
@token_required
def update_task(task_id):
    task = next((t for t in tasks if t["id"] == task_id), None)

    if not task:
        return jsonify({"error": "Task not found"}), 404

    data = request.get_json()
    task["title"] = data.get("title", task["title"])
    task["description"] = data.get("description", task["description"])
    task["status"] = data.get("status", task["status"])

    return jsonify(task)

@app.route("/tasks/<int:task_id>", methods=["DELETE"])
@token_required
def delete_task(task_id):
    global tasks

    if not any(t["id"] == task_id for t in tasks):
        return jsonify({"error": "Task not found"}), 404

    tasks = [t for t in tasks if t["id"] != task_id]

    return jsonify({"message": "Task removed successfully"})

if __name__ == "__main__":
    app.run(debug=True)
