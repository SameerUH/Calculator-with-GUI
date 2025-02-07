from flask import *

"""
Going to work on a new project which is a calculator with a GUI.

Features:
    - Background.
    - Storing variables.
    - Addition, subtraction, multiplication, division, percentage of, percentage add, percentage minus, square, square root.
    - Interface.
    - Custom colour scheme.
"""

app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template("main_screen.html")

if __name__ == "__main__":
    app.run(debug=True)