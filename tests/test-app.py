from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from time import sleep

#Definir drive q ser utilizado
driver = webdriver.Chrome()

#Timeout implícito
driver.set_page_load_timeout(5) #Segundos

#Tentativa de entrar na página
try:
    driver.get("http://localhost:8501")
    sleep(5)
    print("Acessou a página com sucesso")
except TimeoutException:
    print("Tempo de carregamento da página excedeu o limite")
finally:
    driver.quit()
