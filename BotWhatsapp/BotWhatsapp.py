# import das bibliotecas
from selenium import webdriver
import time
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
import codecs

# importar os contatos do txt
def inputConts(nome_arquivo):
    contatos = codecs.open(nome_arquivo, 'r', 'utf-8')
    conts = contatos.readlines()
    arr = []
    for e in conts:
        new = e.replace('\r\n','')
        if(new[0] in '1234567890'):
            new = '+' + new
        arr.append(new)
    return arr

# vai até o whatsappweb e tam 20 segundos pra conectar
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get('https://web.whatsapp.com/')
time.sleep(20)

# definição dos contatos e da mensagem
contatos = inputConts('contatos.txt')
msg = 'menssagem a ser enviada"

# função para pesquisar contato ou grupo
def searchCont(contato):
    search = driver.find_element_by_xpath('//div[contains(@class, "copyable-text selectable-text")]')
    time.sleep(3)
    search.click()
    search.send_keys(contato)
    search.send_keys(Keys.ENTER)

# função para enviar mensagens
def sendMsg(mensagem):
      fieldMsg = driver.find_elements_by_xpath('//div[contains(@class, "copyable-text selectable-text")]')
      fieldMsg[1].click()
      time.sleep(3)
      fieldMsg[1].send_keys(mensagem)
      fieldMsg[1].send_keys(Keys.ENTER)

# percorrendo os contatos para pesquisa-los e enviar as mensagens
for cont in contatos:
    searchCont(cont)
    time.sleep(3)
    sendMsg(msg)
