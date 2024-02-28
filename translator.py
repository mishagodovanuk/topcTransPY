import requests

def translate_text(text, target_lang):
    url = 'https://translation.googleapis.com/language/translate/v2?key=AIzaSyBoWs7ffqpwJAK0TI7A7Tp56qZiD4o0KA4'
    
    payload = {
        'target': target_lang,
        'q': text,
        'key': 'AIzaSyBoWs7ffqpwJAK0TI7A7Tp56qZiD4o0KA4'
    }
    
    try:
        response = requests.post(url, json=payload)
        response_data = response.json()
        translated_text = response_data['data']['translations'][0]['translatedText']
        
        return translated_text
        
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

def main():
    text = input("Enter the text to be translated: ")
    target_lang = input("Enter the target language (e.g., 'fr' for French): ")
    
    translated_text = translate_text(text, target_lang)
    
    if translated_text:
        print(f"Translated text: {translated_text}")
    else:
        print("Failed to translate the text.")

if __name__ == "__main__":
    main()