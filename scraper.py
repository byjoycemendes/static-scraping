import httpx
from solver import CaptchaSolver

class FrenquLabScraper:
    def __init__(self):
        self.base_url = "https://frenqulabi.com"
        # Composição: O Scraper possui um Solver
        self.solver = CaptchaSolver()
        
        # O Client com follow_redirects=True é crucial para cair no Dashboard após o login
        self.client = httpx.Client(
            headers={
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36",
                "Origin": "https://frenqulabi.com",
                "Referer": "https://frenqulabi.com/login"
            },
            follow_redirects=True
        )

    def login(self, email, password):
        print(f"--- Iniciando Processo de Login para: {email} ---")
        
        # 1. Definição dos parâmetros do alvo
        # Re-verifique se não há espaços nesta string
        site_key = "6LeXI2csAAAAAEdvHDyj5EK6Yc5zDY2jksaerQk3"
        login_url = f"{self.base_url}/login"
        
        # 2. Obter o token (aqui chamamos o solver corrigido)
        try:
            token = self.solver.solve_recaptcha(login_url, site_key)
        except Exception as e:
            print(f"Falha técnica na resolução do Captcha: {e}")
            return False
        
        # 3. Montar o payload (Carga Útil)
        payload = {
            "email": email,
            "password": password,
            "g-recaptcha-response": token
        }
        
        # 4. Enviar o POST para o endpoint de login
        print("Enviando credenciais...")
        response = self.client.post(login_url, data=payload)
        
        # 5. Verificação robusta de sucesso
        # O site retorna "Dashboard" no corpo ou redireciona para a rota /dashboard
        if response.status_code == 200:
            content = response.text
            if "Dashboard" in content or "Login successful" in content:
                print("Login realizado com sucesso! Acesso ao Dashboard garantido.")
                return True
            
        print(f"Falha no login. Status: {response.status_code}")
        # Útil para debug: print(response.text[:200]) 
        return False