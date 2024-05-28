# -*- coding: utf-8 -*-

import yagmail
import yaml
import logging
import os
import sys
from timeit import default_timer as timer
import json
from time import sleep, time
import subprocess
import pyautogui
from datetime import datetime, timedelta
import re
import pygetwindow as gw
import pyperclip
import openpyxl
from pdf2image import convert_from_path
import glob
import shutil
import os
import pytesseract
import cv2
import fitz
import pdfplumber
import psutil
import signal
import ctypes
import pandas as pd
import ocrmypdf
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib.utils import ImageReader
import textract
import pdfminer.pdfdevice
from pdfminer.high_level import extract_text
import PyPDF2
from tika import parser
from PIL import Image, ImageEnhance
import numpy as np
import io

Image.MAX_IMAGE_PIXELS = None

pyautogui.FAILSAFE = False



base_path = os.getcwd()
log_path = f'{base_path}/LOG'
excel_path = f'{base_path}/EXCEL'
email_path = f'{base_path}/EMAIL'
image_path = f'{base_path}/IMAGES'
user = 'integracao'
password = 'arrobaint;321'
tipo_documento = 'INV'
nome_bot = 'Pagamento Moeda Estrangeira'
texto_msg = 'Sucesso na execução do Bot de Pagamento de Moeda Estrangeira'
tipo_filtro1 = r'Busca Valor'
tipo_filtro2 = r'HISTÓRICO'
conta_caixa1 = '001464585'
conta_caixa = 'BANCO BTG PACTUAL AG:0001 CC:001464585'
natureza = 'IMPOSTOS'

localRM = 'C:\Totvs\CLOUD HML\RM.exe'
processList = ["RM.exe"]


with open('config.yaml', 'r', encoding='utf=8') as params:
    config = yaml.safe_load(params)


email_login = config['email']['login']
email_password = config['email']['password']
email_receivers = config['email']['receivers']
log_level = config['logLevel']


yag = yagmail.SMTP(user=email_login, password=email_password)


pytesseract_caminho = r"C:\\Program Files\\Tesseract-OCR\\tesseract.exe"

caminho_pdf = r"C:\\Projetos\\Retornos\\Retorno_Baixa_Remessa_Moeda_Estrangeira\\PDF\\"
caminho_massa = r"C:\\Projetos\\Retornos\\Retorno_Baixa_Remessa_Moeda_Estrangeira\\MASSA\\"
caminho_imagem = r"C:\\Projetos\\Retornos\\Retorno_Baixa_Remessa_Moeda_Estrangeira\\PDF\\imagens"
caminho_copia_pdf = r"C:\\Projetos\\Retornos\\Retorno_Baixa_Remessa_Moeda_Estrangeira\\PDF\\pdf_img_orig\\"

# log configs
today = datetime.today().strftime('%Y-%m-%d')
log_file_name = datetime.now().strftime('%H_%M_%S')

if  os.path.exists(f'{log_path}/{today}') == False:
    os.makedirs(f'{log_path}/{today}')

logging.basicConfig(level=log_level, datefmt='%Y-%m-%d %H:%M:%S',
                    format='%(asctime)s.%(msecs)03dZ;'
                               '%(module)s.%(funcName)s.%(lineno)d:'
                               '  %(message)s',
                    handlers=[
                        logging.FileHandler(os.path.join(f'{log_path}/{today}/{log_file_name}.log'), mode='w', encoding='utf-8', delay=False),
                        logging.StreamHandler(sys.stdout)
                    ])


#EXCEL CONFIG
# checking if there's a {today} directory in EXCEL
if os.path.exists(f'{excel_path}/{today}') == False:
    os.makedirs(f'{excel_path}/{today}')

writer = f'{excel_path}/{today}/{log_file_name}.xlsx'


##  IMAGENS  ##
integracao_bancaria = f'{image_path}/integracao_bancaria.PNG'
boleto = f'{image_path}/boleto.PNG'
button_ok = f'{image_path}/button_ok.PNG'
button_ok_2 = f'{image_path}/button_ok_2.PNG'
filter_clear = f'{image_path}/filter_clean.PNG'
lancamentos = f'{image_path}/lancamentos.PNG'
licencas_excedidas = f'{image_path}/licencas_excedidas.PNG'
forma_pag = f'{image_path}/forma_pagamento.PNG'
boleto_min = f'{image_path}/boleto_minusculo.PNG'
boleto_min_des = f'{image_path}/boleto_min_desbili.PNG'
exec_sucesso = f'{image_path}/exec_success.PNG'
boleto_min_hab = f'{image_path}/boleto_min_habili.PNG'
table_empty_img = f'{image_path}/table_empty.PNG'
concessionarias_img = f'{image_path}/concessionarias.PNG'
novo_filtro_img = f'{image_path}/novo_filtro.PNG'
janela_lancamentos_img = f'{image_path}/janela_lancamentos.PNG'
data_emissao_img = f'{image_path}/data_emissao.PNG'
data_vencimento_img = f'{image_path}/data_vencimento.PNG'
data_prev_img = f'{image_path}/data_prev.PNG'
historico_img = f'{image_path}/historico.PNG'
valor_original_img = f'{image_path}/valor_original.PNG'
conta_caixa_img =  f'{image_path}/conta_caixa.PNG'
dados_adicionais_img =  f'{image_path}/dados_adicionais.PNG'
opcionais_img =  f'{image_path}/opcionais.PNG'
rateio_img =  f'{image_path}/rateio.PNG'
rateio_img2 =  f'{image_path}/rateio2.PNG'
salvar_img =  f'{image_path}/salvar.PNG'
ok_img = f'{image_path}/ok.PNG'
data_recente_img = f'{image_path}/data_recente.PNG'
data_recente_img2 = f'{image_path}/data_recente2.PNG'
marcar_todos_img = f'{image_path}/marcar_todos.PNG'

valores = f'{image_path}/valores.PNG'
baixa_success = f'{image_path}/baixa_success.PNG'
baixa_error = f'{image_path}/baixa_error.PNG'

error_process_lanc = f'{image_path}/erro_lancamento.PNG'
pix = f'{image_path}/pix.PNG'
pix_transf = f'{image_path}/pix_transferencia.PNG'
tipo_chave_pix = f'{image_path}/tipo_chave_pix.PNG'
chave_pix = f'{image_path}/chave_pix.PNG'
pix_subli = f'{image_path}/pix_sublinhado.PNG'
sem_pix = f'{image_path}/sem_opcao_pix.PNG'
pix_desabilitado = f'{image_path}/tres_pontos_desabilitado.PNG'
erro_img = f'{image_path}/erro.PNG'
erro2_img = f'{image_path}/erro2.PNG'
confirmar_cancelamento_img = f'{image_path}/confirmar_cancelamento.PNG'



