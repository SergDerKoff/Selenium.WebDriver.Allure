# импортируем модули и отдельные классы
import pytest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from tests.helper.common import CommonHelper

# каждый тест должен начинаться с test_

def test_qastudio_buy_lamp():
    """
    Test case qastudio
    """
    # Описываем опции запуска браузера
    chrome_options = Options()
    chrome_options.add_argument("start-maximized") # открываем на полный экран
    chrome_options.add_argument("--disable-infobars") # отключаем инфо сообщения
    chrome_options.add_argument("--disable-extensions") # отключаем расширения
    # chrome_options.add_argument("--headless") # спец. режим "без браузера"
	
	# устанавливаем webdriver в соответствии с версией используемого браузера
    service = Service(ChromeDriverManager().install())
    # запускаем браузер с указанными выше настройками
    driver = webdriver.Chrome(service=service, options=chrome_options)
	# определяем адрес страницы для теста и переходим на неё
    url = "https://testqastudio.me/"
    driver.get(url=url)

    element = driver.find_element(by=By.CSS_SELECTOR, value="[class='tab-new ']")
    element.click()
    
    x_path_lamp = '//*[@id="rz-shop-content"]/ul/li[4]/div/div[1]/a/img'
    element = driver.find_element(By.XPATH, value=x_path_lamp)
    element.click()

    element = driver.find_element(by=By.CSS_SELECTOR, value="[name='add-to-cart']")
    element.click()
    
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((
        By.XPATH, '//*[@id="cart-modal"]/div[2]/div[2]/div/div/p[2]/a[2]'))).click()

    common_helper = CommonHelper(driver)
    common_helper.enter_input(input_id="billing_first_name", data="Serg")
    common_helper.enter_input(input_id="billing_last_name", data="Der")
    common_helper.enter_input(input_id="billing_address_1", data="1-11, Live street")
    common_helper.enter_input(input_id="billing_city", data="Bor")
    common_helper.enter_input(input_id="billing_state", data="Bor")
    common_helper.enter_input(input_id="billing_postcode", data="332244")
    common_helper.enter_input(input_id="billing_phone", data="+79996543210")
    common_helper.enter_input(input_id="billing_email", data="serg123tro@mail.ru")

    payments_el = '//*[@id="payment"] [contains(@style, "position: static; zoom: 1;")]'
    WebDriverWait(driver, timeout=10, poll_frequency=1).until(
        EC.presence_of_element_located((By.XPATH, payments_el)))
    driver.find_element(by=By.ID, value="place_order").click()

    WebDriverWait(driver, timeout=5, poll_frequency=1).until(
        EC.url_changes("https://test.qa.studio/?page_id=10"))

    result = WebDriverWait(driver, timeout=10, poll_frequency=2).until(
        EC.text_to_be_present_in_element(
            (By.CSS_SELECTOR, "p.woocommerce-thankyou-order-received"), \
                "Ваш заказ принят. Благодарим вас."))

    assert result, 'Unexpected notification text'
