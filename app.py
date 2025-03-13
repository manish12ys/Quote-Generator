from flask import Flask, render_template, request, jsonify
import requests
import random

app = Flask(__name__)

# Fetch all quotes once and store them in memory
cached_quotes = []

def fetch_online_quotes():
    global cached_quotes
    url = 'https://zenquotes.io/api/quotes'
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        cached_quotes = [{"text": quote["q"], "author": quote["a"]} for quote in data]
        print(f"{len(cached_quotes)} quotes cached.")
    except requests.RequestException as e:
        print(f"Error fetching quotes: {e}")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get-quote', methods=['POST'])
def get_quote():
    if not cached_quotes:
        fetch_online_quotes()
    
    if cached_quotes:
        quote = random.choice(cached_quotes)
        return jsonify(quote)
    else:
        return jsonify({'text': 'No quotes found.', 'author': 'Unknown'}), 404

if __name__ == '__main__':
    fetch_online_quotes()
    app.run(debug=True)
