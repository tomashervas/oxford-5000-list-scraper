import json
from ollama import generate

def translate(word, type_word = None):
  prompt = f'''
          Hola, puedes traducir la palabra "{word}", es un "{type_word}", puedes contestar en formato JSON?
          {{
            "traduction":"traduccion de la palabra en castellano"
            "example":"una frase de ejemplo en ingles que la contenga"
            "example_traduction":"traduccion de la frase de ejemplo al español"
          }}
          '''
  response = generate('phi3', prompt)
  response_json = response['response'].replace("```json\n", "").replace("```", "")
  data = json.loads(response_json)
  return data

if __name__ == "__main__":
  print(translate("bath", "noun"))
