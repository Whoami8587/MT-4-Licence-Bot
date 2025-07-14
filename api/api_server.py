from flask import Flask, request, jsonify
from database.models import get_user_by_uid_and_license

app = Flask(__name__)

@app.route("/api/check_license")
def check_license():
    uid = request.args.get("uid")
    code = request.args.get("code")
    ip = request.args.get("ip")

    user = get_user_by_uid_and_license(uid, code)
    if user and user.active:
        return "ok"
    return "denied"

@app.route("/api/get_ip")
def get_ip():
    return request.remote_addr

if __name__ == "__main__":
    app.run(debug=True)
