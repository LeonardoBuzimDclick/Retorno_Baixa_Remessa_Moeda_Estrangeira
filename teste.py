import pygetwindow as gw
import pyautogui
import time
import re
from clicknium import clicknium as cc
from SUBPROGRAMS.parameters import *
from SUBPROGRAMS.functions import *
from clicknium import locator, ui
from clicknium import clicknium as cc
import time
import subprocess
import pyautogui
from datetime import datetime, timedelta
import re
import pygetwindow as gw
import pyperclip



'''# wait for image with pyautogui
def waitForImage(image, timeout, name):
    inicialTime = time.time()

    while True:
        # try to find image on screen
        location = pyautogui.locateOnScreen(image=image, confidence=0.9)

        if location is not None:
            # Image found
            logging.info(f'{name} image found.')
            return location

        # checking if timeout is over
        currentTime = time.time()
        if currentTime - inicialTime >= timeout:
            # timeout is over and the image was not found.
            logging.info(f'{name} image not found.')
            return None'''



def emailSuccess(nome_bot, texto_msg):
    with open(f'{email_path}/emailSuccess.html', 'r', encoding='utf=8') as fileSuccess:
        templateSuccess = fileSuccess.read()
        htmlSuccess = templateSuccess.format(automacao = nome_bot, mensagem = texto_msg)
    yag.send(to=str(email_receivers).split(','), subject=f"SUCESSO - BOT REMESSAS PIX",
    contents=htmlSuccess)
    #attachments=f'{log_path}/{today}/{log_file_name}.log')
    logging.info('Success e-mail sent.')


#pdf_texto()
'''tranf_pdf_img()


caminho = F'{caminho_pdf}EXTRATO BTG 012024.pdf' ### VERIFICAR PADRAO NOME

caminho_imagem = caminho.split('.')[0]


texto = read_img(caminho_imagem)


linha_list, liq_cambio_list, iof_list, pag_list = regex_extrato_texto(texto)'''

'''flag = 0
valorers = ['10,00', '15,54']

for valor in valorers:

    flag = selec_filtro(flag, valor)'''

'''inv = '44275'
coligada = 'GILL INSTRUMENTS LIMITED'
quant_res = 1

valor_extr = '2.416,00'

check_inv(inv, coligada, quant_res)

#baixar_lancamento(valor_extr)'''

#copiar_processo()
#flag = False
'''valor = '1.542.000,00'
valor = valor.replace('.', '')
valor_original = waitForImage(image = valor_original_img, timeout=30, name = 'VALOR ORIGINAL')
if valor_original is not None and flag == False:
    x_img, y_img = pyautogui.center(valor_original)
    y_img = y_img + 20
    pyautogui.doubleClick(x_img, y_img)
    logging.info('CLICK EM VALOR ORIGINAL')
    pyautogui.write(valor)
else:
    flag = True'''
'''flag = False
salvar = waitForImage(image = salvar_img, timeout=30, name = 'SALVAR')
if salvar is not None and flag == False:
    pyautogui.click(salvar)
    logging.info('CLICK EM SALVAR')
else:
    flag = True'''


historico = 'teste - teste'

'''historico_click = waitForImage(image = historico_img, timeout=60, name = 'NOVO FILTRO')
if historico_click is not None:
    x_img, y_img = pyautogui.center(historico_click)
    y_img = y_img + 20
    for i in range(50):
        pyautogui.doubleClick(x_img, y_img)
        pyautogui.hotkey('delete')
    logging.info('CLICK - BOTÃO DE NOVA SELECAO DE FILTRO')
sleep(1)
pyautogui.write(historico)
logging.info(f'Histórico definido {historico}')'''

'''valor_original = waitForImage(image = valor_original_img, timeout=30, name = 'VALOR ORIGINAL')
if valor_original is not None:
    x_img, y_img = pyautogui.center(valor_original)
    y_img = y_img + 20
    pyautogui.click(x_img, y_img)
    logging.info('CLICK EM VALOR ORIGINAL')'''

'''conta_caixa_loc = waitForImage(image = conta_caixa_img, timeout=30, name = 'CONTA CAIXA')
if conta_caixa_loc is not None:
    x_imagem, y_imagem, largura_imagem, altura_imagem = conta_caixa_loc
    
    # Calcule as coordenadas da quina inferior esquerda
    x_quina_esquerda = x_imagem + 10
    y_quina_inferior = y_imagem + altura_imagem - 10
    
    # Clique na quina inferior esquerda
    pyautogui.click(x_quina_esquerda, y_quina_inferior)
sleep(5)


pyautogui.write(conta_caixa)
logging.info(f'Conta caixa digitada: {conta_caixa}')

pyautogui.hotkey('enter')
sleep(3)
pyautogui.hotkey('enter')'''

