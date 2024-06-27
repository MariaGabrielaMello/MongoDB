import pymongo
from pymongo.server_api import ServerApi
from bson.objectid import ObjectId

client = pymongo.MongoClient("mongodb+srv://admin:admin@fatec.x655kkc.mongodb.net/?retryWrites=true&w=majority&appName=FATEC", server_api=ServerApi('1'))
db = client.MercadoLivre

global mydb
mydb = client.MercadoLivre

mycol = ["Usuário"]
mycolvend = ["Vendedor"]
mycolprod = ["Produto"]
mycolfav = ["Favoritos"]
mycolcom = ["Compra"]


def insert(nome, cpf, email, endereco):
    global mydb
    mycol = mydb.Usuário
    print("\n####INSERT####")
    mydict = {"nome": nome, "cpf": cpf, "email": email, "endereco": endereco}
    x = mycol.insert_one(mydict)
    print(x.inserted_id)

def insertproduto(produto, quantidade, preco):
    global mydb
    mycolprod = mydb.Produto
    print("\n####INSERT####")
    mydict = {"produto": produto, "quantidade": quantidade, "preco": preco}
    x = mycolprod.insert_one(mydict)
    print(x.inserted_id)

def insertvendedor(vendedor, codigo, produtoVendido):
    global mydb
    mycolvend = mydb.Vendedor
    print("\n####INSERT####")
    mydict = {"vendedor": vendedor, "codigo": codigo, "produtoVendido": produtoVendido}
    x = mycolvend.insert_one(mydict)
    print(x.inserted_id)

def insertcompras(nome_prod, codigo, valor):
    global mydb
    mycolcom = mydb.Compra
    print("\n####INSERT####")
    mydict = {"nomeprod": nome_prod, "codigo": codigo, "valor": valor}
    x = mycolcom.insert_one(mydict)
    print(x.inserted_id)

def insertfavoritos(nome_usario, nome_prod, codigo):
    global mydb
    mycolfav = mydb.Favoritos
    print("\n####INSERT####")
    mydict = {"nomeusuario": nome_usario,"nomeprod": nome_prod, "codigo": codigo}
    x = mycolfav.insert_one(mydict)
    print(x.inserted_id)

def findSort(nome):
    global mydb
    mycol = mydb.Usuário
    print("\n####SORT####")
    mydoc = mycol.find().sort("nome")
    for x in mydoc:
        print(x)

def findSortprodutos(produto):
    global mydb
    mycolprod = mydb.Produtos
    print("\n####SORT####")
    mydoc = mycolprod.find().sort(produto)
    for x in mydoc:
        print(x)

def findSortvendedor(vendedor):
    global mydb
    mycolvend = mydb.Vendedor
    print("\n####SORT####")
    mydoc = mycolvend.find().sort(vendedor)
    for x in mydoc:
        print(x)

def findSortcompras(compras):
    global mydb
    mycolcom = mydb.Compra
    print("\n####SORT####")
    mydoc = mycolcom.find().sort(compras)
    for x in mydoc:
        print(x)

def findSortfavoritos(favoritos):
    global mydb
    mycolfav = mydb.Favorito
    print("\n####SORT####")
    mydoc = mycolfav.find().sort(favoritos)
    for x in mydoc:
        print(x)

def find(nome):
    global mydb
    mycol = mydb.Usuário
    print("\n####FIND####")
    myquery = {"nome": nome}
    mydoc = mycol.find(myquery)
    for x in mydoc:
        print(x)

def findprodutos(produto):
    global mydb
    mycolprod = mydb.Produto
    print("\n####FIND####")
    myquery = {"produto": produto}
    mydoc = mycolprod.find(myquery)
    for x in mydoc:
        print(x)

def findvendedor(vendedor):
    global mydb
    mycolvend = mydb.Vendedor
    print("\n####FIND####")
    myquery = {"vendedor": vendedor}
    mydoc = mycolvend.find(myquery)
    for x in mydoc:
        print(x)

def findcompras(compras):
    global mydb
    mycolcom = mydb.Compra
    print("\n####FIND####")
    myquery = {"compras": compras}
    mydoc = mycolcom.find(myquery)
    for x in mydoc:
        print(x)

