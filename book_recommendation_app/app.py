from flask import Flask, render_template, request, jsonify
from recommendation import get_recommendations  # Import your recommendation logic

app = Flask(__name__)

# Route for the homepage
@app.route('/')
def index():
    return render_template('index.html')  # Load HTML template

# Route to get book recommendations
@app.route('/recommend', methods=['POST'])
def recommend():
    book_name = request.form['book_name']  # Get book name from user input
    recommendations = get_recommendations(book_name)  # Get recommendations using your logic
    return jsonify(recommendations)  # Return recommendations as JSON

if __name__ == '__main__':
    app.run(debug=True)  # Run the Flask app in debug mode
