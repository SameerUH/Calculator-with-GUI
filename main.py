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

class Inputs():
    def __init__(self):
        self.first_num = "unknown"
        self.first_operation = "unknown"
    
    def update(self, first_num, first_operation):
        self.first_num = first_num
        self.first_operation = first_operation

user = Inputs()

@app.route("/", methods = ["POST", "GET"])
def main_screen():
    if request.method == "POST":
        number = request.form.get('number')
        operator = request.form.get('operator')
        return render_template("main_screen.html", display = (number or operator))
    else:
        return render_template("main_screen.html")

if __name__ == "__main__":
    app.run(debug=True)