from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import pandas as pd

custom_options = Options()
custom_options.add_argument("--start-maximized")
path_driver = Service(r'chromedriver.exe')
driver = webdriver.Chrome(service=path_driver, options=custom_options)
link = "https://www.flashscorekz.com/"
driver.get(link)

class_name = "event__match"
driver_m = driver.find_elements(By.CLASS_NAME, class_name)
columns_name = ["status", "team_1", "team_2", "score_1", "score_2", "first_time_1", "first_time_2"]
data = list()
file_name = "football.xlsx"

for match in driver_m:
    match_data = match.text.splitlines()
    if match_data[0] == "Завершен":
        data.append(match_data)

result = pd.DataFrame(data, columns=columns_name)
result.to_excel(file_name, index=False)
