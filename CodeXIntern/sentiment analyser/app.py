# import textblob
from flask import Flask, render_template
from textblob import TextBlob

app = Flask(__name__)

@app.route("/", method=['GET','POST'])
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


if __name__ == "__main__":
    app.run(debug=True)
