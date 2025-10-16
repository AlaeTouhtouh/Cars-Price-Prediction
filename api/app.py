import streamlit as st
import requests

# Configuration de l'application
st.set_page_config(page_title="Prédiction de prix de voitures", layout="wide")
st.title("🚗 Prédiction du Prix des Voitures")

# Sidebar
st.sidebar.header("Configuration")
api_url = st.sidebar.text_input("URL de l'API", "http://localhost:8000/predict/")

# Fonction pour appeler l'API
def call_prediction_api(data):
    try:
        # Formatage des données pour correspondre exactement à ce que l'API attend
        formatted_data = {
            "Levy": data["Levy"],
            "Manufacturer": data["Manufacturer"],
            "Model": data["Model"],
            "Prod_year": data["Prod_year"],
            "Category": data["Category"],
            "Leather_interior": data["Leather_interior"],
            "Fuel_type": data["Fuel_type"],
            "Engine_volume": data["Engine_volume"],
            "Mileage": data["Mileage"],
            "Cylinders": data["Cylinders"],
            "Gear_box_type": data["Gear_box_type"],  # Nom exact attendu par l'API
            "Drive_wheels": data["Drive_wheels"],    # Nom exact attendu par l'API
            "Wheel": data["Wheel"],                 # Nom exact attendu par l'API
            "Color": data["Color"].capitalize(),
            "Airbags": data["Airbags"]
        }
        
        response = requests.post(api_url, json=formatted_data)
        if response.status_code == 200:
            return response.json()['prediction']
        else:
            st.error(f"Erreur API: {response.status_code} - {response.text}")
            return None
    except Exception as e:
        st.error(f"Erreur de connexion: {str(e)}")
        return None

# Formulaire
with st.form("car_form"):
    col1, col2, col3 = st.columns(3)
    
    with col1:
        manufacturer = st.selectbox("Marque", ['BMW', 'Lexus', 'Mercedes'])
        model = st.text_input("Modèle", "RX 350")
        category = st.selectbox("Catégorie", ['Jeep', 'Sedan'])
        prod_year = st.slider("Année", 1990, 2023, 2018)
        color = st.selectbox("Couleur", ['Black', 'Silver', 'White'])
        
    with col2:
        engine_volume = st.number_input("Volume moteur", value=2.0)
        cylinders = st.number_input("Cylindres", value=4)
        fuel_type = st.selectbox("Carburant", ['Hybrid', 'Petrol'])
        gear_box_type = st.selectbox("Boîte vitesse", ['Automatic', 'Manual'])
        drive_wheels = st.selectbox("Roues motrices", ['4x4', 'Front'])
        
    with col3:
        mileage = st.number_input("Kilométrage", value=50000)
        airbags = st.number_input("Airbags", value=6)
        leather_interior = st.selectbox("Cuir", ['Yes', 'No'])
        wheel = st.selectbox("Volant", ['Left wheel', 'Right-hand drive'])
        levy = st.number_input("Taxe", value=1000)
    
    submitted = st.form_submit_button("Estimer le prix")

if submitted:
    input_data = {
        "Levy": levy,
        "Manufacturer": manufacturer,
        "Model": model,
        "Prod_year": prod_year,
        "Category": category,
        "Leather_interior": leather_interior,
        "Fuel_type": fuel_type,
        "Engine_volume": float(engine_volume),
        "Mileage": mileage,
        "Cylinders": float(cylinders),
        "Gear_box_type": gear_box_type,
        "Drive_wheels": drive_wheels,
        "Wheel": wheel,
        "Color": color,
        "Airbags": airbags
    }
    
    with st.spinner("Calcul en cours..."):
        prediction = call_prediction_api(input_data)
    
    if prediction:
        st.success(f"Prix estimé: ${prediction:,.2f}")
        st.json(input_data)