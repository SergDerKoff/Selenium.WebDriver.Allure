"""
Тест погода
"""
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

def test_weather():
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)

    driver.get("https://www.gismeteo.ru/weather-cheboksary-4361/")

    x_path_10 = '/html/body/header/div[2]/div[2]/div/div[2]/div/a[5]'
    element = driver.find_element(By.XPATH, value=x_path_10)
    element.click()
    # ищем по имени класса нужный текст 
    car = driver.find_element(By.CLASS_NAME, value="triggers-info")
		# проверяем соответствие
    assert car.text == 'Пора менять резину', "Unexpected car"
