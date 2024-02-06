from selenium import webdriver
from time import sleep
import pytest
import subprocess

@pytest.fixture
def driver():
    process = subprocess.Popen(["task", "run"])

    #Definir drive q ser utilizado
    driver = webdriver.Chrome()

    #Timeout implícito
    driver.set_page_load_timeout(10) #Segundos
    yield driver

    #Fechar o webdriver e encerrar o processo após o teste
    driver.quit()
    process.kill()

def test_app_opens(driver):

    driver.get("http://localhost:8501")
    sleep(5)