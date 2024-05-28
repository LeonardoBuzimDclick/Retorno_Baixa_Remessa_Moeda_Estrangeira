from SUBPROGRAMS.parameters import *
from clicknium import locator, ui
from clicknium import clicknium as cc


def bot_text_art():
    logging.info("    ____   ")
    logging.info("   [____]    ")
    logging.info(" |=]()()[=|  ")
    logging.info("   _\==/__    _____    ____     _        _____    ___   _  __")
    logging.info(" |__|   |_|  |  _  \  / ___|   | |      |_   _| / ___| | |/ /")
    logging.info(" |_|_/\_|_|  | |  | | | |      | |        | |   | |    | ' / ")
    logging.info(" | | __ | |  | |  | | | |      | |        | |   | |    |  <  ")
    logging.info(" |_|[  ]|_|  | |__| | | |____  | |____   _| |_  | |__  | . \ ")
    logging.info(" \_|_||_|_/  |_____/   \_____| |______| |_____| \ ___| |_|\_\\")
    logging.info("   |_||_|                                                     ")
    logging.info("   | ||_|_   ")
    logging.info(" |___||___|  ")	
    logging.info("             ")

def show_exception_and_exit(exc_type, exc_value, tb):

    # https:/www.youtube.com/watch?v=8MjfalI4AO8
    # traceback.print_exception(exc_type, exc_value, tb)
    logging.error(exc_value, exc_info=(exc_type, exc_value, tb))

    with open(f'{email_path}/emailError.html', 'r', encoding='utf-8') as fileError:
        templateError = fileError.read()
        htmlError = templateError.format(exc_value=exc_value)
        
    yag.send(to=email_receivers.split(','), subject=f"ERRO - BOT REMESSAS",
    contents=htmlError,
    attachments=f'{log_path}/{today}/{log_file_name}.log')

    sys.exit(-1)

def open_RM():
    subprocess.Popen(localRM)
    logging.info('OPEN PROGRAM RM')

def loggin_RM():
    cc.wait_appear(locator.rm.pane_picturebox1, wait_timeout=500)

    user_rm = cc.wait_appear(locator.rm.user_field, wait_timeout=15)
    user_rm.double_click()
    user_rm.send_hotkey(f'{user}')
    logging.info('ENTER USER_NAME')
    pass_rm = cc.wait_appear(locator.rm.pass_field, wait_timeout=15)
    pass_rm.click()
    pyautogui.typewrite(f'{password}')
    logging.info('ENTER PASSWORD')
    click_button = cc.wait_appear(locator.rm.button_entrar, wait_timeout=15)
    click_button.click()
    logging.info('ENTER RM')

def enter_coligada():

    cc.wait_appear(locator.rm.click_contexto, wait_timeout=30)

    filtro_ref = cc.wait_appear(locator.rm.group_filtros_globais, wait_timeout=60)
    if filtro_ref is not None:
        filtro_ref.click()
        sleep(1)
        pyautogui.press('esc')

    click_context = cc.wait_appear(locator.rm.click_contexto, wait_timeout=300)
    click_context.click()
    logging.info('CLICK CONTEXTO')
    click_coligada = cc.wait_appear(locator.rm.menuitem_alterar_contexto_do_módulo, wait_timeout=15)
    click_coligada.click()
    logging.info('CLICK COLIGADA')
    click_colig_cod = cc.wait_appear(locator.rm.edit_coligada_code, wait_timeout=15)
    click_colig_cod.click()
    click_colig_cod.set_text('1')
    logging.info('INSERE O COLIGADA CODE = 1')
    pyautogui.press('tab')
    logging.info('APERTA TAB PARA PREENCHER O CAMPO COM A STRING: OCEANICA ENGENHARIA E CONSULTORIA S.A.')
    click_avancar_final = cc.wait_appear(locator.rm.button_bavancar1, wait_timeout=15)
    click_avancar_final.click()
    logging.info('CLICK AVANÇAR NOVAMENTE')
    click_concluir = cc.wait_appear(locator.rm.button_concluir, wait_timeout=15)
    click_concluir.click()
    sleep(2)
    logging.info('CLICK CONCLUIR')
    try:
        click_concluir = cc.wait_disappear(locator.rm.button_concluir, wait_timeout=120)
        logging.info('POP UP COLIGADA CLICADO PARA DESAPARECER')
    except:
        logging.info('POP UP COLIGADA NÃO EXIBIDO')
        pass



def enter_contas_a_pagar():
    cc.wait_appear(locator.rm.linha_rm, wait_timeout=300).click()
    logging.info('CLICK - TOTVS - LINHA RM')

    cc.wait_appear(locator.rm.back_office, wait_timeout=15).click()
    logging.info('CLICK - BACK OFFICE')

    cc.wait_appear(locator.rm.gestao_financeira, wait_timeout=15).click()
    logging.info('CLICK - GESTAO FINANCEIRA')

    cc.wait_appear(locator.rm.contas_pagar, wait_timeout=30).click()
    logging.info('CLICK - CONTAS A PAGAR')

    cont1 = 0
    while cont1 <= 50:

        select_lancamentos = waitForImage(image = lancamentos, timeout=10, name = 'LANÇAMENTOS')
        if select_lancamentos is not None:
            pyautogui.click(select_lancamentos)
            logging.info('CLICA EM LANÇAMENTOS')

        licencas = waitForImage(image = licencas_excedidas, timeout=10, name = 'LICENCAS EXCEDIDAS')
        if licencas is not None:
            logging.info('LICENCAS EXCEDIDAS')
            pyautogui.hotkey(f'esc')

            if cont1 == 50:
                encerra_prog()
                texto_msg = 'ENVIANDO EMAIL DE ERRO'
                logging.info(texto_msg)
                emailErro(texto_msg)

            logging.info(f'TENTANDO NOVAMENTE - {cont1+1}')
            cont1 += 1
            sleep(10)
        
        else:
            break


def obter_intervalo_data():
    hoje = datetime.now()
    dia_semana_hoje = hoje.weekday()  # Retorna um número entre 0 (segunda) e 6 (domingo)

    if dia_semana_hoje in [2, 3, 4, 5, 6]:  # Quarta, quinta ou sexta
        data_inicio = hoje - timedelta(days=dia_semana_hoje - 2)  # Início da quarta-feira atual
        data_fim = data_inicio + timedelta(days=6)  # Fim da terça-feira da próxima semana
    elif dia_semana_hoje in [0, 1]:  # Segunda ou terça
        data_inicio = hoje - timedelta(days=dia_semana_hoje + 5)  # Início da quarta-feira passada
        data_fim = data_inicio + timedelta(days=6)  # Fim da terça-feira desta semana
    else:
        # Lidar com outros dias da semana conforme necessário
        data_inicio = data_fim = None

    return data_inicio, data_fim

def filter_lancamento1():

    select_filter = cc.wait_appear(locator.rm.select_filter, wait_timeout=60)
    select_filter.set_text('Histórico')
    logging.info('ESCREVE Histórico NO FILTRO')

    execute = cc.wait_appear(locator.rm.button_exec_filtro, wait_timeout=15)
    execute.click()
    logging.info('CLICK - BUTÃO DE SELECAO DE FILTRO')

    enter_inv = cc.wait_appear(locator.rm.edit_filter_lancamento, wait_timeout=15)
    enter_inv.click()
    enter_inv.send_hotkey('INV')
    logging.info('CLICK - BUTÃO DE SELECAO DE FILTRO')

    select_filter = cc.wait_appear(locator.rm.button_ok_filtro, wait_timeout=15)
    select_filter.click()
    logging.info('CLICK - BUTÃO DE EXECUTAR O FILTRO')
    sleep(5)

    
def filter_clean1():
    clear_filter_x = waitForImage(image = filter_clear, timeout=10, name = 'FILTER CLEAN')
    #clear_filter_x = pyautogui.locateOnScreen(filter_clear, 0.9)
    if clear_filter_x is not None:
        pyautogui.click(clear_filter_x)
        logging.info('CLICA NO BOTÃO X DO LIMPA FILTRO')   
        sleep(2)


def desmark_filte1r():

    check_lancamentos_receber = cc.wait_appear(locator.rm.checkbox_lançamentos_a_receber, wait_timeout=360)
    check_lancamentos_receber.click()
    logging.info('CLICK CHECKBOX LANÇAMENTOS A RECEBER')

    check_lancamentos_baixados = cc.wait_appear(locator.rm.checkbox_lançamentos_baixados, wait_timeout=15)
    check_lancamentos_baixados.click()
    logging.info('CLICK CHECKBOX LANÇAMENTOS BAIXADOS')

    check_lancamentos_cancelados = cc.wait_appear(locator.rm.checkbox_lançamentos_cancelados, wait_timeout=15)
    check_lancamentos_cancelados.click()
    logging.info('CLICK CHECKBOX LANÇAMENTOS CANCELADOS')

    check_lancamentos_faturados = cc.wait_appear(locator.rm.checkbox_lançamentos_faturados, wait_timeout=15)
    check_lancamentos_faturados.click()
    logging.info('CLICK CHECKBOX LANÇAMENTOS FATURADOS')

    filter_refresh = cc.wait_appear(locator.rm.button_atualiza_filtro, wait_timeout=15)
    filter_refresh.click()
    logging.info('ATUALIZA O FILTRO')


def check_table_record1():

    logging.info('VERIFICANDO SE A TABELA ESTÁ VAZIA')

    #sleep(10)  AGUARDAR A CONFIRMAÇÃO DE UMA LINHA APARECER
    cc.wait_appear(locator.rm.dataitem_x_row0, wait_timeout=15)
    sleep(2)
    pyautogui.hotkey('ctrl', 'g')
    sleep(2)

    numero_registros = cc.wait_appear(locator.rm.text_table_row, wait_timeout=15)
    txt_table = numero_registros.get_text()
    logging.info(txt_table)
    sleep(2)
    number_rows = re.findall(r'\b(\d+)\b', txt_table)

    if txt_table == 'Para este processo é necessário que existam registros na visão.':
        sleep(2)
        logging.info('SEM REMESSAS PIX')   
        sleep(2)
        pyautogui.press('enter')
        return True
    else:
        global rows_int
        rows_int = int(number_rows[0])
        logging.info(f'NUMERO DE TUPLAS: {rows_int}')
        logging.info('TABELA CONTÉM REGISTROS')
        #sleep(5)
        click_nao = cc.wait_appear(locator.rm.button_não, wait_timeout=15)
        click_nao.set_focus()
        sleep(1)
        pyautogui.hotkey('alt', 'n')
        logging.info('CLICK NÃO')
        return False 
    
        windows = gw.getWindowsWithTitle(title='TOTVS Linha RM - Construção e Projetos  Alias: CorporeRM | 1-OCEANICA ENGENHARIA E CONSULTORIA S.A.')
        print(windows)
        if windows:
            window=windows[0]
            window.activate()
            window.maximize()


def select_tipo_documento():

    tipo_doc = cc.wait_appear(locator.rm.header_tipo_de_documento, wait_timeout=600)
    colunm_name = tipo_doc.get_text()
    logging.info(f'NOME DA COLUNA: {colunm_name}')

    tipo_doc_hover = cc.wait_appear(locator.rm.header_tipo_de_documento, wait_timeout=15)
    tipo_doc_hover.hover(4)
    logging.info(f'HOVER NOME DA COLUNA: {colunm_name}')

    # BUSCANDO O FILTRO A PARTIR DA POSIÇÃO DO ELEMENTO
    posição = tipo_doc_hover.get_position()
    x, y = posição.Right - 5 , posição.Top + 5
    pyautogui.moveTo(x,y)
    pyautogui.click()

    '''pyautogui.click(650,316)
    logging.info('CLICA PARA APARECER O FILTRO PERSONALIZAR')'''

    pyautogui.press('down')

    pyautogui.typewrite('(Personalizar)')
    pyautogui.press('enter')
    logging.info('CLICA NO FILTRO PERSONALIZAR')

    into_filter_personalizar = cc.wait_appear(locator.rm.listitem_filter_type, wait_timeout=15)
    into_filter_personalizar.click()
    logging.info('CLICA PARA SELECIONAR OPÇÕES DO FILTRO')

    sleep(2)
    pyautogui.write('Igual a')
    sleep(2)
    pyautogui.hotkey('tab')
    sleep(2)
    pyautogui.hotkey('ctrl', 'a')
    pyautogui.write(F'{tipo_documento}')

    button_not_inv = cc.wait_appear(locator.rm.button_confirmar_not_inv, wait_timeout=15)
    button_not_inv.click()
    logging.info('CLICK BUTTON CONFIRMAR FILTRO')


