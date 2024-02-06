from selenium import webdriver
from selenium.webdriver.common.by import By
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

def test_check_title_is(driver):
    driver.get("http://localhost:8501")
    sleep(5)

    page_title = driver.title

    expected_title = "Validador de schema excel" #Título real esperado
    assert page_title == expected_title

def test_check_streamlit_h1(driver):

    driver.get("http://localhost:8501")
    sleep(5)

    #Pega o primeiro elemento com tag <h1>
    h1_element = driver.find_element(By.TAG_NAME, "h1")

    # Verificar se o texto do elemento <h1> é o esperado
    expected_text = "Insira o seu excel para validação"
    assert h1_element.text == expected_text