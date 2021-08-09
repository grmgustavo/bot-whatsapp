# Importe de biblioteclas, instalação do selenium e do webdriver 
from typing import ChainMap
from selenium import webdriver
import time
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys

# criando a variavel 'driver', para importar o webdriver dentro do codigo e abrindo o navegador
driver = webdriver.Chrome(ChromeDriverManager().install())
# site a ser aberto: 'https://web.whatsapp.com'
driver.get('https://web.whatsapp.com')
time.sleep(15)

# Escolhando o NOME dos contatos já salvos a serem usados no envio de mensagem ( é Importante não deixar nenhuma letra maiuscula de fora ou espaço, para que não tenha erro )
contatos = ['Grupo solo', 'Teste bot', 'Irmão', 'Mãe']
# Preenchendo o conteúdo da mensagem
mensagem = 'teste'

# Função de buscar o contato
def buscar_contato(contato):
    # Fazendo o selenium procurar o campo de busca de contato na página do WhatsApp Web
    campo_pesquisa = driver.find_element_by_xpath(
        '//div[contains(@class, "copyable-text selectable-text")]')
    time.sleep(3)
    # O selenium encontrou o campo e está clicando nele
    campo_pesquisa.click()
    # Após o passo anterior, o selenium deixou o campo pronto para digitar algo e, nesse caso, é o nome do contato
    campo_pesquisa.send_keys(contato)
    # O selenium apertará a tecla ENTER para selecionar o contato
    campo_pesquisa.send_keys(Keys.ENTER)

# Função de enviar a mensagem
def enviar_mensagem(mensagem):
    # Fazendo o selenium procurar o campo de mensagem na página do WhatsApp Web
    campo_mensagem = driver.find_elements_by_xpath(
        '//div[contains(@class, "copyable-text selectable-text")]')
    # No caso do WhatsApp Web, existem 2 campos desse, o de contato e o de mensagem, então por isso precisamos colocar o '[1]' na variavel
    # O selenium encontrou o campo e está clicando nele
    campo_mensagem[1].click()
    time.sleep(3)
    # Digitando a mensagem no campo selecionado
    campo_mensagem[1].send_keys(mensagem)
    # O selenium apertará a tecla ENTER para enviar a mensagem
    campo_mensagem[1].send_keys(Keys.ENTER)

#Laço de repetição que irá executar as funções de acordo com o conteúdo presenta na variável 'contatos' 
for contato in contatos:
    buscar_contato(contato)
    enviar_mensagem(mensagem)
    

# supostamente tudo deu certo


# 'copyable-text selectable-text'
