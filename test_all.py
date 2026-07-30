import os
import sys
import json
import xml.etree.ElementTree as ET

if sys.platform == "win32":
    sys.stdout.reconfigure(encoding="utf-8")

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

def run_suite():
    print("=" * 60)
    print("🧪 EXECUTANDO SUÍTE DE TESTES DO AUTO PODCAST GENERATOR")
    print("=" * 60)
    
    passed_tests = 0
    total_tests = 5
    
    # TESTE 1: Validação do Arquivo de Configuração (podcast_config.json)
    print("\n[Teste 1/5] Verificando podcast_config.json...")
    config_path = os.path.join(BASE_DIR, "podcast_config.json")
    try:
        assert os.path.exists(config_path), "Arquivo podcast_config.json não existe!"
        with open(config_path, "r", encoding="utf-8") as f:
            cfg = json.load(f)
        assert "podcast" in cfg and "hosts" in cfg, "Configuração JSON incompleta!"
        assert "title" in cfg["podcast"], "Título do podcast não configurado!"
        print(f"  ✅ APROVADO: Configuração carregada para '{cfg['podcast']['title']}'")
        passed_tests += 1
    except Exception as e:
        print(f"  ❌ FALHOU: {e}")

    # TESTE 2: Módulo de Noticias (autopodcast/news_fetcher.py)
    print("\n[Teste 2/5] Testando busca de notícias (RSS Fetcher)...")
    try:
        from autopodcast.news_fetcher import fetch_tech_news
        news = fetch_tech_news(max_items=2)
        assert len(news) > 0, "Nenhuma notícia retornada!"
        print(f"  ✅ APROVADO: {len(news)} notícia(s) coletadas. Ex: '{news[0]['title'][:40]}...'")
        passed_tests += 1
    except Exception as e:
        print(f"  ❌ FALHOU: {e}")

    # TESTE 3: Teste do Gerador de Roteiro (autopodcast/script_generator.py)
    print("\n[Teste 3/5] Testando gerador de roteiro...")
    try:
        from autopodcast.script_generator import generate_script_with_ai
        sample_news = [{"title": "Teste de Notícia", "source": "Fonte Teste", "link": "http://example.com", "summary": "Resumo de teste"}]
        res = generate_script_with_ai(sample_news)
        assert "title" in res and "script" in res, "Estrutura de roteiro inválida!"
        print(f"  ✅ APROVADO: Roteiro gerado. Título: '{res['title']}'")
        passed_tests += 1
    except Exception as e:
        print(f"  ❌ FALHOU: {e}")

    # TESTE 4: Estrutura do Pacote e Main
    print("\n[Teste 4/5] Verificando integridade de main.py e autopodcast...")
    try:
        import main
        from autopodcast.pipeline import run_pipeline
        assert callable(run_pipeline), "Função run_pipeline não é invocável!"
        print("  ✅ APROVADO: Módulo main.py e pacote autopodcast validados.")
        passed_tests += 1
    except Exception as e:
        print(f"  ❌ FALHOU: {e}")

    # TESTE 5: Verificação do Feed RSS (rss.xml se existir)
    print("\n[Teste 5/5] Verificando arquivo rss.xml...")
    rss_path = os.path.join(BASE_DIR, "rss.xml")
    try:
        if os.path.exists(rss_path):
            tree = ET.parse(rss_path)
            root = tree.getroot()
            assert root.tag == "rss", "Tag raiz não é <rss>!"
            print(f"  ✅ APROVADO: Arquivo rss.xml válido.")
        else:
            print("  ✅ APROVADO: rss.xml será gerado no primeiro episódio.")
        passed_tests += 1
    except Exception as e:
        print(f"  ❌ FALHOU: {e}")

    print("\n" + "=" * 60)
    print(f"📊 RESULTADO DA AUDITORIA: {passed_tests}/{total_tests} TESTES APROVADOS")
    print("=" * 60)

if __name__ == "__main__":
    run_suite()
