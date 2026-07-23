from flask import Flask, render_template, jsonify, request
import random
import time
from datetime import datetime, timezone, timedelta

app = Flask(__name__)

# Code d'accès obligatoire
ACCESS_CODE = "SDYAHV2517"

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/api/predict', methods=['POST'])
def predict():
    data = request.get_json() or {}
    user_code = data.get('access_code', '')

    # Sécurité : On valide le code d'accès reçu du terminal
    if user_code != ACCESS_CODE:
        return jsonify({
            "status": "error",
            "message": "ACCESS DENIED: INVALID SECURITY KEY"
        }), 403

    # 1. On récupère le timestamp Unix actuel (en secondes)
    current_timestamp = int(time.time())
    
    # 2. On crée une fenêtre unique de 20 secondes.
    time_window = current_timestamp // 20
    
    # 3. On utilise cette clé comme GRAINE (Seed) pour le générateur
    random.seed(time_window)
    
    # 4. L'algorithme génère maintenant une cote identique pour cette tranche de 20s
    rand = random.random()
    if rand < 0.70:
        predicted_odds = round(random.uniform(1.85, 6.50), 2)
    else:
        predicted_odds = round(random.uniform(6.50, 32.40), 2)
        
    confidence = random.randint(89, 99)
    
    # Heure de la génération avancée de 45 secondes
    time_plus_45s = datetime.now(timezone.utc) + timedelta(seconds=45)
    current_time_ci = time_plus_45s.strftime("%H:%M:%S")
    
    return jsonify({
        "status": "success",
        "predicted_odds": predicted_odds,
        "confidence": f"{confidence}%",
        "timestamp": current_time_ci
    })

if __name__ == '__main__':
    app.run(debug=True)