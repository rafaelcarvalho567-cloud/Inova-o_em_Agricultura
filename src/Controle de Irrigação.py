# ===============================================
# PROJETO: Controle de Irrigação Inteligente
# DISCIPLINA: Python e Além (Capítulo 6)
# GRUPO: Gustavo Borges, Paulo Enrique, Rodrigo Lucena, Rafael Carvalho
# ===============================================

import json
import os

# -----------------------------------------------
# Funções auxiliares para manipular arquivo JSON
# -----------------------------------------------
def carregar_dados(nome_arquivo):
    """Carrega os dados do arquivo JSON, se existir."""
    if not os.path.exists(nome_arquivo):
        return []
    with open(nome_arquivo, "r", encoding="utf-8") as arquivo:
        return json.load(arquivo)

def salvar_dados(nome_arquivo, dados):
    """Salva os dados no arquivo JSON."""
    with open(nome_arquivo, "w", encoding="utf-8") as arquivo:
        json.dump(dados, arquivo, indent=4, ensure_ascii=False)

# -----------------------------------------------
# Funções principais do sistema
# -----------------------------------------------
def cadastrar_sensor(lista):
    """Cadastra um novo sensor de umidade."""
    codigo = int(input("Código do sensor: "))
    nome = input("Nome do sensor: ")
    local = input("Local de instalação: ")
    sensor = {"codigo": codigo, "nome": nome, "local": local, "umidade": 0}
    lista.append(sensor)
    print("✅ Sensor cadastrado com sucesso!")

def listar_sensores(lista):
    """Mostra todos os sensores cadastrados."""
    if not lista:
        print("⚠️ Nenhum sensor cadastrado.")
        return
    print("\n--- Sensores Cadastrados ---")
    for sensor in lista:
        print(f"Código: {sensor['codigo']} | Nome: {sensor['nome']} | Local: {sensor['local']} | Umidade: {sensor['umidade']}%")

def atualizar_umidade(lista):
    """Atualiza a umidade lida por um sensor específico."""
    codigo = int(input("Informe o código do sensor: "))
    for sensor in lista:
        if sensor["codigo"] == codigo:
            sensor["umidade"] = float(input("Nova leitura de umidade (%): "))
            print("💧 Umidade atualizada com sucesso!")
            return
    print("❌ Sensor não encontrado.")

def verificar_irrigacao(lista):
    """Verifica quais sensores estão abaixo do nível mínimo de umidade."""
    minimo = float(input("Digite o nível mínimo de umidade desejado: "))
    print("\n--- Sensores que precisam de irrigação ---")
    for sensor in lista:
        if sensor["umidade"] < minimo:
            print(f"⚠️ {sensor['nome']} ({sensor['local']}) - Umidade atual: {sensor['umidade']}%")
    print("Verificação concluída.")

# -----------------------------------------------
# Programa principal
# -----------------------------------------------
def main():
    nome_arquivo = "dados_irrigacao.json"
    sensores = carregar_dados(nome_arquivo)

    while True:
        print("\n====== MENU DE CONTROLE DE IRRIGAÇÃO ======")
        print("1 - Cadastrar sensor")
        print("2 - Listar sensores")
        print("3 - Atualizar umidade")
        print("4 - Verificar necessidade de irrigação")
        print("0 - Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            cadastrar_sensor(sensores)
        elif opcao == "2":
            listar_sensores(sensores)
        elif opcao == "3":
            atualizar_umidade(sensores)
        elif opcao == "4":
            verificar_irrigacao(sensores)
        elif opcao == "0":
            salvar_dados(nome_arquivo, sensores)
            print("💾 Dados salvos. Encerrando o sistema...")
            break
        else:
            print("Opção inválida. Tente novamente.")

# Execução do programa
if __name__ == "__main__":
    main()
