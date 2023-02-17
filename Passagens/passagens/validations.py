def origem_destino_iguais(origem, destino, lista_de_erros):
    """Verifica se a Origem é Igual ao Destino"""
    if origem == destino:
        lista_de_erros['origem'] = 'Origem e Destino não podem ser iguais'

def campo_tem_algum_numero(valor_campo, nome_campo, lista_de_erros):
    """Verifica se existem numero nos campos de origem e destino"""
    if any(char.isdigit() for char in valor_campo):
        lista_de_erros[nome_campo] = 'Não Inclua Numero a este campo'

def data_ida_maior_data_volta(data_ida, data_volta, lista_de_erros):
    """Verifica se a data de ida é menor que a data de volta"""
    if data_ida > data_volta:
        lista_de_erros['data_ida']= "Data de Ida não pode ser maior que a data de volta"
def data_ida_menor_data_de_hoje(data_ida, data_pesquisa,lista_de_erros):
    """Verifica se a Data de Ida é Menor que a Data Hoje"""
    if data_ida < data_pesquisa:
        lista_de_erros['data_ida'] = "Data de Ida não pode ser menor que a data de hoje"
 