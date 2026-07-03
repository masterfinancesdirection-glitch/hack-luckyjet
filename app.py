from flask import Flask, render_template, jsonify
import random
from datetime import datetime
from zoneinfo import ZoneInfo

app = Flask(__name__)

def generate_lucky_jet_odds():
    """
    Génère une fausse prévision de cote strictement comprise entre 1.85 et 35.70.
    """
    rand = random.random()
    if rand < 0.60:
        return round(random.uniform(1.85, 5.00), 2)
    elif rand < 0.90:
        return round(random.uniform(5.00, 15.00), 2)
    else:
        return round(random.uniform(15.00, 35.70), 2)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/api/predict')
def predict():
    predicted_odds = generate_lucky_jet_odds()
    confidence = random.randint(84, 99)
    
    # Extraction de l'heure précise basée sur le fuseau horaire de la Côte d'Ivoire
    tz_ci = ZoneInfo("Africa/Abidjan")
    current_time_ci = datetime.now(tz_ci).strftime("%H:%M:%S")
    
    return jsonify({
        "status": "success",
        "program_name": "Hack Lucky jet Algorithme",
        "predicted_odds": predicted_odds,
        "confidence": f"{confidence}%",
        "timestamp": f"{current_time_ci} (GMT)"
    })

if __name__ == '__main__':
    app.run(debug=True)