def findfavoritos(favoritos):
    global mydb
    mycolfav = mydb.Favoritos
    print("\n####FIND####")
    myquery = {"favoritos": favoritos}
    mydoc = mycolfav.find(myquery)
    for x in mydoc:
        print(x)

def deleteOne(nome):
    global mydb
    mycol = mydb.Usuário
    print("\n####DELETE####")
    myquery = {"nome": nome}
    mycol.delete_one(myquery)
    print("Registro deletado com sucesso!")

def deleteOneprod(produto):
    global mydb
    mycolprod = mydb.Produto
    print("\n####DELETE####")
    myquery = {"produto": produto}
    mycolprod.delete_one(myquery)
    print("Registro deletado com sucesso!")

def deleteOnevendedor(vendedor):
    global mydb
    mycolvend = mydb.Vendedor
    print("\n####DELETE####")
    myquery = {"vendedor": vendedor}
    mycolvend.delete_one(myquery)
    print("Registro deletado com sucesso!")

def deleteOnecompras(compras):
    global mydb
    mycolcom = mydb.Compra
    print("\n####DELETE####")
    myquery = {"compras": compras}
    mycolcom.delete_one(myquery)
    print("Registro deletado com sucesso!")

def deleteOnefavoritos(favoritos):
    global mydb
    mycolfav = mydb.Favoritos
    print("\n####DELETE####")
    myquery = {"favoritos": favoritos}
    mycolfav.delete_one(myquery)
    print("Registro deletado com sucesso!")

def atualizarUsuario(nome_usuario, novos_dados):
    global mydb
    mycol = mydb.Usuário
    resultado = mycol.update_one({"nome": nome_usuario}, {"$set": novos_dados})
    print("Usuário atualizado:", resultado.modified_count)

def atualizarProduto(nome_produto, novos_dados):
    global mydb
    mycol = mydb.Produto
    resultado = mycol.update_one({"produto": nome_produto}, {"$set": novos_dados})
    print("Produto atualizado:", resultado.modified_count)

def atualizarVendedor(nome_vendedor, novos_dados):
    global mydb
    mycol = mydb.Vendedor
    resultado = mycol.update_one({"vendedor": nome_vendedor}, {"$set": novos_dados})
    print("Vendedor atualizado:", resultado.modified_count)

def atualizarFavorito(nome_usuario, novos_dados):
    global mydb
    mycol = mydb.Favoritos
    resultado = mycol.update_one({"nomeusuario": nome_usuario}, {"$set": novos_dados})
    print("Favorito atualizado:", resultado.modified_count)