centro_custo = 'ROV'
natureza = 'IMPOSTOS'
'''
dados_adicionais_loc = waitForImage(image = dados_adicionais_img, timeout=30, name = 'DADOS ADICIONAIS')
if dados_adicionais_loc is not None:
    pyautogui.click(dados_adicionais_loc)
    logging.info('CLICK EM DADOS ADICIONAIS')
sleep(5)

for i in range(3):
    pyautogui.hotkey('tab')
logging.info(f'TAB clicado 3 vezes')

pyautogui.hotkey('enter')
logging.info(f'Centro de Custo acessado com enter')
sleep(5)

pyautogui.write(centro_custo)
logging.info(f'Centro de Custo digitado: {centro_custo}')

pyautogui.hotkey('enter')
sleep(3)
pyautogui.hotkey('enter')

rateio = waitForImage(image = rateio_img, timeout=10, name = 'RATEIO')
if rateio is not None:
    pyautogui.hotkey('enter')
    logging.info('CLICK EM RATEIO')

opcionais = waitForImage(image = opcionais_img, timeout=30, name = 'OPCIONAIS')
if opcionais is not None:
    pyautogui.click(opcionais)
    logging.info('CLICK EM OPCIONAIS')
sleep(5)

for i in range(3):
    pyautogui.hotkey('tab')
logging.info(f'TAB clicado 3 vezes')

pyautogui.hotkey('enter')
logging.info(f'Natureza Financeira acessado com enter')
sleep(5)

pyautogui.write(natureza)
logging.info(f'Centro de Custo digitado: {centro_custo}')

pyautogui.hotkey('enter')
sleep(3)
'''
'''
imp = {'data': '03/01/24', 'descricao': 'IOF S/CAMBIO', 'valor': '25,97', 'contrato': 'IOF-387584076', 'imposto': 'IOF'}

data = imp["data"]
descricao = imp["descricao"]
imposto = imp["imposto"]
valor = imp["valor"]
#if imp["multa"]:
multa = imp["multa"]
#if imp["valor_multa"]:
valor_multa = imp["valor_multa"]


baixar_ref(valor_multa)'''


'''data_recente = waitForImage1(image = data_recente_img, timeout=5, name = 'DATA DE VENCIMENTO RECENTE')
if data_recente is not None:

    #pyautogui.click(data_recente)
    logging.info('DATA DE VENCIMENTO RECENTE DEFINIDA')

else:
    cont = 0
    while data_recente is None:
        cont +=1
        cc.wait_appear(locator.rm.header_data_de_vencimento, wait_timeout=5).click()
        logging.info('DATA DE VENCIMENTO RECENTE TROCADA')

        largura_tela, altura_tela = pyautogui.size()

        # Calcula as coordenadas do meio da tela
        meio_x = largura_tela // 2
        meio_y = altura_tela // 2

        pyautogui.moveTo(meio_x, meio_y)

        data_recente = waitForImage1(image = data_recente_img, timeout=2, name = 'DATA DE VENCIMENTO RECENTE')
        if data_recente is not None:
            logging.info('DATA DE VENCIMENTO RECENTE ENCONTRADA')
        else:
            logging.info('DATA DE VENCIMENTO RECENTE NÃO ENCONTRADA')

        if cont == 10:
            erro = 'Data de vencimento mais recente não definida'

        sleep(5)'''

'''def caps():
    return True if ctypes.WinDLL("User32.dll").GetKeyState(0x14) else False

iai = caps()
print(iai)

pyautogui.press("capslock")
sleep(2)
print(iai)'''


'''
largura_tela, altura_tela = pyautogui.size()
meio_x = largura_tela // 2
meio_y = altura_tela // 2
pyautogui.click(meio_x, meio_y)
sleep(0.5)

while True: 
    data_recente2 = waitForImage1(image = data_recente_img2, timeout=1, name = 'DATA DE VENCIMENTO RECENTE 2')
    if data_recente2 is None:
        pyautogui.press('right')
        logging.info('DATA DE VENCIMENTO NÃO ENCONTRADA')
    else:
        logging.info('DATA DE VENCIMENTO ENCONTRADA')
        break
    sleep(3)

data_recente = waitForImage1(image = data_recente_img, timeout=5, name = 'DATA DE VENCIMENTO RECENTE')
if data_recente is not None:
    logging.info('DATA DE VENCIMENTO RECENTE DEFINIDA')

else:
    cont = 0
    while data_recente is None:
        cont +=1
        cc.wait_appear(locator.rm.header_data_de_vencimento, wait_timeout=5).click()
        logging.info('DATA DE VENCIMENTO RECENTE TROCADA')

        largura_tela, altura_tela = pyautogui.size()
        meio_x = largura_tela // 2
        meio_y = altura_tela // 2
        pyautogui.moveTo(meio_x, meio_y)

        data_recente = waitForImage1(image = data_recente_img, timeout=2, name = 'DATA DE VENCIMENTO RECENTE')
        if data_recente is not None:
            logging.info('DATA DE VENCIMENTO RECENTE ENCONTRADA')
        else:
            logging.info('DATA DE VENCIMENTO RECENTE NÃO ENCONTRADA')

        if cont == 10:
            erro = 'Data de vencimento mais recente não definida'
            return erro

        sleep(5)'''

