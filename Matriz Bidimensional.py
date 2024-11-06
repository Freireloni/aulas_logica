#preços da  Moeda

precos_em_moedas = [
    [10,12,14]
    [20,22,24]
    [30,32,34]
]

taxas_conversao = {
    'EUA' : 1.10,
    'GEP' : 1.24
}

def conversao_para_dolar(preco, moeda):
    return preco * taxas_conversao[moeda]

preco_em_dolar = [ 
    [conversao_para_dolar(preco, 'EUA') for preco in linha] if i == 0
    else [convesao_para_dolar(preco, 'GEP') for preco in linha]
    for i, linha enumerate(precos_em_moedas)
    ]

print("preços convertidos para dolar: ")
for linha in preco_em_dolar:
    print(linha)