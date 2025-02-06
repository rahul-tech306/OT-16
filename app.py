from flask import Flask, render_template, request, jsonify
import logging
from datetime import datetime

# Create and configure the Flask app
app = Flask(__name__)

# Configure logging
logging.basicConfig(level=logging.INFO, format='[%(asctime)s] %(levelname)s: %(message)s')

# Routes
@app.route("/")
def home():
    app.logger.info("Rendering Home Page")
    return render_template("index.html")

@app.route("/api/news", methods=['GET'])
def get_news():
    # Simulated news data for demonstration
    news_data = [
        {"title": "Tech Stocks Surge", "date": "2025-02-06", "content": "Positive market trends boost tech sector.", "sentiment": "Positive"},
        {"title": "Oil Prices Decline", "date": "2025-02-06", "content": "Supply issues cause oil price drop.", "sentiment": "Negative"},
        {"title": "Stable Employment Reports", "date": "2025-02-06", "content": "Balanced job reports stabilize market.", "sentiment": "Neutral"}
    ]
    app.logger.info("Sending news data to client")
    return jsonify(news_data)

@app.route("/submit-feedback", methods=['POST'])
def submit_feedback():
    feedback = request.form.get("feedback")
    if feedback:
        app.logger.info(f"Feedback received: {feedback}")
        return jsonify({"message": "Thank you for your feedback!"}), 200
    else:
        app.logger.warning("No feedback provided")
        return jsonify({"error": "Feedback cannot be empty"}), 400

@app.errorhandler(404)
def page_not_found(e):
    app.logger.error("404 error encountered")
    return render_template("404.html"), 404

@app.errorhandler(500)
def internal_server_error(e):
    app.logger.error("500 error encountered")
    return render_template("500.html"), 500

if __name__ == "__main__":
    app.logger.info("Starting the server...")
    app.run(host="0.0.0.0", port=5000, debug=True)