'''valor_multa = '25,40'
erro = selecionar_processo()
if erro != "" and erro != None:
    logging.info(f'{erro}')
    status = 'Não Baixado'
    #createRowExcel(ref, valor_ref, erro, status)
    #continue

copiar_processo()

erro = baixar_ref(valor_multa)
if erro != "" and erro != None:
    logging.info(f'{erro}')
    status = 'Não Baixado'
    #createRowExcel(ref, valor_ref, erro, status)
    #continue

fim_lancamento()'''

def extrato_excel():

    arquivos_na_pasta = os.listdir(caminho_massa)
        
    arquivos_xls = [arquivo for arquivo in arquivos_na_pasta if arquivo.endswith(('.xls', '.xlsx'))]

    xls_list = []
    for arquivo_xls in arquivos_xls:
        caminho_completo = os.path.join(caminho_massa, arquivo_xls)
        logging.info(f'arquivo_xls {arquivo_xls}')
        sheet_name = 'Conta Corrente'
        
        dados = pd.read_excel(caminho_completo,  header=11, sheet_name=sheet_name)
        logging.info(f'dados {dados}')

        df_selecionado = dados.iloc[:, [1, 2, 3]]
        #logging.info(f'df_selecionado {df_selecionado}')

        linha_list = []
        for indice, linha in df_selecionado.iterrows():

            data = linha[0]
            if isinstance(data, datetime):
                data = data.strftime('%d/%m/%Y') 

            descricao = linha[1]  

            valor = str(linha[2]) 
            valor = valor.replace('-', '')  
            valor = valor.replace('.', ',')  
            if ','not in valor:
                valor = f'{valor},00'
            
            referencia = {
                    'data': data,
                    'descricao': descricao,
                    'valor': valor
                    }
            
            logging.info(referencia)
            linha_list.append(referencia)


        logging.info(f"linha_list {linha_list}")


'''camin = "C:\\Projetos\\Retornos\\Retorno_Baixa_Remessa_Moeda_Estrangeira\\PDF\\EXTRATO BTG 012024.pdf"

texto1 = pdf_image_to_text1(camin)
logging.info(f'texto1 {texto1}')'''
    

linha_list, liq_cambio_list, imposto_list, contrato_extr_list = excel()

logging.info(f'linha_list {linha_list}')
logging.info(f'liq_cambio_list {liq_cambio_list}')
logging.info(f'imposto_list {imposto_list}')
logging.info(f'contrato_extr_list {contrato_extr_list}')



