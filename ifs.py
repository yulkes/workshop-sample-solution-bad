import os
import os.path

from flask import Flask, request

app = Flask(__name__)

@app.route("/fs/", methods=["GET"])
@app.route("/fs/*", methods=["GET"])
def get():
    path = request.path.lstrip("/fs/") or "."
    dirs = []
    files = []
    for file in os.listdir(path):
        if os.path.isdir(path + "/" + file):
            dirs.append(file)
        else:
            files.append(file)
    return {"success": True, "files": files, "dirs": dirs}


@app.route("/fs/", methods=["DELETE"])
@app.route("/fs/*", methods=["DELETE"])
def delete():
    path = request.path.lstrip("/fs/") or "."
    os.remove(path)
    return {"success": True}


@app.route("/fs/", methods=["PUT"])
@app.route("/fs/*", methods=["PUT"])
def move():
    path = request.path.lstrip("/fs/") or "."
    new_path = request.json["name"]
    os.renames(path, new_path)
    return {"success": True}


if __name__ == "__main__":
    app.run(port=5000)