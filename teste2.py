from SUBPROGRAMS.functions import baixa_inv, informacoes_extraidas
from clicknium import locator, ui
from clicknium import clicknium as cc
#from clicknium.common.models.MouseLocation import MouseLocation
from SUBPROGRAMS.parameters import *


import time
import subprocess
import pyautogui
from datetime import datetime, timedelta
import re
import pygetwindow as gw
import os
import pyperclip
import yagmail
import yaml
import logging
import os
import sys
from datetime import datetime
from timeit import default_timer as timer
import json





base_path = os.getcwd()
log_path = f'{base_path}/LOG'

image_path = f'{base_path}/IMAGES'
personalizar = f'{image_path}/personalizar.PNG'
valores_aba = f'{image_path}/valores_aba.PNG'
conta_caixa_botao = f'{image_path}/conta_caixa_botao.PNG'
descricao = f'{image_path}/descricao.PNG'
button_ok_3 = f'{image_path}/button_ok_3.PNG'
numero_documento = f'{image_path}/numero_documento.PNG'
barra_de_rolagem_direita = f'{image_path}/barra_rolagem_direita.PNG'
barra_de_rolagem_esquerda = f'{image_path}/barra_rolagem_esquerda.PNG'
imagem_natureza = f'{image_path}/imagem_natureza.PNG'

with open('config.yaml', 'r', encoding='utf=8') as params:
    config = yaml.safe_load(params)

print(config)

email_login = config['email']['login']
email_password = config['email']['password']
email_receivers = config['email']['receivers']
log_level = config['logLevel']

# log configs
today = datetime.today().strftime('%d-%m-%Y')
log_file_name = datetime.now().strftime('%H_%M_%S')

if  os.path.exists(f'{log_path}/{today}') == False:
    os.makedirs(f'{log_path}/{today}')

logging.basicConfig(level=log_level, datefmt='%d-%m-%Y %H:%M:%S',
                    format='%(asctime)s.%(msecs)03dZ;'
                               '%(module)s.%(funcName)s;'
                               '  %(message)s',
                    handlers=[
                        logging.FileHandler(os.path.join(f'{log_path}/{today}/{log_file_name}.log'), mode='w', encoding='utf-8', delay=False),
                        logging.StreamHandler(sys.stdout)
                    ])


# wait for image with pyautogui
def waitForImage(image, timeout, name):
    inicialTime = time.time()

    while True:
        try:
            # try to find image on screen
            location = pyautogui.locateOnScreen(image=image, confidence=0.9)

            if location is not None:
                # Image found
                logging.info(f'{name} image found.')
                return location

            
        except:
            # checking if timeout is over
            currentTime = time.time()
            if currentTime - inicialTime >= timeout:
                # timeout is over and the image was not found.
                logging.info(f'{name} image not found.')
                return None

            # waiting for searching again
            time.sleep(0.1)


'''tipo_doc_hover = cc.wait_appear(locator.rm.header_tipo_de_documento, wait_timeout=15)
tipo_doc_hover.set_focus()
print(tipo_doc_hover)'''


"""def localizarColuna(image, timeout, name):

    '''natureza =  waitForImage(image = imagem_natureza, timeout=10, name = 'IMAGEM NATUREZA')
    while natureza is None:
        barra_rolagem_esquerda = waitForImage(image = barra_de_rolagem_esquerda, timeout=0.1, name = 'Barra de Rolagem Esquerda')
        if barra_rolagem_esquerda is not None:
            pyautogui.doubleClick(barra_rolagem_esquerda)
        natureza =  waitForImage(image = imagem_natureza, timeout=10, name = 'IMAGEM NATUREZA')'''
        

    coluna = waitForImage(image = image, timeout= timeout, name = name)
    while coluna is None:
        barra_rolagem_direita = waitForImage(image = barra_de_rolagem_direita, timeout=10, name = 'Barra de Rolagem Direita')
        if barra_rolagem_direita is not None:
            pyautogui.doubleClick(barra_rolagem_direita)
        num_documento = waitForImage(image = image, timeout= timeout, name = name)
"""

#localizarColuna(numero_documento, 10, 'numero documento')

'''natureza =  waitForImage(image = imagem_natureza, timeout=1, name = 'IMAGEM NATUREZA')
if natureza is None:
    teste = cc.wait_appear(locator.rm.dataitem_x_row0, wait_timeout=360) 
    posicao = teste.get_position()
    x, y = posicao.Right + 20 , (posicao.Bottom + posicao.Top) // 2
    print(x,y)
    pyautogui.moveTo(x, y)
    pyautogui.click()'''


'''while natureza is None:
    barra_rolagem_esquerda = waitForImage(image = barra_de_rolagem_esquerda, timeout=1, name = 'Barra de Rolagem Esquerda')
    if barra_rolagem_esquerda is not None:
        pyautogui.doubleClick(barra_rolagem_esquerda)
    natureza =  waitForImage(image = imagem_natureza, timeout=1, name = 'IMAGEM NATUREZA')'''



'''teste = cc.wait_appear(locator.rm.dataitem_x_row0, wait_timeout=360) 
posicao = teste.get_position()
x, y = posicao.Right + 20 , (posicao.Bottom + posicao.Top) // 2
print(x,y)
pyautogui.moveTo(x, y)
pyautogui.click()
natureza =  waitForImage(image = imagem_natureza, timeout=1, name = 'IMAGEM NATUREZA')
while natureza is None:
    pyautogui.hotkey('left')
    natureza =  waitForImage(image = imagem_natureza, timeout=1, name = 'IMAGEM NATUREZA')
'''