def filter_clean():

    for i in range (3):
        try:
            clear_filter_x = waitForImage(image = filter_clear, timeout=10, name = 'FILTER CLEAN')
            if clear_filter_x is not None:
                sleep(1)
                pyautogui.click(clear_filter_x)
                logging.info('CLICA NO BOTÃO X DO LIMPA FILTRO')
        except:
            pass
            

def selec_filtro(flag, filtro, valor):

    if flag == 0:

        cc.wait_appear(locator.rm.linha_rm, wait_timeout=300).click()
        logging.info('CLICK - TOTVS - LINHA RM')

        cc.wait_appear(locator.rm.back_office, wait_timeout=15).click()
        logging.info('CLICK - BACK OFFICE')

        cc.wait_appear(locator.rm.gestao_financeira, wait_timeout=15).click()
        logging.info('CLICK - GESTAO FINANCEIRA')

        cc.wait_appear(locator.rm.contas_pagar, wait_timeout=30).click()
        logging.info('CLICK - CONTAS A PAGAR')

        cont1 = 0
        while cont1 <= 50:

            select_lancamentos = waitForImage(image = lancamentos, timeout=10, name = 'LANÇAMENTOS')
            if select_lancamentos is not None:
                pyautogui.click(select_lancamentos)
                logging.info('CLICA EM LANÇAMENTOS')

            licencas = waitForImage(image = licencas_excedidas, timeout=10, name = 'LICENCAS EXCEDIDAS')
            if licencas is not None:
                logging.info('LICENCAS EXCEDIDAS')
                pyautogui.hotkey(f'esc')

                if cont1 == 50:
                    encerra_prog()
                    texto_msg = 'ENVIANDO EMAIL DE ERRO'
                    logging.info(texto_msg)
                    emailErro(texto_msg)

                logging.info(f'TENTANDO NOVAMENTE - {cont1+1}')
                cont1 += 1
                sleep(10)
            
            else:
                break

        cc.wait_appear(locator.rm.group_filtros_globais, wait_timeout=300).click()
        logging.info(f'Buscar filtro clicado')
        sleep(1)

        pyautogui.write(filtro)
        logging.info(f'{filtro} digitado')
        sleep(1)

        pyautogui.hotkey('enter')
        logging.info(f'Enter clicado')
        sleep(1)

        '''cc.wait_appear(locator.rm.button_buttonexec, wait_timeout=15).click()
        logging.info(f'Executar clicada')'''

        cc.wait_appear(locator.rm.edit, wait_timeout=60).set_text(valor)
        logging.info(f'Valor de filtro {valor} preenchida')

        sleep(1)
        pyautogui.hotkey('enter')
        logging.info(f'Enter clicado')
    
        filter_clean()
        if filtro == 'Busca Valor':
            select_tipo_documento()
            desmark_filter()

        return 1


    else:
        cc.wait_appear(locator.rm.checkbox_lançamentos_a_receber, wait_timeout=480)

        #time.sleep(1)
        novo_filtro = waitForImage(image = novo_filtro_img, timeout=30, name = 'NOVO FILTRO')
        if novo_filtro is not None:
            pyautogui.click(novo_filtro)
            logging.info('CLICK - BOTÃO DE NOVA SELECAO DE FILTRO')

        cc.wait_appear(locator.rm.edit, wait_timeout=60).set_text(valor)
        logging.info(f'Valor de filtro {valor} preenchida')

        sleep(1)
        pyautogui.hotkey('enter')
        logging.info(f'Enter clicado')


def selec_filtro2(flag, imposto):

    if flag == 0:

        cc.wait_appear(locator.rm.linha_rm, wait_timeout=300).click()
        logging.info('CLICK - TOTVS - LINHA RM')

        cc.wait_appear(locator.rm.back_office, wait_timeout=15).click()
        logging.info('CLICK - BACK OFFICE')

        cc.wait_appear(locator.rm.gestao_financeira, wait_timeout=15).click()
        logging.info('CLICK - GESTAO FINANCEIRA')

        cc.wait_appear(locator.rm.contas_pagar, wait_timeout=30).click()
        logging.info('CLICK - CONTAS A PAGAR')

        cont1 = 0
        while cont1 <= 50:

            select_lancamentos = waitForImage(image = lancamentos, timeout=10, name = 'LANÇAMENTOS')
            if select_lancamentos is not None:
                pyautogui.click(select_lancamentos)
                logging.info('CLICA EM LANÇAMENTOS')

            licencas = waitForImage(image = licencas_excedidas, timeout=10, name = 'LICENCAS EXCEDIDAS')
            if licencas is not None:
                logging.info('LICENCAS EXCEDIDAS')
                pyautogui.hotkey(f'esc')

                if cont1 == 50:
                    encerra_prog()
                    texto_msg = 'ENVIANDO EMAIL DE ERRO'
                    logging.info(texto_msg)
                    emailErro(texto_msg)

                logging.info(f'TENTANDO NOVAMENTE - {cont1+1}')
                cont1 += 1
                sleep(10)
            
            else:
                break

        cc.wait_appear(locator.rm.group_filtros_globais, wait_timeout=300).click()
        logging.info(f'Buscar filtro clicado')
        sleep(1)

        pyautogui.write(tipo_filtro2)
        logging.info(f'{tipo_filtro2} digitado')
        sleep(1)

        pyautogui.hotkey('enter')
        logging.info(f'Enter clicado')
        sleep(1)

        '''cc.wait_appear(locator.rm.button_buttonexec, wait_timeout=15).click()
        logging.info(f'Executar clicada')'''

        cc.wait_appear(locator.rm.edit, wait_timeout=60).set_text(imposto)
        logging.info(f'Imposto {imposto} preenchido')

        sleep(1)
        pyautogui.hotkey('enter')
        logging.info(f'Enter clicado')
    
        desmark_filter()
        filter_clean()
        #select_tipo_documento()

        return 1


    else:
        cc.wait_appear(locator.rm.checkbox_lançamentos_a_receber, wait_timeout=480)

        #time.sleep(1)
        novo_filtro = waitForImage(image = novo_filtro_img, timeout=30, name = 'NOVO FILTRO')
        if novo_filtro is not None:
            pyautogui.click(novo_filtro)
            logging.info('CLICK - BOTÃO DE NOVA SELECAO DE FILTRO')

        cc.wait_appear(locator.rm.edit, wait_timeout=60).set_text(imposto)
        logging.info(f'Imposto {imposto} preenchido')

        sleep(1)
        pyautogui.hotkey('enter')
        logging.info(f'Enter clicado')


def copiar_processo():
#def copiar_processo(data, historico, valor, centro_custo):  ###

    valor = '25,97'
    historico = 'IOF S/CAMBIO - BANCO BTG PACTUAL - MACGREGOR PTE. LTD. - 187260387 - contrato: 387584076'
    data = '03/01/24'
    centro_custo = '2.02.01.07'

    def rateio(flag):
        rateio = waitForImage(image = rateio_img, timeout=3, name = 'RATEIO') ###
        rateio2 = waitForImage(image = rateio_img2, timeout=3, name = 'RATEIO2') ###
        if rateio is not None or rateio2 is not None and flag == False:
            pyautogui.hotkey('enter')
            logging.info('CLICK EM RATEIO')
            sleep(4)

    valor = valor.replace('.', '')
    data = data.replace('/','')

    flag = False

    sleep(2)
    pyautogui.hotkey('ctrl','enter')
    logging.info('ctrl + enter')

    janela_lancamentos = waitForImage(image = janela_lancamentos_img, timeout=120, name = 'Janela aberta')
    if janela_lancamentos is not None and flag == False:
        pyautogui.click(janela_lancamentos)
        logging.info('CLICK - JANELA ABERTA')
        sleep(1)

        pyautogui.hotkey('ctrl','shift', 'c')
        sleep(5)
    else:
        flag = True

    marcar_todos = waitForImage(image = marcar_todos_img, timeout=120, name = 'Marcar Todos')
    if marcar_todos is not None and flag == False:
        pyautogui.click(marcar_todos)
        logging.info('CLICK - Marcar Todos')
        sleep(1)

        #cc.wait_appear(locator.rm.button_rmssimplebutton4, wait_timeout=60).click()
        pyautogui.hotkey('alt','o')
        logging.info(f'Ok clicado')       
        sleep(2)

        #cc.wait_appear(locator.rm.button_incluir_ctrlins, wait_timeout=60).click()
        pyautogui.hotkey('ctrl','insert')
        logging.info(f'+ clicado')  
        sleep(5)

        pyautogui.hotkey('ctrl','shift', 'v')
        sleep(7)
    else:
        flag = True
    

    data_emissao = waitForImage(image = data_emissao_img, timeout=60, name = 'DATA EMISSÃO')
    if data_emissao is not None and flag == False:
        x_img, y_img = pyautogui.center(data_emissao)
        y_img = y_img + 20
        pyautogui.doubleClick(x_img, y_img)
        logging.info('CLICK - DATA EMISSÃO')
        sleep(1)
        pyautogui.write(data)
        logging.info(f'Data emissão {data}')
    else:
        flag = True


    data_vencimento = waitForImage(image = data_vencimento_img, timeout=60, name = 'DATA VENCIMENTO')
    if data_vencimento is not None and flag == False:
        x_img, y_img = pyautogui.center(data_vencimento)
        y_img = y_img + 20
        pyautogui.doubleClick(x_img, y_img)
        logging.info('CLICK - DATA VENCIMENTO')
        sleep(1)
        pyautogui.write(data)
        logging.info(f'Data vencimento {data}')
    else:
        flag = True


    data_prev = waitForImage(image = data_prev_img, timeout=60, name = 'DATA PREV')
    if data_prev is not None and flag == False:
        x_img, y_img = pyautogui.center(data_prev)
        y_img = y_img + 20
        pyautogui.doubleClick(x_img, y_img)
        logging.info('CLICK - DATA PREV')
        pyautogui.write(data)
        logging.info(f'Data prev {data}')
    else:
        flag = True


    historico_click = waitForImage(image = historico_img, timeout=60, name = 'HISTORICO')
    if historico_click is not None and flag == False:
        x_img, y_img = pyautogui.center(historico_click)
        y_img = y_img + 20
        for i in range(50):
            pyautogui.doubleClick(x_img, y_img)
            pyautogui.hotkey('delete')
        logging.info('CLICK - HISTORICO')
        sleep(1)
        pyautogui.write(historico)
        logging.info(f'Histórico definido {historico}')
    else:
        flag = True


    select_valores = waitForImage(image = valores, timeout=30, name = 'VALORES')
    if select_valores is not None and flag == False:
        pyautogui.click(select_valores)
        logging.info('CLICK EM VALORES')
        sleep(1)
    else:
        flag = True


    valor_original = waitForImage(image = valor_original_img, timeout=30, name = 'VALOR ORIGINAL')
    if valor_original is not None and flag == False:
        x_img, y_img = pyautogui.center(valor_original)
        y_img = y_img + 20
        pyautogui.doubleClick(x_img, y_img)
        logging.info('CLICK EM VALOR ORIGINAL')
        pyautogui.write(valor)
        pyautogui.hotkey('tab')
    else:
        flag = True


    rateio(flag)    


    conta_caixa_loc = waitForImage(image = conta_caixa_img, timeout=30, name = 'CONTA CAIXA')
    if conta_caixa_loc is not None and flag == False:
        x_imagem, y_imagem, largura_imagem, altura_imagem = conta_caixa_loc
        x_quina_esquerda = x_imagem + 10
        y_quina_inferior = y_imagem + altura_imagem - 10
        
        pyautogui.click(x_quina_esquerda, y_quina_inferior)
        sleep(5)

        pyautogui.write(conta_caixa)
        logging.info(f'Conta caixa digitada: {conta_caixa}')
        pyautogui.hotkey('enter')
        sleep(3)
        pyautogui.hotkey('enter')
    else:
        flag = True
        

    dados_adicionais_loc = waitForImage(image = dados_adicionais_img, timeout=30, name = 'DADOS ADICIONAIS')
    if dados_adicionais_loc is not None and flag == False:
        pyautogui.click(dados_adicionais_loc)
        logging.info('CLICK EM DADOS ADICIONAIS')
        sleep(3)

        for i in range(3):
            pyautogui.hotkey('tab')
        logging.info(f'TAB clicado 3 vezes')

        pyautogui.hotkey('enter')
        logging.info(f'Centro de Custo acessado com enter')
        sleep(3)

        pyautogui.hotkey('shift','tab')
        logging.info(f"'shift','tab'")
        sleep(0.2)

        pyautogui.write('codigo')
        logging.info(f'escreve codigo')
        sleep(0.2)

        pyautogui.hotkey('tab')
        logging.info(f"'tab'")
        sleep(0.2)

        pyautogui.write(centro_custo)
        logging.info(f'Centro de Custo digitado: {centro_custo}')

        pyautogui.hotkey('enter')
        sleep(3)
        pyautogui.hotkey('enter')
    else:
        flag = True


    rateio(flag)


    opcionais = waitForImage(image = opcionais_img, timeout=30, name = 'OPCIONAIS')
    if opcionais is not None and flag == False:
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
        pyautogui.hotkey('enter')
    else:
        flag = True


    salvar = waitForImage(image = salvar_img, timeout=30, name = 'SALVAR')
    if salvar is not None and flag == False:
        pyautogui.click(salvar)
        logging.info('CLICK EM SALVAR')
    else:
        flag = True


    ok_button = waitForImage(image = ok_img, timeout=30, name = 'SALVAR')
    if ok_button is not None and flag == False:
        pyautogui.click(ok_button)
        logging.info('CLICK EM SALVAR')
    else:
        flag = True

    
    if flag == True:
        check_erro()
        logging.info('FUNÇÃO copiar_processo ENCONTROU UM ERRO AO BUSCAR ALGUMA IMAGEM')
        erro = 'Erro ao copiar processo'
        return erro



