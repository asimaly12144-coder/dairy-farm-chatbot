from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():

    reply = ""

    if request.method == "POST":

        question = request.form["user_input"].lower()

        if question == "what is your father's profession?":
            reply = "My father is a Dairy Farmer."

        elif question == "what is your father's current post?":
            reply = "My father is the Owner and Manager of a Dairy Farm."

        elif question == "what are his responsibilities?":
            reply = "He manages cows and buffaloes, takes care of their health, feeding, and milk production."

        elif question == "what products are produced on the dairy farm?":
            reply = "The dairy farm produces milk, yogurt, butter, cheese, and other dairy products."

        elif question == "how can the dairy farm grow in the future?":
            reply = "The dairy farm can grow by increasing the number of animals, improving milk production, and expanding sales."

        elif question == "what promotion can your father get?":
            reply = "Since my father owns the business, there is no official promotion. However, he can expand the farm and become a large-scale dairy entrepreneur."

        else:
            reply = "Sorry, I don't understand that question."

    return render_template("index.html", reply=reply)

if __name__ == "__main__":
    app.run(debug=True)