'''#pyautogui.scroll(5)
cc.mouse.scroll(10)
referencia_inicial = cc.wait_appear(locator.rm.dataitem_x_row0, wait_timeout=360) 
posicao = referencia_inicial.get_position()
x, y = posicao.Right + 20 , (posicao.Bottom + posicao.Top) // 2
print(x,y)
pyautogui.moveTo(x, y)
pyautogui.click()
for i in range (35):
    pyautogui.press('left')
logging.debug('35 PASSOS PARA ESQUERDA')'''


'''def informacoes_extraidas():
    return """
[
    {
        "inv": "747431",
        "moeda": "USD",
        "valor": 1000
    },
    {
        "inv": "2222",
        "moeda": "EUR",
        "valor": 2000
    }
]
    """

vetor_inv_json = informacoes_extraidas()
vetor_inv = json.loads(vetor_inv_json)

for vetor in vetor_inv:
    if '747431' in vetor["inv"]:    
        print('sim')
        print(vetor['moeda'])
    else:
        print('nao')'''
button_ok = f'{image_path}/button_ok.PNG'
valor = f'{image_path}/valores.PNG'


#baixa_inv()

'''simplificada = cc.wait_appear(locator.rm.radiobutton_simplificada, wait_timeout=60)
simplificada.click()
logging.debug('SELECIONA SIMPLIFICADA')'''

'''data = cc.wait_appear(locator.rm.edit_data, wait_timeout=60)
date = data.get_text()
#logging.debug(f'DATA AUTOMÁTICA: {date}')

## SE NECESSÁRIO DIFITAR DATA
data.set_text('20112023')
pyautogui.hotkey('tab')'''


'''
def check_inv():

    rows_int = 52 #################

    time.sleep(3)

    #SELECIONAR PRIMEIRA CÉLULA INDEPENDENTE DE ONDE ESTEJA
    cc.mouse.scroll(10)
    referencia_inicial = cc.wait_appear(locator.rm.dataitem_x_row0, wait_timeout=360) 
    posicao = referencia_inicial.get_position()
    x, y = posicao.Right + 20 , (posicao.Bottom + posicao.Top) // 2
    print(x,y)
    pyautogui.moveTo(x, y)
    pyautogui.click()
    for esquerda in range (35):
        pyautogui.press('left')
    logging.debug('35 PASSOS PARA ESQUERDA')

    # PEGANDO DA PRIMEIRISSIMA CELULA
    for direita in range (19):
        pyautogui.press('right')
    logging.debug('19 PASSOS PARA DIREITA')

    time.sleep(2)
    for i in range(rows_int):

        vetor_inv = informacoes_extraidas()
        padrao = re.compile(r'INV - (\d+) -')

        logging.debug('ctrl c')
        pyautogui.hotkey('ctrl', 'c')
        time.sleep(0.5)
        historico = pyperclip.paste()
        logging.debug(f'Historico completo: {historico}')

        inv_number = padrao.search(historico)
        if inv_number:
            inv_number = inv_number.group(1)
        else:
            inv_number = 'NÃO ENCONTRADA'
        logging.debug(f'INV: {inv_number}')

        if inv_number in vetor_inv:
            time.sleep(0.5)
            pyautogui.hotkey('ctrl', 'enter')
            break
            
        else:
            time.sleep(0.5)
            pyautogui.press('down')
            logging.debug('APERTA PARA BAIXO PARA VERIFICAR O PRÓXIMO REGISTRO')
   '''


'''extrato_list_nao_tratado = informacoes_extraidas()
extrato_list = json.loads(extrato_list_nao_tratado)

for extrato in extrato_list:
    inv = extrato["inv"]
    print(inv)'''

'''data = cc.wait_appear(locator.rm.edit_data, wait_timeout=60)
date = data.get_text()
logging.debug(f'DATA AUTOMÁTICA: {date}')

## SE NECESSÁRIO DIFITAR DATA
data.set_text('20112023')
pyautogui.hotkey('tab')'''


'''select_lancamentos = waitForImage(image = lancamentos, timeout=60, name = 'LANÇAMENTOS')
if select_lancamentos is not None:
    time.sleep(2)
    pyautogui.click(select_lancamentos)
    logging.debug('CLICA EM LANÇAMENTOS')
    time.sleep(2)
'''


time.sleep(2)

data = cc.wait_appear(locator.rm.edit_data, wait_timeout=60)
date = data.get_text()
logging.debug(f'DATA AUTOMÁTICA: {date}')

## SE NECESSÁRIO DIFITAR DATA
data.set_text('20112023')
pyautogui.hotkey('tab')

erro1 = cc.wait_appear(locator.rm.titlebar_titlebar, wait_timeout=1)
erro2 = cc.wait_appear(locator.rm.window_rm, wait_timeout=1)
erro3 = cc.wait_appear(locator.rm.pane_rmspictureedit1, wait_timeout=1)

if erro1 or erro2 or erro3:
    erro = f'ERRO ENVOLVENDO MOEDA OU DATA'
    logging.debug(f'{erro}')
    pyautogui.hotkey('alt', 'f4')
    time.sleep(1)
    pyautogui.hotkey('alt', 'f4')
    