while True:
    print("\n========================")
    print("     MERCADO LIVRE")
    print("========================")
    print("1 - Inserir usuário")
    print("2 - Inserir produto")
    print("3 - Inserir vendedor")
    print("4 - Inserir compras")
    print("5 - Inserir favoritos")
    print("6 - Listar usuários")
    print("7 - Listar produtos")
    print("8 - Listar vendedores")
    print("9 - Listar compras")
    print("10 - Listar favoritos")
    print("11 - Deletar usuário")
    print("12 - Deletar produto")
    print("13 - Deletar vendedor")
    print("14 - Deletar compras")
    print("15 - Deletar favoritos")
    print("16 - Editar usuário")
    print("17 - Editar produto")
    print("18 - Editar vendedor")
    print("19 - Editar favoritos")
    
    
    print("0 - Sair")
    op = int(input("Digite uma opção: "))

    if op == 1:
        nome = input("Digite o nome do usuário: ")
        cpf = input("Digite o CPF do usuário: ")
        email = input("Digite o email do usuário: ")
        endereco = input("Digite o endereço do usuário: ")
        insert(nome, cpf, email, endereco)
    elif op == 2:
        produto = input("Digite o nome do produto: ")
        quantidade = input("Digite a quantidade do produto: ")
        preco = input("Digite o preço do produto: ")
        insertproduto(produto, quantidade, preco)
    elif op == 3:
        vendedor = input("Digite o nome do vendedor: ")
        codigo = input("Digite o código do vendedor: ")
        produtoVendido = input("Digite o produto vendido pelo vendedor: ")
        insertvendedor(vendedor, codigo, produtoVendido)
    elif op == 4:
        nome_prod = input("Digite o nome do produto: ")
        codigo = input("Digite o código do produto: ")
        valor = input("Digite o valor do produto: ")
        insertcompras(nome_prod, codigo, valor)
    elif op == 5:
        nome_usuario = input("Digite o nome do usuario: ")
        nome_prod = input("Digite o nome do produto: ")
        codigo = input("Digite o código do produto: ")
        insertfavoritos(nome_usuario, nome_prod, codigo)
    elif op == 6:
        findSort("nome")
    elif op == 7:
        findSortprodutos("produto")
    elif op == 8:
        findSortvendedor("vendedor")
    elif op == 9:
        findSortcompras("compras")
    elif op == 10:
        findSortfavoritos("favoritos")
    elif op == 11:
        nome = input("Digite o nome do usuário que deseja deletar: ")
        deleteOne(nome)
    elif op == 12:
        produto = input("Digite o nome do produto que deseja deletar: ")
        deleteOneprod(produto)
    elif op == 13:
        vendedor = input("Digite o nome do vendedor que deseja deletar: ")
        deleteOnevendedor(vendedor)
    elif op == 14:
        compras = input("Digite a compra que deseja deletar: ")
        deleteOnecompras(compras)
    elif op == 15:
        favoritos = input("Digite o favorito que deseja deletar: ")
        deleteOnefavoritos(favoritos)
    elif op == 16:
        nome_usuario = input("Digite o nome do usuário que deseja editar: ")
        novos_dados = {}
        novo_nome = input("Digite o novo nome do usuário (deixe em branco para não alterar): ")
        novo_cpf = input("Digite o novo CPF do usuário (deixe em branco para não alterar): ")
        novo_email = input("Digite o novo email do usuário (deixe em branco para não alterar): ")
        novo_endereco = input("Digite o novo endereço do usuário (deixe em branco para não alterar): ")
        if novo_nome: novos_dados['nome'] = novo_nome
        if novo_cpf: novos_dados['cpf'] = novo_cpf
        if novo_email: novos_dados['email'] = novo_email
        if novo_endereco: novos_dados['endereco'] = novo_endereco
        atualizarUsuario(nome_usuario, novos_dados)
    elif op == 17:
        nome_produto = input("Digite o nome do produto que deseja editar: ")
        novos_dados = {}
        novo_nome_produto = input("Digite o novo nome do produto (deixe em branco para não alterar): ")
        nova_quantidade = input("Digite a nova quantidade do produto (deixe em branco para não alterar): ")
        novo_preco = input("Digite o novo preço do produto (deixe em branco para não alterar): ")

        if novo_nome_produto: novos_dados['produto'] = novo_nome_produto
        if nova_quantidade: novos_dados['quantidade'] = nova_quantidade
        if novo_preco: novos_dados['preco'] = novo_preco

        atualizarProduto(nome_produto, novos_dados)
    elif op == 18:
        nome_vendedor = input("Digite o nome do vendedor que deseja editar: ")
        novos_dados = {}
        novo_nome_vendedor = input("Digite o novo nome do vendedor (deixe em branco para não alterar): ")
        novo_codigo = input("Digite o novo código do vendedor (deixe em branco para não alterar): ")
        novo_produto_Vendido = input("Digite o novo produto vendido (deixe em branco para não alterar): ")
        if novo_nome_vendedor: novos_dados['vendedor'] = novo_nome_vendedor
        if novo_codigo: novos_dados['codigo'] = novo_codigo
        if novo_produto_Vendido: novos_dados['produtoVendido'] = novo_produto_Vendido
        

        atualizarVendedor(nome_vendedor, novos_dados)

    elif op == 19:
        nome_usuario = input("Digite o nome do usuário que favoritou o produto que deseja editar: ")
        novos_dados = {}
        novo_nomeprod = input("Digite o novo nome do produto favoritado (deixe em branco para não alterar): ")
        novo_codigo = input("Digite o novo código do produto favorito (deixe em branco para não alterar): ")
        if novo_nomeprod: novos_dados['nomeprod'] = novo_nomeprod
        if novo_codigo: novos_dados['codigo'] = novo_codigo
        
        atualizarFavorito(nome_usuario, novos_dados)
    elif op == 0:
        break

    else:
        print("Opção inválida. Digite novamente.")