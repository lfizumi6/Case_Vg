import json
from datetime import datetime

dados_json = '''
{
  "vendas": [
    { "vendedor": "João Silva", "valor": 1200.50 },
    { "vendedor": "João Silva", "valor": 950.75 },
    { "vendedor": "João Silva", "valor": 1800.00 },
    { "vendedor": "João Silva", "valor": 1400.30 },
    { "vendedor": "João Silva", "valor": 1100.90 },
    { "vendedor": "João Silva", "valor": 1550.00 },
    { "vendedor": "João Silva", "valor": 1700.80 },
    { "vendedor": "João Silva", "valor": 250.30 },
    { "vendedor": "João Silva", "valor": 480.75 },
    { "vendedor": "João Silva", "valor": 320.40 },
    
    { "vendedor": "Maria Souza", "valor": 2100.40 },
    { "vendedor": "Maria Souza", "valor": 1350.60 },
    { "vendedor": "Maria Souza", "valor": 950.20 },
    { "vendedor": "Maria Souza", "valor": 1600.75 },
    { "vendedor": "Maria Souza", "valor": 1750.00 },
    { "vendedor": "Maria Souza", "valor": 1450.90 },
    { "vendedor": "Maria Souza", "valor": 400.50 },
    { "vendedor": "Maria Souza", "valor": 180.20 },
    { "vendedor": "Maria Souza", "valor": 90.75 },
    
    { "vendedor": "Carlos Oliveira", "valor": 800.50 },
    { "vendedor": "Carlos Oliveira", "valor": 1200.00 },
    { "vendedor": "Carlos Oliveira", "valor": 1950.30 },
    { "vendedor": "Carlos Oliveira", "valor": 1750.80 },
    { "vendedor": "Carlos Oliveira", "valor": 1300.60 },
    { "vendedor": "Carlos Oliveira", "valor": 300.40 },
    { "vendedor": "Carlos Oliveira", "valor": 500.00 },
    { "vendedor": "Carlos Oliveira", "valor": 125.75 },
    
    { "vendedor": "Ana Lima", "valor": 1000.00 },
    { "vendedor": "Ana Lima", "valor": 1100.50 },
    { "vendedor": "Ana Lima", "valor": 1250.75 },
    { "vendedor": "Ana Lima", "valor": 1400.20 },
    { "vendedor": "Ana Lima", "valor": 1550.90 },
    { "vendedor": "Ana Lima", "valor": 1650.00 },
    { "vendedor": "Ana Lima", "valor": 75.30 },
    { "vendedor": "Ana Lima", "valor": 420.90 },
    { "vendedor": "Ana Lima", "valor": 315.40 }
  ]
}
'''

def calcular_comissoes(json_texto):
    base = json.loads(json_texto)
    for v in base["vendas"]:
        vendedor = v["vendedor"]
        valor = v["valor"]
        
        if valor < 100:
            print(f"{vendedor} - Venda de R$ {valor:.2f}: abaixo de 100, sem comissão.")
        elif valor < 500:
            comissao = valor * 0.01
            print(f"{vendedor} - Venda de R$ {valor:.2f}: comissão de 1% = R$ {comissao:.2f}")
        else:
            comissao = valor * 0.05
            print(f"{vendedor} - Venda de R$ {valor:.2f}: comissão de 5% = R$ {comissao:.2f}")

calcular_comissoes(dados_json)


estoque_json = '''
{
	"estoque": [
	  { "codigoProduto": 101, "descricaoProduto": "Caneta Azul", "estoque": 150 },
	  { "codigoProduto": 102, "descricaoProduto": "Caderno Universitário", "estoque": 75 },
	  { "codigoProduto": 103, "descricaoProduto": "Borracha Branca", "estoque": 200 },
	  { "codigoProduto": 104, "descricaoProduto": "Lápis Preto HB", "estoque": 320 },
	  { "codigoProduto": 105, "descricaoProduto": "Marcador de Texto Amarelo", "estoque": 90 }
	]
}
'''

sistema_estoque = json.loads(estoque_json)

def movimentar_estoque(codigo, qtd_movimento, tipo_mov, id_movimento, desc_movimento):
    for prod in sistema_estoque["estoque"]:
        if prod["codigoProduto"] == codigo:
            if tipo_mov == "entrada":
                prod["estoque"] += qtd_movimento
            elif tipo_mov == "saida":
                prod["estoque"] -= qtd_movimento
            
            print(f"\nMovimentação {id_movimento}: {desc_movimento}")
            print(f"Produto: {prod['descricaoProduto']} | Estoque atualizado: {prod['estoque']} unidades")
            return
    print("Produto não encontrado!")

movimentar_estoque(101, 50, "entrada", 1, "Reposição de canetas do fornecedor")
movimentar_estoque(102, 10, "saida", 2, "Venda para cliente balcão")


def calcular_juros(valor_titulo, data_venc):
    hoje = datetime.now().date()
    vencimento = datetime.strptime(data_venc, "%Y-%m-%d").date()
    dias = (hoje - vencimento).days
    
    if dias <= 0:
        print(f"\nTítulo em dia. Valor original: R$ {valor_titulo:.2f}")
    else:
        multa_total = valor_titulo * 0.025 * dias
        valor_final = valor_titulo + multa_total
        
        print(f"\nVencimento: {vencimento} | Hoje: {hoje}")
        print(f"Dias de atraso: {dias}")
        print(f"Valor dos juros (2.5% ao dia): R$ {multa_total:.2f}")
        print(f"Valor total com multa: R$ {valor_final:.2f}")

calcular_juros(300.00, "2026-09-10")

