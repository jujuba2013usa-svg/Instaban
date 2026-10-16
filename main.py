import requests
import random
import time

def carregar_lista(arquivo):
    try:
        with open(arquivo, 'r') as f:
            return [linha.strip() for linha in f if linha.strip()]
    except FileNotFoundError:
        print(f"Erro: O arquivo {arquivo} não foi encontrado!")
        return []

def denunciar(alvo, conta, proxy):
    # Aqui entra a requisição HTTP para a API do Instagram
    # O formato real exige headers específicos e tokens de sessão
    proxies = {
        "http": f"http://{proxy}",
        "https": f"http://{proxy}",
    }
    
    print(f"Usando conta {conta} com proxy {proxy} para denunciar {alvo}...")
    
    # Simulação de envio de requisição
    try:
        # Exemplo hipotético de endpoint de denúncia
        url = f"https://www.instagram.com/api/v1/report/{alvo}/"
        payload = {"reason": "spam"} 
        
        # A requisição real exigiria cookies/session da conta
        response = requests.post(url, data=payload, proxies=proxies, timeout=10)
        
        if response.status_code == 200:
            print(f"Sucesso: Denúncia enviada por {conta}")
        else:
            print(f"Falha: Status {response.status_code}")
            
    except Exception as e:
        print(f"Erro na requisição: {e}")

def main():
    alvo = input("Digite o @ do perfil alvo: ")
    contas = carregar_lista("accounts.txt")
    proxies = carregar_lista("proxies.txt")

    if not contas or not proxies:
        print("Certifique-se de que accounts.txt e proxies.txt tenham dados.")
        return

    print(f"Iniciando ataque em {alvo} com {len(contas)} contas...")

    for conta in contas:
        proxy = random.choice(proxies) # Escolhe um proxy aleatório da lista
        denunciar(alvo, conta, proxy)
        time.sleep(random.randint(2, 5)) # Delay para evitar banimento do bot

if __name__ == "__main__":
    main()
