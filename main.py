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

@app.route("/", methods = ["POST", "GET"])
def hello_world():
    if request.method == "POST":
        number = request.form.get('number')
        operator = request.form.get('operator')
        print(number, operator)
        if number:
            return render_template("main_screen.html", display = number)
        elif operator:
            return render_template("main_screen.html", display = operator)
    else:
        return render_template("main_screen.html")

if __name__ == "__main__":
    app.run(debug=True)