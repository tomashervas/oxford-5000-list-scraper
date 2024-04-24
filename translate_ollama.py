import json
from ollama import generate

def translate(word):
  prompt = f'''
          Hola, puedes traducir la palabra "{word}", puedes contestar en formato JSON?
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

# hola = translate("hello")
# print(hola)