def desmark_filter():

    #cc.wait_appear(locator.rm.checkbox_lançamentos_a_receber, wait_timeout=600)
    cc.wait_appear(locator.rm.checkbox_lançamentos_a_receber, wait_timeout=600).click()
    logging.info('CLICK CHECKBOX LANÇAMENTOS A RECEBER')

    cc.wait_appear(locator.rm.checkbox_lançamentos_baixados, wait_timeout=15).click()
    logging.info('CLICK CHECKBOX LANÇAMENTOS BAIXADOS')

    cc.wait_appear(locator.rm.checkbox_lançamentos_cancelados, wait_timeout=15).click()
    logging.info('CLICK CHECKBOX LANÇAMENTOS CANCELADOS')

    cc.wait_appear(locator.rm.checkbox_lançamentos_faturados, wait_timeout=15).click()
    logging.info('CLICK CHECKBOX LANÇAMENTOS FATURADOS')

    cc.wait_appear(locator.rm.button_atualiza_filtro, wait_timeout=15).click()
    logging.info('ATUALIZA O FILTRO')


def check_table_record():


    logging.info('VERIFICANDO SE A TABELA ESTÁ VAZIA')

    texto = cc.wait_appear(locator.rm.button_00, wait_timeout=120)
    txt_extraido = texto.get_text()
    resultado = re.search(r"/(\d+)", txt_extraido)
    count = int(resultado.group(1))
    logging.info(f'Resultado de buscas: {count}')

    return count



def encerra_prog():
    pidKillFinish()

    #workbook.save(f'{writer}') 

    logging.info('RM ENCERRADO')

'''def check_inv():

    sleep(5)
    select_first_row = cc.wait_appear(locator.rm.dataitem_ref_lançamento_row0, wait_timeout=120)
    select_first_row.click()
    logging.info('SELECIONA A PRIMEIRA LINHA REF LANÇAMENTO')

    for i in range (16):
        pyautogui.press('right')
    logging.info('16 PASSOS PARA DIREITA')

    for i in range(rows_int):

        vetor_inv = []

        sleep(2)
        logging.info('ctrl c')
        pyautogui.hotkey('ctrl', 'c')
        sleep(2)
        inv_number = pyperclip.paste()
        logging.info(f'INV: {inv_number}')

        if inv_number in vetor_inv:
            sleep(2)
            pyautogui.hotkey('ctrl', 'enter')

            select_valores = waitForImage(image = valor, timeout=30, name = 'INTEGRAÇÃO BANCÁRIA')
            if select_valores is not None:
                sleep(2)
                pyautogui.click(select_valores)
                logging.info('CLICK EM VALOR')

            for i in range (4):
                pyautogui.press('tab')
            logging.info('4 TAB')

            pyautogui.press('enter')
            sleep(3)
            pyautogui.write(vetor_inv.moeda)
            sleep(2)
            pyautogui.press('enter')
            sleep(2)
            pyautogui.press('enter')

            btt_ok = waitForImage(image = button_ok, timeout=10, name = 'PRESS BUTTON OK')
            if btt_ok is not None:
                sleep(2)
                pyautogui.click(btt_ok)
                logging.info('APERTA OK')
                sleep(2)

            baixa_inv()
            
        else:
            pyautogui.press('down')
            logging.info('APERTA PARA BAIXO PARA VERIFICAR O PRÓXIMO REGISTRO')
            sleep(2)'''


def selecionar_processo1(quant_res):

    
    cc.wait_appear(locator.rm.checkbox_lançamentos_a_receber, wait_timeout=360)

    largura_tela, altura_tela = pyautogui.size()

    meio_x = largura_tela // 2
    meio_y = altura_tela // 2

    pyautogui.moveTo(meio_x, meio_y)

    sleep(1)

    #cc.mouse.scroll(quant_res)
    #logging.info(f'MOVIDO PRA CIMA {quant_res} VEZES')
    cont=0
    while cont < quant_res:
        if cc.wait_appear(locator.rm.dataitem_x_row0, wait_timeout=1):
            referencia_inicial = cc.wait_appear(locator.rm.dataitem_x_row0, wait_timeout=1) 
            posicao = referencia_inicial.get_position()
            x, y = posicao.Right + 20 , (posicao.Bottom + posicao.Top) // 2
            pyautogui.moveTo(x, y)
            pyautogui.click()
            logging.info('PRIMEIRA CELULA CLICADA')
            break
        else:
            cc.mouse.scroll(1)
            logging.info(f'MOVIDO')
    
    logging.info(f'MOVIDO PRA CIMA {cont} VEZES')

    for esquerda in range (35):
        pyautogui.press('left')
    logging.info('35 PASSOS PARA ESQUERDA')

    for direita in range (14):
        pyautogui.press('right')
    logging.info('14 PASSOS PARA DIREITA')

    sleep(2)
    
    data_recente = waitForImage1(image = data_recente_img, timeout=5, name = 'DATA DE VENCIMENTO RECENTE')
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
                return erro

            sleep(5)

            primeira_linha_RM(quant_res)


def selecionar_processo():
    
    cc.wait_appear(locator.rm.checkbox_lançamentos_a_receber, wait_timeout=360)
        
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
        sleep(2)

    data_recente = waitForImage1(image = data_recente_img, timeout=1, name = 'DATA DE VENCIMENTO RECENTE')
    if data_recente is not None:
        logging.info('DATA DE VENCIMENTO RECENTE DEFINIDA')

    else:
        cont = 0
        while data_recente is None:
            cont +=1
            cc.wait_appear(locator.rm.header_data_de_vencimento, wait_timeout=1).click()
            logging.info('DATA DE VENCIMENTO RECENTE TROCADA')

            largura_tela, altura_tela = pyautogui.size()
            meio_x = largura_tela // 2
            meio_y = altura_tela // 2
            pyautogui.moveTo(meio_x, meio_y)

            data_recente = waitForImage1(image = data_recente_img, timeout=1, name = 'DATA DE VENCIMENTO RECENTE')
            if data_recente is not None:
                logging.info('DATA DE VENCIMENTO RECENTE ENCONTRADA')
            else:
                logging.info('DATA DE VENCIMENTO RECENTE NÃO ENCONTRADA')

            if cont == 10:
                erro = 'Data de vencimento mais recente não definida'
                return erro

            sleep(2)

        erro = primeira_linha_RM()
        return erro



def primeira_linha_RM():

    erro = None

    cc.wait_appear(locator.rm.checkbox_lançamentos_a_receber, wait_timeout=360)

    largura_tela, altura_tela = pyautogui.size()
    meio_x = largura_tela // 2
    meio_y = altura_tela // 2
    pyautogui.moveTo(meio_x, meio_y)
    sleep(1)

    logging.info(f'MOVENDO PRA CIMA')
    cont = 0
    referencia_inicial = cc.wait_appear(locator.rm.dataitem_x_row0, wait_timeout=1)
    while not referencia_inicial: 
        cc.mouse.scroll(10)
        logging.info(f'MOVIDO PRA CIMA {cont+1} vezes')
        referencia_inicial = cc.wait_appear(locator.rm.dataitem_x_row0, wait_timeout=1)
        sleep(3)
        if cont>=50:
            erro = 'Erro na tabela do RM'
            return erro
        cont += 1
    logging.info(f'PRIMEIRA LINHA ENCONTRADA')

    posicao = referencia_inicial.get_position()
    x, y = posicao.Right + 20 , (posicao.Bottom + posicao.Top) // 2
    pyautogui.moveTo(x, y)
    pyautogui.click()
    logging.info('PRIMEIRA CELULA CLICADA')



def check_inv(inv, coligada, quant_res):

    erro = primeira_linha_RM()
    if erro:
        return erro , None

    
    for esquerda in range (35):
        pyautogui.press('left')
    logging.info('35 PASSOS PARA ESQUERDA')

    for direita in range (18):
        pyautogui.press('right')
    logging.info('18 PASSOS PARA DIREITA')

    sleep(2)

    for i in range(quant_res):

        logging.info(f'BUSCA NA LINHA: {i+1}')


        #inv = informacoes_extraidas()
        padrao = re.compile(r'INV - ?(\d+) ?- (.+)$')

        logging.info('ctrl c')
        pyautogui.hotkey('ctrl', 'c')
        sleep(0.5)
        historico = pyperclip.paste()
        logging.info(f'Historico completo: {historico}')

        localizar = padrao.search(historico)
        if localizar:
            inv_number = localizar.group(1)
            nome_coligada = localizar.group(2)
        else:
            inv_number = 'erro: INV NÃO ENCONTRADA'
            nome_coligada = 'erro: COLIGADA NÃO ENCONTRADA'

        logging.info(f'INV E COLIGADA BUSCADAS: {inv} - {coligada}')

        inv_number1 = inv_number.lower()
        inv1 = inv.lower()
        coligada1 = coligada.lower()
        nome_coligada1 = nome_coligada.lower()

        coligada2 = coligada1.replace('.','')
        coligada21 = coligada2.replace(' - ',' ')
        coligada22 = coligada21.replace(' e ',' & ')
        coligada23 = coligada22.replace(' and ',' & ')
        coligada24 = coligada23.replace(' inc','')

        coligada3 = coligada1.replace(' - ',' ')
        coligada31 = coligada3.replace('.','')
        coligada32 = coligada31.replace(' e ',' & ')
        coligada33 = coligada32.replace(' and ',' & ')
        coligada34 = coligada33.replace(' inc','')

        coligada4 = coligada1.replace(' e ',' & ')
        coligada41 = coligada4.replace('.','')
        coligada42 = coligada41.replace(' - ',' ')

        coligada5 = coligada1.replace(' and ',' & ')
        coligada51 = coligada5.replace('.','')
        coligada52 = coligada51.replace(' - ',' ')

        if inv1 in inv_number1 and coligada1 in nome_coligada1 or \
            \
            inv1 in inv_number1 and coligada2 in nome_coligada1 or \
            inv1 in inv_number1 and coligada21 in nome_coligada1 or \
            inv1 in inv_number1 and coligada22 in nome_coligada1 or \
            inv1 in inv_number1 and coligada23 in nome_coligada1 or \
            inv1 in inv_number1 and coligada24 in nome_coligada1 or \
            \
            inv1 in inv_number1 and coligada3 in nome_coligada1 or \
            inv1 in inv_number1 and coligada31 in nome_coligada1 or \
            inv1 in inv_number1 and coligada32 in nome_coligada1 or \
            inv1 in inv_number1 and coligada33 in nome_coligada1 or \
            inv1 in inv_number1 and coligada34 in nome_coligada1 or \
            \
            inv1 in inv_number1 and coligada4 in nome_coligada1 or \
            inv1 in inv_number1 and coligada41 in nome_coligada1 or \
            inv1 in inv_number1 and coligada42 in nome_coligada1 or \
            \
            inv1 in inv_number1 and coligada5 in nome_coligada1 or \
            inv1 in inv_number1 and coligada51 in nome_coligada1 or \
            inv1 in inv_number1 and coligada52 in nome_coligada1 :


            sleep(0.5)
            logging.info(f'INV E COLIGADA CORRETA ENCONTRADA: {inv_number} - {nome_coligada}')

            for direita in range (6):
                pyautogui.press('right')
            logging.info('6 PASSO PARA DIREITA')

            pyautogui.hotkey('ctrl', 'c')
            logging.info('ctrl c')
            sleep(0.5)
            centro_custo = pyperclip.paste()
            logging.info(f'centro_custo: {centro_custo}')


            '''for esquerda in range (4):
                pyautogui.press('left')
            logging.info('4 PASSOS PARA ESQUERDA')

            pyautogui.hotkey('ctrl', 'c')
            logging.info('ctrl c')
            sleep(0.5)

            valor_processo = pyperclip.paste()
            for _ in range(3):
                valor_processo = valor_processo.replace(".","")
            logging.info(f'VALOR PROCESSO: {valor_processo}')
            logging.info(f'VALOR PROCESSO2: {type(valor_processo)}')

            if valor_processo == valor_extrato:
                logging.info('VALOR CORRETO ENCONTRADO.')
                break'''
            
            break
            
            
        if i+1 == quant_res:
            logging.info(f'ULTIMA INV, COLIGADA OU VALOR INCORRETAS ENCONTRADAS: {inv_number} - {nome_coligada}')
            
            erro = f'Processo não encontrado'
            logging.info(f'{erro}')
            return erro , None
        
        logging.info(f'INV, COLIGADA OU VALOR INCORRETAS ENCONTRADAS: {inv_number} - {nome_coligada}')
        sleep(0.3)

        pyautogui.press('down')
        logging.info('APERTA PARA BAIXO PARA VERIFICAR O PRÓXIMO REGISTRO')

    return None , centro_custo
    



