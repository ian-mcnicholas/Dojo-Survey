from flask import Flask, render_template, request
app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/result', methods=['POST'])
def create_user():
    print("Got Post Info")
    print(request.form)
    name_from_form = request.form['name']
    location = request.form['location']
    language = request.form['language']
    comments = request.form['comment']
    # email_from_form = request.form['email']
    return render_template("results.html", name_on_template=name_from_form, location=location, language=language, comment=comments)






















if __name__ == "__main__":
    app.run(debug=True)

