from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

driver.get("C:/Users/pedro_g_costa/Documents/teste_de_sistemas/index.html")

nome_input = driver.find_element(By. ID, "name")
nome_input.send_keys("joao da silva")

cpf_input = driver.find_element(By. ID, "cpf")
cpf_input.send_keys("123456789010")

endereco_input = driver.find_element(By.ID, "adress")
endereco_input.send_keys("rua das flores, 123")

telefone_input = driver.find_element(By.ID, "phone")
telefone_input.send_keys("12345678910")

submit_button = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
submit_button.click()

time.sleep(8)

driver.quit()