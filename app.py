from flask import Flask, render_template

app = Flask(__name__)

class Cat:
    def __init__(self, name, age, picture):
        self.name = name
        self.age = age
        self.picture = picture

cat1 = Cat("Mises", 5, "IMG_0814.jpg")
cat2 = Cat("Snowball", 1, "IMG_08dsfasdf14.jpg")
cat3 = Cat("Garfield", 7, "dfasfd4.jpg")
cat4 = Cat("Puss", 15, "IMG_0814.jpg")

my_list = [cat1, cat2, cat3, cat4]

@app.route('/')
def home():
    return render_template("index.html", cat_list = my_list, title = "Cats-R-Us")

@app.route("/cat/<name>")
def show_cat(name):
    for cat in my_list:
        if cat.name == name:
            return render_template("cat.html", cat = cat, title = cat.name)
    return "Nope"


if __name__ == "__main__":
    app.env = "development"
    app.run(port=80, host="localhost", debug=True)