def define_moeda(moeda):
    
    select_valores = waitForImage(image = valores, timeout=30, name = 'INTEGRAÇÃO BANCÁRIA')
    if select_valores is not None:
        sleep(2)
        pyautogui.click(select_valores)
        logging.info('CLICK EM VALOR')

    for i in range (4):
        pyautogui.press('tab')
    logging.info('4 TAB')

    pyautogui.press('enter')
    sleep(3)
    pyautogui.write(moeda)
    logging.info(f'MOEDA PREENCHIDA COM {moeda}')

    sleep(2)
    pyautogui.press('enter')
    sleep(2)
    pyautogui.press('enter')

    btt_ok = waitForImage(image = button_ok, timeout=10, name = 'PRESS BUTTON OK')
    if btt_ok is not None:
        sleep(2)
        pyautogui.click(btt_ok)
        logging.info('APERTA OK')
        sleep(2)


def baixar_lancamento(valor_extr):
    
    cc.wait_appear(locator.rm.dataitem_x_row0, wait_timeout=360).click()
    logging.info('PRIMEIRA CELULA CLICADA')

    cc.wait_appear(locator.rm.button_baixa, wait_timeout=60).click()
    logging.info('SELECIONA BOTÃO BAIXA')

    try:
        cc.wait_appear(locator.rm.button_btnok2, wait_timeout=30).click()
        logging.info('CLICA OK')
    except:
        logging.info('POPUP BOTÃO OK NÃO APARECEU')
        pass

    cc.wait_appear(locator.rm.button_btnnext, wait_timeout=120).click()
    logging.info('CLICA AVANÇAR')

    sleep(5)

    cc.wait_appear(locator.rm.radiobutton_simplificada, wait_timeout=120).click()
    logging.info('SELECIONA SIMPLIFICADA')

    conta_caixa_ext = cc.wait_appear(locator.rm.edit_lkpcontacaixalookupeditinneredit, wait_timeout=60).get_text()
    logging.info(f'CONTA CAIXA: {conta_caixa_ext}')

    if conta_caixa.lower() in conta_caixa_ext.lower():
        logging.info('CONTA CAIXA PREENCHIDA CORRETAMENTE')

    else:
        logging.info('CONTA CAIXA NÃO PREENCHIDA CORRETAMENTE')

        cc.wait_appear(locator.rm.button_lkpcontacaixalookupeditinneredit, wait_timeout=30).click()
        logging.info(f'Abrir Conta Caixa clicada')

        cc.wait_appear(locator.rm.edit_tbxsearch1, wait_timeout=30).click()
        logging.info(f'Selecionar Conta Caixa clicada')

        #pyautogui.write(r'02675-5')
        pyautogui.write(conta_caixa)
        logging.info(f'Escreve a conta caixa: {conta_caixa}')
        sleep(1)

        pyautogui.hotkey('enter')
        logging.info('Aperta enter')
        sleep(1)

        pyautogui.hotkey('enter')
        logging.info('Aperta enter')
        sleep(1)

    cc.wait_appear(locator.rm.button_btnnext1, wait_timeout=60).click()
    logging.info(f'AVANÇAR')


    valor_total_rm = cc.wait_appear(locator.rm.edit_cvalordabaixadolancto, wait_timeout=60).get_text()
    for _ in range(3):
        valor_total_rm = valor_total_rm.replace(".","")
    logging.info(f'VALOR TOTAL REF NO RM: {valor_total_rm}')

    if valor_total_rm != valor_extr:
        erro = 'Valores do Extrato e RM divergentes'
        logging.info(f'{erro}')
        return erro

    '''if valor_original_ref > valor_total_rm:
        logging.info(f'Valor extraído do pdf maior do que valor do RM')

        valor_original_ref = float(valor_original_ref.replace(',','.'))
        valor_total_rm = float(valor_total_rm.replace(',','.'))

        diferenca_valor = str(round(valor_original_ref - valor_total_rm, 2))

        cc.wait_appear(locator.rm.edit_cvalorjuros, wait_timeout=30).double_click()
        logging.info(f'Juros clicada')

        pyautogui.write(diferenca_valor.replace('.',','))
        logging.info(f"Preenche juros com: {diferenca_valor.replace('.',',')}")
        sleep(1)

        pyautogui.hotkey('tab')
        logging.info('Aperta tab')


    elif valor_original_ref < valor_total_rm:
        erro = f'Valor extraído do pdf menor do que valor do RM'
        logging.info(f'{erro}')
        return erro'''

    cc.wait_appear(locator.rm.button_btnnext1, wait_timeout=60).click()
    logging.info(f'AVANÇAR')

    cc.wait_appear(locator.rm.button_btnnext1, wait_timeout=60).click()
    logging.info(f'AVANÇAR')

    cc.wait_appear(locator.rm.button_btnnext1, wait_timeout=60).click()
    logging.info(f'EXECUTAR')

    cc.wait_appear(locator.rm.button_btncancel, wait_timeout=300)

    processa_success = waitForImage(image = baixa_success, timeout=15, name = 'PRESS BUTTON OK')
    if processa_success is not None:
        logging.info('SUCESSO')

    else:
        erro = 'ERRO AO BAIXAR REF'
        logging.info(f'{erro}')
        pyautogui.hotkey('alt', 'f4')
        sleep(0.5)
        pyautogui.hotkey('alt', 'f4')
        return erro

    cc.wait_appear(locator.rm.edit_textboxlog1, wait_timeout=15).click()
    sleep(2)
    pyautogui.hotkey('ctrl', 'a')
    sleep(2)
    pyautogui.hotkey('ctrl', 'c')
    sleep(2)
    txt_log = pyperclip.paste()
    logging.info(f'{txt_log}')

    cc.wait_appear(locator.rm.button_btncancel, wait_timeout=60).click()
    logging.info(f'FECHAR')



def informacoes_extraidas():
    return """
[
    {
        "pi": "teste",
        "inv": "00525829",
        "moeda": "EUR",
        "valor": "1000",
        "nome": "teste1",
        "cod": "teste2"
    }
]
    """

"""
[
    {
        "pi": "",
        "inv": "000747431",
        "moeda": "NOK",
        "valor": "1000",
        "nome": "",
        "cod": ""
    },
    {
        "pi": "",
        "inv": "01401514",
        "moeda": "GBP",
        "valor": "2000",
        "nome": "",
        "cod": ""
    }
]
    """


def baixa_inv(valor_original, conta_certa):

    sleep(2)
    pyautogui.hotkey('ctrl', 'space')
    logging.info('CHECK LINHA')

    baixa_inv = cc.wait_appear(locator.rm.button_baixa, wait_timeout=60)
    baixa_inv.click()
    logging.info('SELECIONA BOTÃO BAIXA')

    try:
        button_ok = cc.wait_appear(locator.rm.button_btnok1, wait_timeout=30)
        button_ok.click()
        logging.info('CLICA OK')
    except:
        logging.info('POPUP BOTÃO OK NÃO APARECEU')
        pass

    avancar = cc.wait_appear(locator.rm.button_btnnext, wait_timeout=120)
    avancar.click()
    logging.info('CLICA AVANÇAR')

    sleep(5)

    simplificada = cc.wait_appear(locator.rm.radiobutton_simplificada, wait_timeout=120)
    simplificada.click()
    logging.info('SELECIONA SIMPLIFICADA')

    data = cc.wait_appear(locator.rm.edit_data, wait_timeout=60)
    date = data.get_text()
    logging.info(f'DATA AUTOMÁTICA: {date}')

    ## SE NECESSÁRIO DIFITAR DATA
    data.set_text('20112023')
    pyautogui.hotkey('tab')

    ###entrar if para compara com a data do documento inicial

    '''conta_caixa = cc.wait_appear(locator.rm.edit_lkpcontacaixacode, wait_timeout=60)
    conta = conta_caixa.get_text()'''

    
    erro1 = cc.wait_appear(locator.rm.titlebar_titlebar, wait_timeout=1)
    erro2 = cc.wait_appear(locator.rm.window_rm, wait_timeout=1)
    erro3 = cc.wait_appear(locator.rm.pane_rmspictureedit1, wait_timeout=1)

    if erro1 or erro2 or erro3:
        erro = f'ERRO ENVOLVENDO MOEDA OU DATA'
        logging.info(f'{erro}')
        pyautogui.hotkey('alt', 'f4')
        sleep(0.5)
        pyautogui.hotkey('alt', 'f4')
        return erro
    

    conta_caixa = cc.wait_appear(locator.rm.edit_lkpcontacaixalookupeditinneredit, wait_timeout=60)
    conta = conta_caixa.get_text()
    logging.info(f'CONTA CAIXA: {conta}')

    '''if conta != '':
        logging.info('CONTA CAIXA PREENCHIDA')
    else:
        logging.info('CONTA CAIXA NÃO PREENCHIDA')'''
    if conta_certa.lower() in conta.lower():
        logging.info('CONTA CAIXA PREENCHIDA CORRETAMENTE')
    else:
        logging.info('CONTA CAIXA NÃO PREENCHIDA CORRETAMENTE')
    
    
    
    avancar = cc.wait_appear(locator.rm.button_btnnext, wait_timeout=60)
    avancar.click()
    logging.info(f'AVANÇAR')

    valor = cc.wait_appear(locator.rm.edit_cvalordabaixadolancto, wait_timeout=60)
    valor_inv = valor.get_text()
    logging.info(f'VALOR INV: {valor_inv}')

    if valor_original != valor_inv:
        erro = f'PROCESSAMENTO INTERROMPIDO - VALOR DE DOCUMENTO DIFERENTE DO EXTRAIDO'
        logging.info(f'{erro}')
        pyautogui.hotkey('alt', 'f4')
        sleep(0.5)
        pyautogui.hotkey('alt', 'f4')
        return erro

    avancar = cc.wait_appear(locator.rm.button_btnnext, wait_timeout=60)
    avancar.click()
    logging.info(f'AVANÇAR')

    avancar = cc.wait_appear(locator.rm.button_btnnext, wait_timeout=60)
    avancar.click()
    logging.info(f'AVANÇAR')

    exec = cc.wait_appear(locator.rm.button_btnnext, wait_timeout=60)
    exec.click()
    logging.info(f'EXECUTAR')

    processa_success = waitForImage(image = baixa_success, timeout=120, name = 'PRESS BUTTON OK')
    if processa_success is not None:
        sleep(2)
        logging.info('OK SUCESSO')
        sleep(2)
    else:
        erro = 'ERRO AO BAIXAR INV'
        logging.info(f'{erro}')
        pyautogui.hotkey('alt', 'f4')
        sleep(0.5)
        pyautogui.hotkey('alt', 'f4')
        return erro

    log = cc.wait_appear(locator.rm.edit_textboxlog3, wait_timeout=180)
    txt_log = log.get_text()
    logging.info(f'{txt_log}')

    close = cc.wait_appear(locator.rm.button_btncancel, wait_timeout=60)
    close.click()
    logging.info(f'FECHAR')



# wait for image with pyautogui
'''def waitForImage(image, timeout, name):
    inicialTime = time()

    while True:
        #try:
        # try to find image on screen
        location = pyautogui.locateOnScreen(image, confidence=0.9)

        if location is not None:
            # Image found
            logging.info(f'{name} image found.')
            return location

        #except:
        # checking if timeout is over
        else:
            currentTime = time()
            if currentTime - inicialTime >= timeout:
                # timeout is over and the image was not found.
                logging.info(f'{name} image not found.')
                return None

        # waiting for searching again
        sleep(0.5)
'''

