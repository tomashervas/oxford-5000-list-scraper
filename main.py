from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from Word import Word
from translate_ollama import translate

import time
import json



options = webdriver.FirefoxOptions()
# options.add_argument("--headless")
driver = webdriver.Firefox(options=options)

driver.get("https://www.oxfordlearnersdictionaries.com/wordlists/oxford3000-5000")
WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, "onetrust-accept-btn-handler"))
).click()

list_element = driver.find_element(By.CSS_SELECTOR, "ul.top-g")
list = list_element.find_elements(By.TAG_NAME, "li")
output_list = []
for i in range(1000,1003):
    translated_word = translate(list[i].get_attribute("data-hw"))
    print(list[i].get_attribute("data-hw"))
    print(translated_word)
    word = Word()
    word.name = list[i].get_attribute("data-hw")
    word.level = list[i].get_attribute("data-ox5000")
    word.type_word = list[i].find_element(By.CSS_SELECTOR, "span.pos").get_property("innerText")
    output_list.append(word)

    # print(f"word: {word.name}, level: {word.level}, type: {word.type_word}")

# for word in output_list:
#     print(word)

# lista_diccionarios = [palabra.__dict__() for palabra in output_list]

# json_output = json.dumps(lista_diccionarios)

# with open("output.json", "w") as outfile:
#     outfile.write(json_output)
 
time.sleep(5)
driver.quit()