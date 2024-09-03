import os
import time
import shutil
from datetime import datetime
import pandas as pd
from sqlalchemy import create_engine
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

chromedriver_path = "C:/Users/Melisacevik/Desktop/chromedriver-win32/chromedriver.exe"
service = Service(executable_path=chromedriver_path)
driver = webdriver.Chrome(service=service)

driver.get("https://xtraders.meteologica.com/")

# Login
try:
    username = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, 'username'))
    )
    password = driver.find_element(By.ID, 'password')

    username.send_keys('melisa.cevik')
    password.send_keys('*********')

    login_button = driver.find_element(By.CSS_SELECTOR, 'input[type="submit"][value="Login"]')
    login_button.click()

    WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.ID, '#row3'))
    )
except Exception as e:
    print(f"Giriş işlemi başarısız: {e}")

try:
    container = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, 'div#row3'))
    )
    analysis_button = container.find_element(By.CSS_SELECTOR,
                                             'div.header_controls.unselectable.disable-sort iron-icon[data-original-title="Analysis"]')
    driver.execute_script("arguments[0].click();", analysis_button)
    WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.CLASS_NAME, 'contenido_popup'))
    )
    time.sleep(5)
except Exception as e:
    print(f"Element bulunamadı: {e}")

try:
    meteologica_i_tag = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH, '//label[@for="1_17466"]/i'))
    )
    driver.execute_script("arguments[0].scrollIntoView(true);", meteologica_i_tag)
    time.sleep(2)
    meteologica_i_tag.click()
    print("Meteologica seçeneği başarıyla işaretlendi.")
except Exception as e:
    print(f"Element bulunamadı: {e}")

# Dinamik tarih hesaplaması ve seçimi
try:
    # Tarihlerin hesaplanması
    today = datetime.date.today()
    start_date_value = (today - datetime.timedelta(weeks=1) + datetime.timedelta(days=1)).strftime('%d/%m/%Y')
    end_date_value = (today + datetime.timedelta(days=1)).strftime('%d/%m/%Y')

    start_date = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.ID, 'analisis_calidad_rango_start'))
    )
    end_date = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.ID, 'analisis_calidad_rango_end'))
    )

    driver.execute_script("arguments[0].scrollIntoView(true);", start_date)
    start_date.click()
    start_date.clear()
    start_date.send_keys(start_date_value)

    end_date.click()
    end_date.clear()
    end_date.send_keys(end_date_value)

    time.sleep(2)
    print(f"Start Date: {start_date_value}, End Date: {end_date_value}")
except Exception as e:
    print(f"Element bulunamadı: {e}")

# Generate butonuna tıklama ve More options tıklama
try:
    # Generate butonuna tıklama
    generate_button = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable(
            (By.XPATH, "//div[contains(@class, 'botones_popup')]//span[contains(@class, 'xt-btn flat right guardar')]"))
    )
    generate_button.click()
    print("Generate butonuna tıklandı.")
    time.sleep(2)

    # "More options" butonunun görünür olmasını sağlamak için sayfayı kaydırma
    more_options_button = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.CSS_SELECTOR,
                                        "div.header_controls.unselectable.disable-sort iron-icon.header-button.button_desplegable.x-scope.iron-icon-0"))
    )
    driver.execute_script("arguments[0].scrollIntoView(true);", more_options_button)
    time.sleep(1)

    # "More options" butonuna tıklama
    more_options_button = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR,
                                    "div.header_controls.unselectable.disable-sort iron-icon.header-button.button_desplegable.x-scope.iron-icon-0"))
    )
    more_options_button.click()
    print("More options butonuna tıklandı.")
except Exception as e:
    print(f"Hata oluştu: {e}")

# İndirilen dosyanın yolunu belirle ve proje dizinine taşı
download_folder = 'C:/Users/Melisacevik/Downloads'
project_folder = 'C:/Users/Melisacevik/YourProjectFolder'
file_name = 'indirilen_dosya.csv'
downloaded_file_path = os.path.join(download_folder, file_name)
project_file_path = os.path.join(project_folder, file_name)

while not os.path.exists(downloaded_file_path):
    time.sleep(1)

shutil.move(downloaded_file_path, project_file_path)

# CSV dosyasını proje dizininden oku ve veri tabanına gönder
data = pd.read_csv(project_file_path)
db_connection_str = 'postgresql://username:password@localhost:5432/mydatabase'
db_connection = create_engine(db_connection_str)
data.to_sql('table_name', db_connection, if_exists='replace', index=False)

print("Veriler başarıyla veri tabanına yüklendi.")