def waitForImage2(image, timeout, name):
    inicialTime = time()
    try:
        while True:
            # try to find image on screen
            location = pyautogui.locateOnScreen(image, confidence=0.9)

            if location is not None:
                # Image found
                logging.info(f'{name} image found.')
                return location

            #except:
            # checking if timeout is over
            else:
                currentTime = time()
                if currentTime - inicialTime >= timeout:
                    # timeout is over and the image was not found.
                    logging.info(f'{name} image not found.')
                    return None

            # waiting for searching again
            sleep(0.5)
    except:
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
                currentTime = time()
                if currentTime - inicialTime >= timeout:
                    # timeout is over and the image was not found.
                    logging.info(f'{name} image not found.')
                    return None

                # waiting for searching again
                sleep(0.1)


def waitForImage(image, timeout, name):
    inicialTime = time()

    while True:
        try:
            # try to find image on screen
            location = pyautogui.locateOnScreen(image, confidence=0.9)

            if location is not None:
                # Image found
                logging.info(f'{name} image found.')
                return location

            #except:
            # checking if timeout is over
            else:
                currentTime = time()
                if currentTime - inicialTime >= timeout:
                    # timeout is over and the image was not found.
                    logging.info(f'{name} image not found.')
                    return None

            # waiting for searching again

        except:
            currentTime = time()
            if currentTime - inicialTime >= timeout:
                # timeout is over and the image was not found.
                logging.info(f'{name} image not found.')
                return None
            

def waitForImage1(image, timeout, name):
    inicialTime = time()

    while True:
        try:
            # try to find image on screen
            location = pyautogui.locateOnScreen(image, confidence=0.98)

            if location is not None:
                # Image found
                logging.info(f'{name} image found.')
                return location

            #except:
            # checking if timeout is over
            else:
                currentTime = time()
                if currentTime - inicialTime >= timeout:
                    # timeout is over and the image was not found.
                    logging.info(f'{name} image not found.')
                    return None

            # waiting for searching again

        except:
            currentTime = time()
            if currentTime - inicialTime >= timeout:
                # timeout is over and the image was not found.
                logging.info(f'{name} image not found.')
                return None


def emailSuccess(nome_bot, texto_msg):
    with open(f'{email_path}/emailSuccess.html', 'r', encoding='utf=8') as fileSuccess:
        templateSuccess = fileSuccess.read()
        htmlSuccess = templateSuccess.format(automacao = nome_bot, mensagem = texto_msg)
    yag.send(to=str(email_receivers).split(','), subject=f"SUCESSO - BOT REMESSAS PIX",
    contents=htmlSuccess,
    attachments=f'{log_path}/{today}/{log_file_name}.log')
    logging.info('Success e-mail sent.')

def emailErro():
    with open(f'{email_path}/emailError.html', 'r', encoding='utf=8') as fileSuccess:
        templateSuccess = fileSuccess.read()
        htmlSuccess = templateSuccess
    yag.send(to=str(email_receivers).split(','), subject=f"ERRO - BOT REMESSAS PIX",
    contents=htmlSuccess,
    attachments=f'{log_path}/{today}/{log_file_name}.log')
    logging.info('Warning e-mail sent.')



def headerExcel():
    global workbook, sheet

    logging.info('Criando EXCEL')

    workbook = openpyxl.Workbook()

    sheet = workbook.active
    sheet.title = 'Liq Cambio - Processados'
    logging.info('Liq Cambio - Processados criado')

    sheet["A1"] = "Data do extrato"
    sheet["B1"] = "Valor do extrato"
    sheet["C1"] = "Descrição do extrato"
    sheet["D1"] = "Banco"
    sheet["E1"] = "Cambial"
    sheet["F1"] = "Invoice"
    sheet["G1"] = "Pagador"
    sheet["H1"] = "Moeda"
    sheet["I1"] = "Valor"
    sheet["J1"] = "IR"
    sheet["K1"] = "CIDE"
    sheet["L1"] = "PIS"
    sheet["M1"] = "COFINS"
    sheet["N1"] = "IOF"
    sheet["O1"] = "ERRO"
    sheet["P1"] = "STATUS"

    sheet = workbook.create_sheet("Impostos - Processados")
    logging.info('Impostos - Processados criado')

    sheet['A1'] = 'DATA'
    sheet['B1'] = 'DESCRIÇÃO'
    sheet['C1'] = 'IMPOSTO'
    sheet['D1'] = 'VALOR IMPOSTO'
    sheet['E1'] = 'VALOR MULTA'
    sheet['F1'] = 'CENTRO DE CUSTO'
    sheet['G1'] = 'HISTÓRICO'
    sheet['H1'] = 'ERRO'
    sheet['I1'] = 'STATUS'

    workbook.save(f'{writer}') 

    logging.info('EXCEL iniciado')


def create_excel_extrato(linha_list):

    sheet = workbook.create_sheet("Extrato")
    logging.info('Extrato criado')

    sheet['A1'] = 'DATA'
    sheet['B1'] = 'DESCRIÇÃO'
    sheet['C1'] = 'VALOR'
    sheet['D1'] = 'COMPLEMENTO'

    for linha in linha_list:
    
        row_index = 1
        while sheet[f'A{row_index}'].value is not None:
            row_index += 1
        
        sheet[f'A{row_index}'] = linha["data"]
        sheet[f'B{row_index}'] = linha["descricao"]
        sheet[f'C{row_index}'] = linha["valor"]
        sheet[f'D{row_index}'] = linha["contrato"]

    workbook.save(f'{writer}') 
    
    logging.info('EXCEL Extrato Criado')


def create_excel_contratos_extraidos(contrato_padrao_list , contrato_fora_padrao_list):
    logging.info('ENTRANDO EM EXCEL Contratos extraidos Criado')
    
    lista_contrat = ["Contratos no padrão", "Contratos fora do padrão"]

    for cont in lista_contrat:
        sheet = workbook.create_sheet(f'{cont}')
        
        sheet["A1"] = "Data do extrato"
        sheet["B1"] = "Valor do extrato"
        sheet["C1"] = "Descrição do extrato"
        sheet["D1"] = "Banco"
        sheet["E1"] = "Cambial"
        sheet["F1"] = "Invoice"
        sheet["G1"] = "Pagador"
        sheet["H1"] = "Moeda"
        sheet["I1"] = "Valor"
        sheet["J1"] = "IR"
        sheet["K1"] = "CIDE"
        sheet["L1"] = "PIS"
        sheet["M1"] = "COFINS"
        sheet["N1"] = "IOF"
 
        lista_info = contrato_padrao_list if cont == "Contratos no padrão" else contrato_fora_padrao_list

        for index, contrato in enumerate(lista_info, start=2):
            sheet[f'A{index}'] = contrato['data_extr']
            sheet[f'B{index}'] = contrato['valor_extr'].replace('.','')
            sheet[f'C{index}'] = contrato['descricao_extr']
            sheet[f'D{index}'] = contrato['banco']
            sheet[f'E{index}'] = contrato['cambial']
            sheet[f'F{index}'] = contrato['inv']
            sheet[f'G{index}'] = contrato['pagador']
            sheet[f'H{index}'] = contrato['moeda']
            sheet[f'I{index}'] = contrato['valor'].replace('.','')
            sheet[f'J{index}'] = contrato['ir'].replace('.','')
            sheet[f'K{index}'] = contrato['cide'].replace('.','')
            sheet[f'L{index}'] = contrato['pis'].replace('.','')
            sheet[f'M{index}'] = contrato['cofins'].replace('.','')
            sheet[f'N{index}'] = contrato['iof'].replace('.','')

    workbook.save(f'{writer}') 

    logging.info('EXCEL Contratos extraidos Criado')


def create_excel_contratos(contrato_extr_list):
    
    sheet = workbook.create_sheet("Contratos Encontrados")
    
    sheet["A1"] = "Data do extrato"
    sheet["B1"] = "Valor do extrato"
    sheet["C1"] = "Descrição do extrato"
    sheet["D1"] = "Banco"
    sheet["E1"] = "Cambial"
    sheet["F1"] = "Invoice"
    sheet["G1"] = "Pagador"
    sheet["H1"] = "Moeda"
    sheet["I1"] = "Valor"
    sheet["J1"] = "IR"
    sheet["K1"] = "CIDE"
    sheet["L1"] = "PIS"
    sheet["M1"] = "COFINS"
    sheet["N1"] = "IOF"

    for index, contrato in enumerate(contrato_extr_list, start=2):
        sheet[f'A{index}'] = contrato['data_extr']
        sheet[f'B{index}'] = contrato['valor_extr'].replace('.','')
        sheet[f'C{index}'] = contrato['descricao_extr']
        sheet[f'D{index}'] = contrato['banco']
        sheet[f'E{index}'] = contrato['cambial']
        sheet[f'F{index}'] = contrato['inv']
        sheet[f'G{index}'] = contrato['pagador']
        sheet[f'H{index}'] = contrato['moeda']
        sheet[f'I{index}'] = contrato['valor'].replace('.','')
        sheet[f'J{index}'] = contrato['ir'].replace('.','')
        sheet[f'K{index}'] = contrato['cide'].replace('.','')
        sheet[f'L{index}'] = contrato['pis'].replace('.','')
        sheet[f'M{index}'] = contrato['cofins'].replace('.','')
        sheet[f'N{index}'] = contrato['iof'].replace('.','')

    workbook.save(f'{writer}') 

    logging.info('EXCEL Contratos Criado')


def createRowLiqExcel(extrato, erro, status):

    #sheet = workbook.active
    sheet = workbook['Liq Cambio - Processados']
    
    row_index = 1
    while sheet[f'A{row_index}'].value is not None:
        row_index += 1

    sheet[f'A{row_index}'] = extrato['valor_extr']
    sheet[f'B{row_index}'] = extrato['data_extr']
    sheet[f'C{row_index}'] = extrato['descricao_extr']
    sheet[f'D{row_index}'] = extrato['banco']
    sheet[f'E{row_index}'] = extrato['cambial']
    sheet[f'F{row_index}'] = extrato['inv']
    sheet[f'G{row_index}'] = extrato['pagador']
    sheet[f'H{row_index}'] = extrato['moeda']
    sheet[f'I{row_index}'] = extrato['valor']
    sheet[f'J{row_index}'] = extrato['ir']
    sheet[f'K{row_index}'] = extrato['cide']
    sheet[f'L{row_index}'] = extrato['pis']
    sheet[f'M{row_index}'] = extrato['cofins']
    sheet[f'N{row_index}'] = extrato['iof']
    sheet[f'O{row_index}'] = erro
    sheet[f'P{row_index}'] = status

    workbook.save(f'{writer}') 


def createRowImpExcel(data, descricao, imposto, valor, valor_multa, centro_custo, historico, erro, status):

    sheet = workbook['Impostos - Processados"']
    
    row_index = 1
    while sheet[f'A{row_index}'].value is not None:
        row_index += 1

    sheet[f'A{row_index}'] = data
    sheet[f'B{row_index}'] = descricao
    sheet[f'C{row_index}'] = imposto
    sheet[f'D{row_index}'] = valor
    sheet[f'E{row_index}'] = valor_multa
    sheet[f'F{row_index}'] = centro_custo
    sheet[f'G{row_index}'] = historico
    sheet[f'H{row_index}'] = erro
    sheet[f'I{row_index}'] = status

    workbook.save(f'{writer}') 


def inicial():

    bot_text_art()
    pidKillFinish()
    headerExcel()

def inicio_RM():
    caps()
    open_RM()
    loggin_RM()
    enter_coligada()


