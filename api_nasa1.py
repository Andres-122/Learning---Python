'''
Application Programming Interface
Nasa API: https://api.nasa.gov/
API_KEY_NASA:pT9aXQh1kBKGCUkpTzRs6T7C6TY3XaaF6eoIRmyT
Developer: Andres Camilo Rivera
Data: 24.01.2024
Script descrription: Get data from NASA API about comets
'''
import requests

def get_comet_data(api_key):
    print("::: COMET INFORMATION :::")
    url=f"https://api.nasa.gov/neo/rest/v1/neo/3726712?api_key={api_key}"
    
    try:
    #Solicitud a la API
        response = requests.get(url)
        response.raise_for_status()
        datos = response.json()
        
        print(f"comet name: {datos['name']}") 
        print(f"comet absolute_magnitude: {datos['absolute_magnitude_h']}")
    except requests.exceptions.RequestException as e: 
        print(f"Error al realizar la petición a la API de NASA: {e}")
    
    
api_key_nasa = 'pT9aXQh1kBKGCUkpTzRs6T7C6TY3XaaF6eoIRmyT'    
get_comet_data(api_key_nasa)