'''def preprocess_image2(image_path):

    #logging.info(f'image_path: {image_path}')

    
    #image = cv2.imread(image_path) 
    #image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE) ###
    image = np.array(image_path)

    try:
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    except:
        gray = image
    logging.info(f'pre 1')

    denoised = cv2.fastNlMeansDenoising(gray, None, 30, 7, 21) ###
    logging.info(f'pre 2')
    clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8)) ###
    logging.info(f'pre 3')
    enhanced = clahe.apply(denoised) ###
    logging.info(f'pre 4')
    

    # Suavização para reduzir ruído (experimente diferentes algoritmos)
    #blur = cv2.GaussianBlur(enhanced, (5, 5), 0) #gray
    blur = cv2.medianBlur(enhanced, 5)  # Suavização mediana
    #blur = cv2.bilateralFilter(gray, 9, 75, 75)  # Filtro bilateral
    logging.info(f'pre 5')

    #equ = cv2.equalizeHist(blur)

    # Limiarização adaptativa para melhor lidar com iluminação variável
    thresh = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]
    #_, thresh = cv2.threshold(blur, 127, 255, cv2.THRESH_BINARY)
    #thresh = cv2.adaptiveThreshold(blur, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 9, 2)
    #thresh = cv2.adaptiveThreshold(blur, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 2)
    #thresh = cv2.thresholdOTSU(blur, 0, 255, cv2.THRESH_BINARY)[1]

    logging.info(f'pre 6')

    # Morfologia matemática para remover ruídos e melhorar a conectividade
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))
    logging.info(f'pre 7')
    opening = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel)
    logging.info(f'pre 8')
    closing = cv2.morphologyEx(opening, cv2.MORPH_CLOSE, kernel)

    logging.info(f'pre 9')

    #tiff_image_path = os.path.splitext(image_path)[0] + '.tiff'
    #cv2.imwrite(image_path, closing, [cv2.IMWRITE_JPEG_QUALITY, 100, cv2.IMWRITE_PXM_BINARY, 0, cv2.IMWRITE_JPEG_OPTIMIZE, 1])  ###
    #cv2.imwrite(image_path, closing, [cv2.IMWRITE_PXM_BINARY, 0, cv2.IMWRITE_TIFF_COMPRESSION, 0, cv2.IMWRITE_TIFF_XDPI, 300, cv2.IMWRITE_TIFF_YDPI, 300])  ###
    #cv2.imwrite(tiff_image_path, closing)  ###

    logging.info(f'pre 10')

    processed_image = Image.fromarray(closing)

    return processed_image ###



def tranf_pdf_pdf2(caminho):

    if not os.path.exists(caminho_copia_pdf):
        os.makedirs(caminho_copia_pdf)
        logging.info(f'Pasta Copia PDF criada')

    shutil.copy(caminho, caminho_copia_pdf)
    logging.info(f'PDF copiado')

    nome = caminho.split('PDF\\')[1].split('.pdf')[0]
    logging.info(f'nome {nome}')

    #caminho = f'{caminho_copia_pdf}\\{nome}.pdf'
    #logging.info(f'caminho novo {caminho}')

    #melhorar_pdf(caminho)

    documento_pdf = fitz.open(caminho)
    imagens_list = []

    nome_pdf_final = f'{caminho_copia_pdf}{nome}.pdf'
    c = canvas.Canvas(nome_pdf_final, pagesize=letter)

    for pagina_numero in range(documento_pdf.page_count):
        pagina = documento_pdf.load_page(pagina_numero)
        imagem_lida = pagina.get_pixmap(matrix=fitz.Matrix(2, 2), alpha=False)
        
        imagem_pil = Image.frombytes("RGB", [imagem_lida.width, imagem_lida.height], imagem_lida.samples)
        imagem = imagem_pil.convert("L")  # Convertendo para grayscale

        nova_resolucao = 300
        largura_original, altura_original = imagem.size
        nova_largura = int(largura_original * nova_resolucao / 72)
        nova_altura = int(altura_original * nova_resolucao / 72)

        enhancer = ImageEnhance.Contrast(imagem)
        imagem = enhancer.enhance(2.0)
        enhancer = ImageEnhance.Sharpness(imagem)
        imagem = enhancer.enhance(2.0)
        enhancer = ImageEnhance.Brightness(imagem)
        imagem = enhancer.enhance(1.5)

        imagem_redimensionada_tranf = imagem.resize((nova_largura, nova_altura), resample=Image.LANCZOS)
        logging.info(f'Imagem redimensionada')

        
        imagem = preprocess_image2(imagem_redimensionada_tranf)
        logging.info(f'Imagem redimensionada Pos processada')

        c.setPageSize((nova_largura, nova_altura))  

        buffer = io.BytesIO()
        imagem.save(buffer, format='TIFF')
        buffer.seek(0)

        img_reader = ImageReader(buffer)
        logging.info(f'Imagem Pos processada aberta')

        c.drawImage(img_reader, 0, 0, width=nova_largura, height=nova_altura, mask='auto')
        logging.info(f'Imagem Pos processada escrita')
        c.showPage()
    
    documento_pdf.close()
    c.save()
    logging.info(f'Novo PDF com imagens salvo')

    return nome_pdf_final


caminho = "C:\\Projetos\\Retornos\\Retorno_Baixa_Remessa_Moeda_Estrangeira\\PDF\\ARGUS_CONTRATO_ USD 1.374,00_R$ 7.172,28.pdf"


caminho = tranf_pdf_pdf2(caminho)

ocrmypdf.ocr(caminho, caminho, 
language='por',
clean=True,
clean_final=True,
#optimize=3,
#deskew=True,
force_ocr=True,
pdf_renderer='sandwich',
#pdf_renderer='hocr',
#plugins=[spell_checker],
#tesseract_oem=3,  # Usa o modo de engine 3 (default)
#tesseract_pagesegmode=6  # Ajusta o modo de segmentação
#tesseract_configs=["--psm 6", "--oem 1", "digits"]  # Configurações adicionais
#tesseract_config= ["--oem 2 --remove_noise --tessedit_create_hocr 1 --textonly_pdf 1 --remove_background True"],  # Configurações adicionais
tesseract_config= ["--oem 2 --psm 11 dpi 300 --remove_noise --tessedit_create_hocr 1 --textonly_pdf 1 --remove_background True"],  # Configurações adicionais

)
logging.info(f'PDF transformado para texto')


texto = extrair_texto_pdf(caminho)
logging.info(f'texto {texto}')'''