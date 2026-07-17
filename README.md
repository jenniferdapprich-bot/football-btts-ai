# Football BTTS AI

## Vorhersage des Wettmarktes „Both Teams To Score (BTTS)“ mit Machine Learning

Dieses Projekt entstand im Rahmen der Weiterbildung zum **Certified AI Engineer**.

Ziel des Projekts ist die Entwicklung eines Machine-Learning-Modells zur Vorhersage des Fußball-Wettmarktes **Both Teams To Score (BTTS)**. Anhand historischer Spielerdaten der englischen Premier League wird vorhergesagt, ob beide Mannschaften in einem Spiel mindestens ein Tor erzielen.

Das Projekt bildet den vollständigen Machine-Learning-Prozess ab – von der Datenaufbereitung über das Feature Engineering bis hin zur Entwicklung und Bewertung verschiedener Modelle.

---

# Projektübersicht

Für das Projekt wurden historische Spielerdaten der englischen Premier League verarbeitet und verschiedene Machine-Learning-Modelle entwickelt und miteinander verglichen.

Folgende Modelle wurden umgesetzt:

- Logistic Regression (Baseline)
- Neuronales Netzwerk V1
- Neuronales Netzwerk V2 (mit erweiterten Features)

Zur Bewertung der Modelle wurden folgende Kennzahlen verwendet:

- Accuracy
- Precision
- Recall
- F1-Score

---

# Datengrundlage

Die verwendeten Daten stammen von:

**https://www.football-data.co.uk/**

Verarbeitet wurden rund **1.900 Premier-League-Spiele** aus fünf Spielzeiten.

Die Datensätze enthalten unter anderem:

- Tore
- Torschüsse
- Schüsse auf das Tor
- Fouls
- Gelbe Karten
- Rote Karten
- Wettquoten

---

# Feature Engineering

Zur Verbesserung der Modellleistung wurden verschiedene Features auf Basis der letzten fünf Spiele jeder Mannschaft erstellt.

Verwendete Features:

- HomeGoalsLast5
- AwayGoalsLast5
- HomeConcededLast5
- AwayConcededLast5
- HomeFormLast5
- AwayFormLast5

Zusätzliche Features für das zweite neuronale Netzwerk:

- HomeShotsOnTargetLast5
- AwayShotsOnTargetLast5
- HomeBTTSRateLast5
- AwayBTTSRateLast5

Alle Features wurden ausschließlich aus vergangenen Spielen berechnet, wodurch Data Leakage vermieden wurde.

---

# Verwendete Modelle

## Logistic Regression

- Basismodell
- Standardisierung der Eingabedaten
- Umsetzung mit Scikit-learn

## Neuronales Netzwerk V1

- TensorFlow / Keras
- Dense Layers
- Dropout-Regularisierung
- ReLU-Aktivierung
- Sigmoid-Ausgabe

## Neuronales Netzwerk V2

Erweiterte Version des neuronalen Netzwerks mit zusätzlichen Features.

---

# Ergebnisse

| Modell | Accuracy | Precision | Recall | F1-Score |
|---------|----------|-----------|--------|---------|
| Logistic Regression | 0.548 | 0.572 | 0.904 | 0.702 |
| Neuronales Netzwerk V1 | **0.591** | **0.597** | 0.927 | **0.726** |
| Neuronales Netzwerk V2 | 0.540 | 0.541 | **0.929** | 0.684 |

Das erste neuronale Netzwerk erzielte insgesamt die beste Modellleistung.

---

# Verwendete Technologien

- Python
- Pandas
- NumPy
- Scikit-learn
- TensorFlow / Keras
- Matplotlib
- Joblib
- Jupyter Notebook
- Visual Studio Code
- Git & GitHub

---

# Projektstruktur

```text
BTTS_AI_PROJECT
│
├── app/
├── data/
├── docs/
├── images/
│
├── models/
│   ├── neural_network_v1.keras
│   ├── neural_network_v2.keras
│   ├── scaler_v1.pkl
│   └── scaler_v2.pkl
│
├── notebooks/
│   ├── 01_data_understanding.ipynb
│   ├── 02_feature_engineering.ipynb
│   ├── 03_baseline_logistic_regression.ipynb
│   ├── 04_neural_network.ipynb
│   ├── 05_advanced_features.ipynb
│   ├── 06_neural_network_v2.ipynb
│   ├── 07_model_evaluation.ipynb
│   └── 08_prediction_demo.ipynb
│
├── src/
│   └── data_loader.py
│
├── .gitignore
├── README.md
└── requirements.txt
```

---

# Projektablauf

1. Datenimport
2. Datenaufbereitung
3. Feature Engineering
4. Training der Logistic Regression
5. Training der neuronalen Netzwerke
6. Modellbewertung
7. Vergleich der Ergebnisse
8. Vorhersage neuer Spiele

---

# Mögliche Weiterentwicklungen

Folgende Erweiterungen wären zukünftig denkbar:

- Integration von Expected Goals (xG)
- Einsatz weiterer Machine-Learning-Algorithmen (z. B. XGBoost)
- Hyperparameter-Optimierung
- Einbindung weiterer europäischer Ligen
- Nutzung größerer Datensätze
- Kalibrierung der Vorhersagewahrscheinlichkeiten

---

# Dokumentation

Die vollständige Projektarbeit wird nach Abschluss der Bewertung im Ordner **docs** bereitgestellt.

---

# Autorin

**Jennifer Dapprich**

Projektarbeit im Rahmen der Weiterbildung zum **Certified AI Engineer**

2026

---

# Lizenz

Dieses Repository dient ausschließlich zu Lern-, Demonstrations- und Dokumentationszwecken.
