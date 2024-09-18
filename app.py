from flask import Flask, render_template, request
#from transformers import pipeline
#sent_pipeline = pipeline("sentiment-analysis")

from nltk.sentiment import SentimentIntensityAnalyzer
sia = SentimentIntensityAnalyzer()


app = Flask(__name__)

# Set up the sentiment analysis pipeline


@app.route('/', methods=['GET', 'POST'])
def index():
    sentiment = None  # Initialize sentiment to None
    if request.method == 'POST':
        # Get the user input from the form
        text = request.form['text']
        
        # Analyze sentiment
        sentiment = sia.polarity_scores(text)
        #sentiment = sent_pipeline(text)[0]
    
    # Render the template and pass the sentiment result (if any)
    return render_template('index.html', sentiment=sentiment, pagetitle="home page", custom_css="main")

if __name__ == '__main__':
    app.run(debug=True)
