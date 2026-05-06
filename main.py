from scraper import FrenquLabScraper

def main():
    # Instanciamos o Scraper (que por sua vez instancia o Solver)
    bot = FrenquLabScraper()
    
    try:
        # Qualquer e-mail e senha funcionam conforme a descrição do desafio
        sucesso = bot.login("test_user@dev.com", "desafio123")
        
        if sucesso:
            print("\n" + "="*30)
            print("🚀 PROJETO EXECUTADO COM SUCESSO!")
            print("="*30)
        else:
            print("\n" + "!"*30)
            print("❌ FALHA NA VALIDAÇÃO DO LOGIN")
            print("!"*30)
            
    except Exception as e:
        print(f"\n[CRITICAL ERROR] {e}")
        
    finally:
        # Fechamento seguro das conexões httpx
        if hasattr(bot, 'client'):
            bot.client.close()
        if hasattr(bot, 'solver'):
            bot.solver.close()
        print("\nSessões encerradas de forma segura.")

if __name__ == "__main__":
    main()