def tranf_pdf_img1():

    arquivos = []
    for dirpath, dirnames, filenames in os.walk(caminho_pdf):
        logging.info(f'dirpath: {dirpath}\n dirnames: {dirnames}\n filenames: {filenames}')

        for arquivo in filenames:
            if 'EXTRATO' in arquivo:
                arquivos.append(os.path.join(dirpath, arquivo))

    logging.info(f'tranf_pdf_img arquivos: {arquivos}')

    caminho_imagem_list = []
    for caminho in arquivos:
        
        caminho_imagem = caminho.split('.')[0]
        caminho_imagem_list.append(caminho_imagem)

        # Abrir o arquivo PDF
        documento_pdf = fitz.open(caminho)

        imagens_list = []
        cont = 0
        for pagina_numero in range(documento_pdf.page_count):
            pagina = documento_pdf.load_page(pagina_numero)
            imagem = pagina.get_pixmap(matrix=fitz.Matrix(5, 5), alpha=False)

            cont += 1
            
            # Salvar a imagem
            #nome_arquivo = f"imagem_{pagina_numero + 1}.jpg"  # ou qualquer outro formato de imagem suportado
            nome_arquivo = f"imagem_{pagina_numero + 1}.jpg"  # ou qualquer outro formato de imagem suportado

            if  os.path.exists(caminho_imagem) == False:
                os.makedirs(caminho_imagem)

            imagem_salva = f'{caminho_imagem}\\{nome_arquivo}'
            

            imagem.save(imagem_salva)
            #imagem.save(f'{caminho_imagem}\\1{nome_arquivo}')
            logging.info(f"Imagem {nome_arquivo} salva.")

            imagens_list.append(nome_arquivo)
            #imagens_list.append(f'1{nome_arquivo}')

        documento_pdf.close()


        for cont, img in enumerate(imagens_list):
            imagem = Image.open(f'{caminho_imagem}\\{img}')
            #imagem = Image.open(f'{img}')

            logging.info(f"Imagem {img} tratada.")

            #nova_resolucao = 150 
            nova_resolucao = 500

            largura_original, altura_original = imagem.size
            nova_largura = int(largura_original * nova_resolucao / 72)  # Convertendo de polegadas para pixels
            nova_altura = int(altura_original * nova_resolucao / 72)  # Convertendo de polegadas para pixels

            #imagem_redimensionada_tranf = imagem.resize((nova_largura, nova_altura), resample=Image.BICUBIC)  # Usando BICUBIC como método de interpolação
            #imagem_redimensionada_tranf = imagem.resize((nova_largura, nova_altura), resample=Image.BILINEAR)  # Usando BICUBIC como método de interpolação
            imagem_redimensionada_tranf = imagem.resize((nova_largura, nova_altura), resample=Image.LANCZOS)  # Usando BICUBIC como método de interpolação

            nome_arquivo_2 = f'red_{img}'

            imagem_redimensionada_tranf.save(f'{caminho_imagem}\\1{img}', dpi=(nova_resolucao, nova_resolucao))
            #imagem1 = preprocess_image(f'{caminho_imagem}\\{nome_arquivo_2}', f'{caminho_imagem}\\proc_{nome_arquivo_2}')

    return caminho_imagem_list


def preprocess_image1(image_path):

    logging.info(f'image_path: {image_path}')

    
    image = cv2.imread(image_path)

    try:
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    except:
        gray = image

    # Suavização para reduzir ruído (experimente diferentes algoritmos)
    #blur = cv2.GaussianBlur(gray, (5, 5), 0)
    blur = cv2.medianBlur(gray, 5)  # Suavização mediana
    #blur = cv2.bilateralFilter(gray, 9, 75, 75)  # Filtro bilateral



    # Limiarização adaptativa para melhor lidar com iluminação variável
    thresh = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]
    #_, thresh = cv2.threshold(blur, 127, 255, cv2.THRESH_BINARY)
    #thresh = cv2.adaptiveThreshold(blur, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 9, 2)
    #thresh = cv2.thresholdOTSU(blur, 0, 255, cv2.THRESH_BINARY)[1]
    

    # Morfologia matemática para remover ruídos e melhorar a conectividade
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))
    opening = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel)
    closing = cv2.morphologyEx(opening, cv2.MORPH_CLOSE, kernel)

    return closing

def read_img1(caminho_imagem_list):

    texto_formatado = ''
    for caminho_imagem in caminho_imagem_list:

        arquivos = []
        for dirpath, dirnames, filenames in os.walk(caminho_imagem):
            for arquivo in filenames:
                arquivos.append(os.path.join(dirpath, arquivo))

        logging.info(f'READ_IMG arquivos: {arquivos}')

        for img_tratada in arquivos:
            #imagem = cv2.imread(img_tratada)

            imagem = preprocess_image1(img_tratada)

            pytesseract.pytesseract.tesseract_cmd = pytesseract_caminho

            #texto = pytesseract.image_to_string(imagem, lang='por')
            texto = pytesseract.image_to_string(imagem, config='--psm 6 --oem 3')
            logging.info(texto) 

            linhas = texto.strip().split('\n')

            linhas = [linha.strip() for linha in linhas if linha.strip()]

            #linhas = linhas[3:]

            texto_formatado += '\n'.join(linhas)

            logging.info(f'linhas {linhas}')

            linhas = ''

        logging.info(texto_formatado)

    return texto_formatado

#logging.info(texto_formatado)
def regex_extrato_texto(texto_formatado):

    padrao = re.compile(r"(\d{2}\/\d{2}\/\d{2}) (\D*?\d*?\D*?) (\d*\.?\,?\ ?\d*\.?\,?\ ?\d*\.?\,\ ?\d{2}) (\w.*$)")
    linha_list = []

    for linha in texto_formatado.split("\n"):
        ref = padrao.search(linha)

        if ref:
            data = ref.group(1)
            descricao = ref.group(2)
            if descricao == "lIOF S/CAMBIO" or descricao == "lOF S/CAMBIO":
                descricao = "IOF S/CAMBIO"
            valor = ref.group(3)
            valor = valor.replace(' ','')
            valor = valor.replace('.','')
            contrato = ref.group(4)

            referencia = {
                'data': data,
                'descricao': descricao,
                'valor': valor,
                'contrato': contrato
                }
            
            logging.info(referencia)
            linha_list.append(referencia)


    logging.info(f"linha_list {linha_list}")


    return linha_list

def extrair_contrato():

    #arquivo_extrato = r"C:\oceanica\EXTRATO BTG 012024.pdf"

    arquivos_pdf = glob.glob(os.path.join(caminho_pdf, '*.pdf'))
    logging.info(f'SERÃO TRATADOS {len(arquivos_pdf)} ARQUIVOS.')

    logging.info(f'arquivos: {arquivos_pdf}')

    contrato_padrao_list = []
    contrato_fora_padrao_list = []
    
    for contrato in arquivos_pdf:
        logging.info(f'Contrato: {contrato}')
        nome = contrato.split('PDF\\')[1]
        logging.info(f'nome {nome}')

        contrato_nom = contrato.replace(' ','')
        contrato_nom = contrato_nom.replace('.','')

        #if linha["valor"] in contrato_nom:
            #logging.info(f'Contrato encontrado com o valor {linha["valor"]} {contrato}')

        texto = ''
        with pdfplumber.open(contrato) as pdf:
            for pagina in pdf.pages:
                texto += pagina.extract_text()

        if texto:
            logging.info(f'PDF SEM IMAGEM')
            sem_imagem = 1
            logging.info(f'texto: {texto}')

            contrato_padrao = re.compile(r"Venda Contratação (\d*) \d{2}\/\d{2}\/\d{4}")
            banco_padrao = re.compile(r"Nome CNPJ ?\n(\w.*) \d{2}\.\d{3}\.\d{3}\/\d{4}-\d{2}")
            taxa_camb_padrao = re.compile(r"Taxa Cambial Valor em moeda nacional\n(\d+,\d+)")
            inv_padrao = re.compile(r"(INV|inv|INVOICE|invoice|Inv) (\w+)")
            pagador_padrao = re.compile(r"Pagador ou recebedor no exterior\*\n(\w.*)\n")
            moeda_valor_estr_padrao = re.compile(r"Código Moeda Valor em moeda estrangeira\n([A-Z]{3}) (\d*\.?\,?\ ?\d*\.?\,?\ ?\d*\.?\,\ ?\d{2})")

            ir_padrao = re.compile(r"IR\(0473\) (\d+(\.\d+){0,3}?,\d{2})")
            cide_padrao = re.compile(r"CIDE\(8741\) (\d+(\.\d+){0,3}?,\d{2})")
            pis_padrao = re.compile(r"PIS\(5434\) (\d+(\.\d+){0,3}?,\d{2})")
            cofins_padrao = re.compile(r"COFINS\(5442\) (\d+(\.\d+){0,3}?,\d{2})")
            iof_padrao = re.compile(r"IOF (\d+(\.\d+){0,3}?,\d{2})")


        else:

            logging.info(f'PDF COM IMAGEM')
            sem_imagem = 0
            contrato = pdf_image_to_text(contrato)

            texto = extrair_texto_pdf(contrato)

            if texto:
                logging.info(f'texto: {texto}')

                contrato_padrao = re.compile(r"Venda Contratação (\d*) \d{2}\/\d{2}\/\d{4}")
                banco_padrao = re.compile(r"Instituição autorizada a operar no mercado de câmbio ?\n(\w.*) \d{2}\.\d{3}\.\d{3}\/\d{4}-\d{2}")
                taxa_camb_padrao = re.compile(r"(estrangeira|estrangeilra|estrangeiira) ?\n(\d+,\d+)")
                inv_padrao = re.compile(r"(INV|inv|INVOICE|invoice|Inv) (\w+)")
                pagador_padrao = re.compile(r"Pagador ou recebedor no exterior\*? ?\n(\w.*) ?\n")
                moeda_valor_estr_padrao = re.compile(r"Valor em moeda estrangeira ?\n([A-Z]{3})? ?(\d*\.?\,?\ ?\d*\.?\,?\ ?\d*\.?\,\ ?\d{2})")

                ir_padrao = re.compile(r"IR\(0473\) (\d+(\.\d+){0,3}?,\d{2})")
                cide_padrao = re.compile(r"CIDE\(8741\) (\d+(\.\d+){0,3}?,\d{2})")
                pis_padrao = re.compile(r"PIS\(5434\) (\d+(\.\d+){0,3}?,\d{2})")
                cofins_padrao = re.compile(r"COFINS\(5442\) (\d+(\.\d+){0,3}?,\d{2})")
                iof_padrao = re.compile(r"IOF (\d+(\.\d+){0,3}?,\d{2})")
            
            else:
                logging.info(f'ERRO: PDF com erro')
                continue


        
        flag = False

        contrato_busca = contrato_padrao.search(texto)
        if contrato_busca:
            num_contrato = contrato_busca.group(1)
            logging.info(f'num_contrato {num_contrato}')
        else:
            logging.info(f'Erro num_contrato - {contrato}')
            flag = True
            num_contrato = 'FORA DO PADRÃO'
            #return ### APLICAR ERRO

        banco_busca = banco_padrao.search(texto)
        if banco_busca:
            banco = banco_busca.group(1)
            logging.info(f'banco {banco}')
        else:
            logging.info(f'Erro banco - {contrato}')
            flag = True
            banco = 'FORA DO PADRÃO'
            #return ### APLICAR ERRO

        taxa_camb_busca = taxa_camb_padrao.search(texto)
        if taxa_camb_busca:
            if sem_imagem == 1:
                taxa_camb = taxa_camb_busca.group(1)
            else:
                taxa_camb = taxa_camb_busca.group(2)
            logging.info(f'taxa_camb {taxa_camb}')
        else:
            logging.info(f'Erro taxa_camb - {contrato}')
            flag = True
            taxa_camb = 'FORA DO PADRÃO'
            #return ### APLICAR ERRO
        
        inv_busca = inv_padrao.search(texto)
        if inv_busca:
            inv = inv_busca.group(2)
            logging.info(f'inv {inv}')
        else:
            logging.info(f'Erro inv - {contrato}')
            flag = True
            inv = 'FORA DO PADRÃO'
            #return ### APLICAR ERRO
        
        pagador_busca = pagador_padrao.search(texto)
        if pagador_busca:
            pagador = pagador_busca.group(1)
            logging.info(f'pagador {pagador}')
        else:
            logging.info(f'Erro pagador - {contrato}')
            flag = True
            pagador = 'FORA DO PADRÃO'
            #return ### APLICAR ERRO
        
        moeda_valor_estr_busca = moeda_valor_estr_padrao.search(texto)
        if moeda_valor_estr_busca:
            if sem_imagem == 1:
                moeda = moeda_valor_estr_busca.group(1)
                valor_estr = moeda_valor_estr_busca.group(2)
            else:
                moeda = 'Não encontrada'
                valor_estr = moeda_valor_estr_busca.group(2)
            logging.info(f'moeda {moeda}')
            logging.info(f'valor_estr {valor_estr}')
        else:
            logging.info(f'Erro moeda/valor_estr - {contrato}')
            flag = True
            moeda = 'FORA DO PADRÃO'
            valor_estr = 'FORA DO PADRÃO'
            #return ### APLICAR ERRO
        

        ir_busca = ir_padrao.search(texto)
        if ir_busca:
            ir = ir_busca.group(1)
            logging.info(f'ir {ir}')
        else:
            logging.info(f'Erro {contrato}')
            flag = True
            ir = 'FORA DO PADRÃO'
            #return ### APLICAR ERRO

        cide_busca = cide_padrao.search(texto)
        if cide_busca:
            cide = cide_busca.group(1)
            logging.info(f'cide {cide}')
        else:
            logging.info(f'Erro cide - {contrato}')
            flag = True
            cide  = 'FORA DO PADRÃO'
            #return ### APLICAR ERRO

        pis_busca = pis_padrao.search(texto)
        if pis_busca:
            pis = pis_busca.group(1)
            logging.info(f'pis {pis}')
        else:
            logging.info(f'Erro pis - {contrato}')
            flag = True
            pis  = 'FORA DO PADRÃO'
            #return ### APLICAR ERRO

        cofins_busca = cofins_padrao.search(texto)
        if cofins_busca:
            cofins = cofins_busca.group(1)
            logging.info(f'cofins {cofins}')
        else:
            logging.info(f'Erro cofins - {contrato}')
            flag = True
            cofins  = 'FORA DO PADRÃO'
            #return ### APLICAR ERRO

        iof_busca = iof_padrao.search(texto)
        if iof_busca:
            iof = iof_busca.group(1)
            logging.info(f'iof {iof}')
        else:
            logging.info(f'Erro iof - {contrato}')
            flag = True
            iof  = 'FORA DO PADRÃO'
            #return ### APLICAR ERRO
        

        """contr_extr = {
        'valor_extr': linha["valor"],
        'data_extr': linha["data"],
        'descricao_extr': linha["descricao"],
        'contrato': num_contrato,
        'banco': banco,
        'cambial': taxa_camb,
        'inv': inv,
        'pagador': pagador,
        'moeda': moeda,
        'valor': valor_estr,
        'ir': ir,
        'cide': cide,
        'pis': pis,
        'cofins': cofins,
        'iof': iof
        }"""

        contr_extr = {
        'nome': contrato_nom,
        'contrato': num_contrato,
        'banco': banco,
        'cambial': taxa_camb,
        'inv': inv,
        'pagador': pagador,
        'moeda': moeda,
        'valor': valor_estr,
        'ir': ir,
        'cide': cide,
        'pis': pis,
        'cofins': cofins,
        'iof': iof
        }


        '''else:
            

            contrato_padrao = re.compile(r"Venda Contratação (\d*) \d{2}\/\d{2}\/\d{4}")
            banco_padrao = re.compile(r"Nome CNPJ\n(\w.*) \d{2}\.\d{3}\.\d{3}\/\d{4}-\d{2}")
            taxa_camb_padrao = re.compile(r"Valor em moeda nacional\n(\d+,? ?.?\d+)")
            inv_padrao = re.compile(r"(INV|inv|INVOICE|invoice|Inv) (\w+)")
            pagador_padrao = re.compile(r"Pagador ou recebedor no exterior\*?\n(\w.*)\n")
            moeda_valor_estr_padrao = re.compile(r"Valor em moeda estrangeira\n([A-Z]{3})?(\d*\.?\,?\ ?\d*\.?\,?\ ?\d*\.?\,\ ?\d{2})")

            ir_padrao = re.compile(r"IR\(0473\) (\d+(\.\d+){0,3}?,\d{2})")
            cide_padrao = re.compile(r"CIDE\(8741\) (\d+(\.\d+){0,3}?,\d{2})")
            pis_padrao = re.compile(r"PIS\(5434\) (\d+(\.\d+){0,3}?,\d{2})")
            cofins_padrao = re.compile(r"COFINS\(5442\) (\d+(\.\d+){0,3}?,\d{2})")
            iof_padrao = re.compile(r"IOF (\d+(\.\d+){0,3}?,\d{2})")


            continue

            contr_extr = texto'''
        
        logging.info(f'Informações extraidas: {contr_extr}')
        
        if flag:
            contrato_fora_padrao_list.append(contr_extr)
            logging.info(f'contrato_fora_padrao_list')

        else:
            contrato_padrao_list.append(contr_extr)
            logging.info(f'contrato_padrao_list')


    return contrato_padrao_list , contrato_fora_padrao_list

                
    '''else:
            logging.info(f'Contrato Não encontrado com o valor {linha["valor"]} {contrato}')
            ### APLICAR ERRO'''



