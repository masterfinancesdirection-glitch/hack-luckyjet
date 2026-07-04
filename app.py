from flask import Flask, render_template, jsonify, request
import random
from datetime import datetime
from zoneinfo import ZoneInfo

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/api/predict', methods=['POST'])
def predict():
    rand = random.random()
    if rand < 0.70:
        predicted_odds = round(random.uniform(1.85, 6.50), 2)
    else:
        predicted_odds = round(random.uniform(6.50, 32.40), 2)
        
    confidence = random.randint(89, 99)
    
    # Heure exacte d'Abidjan pour le marquage du signal
    tz_ci = ZoneInfo("Africa/Abidjan")
    current_time_ci = datetime.now(tz_ci).strftime("%H:%M:%S")
    
    return jsonify({
        "status": "success",
        "predicted_odds": predicted_odds,
        "confidence": f"{confidence}%",
        "timestamp": current_time_ci
    })

if __name__ == '__main__':
    app.run(debug=True)