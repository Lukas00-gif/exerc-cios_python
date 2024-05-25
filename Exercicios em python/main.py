from classes.loja import Loja
from classes.produto import Produto
from classes.cliente import Cliente
from classes.item_pedido import ItemPedido
from datetime import datetime

def main():
    # Criação da loja
    loja = Loja("Minha Loja")

    # Criação de clientes
    cliente1 = Cliente(nome="Cliente 1", endereco="Rua A, 123")
    cliente2 = Cliente(nome="Cliente 2", endereco="Rua B, 456")

    # Criação de produtos
    produto_a = Produto(nome='Produto A', descricao='Descricao do Produto A', preco=50)
    produto_b = Produto(nome='Produto B', descricao='Descricao do Produto B', preco=20)
    produto_c = Produto(nome='Produto C', descricao='Descricao do Produto C', preco=100)
    produto_d = Produto(nome='Produto D', descricao='Descricao do Produto D', preco=80)

    # Adição de produtos à loja
    loja.adicionar_produto(produto_a)
    loja.adicionar_produto(produto_b)
    loja.adicionar_produto(produto_c)
    loja.adicionar_produto(produto_d)

    # Criação de itens do pedido para o cliente 1
    itens_pedido1 = [
        ItemPedido(produto=produto_a, quantidade=2),
        ItemPedido(produto=produto_b, quantidade=1)
    ]

    # Criação de pedido simples para o cliente 1
    pedido1 = loja.criar_pedido(cliente=cliente1, itens=itens_pedido1, tipo_pedido='simples', taxa_frete=10)

    # Criação de itens do pedido para o cliente 2
    itens_pedido2 = [
        ItemPedido(produto=produto_c, quantidade=1),
        ItemPedido(produto=produto_d, quantidade=1)
    ]

    # Criação de pedido expresso para o cliente 2
    pedido2 = loja.criar_pedido(cliente=cliente2, itens=itens_pedido2, tipo_pedido='express', taxa_frete=30)

    # Cálculo do faturamento total da loja
    faturamento_total = loja.calcular_faturamento_total()
    print(f"Faturamento total da loja: R${faturamento_total:.2f}")

    # Aplicação de descontos aos pedidos
    pedido1.aplicarDesconto(10)
    print(f"Novo valor total do Pedido 1 após desconto: R${pedido1.calcularValorTotal():.2f}")

    pedido2.aplicarDesconto(5)
    print(f"Novo valor total do Pedido 2 após desconto: R${pedido2.calcularValorTotal():.2f}")

    # Listagem de todos os pedidos
    for pedido in loja.listar_pedidos():
        print(f"Pedido ID: {pedido.obterId()}, Cliente: {pedido.obterCliente().obter_nome()}, Valor Total: R${pedido.calcularValorTotal():.2f}")

    # Busca de pedido por ID
    pedido_busca = loja.obter_pedido_por_id(1)
    if pedido_busca:
        print(f"Pedido encontrado - ID: {pedido_busca.obterId()}, Cliente: {pedido_busca.obterCliente().obter_nome()}, Valor Total: R${pedido_busca.calcularValorTotal():.2f}")

if __name__ == "__main__":
    main()
