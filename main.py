
from SUBPROGRAMS.functions import *

def liq_camb(contrato_extr_list):

    flag = 0
    for i, extrato in enumerate(contrato_extr_list):
        logging.info(f'Tratando extrato {i+1}: {extrato}')

        erro = ""

        valor_extr = extrato['valor_extr']
        data_extr = extrato['data_extr']
        descricao_extr = extrato['descricao_extr']
        banco = extrato['banco']
        cambial = extrato['cambial']
        inv = extrato['inv']
        pagador = extrato['pagador']
        moeda = extrato['moeda']
        valor = extrato['valor']
        ir = extrato['ir']
        cide = extrato['cide']
        pis = extrato['pis']
        cofins = extrato['cofins']
        iof = extrato['iof']

        flag = selec_filtro(flag, tipo_filtro1, valor)

        quant = check_table_record()
        if quant == 0:
            erro = f'Valor não encontrado'
            logging.info(f'{erro}')
            status = 'Não Baixado'
            createRowLiqExcel(extrato, erro, status)
            continue

        ####
        erro, extrato['centro_custo'] = check_inv(inv, pagador, quant)
        if erro != "" and erro != None:
            logging.info(f'{erro}')
            status = 'Não Baixado'
            createRowLiqExcel(extrato, erro, status)
            continue

        logging.info(f'extrato ai: {extrato}')

        erro = baixar_lancamento(valor_extr)
        if erro != "" and erro != None:
            status = 'NÃO FINALIZADO'
            createRowLiqExcel(extrato, erro, status)
            continue

        status = 'FINALIZADO'
        erro = ''
        createRowLiqExcel(extrato, erro, status)
        

def impostos(imposto_list, contrato_extr_list):

    flag = 0

    for imp in imposto_list:
        
        logging.info(f'trabalhando em {imp}')

        data = imp["data"]
        descricao = imp["descricao"]
        imposto = imp["imposto"]
        valor = imp["valor"].replace('.','')
        if "multa" in imp:
            multa = imp["multa"]
        else:
            multa = ''
        if "valor_multa" in imp:
            valor_multa = imp["valor_multa"]
        else:
            valor_multa = '0'

        flag_imp = True

        logging.info(f'Buscando: {imposto} {valor}')
        for contrato in contrato_extr_list:
            if valor == contrato[imp["imposto"].lower()].replace('.',''):
                logging.info(f'contrato com {imposto} {valor} encontrado:\n{contrato}')

                if imposto.lower() == 'iof':
                    imposto_historico = descricao
                else:
                    imposto_historico = imposto

                historico = f'{imposto_historico} - {contrato["banco"]} - {contrato["pagador"]} - {contrato["inv"]} - contrato: {contrato["contrato"]}'
                logging.info(f'historico NOVO {historico}')
                flag_imp = False

                if contrato["centro_custo"] != None:
                    centro_custo = contrato["centro_custo"]
                    logging.info(f'centro_custo {centro_custo}')
                else:
                    erro = f'Centro de custo não encontrado. Contrato não finalizado'
                    centro_custo = ''
                    flag_imp = 2

                break

        if flag_imp:
            if flag == 2:
                logging.info(f'{erro} - {imposto} {valor}')
            else:
                erro = f'Valor de Imposto não encontrado nos contratos'
                logging.info(f'{erro} - {imposto} {valor}')
            createRowImpExcel(data, descricao, imposto, valor, valor_multa, centro_custo, historico, erro, status)
            continue

        flag = selec_filtro(flag, tipo_filtro2, imposto)

        quant = check_table_record()
        if quant == 0:
            erro = f'Nenhum IMPOSTO encontrado'
            logging.info(f'{erro}')
            status = 'Não Baixado'
            createRowImpExcel(data, descricao, imposto, valor, valor_multa, centro_custo, historico, erro, status)
            continue
       
        erro = selecionar_processo()
        if erro != "" and erro != None:
            logging.info(f'{erro}')
            status = 'Não Baixado'
            createRowImpExcel(data, descricao, imposto, valor, valor_multa, centro_custo, historico, erro, status)
            continue

        erro = copiar_processo(data, historico, valor, centro_custo)
        if erro != "" and erro != None:
            logging.info(f'{erro}')
            status = 'Não Baixado'
            createRowImpExcel(data, descricao, imposto, valor, valor_multa, centro_custo, historico, erro, status)
            continue

        erro = baixar_ref(valor_multa)
        if erro != "" and erro != None:
            logging.info(f'{erro}')
            status = 'Não Baixado'
            createRowImpExcel(data, descricao, imposto, valor, valor_multa, centro_custo, historico, erro, status)
            continue

        fim_lancamento()


def process():

    inicial()

    #linha_list, liq_cambio_list, \
    #imposto_list, contrato_extr_list = excel()

    #create_excel_extrato(linha_list)
    #create_excel_contratos(contrato_extr_list)

    inicio_RM()
    return
    liq_camb(contrato_extr_list)

    impostos(imposto_list, contrato_extr_list)

    


if __name__ == '__main__':

    #sys.excepthook = show_exception_and_exit
    process()
    
    #encerra_prog()
    #emailSuccess(nome_bot, texto_msg)