def pdf():
    '''caminho_imagem_list = tranf_pdf_img()

    texto_extrato_comp = read_img(caminho_imagem_list)
    logging.info(f'Texto extraído pdf:\n{texto_extrato_comp}')'''

    with open (f'{base_path}/teste/multa.txt', 'r', encoding='utf-8') as texto:
        texto_extrato_comp = texto.read()
    logging.info(f'Texto extraído pdf:\n{texto_extrato_comp}')

    linha_list = regex_extrato_texto(texto_extrato_comp)
    
    padrao_codigo_imposto = re.compile(r"PAG DARF (\d*) ?")
    padrao_codigo_multa = re.compile(r"PAG MULTA ?\/ ?DARF (\d*) ?-")
    imposto_list = []
    liq_cambio_list = []

    for refe in linha_list:
        
        if refe["descricao"] == "LIQ CAMBIO":
            liq_cambio_list.append(refe)
        
        else:
            if 'MULTA' in refe["descricao"]:

                multa = refe["descricao"]
                valor_multa = refe["valor"]
                
                imposto_list[-1]['multa'] = multa
                imposto_list[-1]['valor_multa'] = valor_multa


            elif refe["descricao"] == "IOF S/CAMBIO":
                imposto_list.append(refe)
                imposto_list[-1]['imposto'] = 'IOF'


            else:
                imposto_list.append(refe)
                
                busca = padrao_codigo_imposto.search(refe["descricao"])
                cod_impo = busca.group(1)

                imposto_list[-1]['cod_impo'] = cod_impo
                imposto_list[-1]['imposto'] = config['codigo_imposto'][cod_impo]

    logging.info(f"imposto_list {imposto_list}")
    logging.info(f"liq_cambio_list {liq_cambio_list}")

        
    

    '''contrato_extr_list = []
    for liq_cambio in liq_cambio_list:
        contr_extr = extrair_contrato(liq_cambio)
        if contr_extr != None:
            contrato_extr_list.append(contr_extr)

    logging.info(f'contrato_extr_list {contrato_extr_list}')

    return linha_list, liq_cambio_list, imposto_list, contrato_extr_list'''


def extrato_excel():

    arquivos_na_pasta = os.listdir(caminho_massa)
    arquivos_xls = [arquivo for arquivo in arquivos_na_pasta if arquivo.endswith(('.xls', '.xlsx'))]
    logging.info(f'arquivos_xls {arquivos_xls}')

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

            descricao = str(linha[1])

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

    return linha_list
  


def excel():
    
    linha_list = extrato_excel()
    
    padrao_codigo_imposto = re.compile(r"PAG DARF (\d*) ?")
    padrao_codigo_multa = re.compile(r"PAG MULTA ?\/ ?DARF (\d*) ?-?")
    imposto_list = []
    liq_cambio_list = []

    for refe in linha_list:
        
        if refe["descricao"] == "LIQ CAMBIO":
            liq_cambio_list.append(refe)
        
        else:
            if 'MULTA' in refe["descricao"]:

                multa = refe["descricao"]
                valor_multa = refe["valor"]
                
                imposto_list[-1]['multa'] = multa
                imposto_list[-1]['valor_multa'] = valor_multa


            elif refe["descricao"] == "IOF S/CAMBIO":
                imposto_list.append(refe)
                imposto_list[-1]['imposto'] = 'IOF'


            elif 'PAG DARF' in refe["descricao"]:
                imposto_list.append(refe)
                
                busca = padrao_codigo_imposto.search(refe["descricao"])
                cod_impo = busca.group(1)

                imposto_list[-1]['cod_impo'] = cod_impo
                imposto_list[-1]['imposto'] = config['codigo_imposto'][cod_impo]

    logging.info(f"imposto_list {imposto_list}")
    logging.info(f"liq_cambio_list {liq_cambio_list}")

    contrato_padrao_list , contrato_fora_padrao_list = extrair_contrato()
    logging.info(f"contrato_padrao_list {contrato_padrao_list}")
    logging.info(f"contrato_fora_padrao_list {contrato_fora_padrao_list}")
    create_excel_contratos_extraidos(contrato_padrao_list , contrato_fora_padrao_list)

    contrato_extr_list = []
    for liq_cambio in liq_cambio_list:
        for contrato in contrato_padrao_list:
            #logging.info(f"liq_cambio[valor] {liq_cambio["valor"]} - contrato[contrato_nom] {contrato["contrato_nom"]}")
            if liq_cambio["valor"] in contrato["nome"]:
                logging.info(f'Contrato encontrado com o valor {liq_cambio["valor"]} -> {contrato}')

                contrato['valor_extr'] = liq_cambio["valor"]
                contrato['data_extr'] = liq_cambio["data"]
                contrato['descricao_extr'] = liq_cambio["descricao"]

                contrato_extr_list.append(contrato)
            else:
                logging.info(f'Contrato Não encontrado com o valor {liq_cambio["valor"]} -> {contrato}')

    

    logging.info(f'contrato_extr_list {contrato_extr_list}')

    return linha_list, liq_cambio_list, imposto_list, contrato_extr_list




def getPid():
    logging.info('Dentro função GetPid\n')
    pid_list = []
    name_list = []
    for processName in processList:
        processes = psutil.process_iter(attrs=['pid', 'name'])

        for process in processes:
            pid = process.info['pid']
            name = process.info['name']
            if processName in name: 
                logging.info(f"Process {processName} / PID: {pid} found.")
                pid_list.append(pid)
                name_list.append(processName)
    return pid_list, name_list


def pidKillFinish():
    pid_list, name_list = getPid()

    for pid, name in zip(pid_list, name_list):
        os.kill(pid, signal.SIGTERM)
        logging.info(f'Process {name} / PID: {pid} killed.')



def baixar_ref(valor_multa):

    desmark_filter()
    
    cc.wait_appear(locator.rm.dataitem_x_row0, wait_timeout=360).click()
    logging.info('PRIMEIRA CELULA CLICADA')

    cc.wait_appear(locator.rm.button_baixa, wait_timeout=60).click()
    logging.info('SELECIONA BOTÃO BAIXA')

    try:
        cc.wait_appear(locator.rm.button_btnok1, wait_timeout=30).click()
        logging.info('CLICA OK')
    except:
        logging.info('POPUP BOTÃO OK NÃO APARECEU')
        pass

    cc.wait_appear(locator.rm.button_btnnext, wait_timeout=120).click()
    logging.info('CLICA AVANÇAR')

    sleep(5)

    cc.wait_appear(locator.rm.radiobutton_simplificada, wait_timeout=120).click()
    logging.info('SELECIONA SIMPLIFICADA')

    '''conta_caixa_ext = cc.wait_appear(locator.rm.edit_lkpcontacaixalookupeditinneredit, wait_timeout=60).get_text()
    logging.info(f'CONTA CAIXA: {conta_caixa_ext}')

    if conta_caixa.lower() in conta_caixa_ext.lower():
        logging.info('CONTA CAIXA PREENCHIDA CORRETAMENTE')

    else:
        logging.info('CONTA CAIXA NÃO PREENCHIDA CORRETAMENTE')

        cc.wait_appear(locator.rm.button_lkpcontacaixalookupeditinneredit, wait_timeout=30).click()
        logging.info(f'Abrir Conta Caixa clicada')

        cc.wait_appear(locator.rm.edit_tbxsearch1, wait_timeout=30).click()
        logging.info(f'Selecionar Conta Caixa clicada')

        #pyautogui.write(r'02675-5')
        pyautogui.write(conta_caixa)
        logging.info(f'Escreve a conta caixa: {conta_caixa}')
        sleep(1)

        pyautogui.hotkey('enter')
        logging.info('Aperta enter')
        sleep(1)

        pyautogui.hotkey('enter')
        logging.info('Aperta enter')
        sleep(1)'''

    cc.wait_appear(locator.rm.button_btnnext1, wait_timeout=60).click()
    logging.info(f'AVANÇAR')


    '''valor_total_rm = cc.wait_appear(locator.rm.edit_cvalordabaixadolancto, wait_timeout=60).get_text()
    for _ in range(3):
        valor_total_rm = valor_total_rm.replace(".","")
    logging.info(f'VALOR TOTAL REF NO RM: {valor_total_rm}')

    if valor_original_ref > valor_total_rm:
        logging.info(f'Valor extraído do pdf maior do que valor do RM')

        valor_original_ref = float(valor_original_ref.replace(',','.'))
        valor_total_rm = float(valor_total_rm.replace(',','.'))

        diferenca_valor = str(round(valor_original_ref - valor_total_rm, 2))

        cc.wait_appear(locator.rm.edit_cvalorjuros, wait_timeout=30).double_click()
        logging.info(f'Juros clicada')

        pyautogui.write(diferenca_valor.replace('.',','))
        logging.info(f"Preenche juros com: {diferenca_valor.replace('.',',')}")
        sleep(1)

        pyautogui.hotkey('tab')
        logging.info('Aperta tab')


    elif valor_original_ref < valor_total_rm:
        erro = f'Valor extraído do pdf menor do que valor do RM'
        logging.info(f'{erro}')
        return erro'''
    
    #if valor_multa:
    cc.wait_appear(locator.rm.edit_cvalormulta, wait_timeout=60).double_click()
    logging.info(f'MULTAS SELECIONADO')

    pyautogui.write(valor_multa.replace('.',''))
    logging.info(f"Preenche multa com: {valor_multa.replace('.','')}")

    #validar avancar
    
    cc.wait_appear(locator.rm.button_btnnext1, wait_timeout=60).click()
    logging.info(f'AVANÇAR')

    ### TRAVADO. SOLTAR
    cc.wait_appear(locator.rm.button_btnnext1, wait_timeout=60).click()
    logging.info(f'AVANÇAR')

    cc.wait_appear(locator.rm.button_btnnext1, wait_timeout=60).click()
    logging.info(f'EXECUTAR')

    cc.wait_appear(locator.rm.button_btncancel, wait_timeout=300)

    flag_erro = False
    processa_success = waitForImage(image = baixa_success, timeout=30, name = 'SUCESSO BAIXA')
    if processa_success is not None:
        logging.info('SUCESSO BAIXA')

    processa_erro = waitForImage(image = baixa_error, timeout=5, name = 'ERRO BAIXA')
    if processa_erro is not None:
        erro = 'ERRO AO BAIXAR REF'
        logging.info(f'{erro}')
        flag_erro = True

    cc.wait_appear(locator.rm.edit_textboxlog1, wait_timeout=15).click()
    sleep(2)
    pyautogui.hotkey('ctrl', 'a')
    sleep(1)
    pyautogui.hotkey('ctrl', 'c')
    sleep(1)
    txt_log = pyperclip.paste()
    logging.info(f'{txt_log}')

    cc.wait_appear(locator.rm.button_btncancel, wait_timeout=60).click()
    logging.info(f'FECHAR')

    if flag_erro:
        return erro


