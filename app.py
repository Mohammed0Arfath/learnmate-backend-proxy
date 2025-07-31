from flask import Flask, request, jsonify
import requests
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)

API_KEY = os.environ.get("IBM_API_KEY")
ENDPOINT = os.environ.get("IBM_ENDPOINT")

@app.route("/", methods=["POST"])
def proxy():
    data = request.get_json()
    goal = data.get("goal")
    skills = data.get("skills")
    hours = data.get("hours")

    prompt = f"""
    You are LearnMate, an AI education coach. A student wants to become a {goal} and currently knows {skills}. They can study {hours} hours per week.

    Generate a 12-week personalized learning roadmap using free online resources. For each week, include:
    - Topics to learn
    - Specific online resources
    - A hands-on project idea
    - Estimated study time
    """

    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }

    response = requests.post(ENDPOINT, json={"input": prompt}, headers=headers)
    return jsonify(response.json())

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
