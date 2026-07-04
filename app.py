from flask import Flask, render_template, jsonify, request
import random
import time
from datetime import datetime, timezone

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/api/predict', methods=['POST'])
def predict():
    # 1. On récupère le timestamp Unix actuel (en secondes)
    current_timestamp = int(time.time())
    
    # 2. On crée une fenêtre unique de 20 secondes.
    # Tous les serveurs/appareils diviseront par 20 et obtiendront la même clé unique.
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
    
    # Heure de la génération (GMT+0 pour Abidjan)
    current_time_ci = datetime.now(timezone.utc).strftime("%H:%M:%S")
    
    return jsonify({
        "status": "success",
        "predicted_odds": predicted_odds,
        "confidence": f"{confidence}%",
        "timestamp": current_time_ci
    })

if __name__ == '__main__':
    app.run(debug=True)