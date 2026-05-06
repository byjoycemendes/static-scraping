import httpx
import time
import os
from dotenv import load_dotenv

load_dotenv()

class CaptchaSolver:
    def __init__(self):
        self.api_key = os.getenv("CAPMONSTER_API_KEY")
        # Adicionado timeout de 60s para evitar que a requisição caia antes do captcha ser criado
        self.client = httpx.Client(base_url="https://api.capmonster.cloud", timeout=60.0)

    def solve_recaptcha(self, site_url, site_key):
        # 1. Criar a tarefa
        task_data = {
            "clientKey": self.api_key,
            "task": {
                "type": "NoCaptchaTaskProxyless",
                "websiteURL": site_url,
                "websiteKey": site_key.strip()  # .strip() remove espaços acidentais
            }
        }
        
        response = self.client.post("/createTask", json=task_data)
        data_resp = response.json()
        
        # Verificação se o erro já acontece na criação
        if data_resp.get("errorId") != 0:
            raise Exception(f"Erro ao criar tarefa: {data_resp.get('errorCode')} - {data_resp.get('errorDescription')}")

        task_id = data_resp.get("taskId")

        # 2. Consultar o resultado (Polling)
        print(f"Tarefa {task_id} criada. Aguardando solução...")
        tentativas = 0
        while True:
            tentativas += 1
            result_data = {
                "clientKey": self.api_key,
                "taskId": task_id
            }
            
            try:
                res = self.client.post("/getTaskResult", json=result_data)
                data = res.json()
            except Exception as e:
                print(f"\n[Aviso] Falha na comunicação com CapMonster: {e}. Tentando novamente...")
                time.sleep(3)
                continue

            status = data.get("status")
            
            if status == "ready":
                print(f"\n[OK] Captcha resolvido em aproximadamente {tentativas * 3} segundos!")
                return data["solution"]["gRecaptchaResponse"]
            
            if data.get("errorId") != 0:
                print(f"\n[ERRO] O CapMonster retornou um problema: {data.get('errorCode')}")
                raise Exception(f"Erro no CapMonster: {data.get('errorCode')}")
            
            print(f" Aguardando... (Tentativa {tentativas})", end="\r")
            time.sleep(3)
        
    def close(self):
        self.client.close()