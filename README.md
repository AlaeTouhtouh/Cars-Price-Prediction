# 🚗 Cars Price Prediction

Ce projet a pour objectif de prédire le **prix des voitures** à partir de différentes caractéristiques (année, kilométrage, marque, carburant, etc.) en utilisant des techniques de **Machine Learning**. Le projet inclut plusieurs notebooks pour l’exploration des données, la préparation, l’entraînement et l’évaluation des modèles.

## 📂 Structure du projet

CARS/
├─ api/ # API Flask pour déployer le modèle
│ ├─ app.py
│ └─ main.py
├─ data/ # Données (non incluses dans le dépôt)
│ └─ raw/car_price_prediction.csv
├─ models/ # Modèles et transformateurs (non inclus)
│ ├─ model.pkl
│ ├─ scaler.pkl
│ ├─ label_encoders.pkl
│ └─ one_hot_encoder.pkl
├─ notebooks/ # Notebooks pour EDA, préparation et entraînement
│ ├─ EDA.ipynb
│ ├─ first-stage.ipynb
│ ├─ training-final.ipynb
│ ├─ training-target-encoding.ipynb
│ └─ training.ipynb
├─ scripts/ # Scripts Python pour preprocessing
│ └─ preprocessing.py
└─ README.md

markdown
Copier le code

> Les dossiers `data/` et `models/` **ne contiennent pas les fichiers lourds** pour éviter des problèmes de push GitHub.

## 🔧 Technologies utilisées

- Python 3.12  
- Pandas, NumPy  
- Scikit-learn (RandomForestRegressor, LinearRegression, etc.)  
- Jupyter Notebook  
- Flask (pour l’API)

## 🤖 Modélisation

Différents modèles ont été testés pour prédire le prix :  

- **Linear Regression** → simple, interprétable, mais limité pour des relations non linéaires.  
- **Random Forest Regressor** → modèle d’ensemble capable de capturer des relations complexes entre les variables.

Après comparaison, le **RandomForestRegressor** a été retenu comme modèle final, car il offre **la meilleure précision et une bonne généralisation**.

## 📂 Données et test du projet

Le dataset utilisé provient de **[Kaggle](https://www.kaggle.com/)**. Les fichiers CSV et les modèles ne sont pas inclus dans ce dépôt.  

Pour tester le projet sans télécharger le dataset complet, vous pouvez créer un mini fichier CSV `data/car_price_prediction.csv` avec cet exemple :  

```csv
year,mileage,brand,fuel,price
2015,50000,Toyota,Gasoline,15000
2018,30000,Honda,Gasoline,18000
2017,40000,Ford,Diesel,16000
2016,45000,Nissan,Gasoline,15500
2019,20000,Volkswagen,Diesel,20000
Instructions pour tester :
Créez le dossier data/ si ce n’est pas déjà fait.

Copiez le mini CSV ci-dessus dans data/car_price_prediction.csv.

Lancez les notebooks pour explorer les données et entraîner le modèle :

bash
Copier le code
cd notebooks
jupyter notebook
Une fois le modèle entraîné, vous pouvez l’utiliser via l’API Flask :

bash
Copier le code
cd api
python app.py
⚠️ Remarque
Les fichiers lourds (.csv, .pkl) ne sont pas suivis par Git pour respecter la limite GitHub.

Si vous souhaitez partager les modèles ou de gros fichiers, utilisez Git LFS.

✨ Objectif
Ce projet est destiné à apprendre et démontrer la construction d’un pipeline de Machine Learning complet, allant de la préparation des données à la mise en production via une API.
