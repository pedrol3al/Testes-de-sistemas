from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

driver.get("https://localhost:8080/teste_de_sistemas/Testes-de-sistemas/login.html")


time.sleep(1)


 # Preenche o campo de usuário
usuario_input = driver.find_element(By.ID, "username")
usuario_input.send_keys("admin")
time.sleep(1)

 # Preenche o campo de senha
senha_input = driver.find_element(By.ID, "password")
senha_input.send_keys("123456")

 # Clica no botão de login
botao_login = driver.find_element(By.CSS_SELECTOR, "button [type='submit']")
botao_login.click()

if "Cadastro de Cliente" in driver.page_source:
    print("Login realizado com sucesso e redirecionado para index.html!")
else:
 print("Falha no login ou redirecionamento.")

print("Título atual da página:", driver.title)

# Encerra o navegador
 #driver.quit()