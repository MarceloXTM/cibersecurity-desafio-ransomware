from cryptography.fernet import Fernet

# Carrega a chave do arquivo especificado
def carregar_chave():
    return open('SaiForaZika.key', 'rb').read()

# Função para descriptografar arquivos
def descriptografar_arquivo(nome_arquivo):
    chave = carregar_chave()
    fernet = Fernet(chave)

    with open(nome_arquivo, 'rb') as arquivo:
        dados_encriptados = arquivo.read()

    dados_descriptografados = fernet.decrypt(dados_encriptados)

    with open(nome_arquivo, 'wb') as arquivo:
        arquivo.write(dados_descriptografados)

# Exemplo de uso
arquivo = input("Digite o nome do arquivo a ser descriptografado: ")
descriptografar_arquivo(arquivo)
