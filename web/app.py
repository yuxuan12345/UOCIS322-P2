"""
John Doe's Flask API.
"""

from flask import Flask, send_from_directory, abort

app = Flask(__name__)

@app.route("/")
def hello():
    return "UOCIS docker demo!\n"

@app.route("/<path:file>")
def OK(file):
    if (("//" in file) or ("~" in file) or (".." in file)):
        abort(403)
    return send_from_directory("./", file)

@app.errorhandler(403)
def error_403(e):
    return send_from_directory("./", "403.html"), 403

@app.errorhandler(404)
def error_404(e):
    return send_from_directory("./", "404.html"), 404

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
