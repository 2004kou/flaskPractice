from flask import Flask, render_template

app = Flask (__name__)

@app.route("/")
def index():
   first_name = "John"
   stuff = "This is  bold text"
   favorite_pizza = [
       "Pepperoni",
       "Cheese",
       "Mushrooms",
       41

   ]
   return render_template("index.html", 
                          first_name=first_name,
                          stuff = stuff,
                          favorite_pizza = favorite_pizza)

#def index():
 #   return "<h1> Hello World!</h1>"



@app.route("/user/<name>")
def user(name):
    return render_template("user.html", user_name=name)


@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"),404

#サーバーエラーページ
@app.errorhandler(500)
def page_not_found(e):
    return render_template("404.html"),500