def fim_lancamento():

    desmark_filter()

    cc.wait_appear(locator.rm.header_x, wait_timeout=60).click()
    logging.info(f'MARCA TODOS OS PROCESSOS')
    sleep(3)

    cc.wait_appear(locator.rm.header_x, wait_timeout=60).click()
    logging.info(f'DESMARCA TODOS OS PROCESSOS')



def caps():
    pyautogui.press("capslock") if ctypes.WinDLL("User32.dll").GetKeyState(0x14) else False


def check_erro():

    pyautogui.hotkey('alt','c')
    logging.info('alt+c clicado')

    confirmar_cancelamento = waitForImage(image = confirmar_cancelamento_img, timeout=10, name = 'CONFIRMAR CANCELAMENTO')
    if confirmar_cancelamento is not None:
        pyautogui.click(confirmar_cancelamento)
        logging.info('confirmar cancelamento clicado')
        sleep(0.3)
        pyautogui.hotkey('space')
        logging.info('space clicado')

    erro_1 = waitForImage(image = erro_img, timeout=5, name = 'ERRO 1')
    erro_2 = waitForImage(image = erro2_img, timeout=5, name = 'ERRO 2')

    if erro_1 is not None or erro_2 is not None:
        logging.info('erro')
        if erro_1:
            pyautogui.click(erro_1) 
            logging.info('erro 1 clicado')
        else:
            pyautogui.click(erro_2)
            logging.info('erro 2 clicado')
        pyautogui.hotkey('esc')
        logging.info('esc clicado')
        sleep(0.3)
        pyautogui.hotkey('alt','c')
        logging.info('alt+c clicado')

        confirmar_cancelamento = waitForImage(image = confirmar_cancelamento_img, timeout=10, name = 'CONFIRMAR CANCELAMENTO')
        if confirmar_cancelamento is not None:
            pyautogui.click(confirmar_cancelamento)
            logging.info('confirmar cancelamento clicado')
            sleep(0.3)
            pyautogui.hotkey('space')
            logging.info('space clicado')

def pdf_image_to_text1(caminho):
    caminho_imagem_list = tranf_pdf_img1()
    texto_formatado = read_img1(caminho_imagem_list)
    return texto_formatado


def tranf_pdf_img(caminho):
    #caminho = F'{caminho_pdf}PGTS 2901.pdf' ### VERIFICAR PADRAO NOME
    #caminho = F'{caminho_pdf}PIX 1001.pdf' ### VERIFICAR PADRAO NOME

    # Abrir o arquivo PDF
    documento_pdf = fitz.open(caminho)

    imagens_list = []
    cont = 0
    for pagina_numero in range(documento_pdf.page_count):
        pagina = documento_pdf.load_page(pagina_numero)
        imagem = pagina.get_pixmap(matrix=fitz.Matrix(5, 5), alpha=False)

        cont += 1
        
        nome = caminho.split('PDF\\')[1]
        nome = nome.split('.pdf')[0]
        #nome_arquivo = f"imagem_{pagina_numero + 1}.jpg"  # ou qualquer outro formato de imagem suportado
        nome_arquivo = f"{nome}_{pagina_numero + 1}.jpg"  # ou qualquer outro formato de imagem suportado

        if not os.path.exists(caminho_imagem):
            os.makedirs(caminho_imagem)

        imagem_salva = f'{caminho_imagem}\\{nome_arquivo}'

        imagem.save(imagem_salva)
        #logging.info(f"Imagem {nome_arquivo} salva.")

        imagens_list.append(nome_arquivo)

    documento_pdf.close()


    for cont, img in enumerate(imagens_list):
        imagem = Image.open(f'{caminho_imagem}\\{img}')
        #imagem = Image.open(f'{img}')

        #logging.info(f"Imagem {img} tratada.")
        #logging.info(f"Imagem1 {imagem}.")

        #nova_resolucao = 150 
        nova_resolucao = 400

        largura_original, altura_original = imagem.size
        nova_largura = int(largura_original * nova_resolucao / 72)  # Convertendo de polegadas para pixels
        nova_altura = int(altura_original * nova_resolucao / 72)  # Convertendo de polegadas para pixels

        #imagem_redimensionada_tranf = imagem.resize((nova_largura, nova_altura), resample=Image.BICUBIC)  # Usando BICUBIC como método de interpolação
        #imagem_redimensionada_tranf = imagem.resize((nova_largura, nova_altura), resample=Image.BILINEAR)  # Usando BICUBIC como método de interpolação
        #imagem_redimensionada_tranf = imagem.resize((nova_largura, nova_altura), resample=Image.HAMMING)  # Usando BICUBIC como método de interpolação
        #imagem_redimensionada_tranf = imagem.resize((nova_largura, nova_altura), resample=Image.BOX)  # Usando BICUBIC como método de interpolação
        #imagem_redimensionada_tranf = imagem.resize((nova_largura, nova_altura), resample=Image.NEAREST)  # Usando BICUBIC como método de interpolação
        imagem_redimensionada_tranf = imagem.resize((nova_largura, nova_altura), resample=Image.LANCZOS)  # Usando BICUBIC como método de interpolação

        #nome_arquivo_2 = f'red_{img}'

        imagem_redimensionada_tranf.save(f'{caminho_imagem}\\{img}', dpi=(nova_resolucao, nova_resolucao))
        #imagem1 = preprocess_image(f'{caminho_imagem}\\{nome_arquivo_2}', f'{caminho_imagem}\\proc_{nome_arquivo_2}')


def read_img():

    arquivos = []
    for dirpath, dirnames, filenames in os.walk(caminho_imagem):
        for arquivo in filenames:
            arquivos.append(os.path.join(dirpath, arquivo))

    #logging.info(f'arquivos: {arquivos}')

    texto_formatado = ''
    for img_tratada in arquivos:
        #imagem = cv2.imread(img_tratada)

        #imagem = img_tratada
        imagem = preprocess_image(img_tratada)

        pytesseract.pytesseract.tesseract_cmd = pytesseract_caminho

        #texto = pytesseract.image_to_string(imagem, lang='por')
        #texto = pytesseract.image_to_string(imagem, config='--psm 6 --oem 3')
        texto = pytesseract.image_to_string(imagem, config='--psm 3 --oem 3 -l por')
        #logging.info(texto) 

        linhas = texto.strip().split('\n')

        linhas = [linha.strip() for linha in linhas if linha.strip()]

        #linhas = linhas[3:]

        texto_formatado += '\n'.join(linhas)

        #logging.info(f'linhas {linhas}')

        linhas = ''

    #logging.info(texto_formatado)

    return texto_formatado



def preprocess_image(image_path):

    #logging.info(f'image_path: {image_path}')

    
    #image = cv2.imread(image_path) 
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE) ###

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

    tiff_image_path = os.path.splitext(image_path)[0] + '.tiff'
    #cv2.imwrite(image_path, closing, [cv2.IMWRITE_JPEG_QUALITY, 100, cv2.IMWRITE_PXM_BINARY, 0, cv2.IMWRITE_JPEG_OPTIMIZE, 1])  ###
    #cv2.imwrite(image_path, closing, [cv2.IMWRITE_PXM_BINARY, 0, cv2.IMWRITE_TIFF_COMPRESSION, 0, cv2.IMWRITE_TIFF_XDPI, 300, cv2.IMWRITE_TIFF_YDPI, 300])  ###
    cv2.imwrite(tiff_image_path, closing)  ###

    logging.info(f'pre 10')

    #return closing ###



def tranf_pdf_pdf(caminho):

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

    for pagina_numero in range(documento_pdf.page_count):
        pagina = documento_pdf.load_page(pagina_numero)
        imagem = pagina.get_pixmap(matrix=fitz.Matrix(4, 4), alpha=False)

        #nome_arquivo = f"{nome}_{pagina_numero + 1}.jpg"
        nome_arquivo = f"{nome}_{pagina_numero + 1}"

        if not os.path.exists(caminho_imagem):
            os.makedirs(caminho_imagem)

        imagem_salva = f'{caminho_imagem}\\{nome_arquivo}.PNG'
        imagem.save(imagem_salva)

        

        imagens_list.append(f'{nome_arquivo}')
    logging.info(f'Imagens extraidas')

    documento_pdf.close()

    nome_pdf_final = f'{caminho_copia_pdf}{nome}.pdf'
    c = canvas.Canvas(nome_pdf_final, pagesize=letter)

    for img in imagens_list:
        imagem = Image.open(f'{caminho_imagem}\\{img}.PNG')

        nova_resolucao = 300
        largura_original, altura_original = imagem.size
        nova_largura = int(largura_original * nova_resolucao / 72)
        nova_altura = int(altura_original * nova_resolucao / 72)

        '''enhancer = ImageEnhance.Contrast(imagem)
        imagem = enhancer.enhance(2.0)
        enhancer = ImageEnhance.Sharpness(imagem)
        imagem = enhancer.enhance(2.0)
        enhancer = ImageEnhance.Brightness(imagem)
        imagem = enhancer.enhance(1.5)'''

        imagem_redimensionada_tranf = imagem.resize((nova_largura, nova_altura), resample=Image.LANCZOS)
        logging.info(f'Imagem redimensionada')

        imagem_redimensionada_tranf.save(f'{caminho_imagem}\\{img}.PNG', dpi=(nova_resolucao, nova_resolucao))
        logging.info(f'Imagem redimensionada Salva')
        #imagem_redimensionada_tranf = preprocess_image(f'{caminho_imagem}\\{img}')
        preprocess_image(f'{caminho_imagem}\\{img}.PNG')
        logging.info(f'Imagem redimensionada Pos processada')
        #imagem_pil = Image.fromarray(imagem_redimensionada_tranf)
        #imagem_pil.save(f'{caminho_imagem}\\{img}', dpi=(nova_resolucao, nova_resolucao))

        c.setPageSize((nova_largura, nova_altura))  # Defina o tamanho da página com base na imagem
        #imagem_redimensionada_tranf = preprocess_image(imagem)

        #img_reader = ImageReader(imagem_redimensionada_tranf)
        #img_reader = Image.open(f'{caminho_imagem}\\{img}')
        img_reader = ImageReader(f'{caminho_imagem}\\{img}.tiff')
        logging.info(f'Imagem Pos processada aberta')

        #img_reader = ImageReader(imagem)
        c.drawImage(img_reader, 0, 0, width=nova_largura, height=nova_altura, mask='auto')
        logging.info(f'Imagem Pos processada escrita')
        #c.drawImage(img_reader, 0, 0)
        c.showPage()

    c.save()
    logging.info(f'Novo PDF com imagens salvo')

    return nome_pdf_final



def pdf_image_to_text(caminho):

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
    
    return caminho


def extrair_texto_pdf(caminho_pdf):
    texto_extraido = ""
    with open(caminho_pdf, 'rb') as arquivo_pdf:
        leitor_pdf = PyPDF2.PdfReader(arquivo_pdf)
        
        for num_pagina in range(len(leitor_pdf.pages)):
            pagina = leitor_pdf.pages[num_pagina]
            texto_extraido += pagina.extract_text()
    #texto_extraido = extract_text(caminho_pdf)
            
    return texto_extraido


def melhorar_pdf(pdf_path):
    command = f"convert -density 300 {pdf_path} -depth 8 -strip -background white -alpha off {pdf_path}"
    os.system(command)



def preprocess_image2(image_path):

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