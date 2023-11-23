from openai import OpenAI
from textos_a_traducir import textos
import time

client = OpenAI()
i = 1

for texto_a_traducir in textos:
    print(f"Traduciendo... {i}/{len(textos)}")
    i = i + 1
    prompt = f"Necesito que vayas traduciendo y ordenando el formato un texto sobre trading, backtesting, testeos de estrategias de trading y analisis walk-forward. Aca te envio el texto y traducelo a español. Solo escribeme la version en español y no la que esta en ingles: '{texto_a_traducir}' \nNOTA PARA GPT: Recuerda que debes ordenar bien el formato y deja un renglon entre parrafo y parrafo"

    completion = client.chat.completions.create(
      model="gpt-4-1106-preview",
      messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": prompt}
      ]
    )
    
    with open('texto.txt', 'a') as file:
        file.write(completion.choices[0].message.content + "\n\n")

    time.sleep(2)