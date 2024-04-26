from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from Word import Word
from translate_ollama import translate

import time
import json
import csv

options = webdriver.FirefoxOptions()
options.add_argument("--headless")
driver = webdriver.Firefox(options=options)

driver.get("https://www.oxfordlearnersdictionaries.com/wordlists/oxford3000-5000")
WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, "onetrust-accept-btn-handler"))
).click()

list_element = driver.find_element(By.CSS_SELECTOR, "ul.top-g")
list = list_element.find_elements(By.TAG_NAME, "li")
output_list = []
error_list = []
for i in range(len(list)):
    try:
        word = Word()
        word.name = list[i].get_attribute("data-hw")
        word.level = list[i].get_attribute("data-ox5000")
        word.type_word = list[i].find_element(By.CSS_SELECTOR, "span.pos").get_property("innerText")
        translated_word = translate(word.name, word.type_word)
        word.traduction = translated_word.get("traduction") if "traduction" in translated_word else translated_word.get("translation")
        word.example = translated_word["example"]
        word.example_traduction =  translated_word.get("example_traduction") if "example_traduction" in translated_word else translated_word.get("example_translation")
        print(word)
        output_list.append(word)
    except Exception as e:
        error_list.append(word.name)
        print("Error with word:  " + word.name + " " + str(e))

print('----------------- Error list -----------------')
for error_word in error_list:
    print(word)

dict_list = [word_dict.__dict__() for word_dict in output_list]

json_output = json.dumps(dict_list, ensure_ascii=False, indent=4)

with open("output.json", "w", encoding="utf-8") as outfile:
    outfile.write(json_output)

fieldnames = ["name", "level", "type_word", "traduction", "example", "example_traduction"]

csv_filename = "output.csv"

with open(csv_filename, mode="w", newline="", encoding="utf-8") as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    
    for row in dict_list:
        writer.writerow(row)
 
time.sleep(5)
driver.quit()