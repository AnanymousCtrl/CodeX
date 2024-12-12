from flask import Flask, render_template,request
from textblob import TextBlob

app = Flask(__name__)

def sent_ana(text):
    blob = TextBlob(text)

    senti = blob.sentiment
    polar = senti.polarity
    if polar>0:
        sent_category = "Positive"
    elif polar == 0:
        sent_category = "Neutral"
    else:
        sent_category = "Negative"
    
    return sent_category

@app.route("/", methods=['GET','POST'])
def index():
    category = None
    if request.method == 'POST':
        text = request.form['text']
        category = sent_ana(text)

    return render_template("index.html", category=category)

if __name__ == "__main__":
    app.run(debug=True)
