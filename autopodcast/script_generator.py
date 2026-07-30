import os
import re
import json
from google import genai
from autopodcast.config_loader import load_config

def get_gemini_api_key():
    for key, val in os.environ.items():
        if "GEMINI" in key.upper() and ("KEY" in key.upper() or "TOKEN" in key.upper() or "API" in key.upper()):
            if val and len(val) > 5:
                return val
    return os.environ.get("GEMINI_API_KEY")

def clean_topic_title(raw_title: str) -> str:
    if not raw_title:
        return "Tecnologia e Inovação"
    title = raw_title.strip()
    title = re.sub(r'^(?:Ep\.?|Episódio)\s*\d+[:\-]?\s*', '', title, flags=re.IGNORECASE).strip()
    title = re.sub(r'[\(\[\{].*?[\)\]\}]', '', title).strip()
    title = re.sub(r'^[:\-–—\s]+', '', title).strip()
    return title if title else raw_title

def generate_script_with_ai(news_items):
    cfg = load_config()
    podcast_title = cfg["podcast"].get("title", "Podcast")
    h1_name = cfg["hosts"]["host_1"].get("name", "Host1")
    h1_role = cfg["hosts"]["host_1"].get("role", "Apresentador curioso")
    h2_name = cfg["hosts"]["host_2"].get("name", "Host2")
    h2_role = cfg["hosts"]["host_2"].get("role", "Apresentador especialista")

    prompt_rules = f"""
Você é um curador de conteúdo educacional e roteirista sênior do podcast '{podcast_title}'.
Sua missão é gerar um roteiro de podcast dinâmico, didático, altamente envolvente e EXTENSO para o {podcast_title} (duração estimada de 18 a 22 minutos de conversa falada).

Apresentadores:
- {h1_name}: {h1_role}
- {h2_name}: {h2_role}

REGRAS DE CONTEÚDO E FALA NATURAL (EXTREMAMENTE IMPORTANTE):
1. NUNCA cite números de episódios de outros conteúdos (ex: NUNCA diga "Ep. 53", "Ep 50").
2. NUNCA cite nomes de fontes de notícias ou sites em voz alta (ex: NUNCA diga "veio do site X").
3. NUNCA cite links ou URLs no meio da fala.
4. {h1_name} e {h2_name} devem introduzir os assuntos de forma 100% natural e conversacional. Exemplo:
   {h1_name}: {h2_name}, vi que muita gente comenta sobre esse assunto. Como um iniciante pode começar?
   {h2_name}: Essa área é incrível, {h1_name}! O segredo é entender a lógica sem tentar memorizar tudo...

REGRAS DE DURAÇÃO (18 a 22 MINUTOS):
- O ROTEIRO DEVE SER LONGO, COMPLETO E APROFUNDADO (Aproximadamente 2.500 a 3.000 palavras no total).
- Desenvolva entre 8 e 12 trocas de fala ricas para cada um dos 3 temas principais.

Regras de Formatação:
1. O diálogo DEVE ter marcações claras de tempo [MM:SS] no início de cada bloco.
2. Cada linha de diálogo deve começar estritamente com '{h1_name}:' ou '{h2_name}:'.
3. Exemplo de marcação de bloco: [00:00] INTRODUÇÃO

Retorne estritamente um objeto JSON com a seguinte estrutura:
{{
  "title": "Título chamativo e profissional do episódio",
  "summary": "Resumo abrangente do episódio em 3 a 4 frases.",
  "chapters": [
    ["00:00", "Intro & Destaques do Dia"],
    ["02:30", "Bloco 1: Título do Tema 1"],
    ["08:00", "Bloco 2: Título do Tema 2"],
    ["14:00", "Bloco 3: Título do Tema 3"],
    ["19:00", "Recapitulação & Dicas Finais"]
  ],
  "sources": [
    ["Nome da Fonte 1", "https://url1.com"],
    ["Nome da Fonte 2", "https://url2.com"]
  ],
  "script": "[00:00] INTRODUÇÃO\\n{h1_name}: ...\\n{h2_name}: ...\\n\\n[02:30] BLOCO 1\\n..."
}}
"""

    api_key = get_gemini_api_key()
    
    formatted_news = ""
    for i, item in enumerate(news_items, 1):
        clean_t = clean_topic_title(item['title'])
        formatted_news += f"{i}. Tema: {clean_t}\n   Resumo: {item['summary']}\n\n"

    if api_key:
        try:
            print(f"[+] Gerando roteiro extenso para {podcast_title} com Gemini AI...")
            client = genai.Client(api_key=api_key)
            response = client.models.generate_content(
                model="gemini-2.0-flash",
                contents=f"{prompt_rules}\n\nAqui estão os temas reais para o episódio de hoje:\n{formatted_news}",
                config={"response_mime_type": "application/json"}
            )
            raw_text = response.text.strip() if response.text else ""
            if raw_text.startswith("```"):
                raw_text = re.sub(r'^```(?:json)?\s*', '', raw_text, flags=re.IGNORECASE)
                raw_text = re.sub(r'\s*```$', '', raw_text)
            data = json.loads(raw_text)
            
            if isinstance(data, dict):
                script_text = data.get("script") or data.get("roteiro") or data.get("dialogo")
                first_clean_topic = clean_topic_title(news_items[0]['title']) if news_items else 'Tecnologia'
                title_text = data.get("title") or data.get("titulo") or f"Destaques do Dia: {first_clean_topic}"
                if script_text:
                    data["script"] = script_text
                    data["title"] = title_text
                    data.setdefault("summary", f"Neste episódio do {podcast_title}, {h1_name} e {h2_name} conversam sobre as principais novidades em tecnologia!")
                    data.setdefault("chapters", [["00:00", "Intro & Destaques do Dia"]])
                    data.setdefault("sources", [[item['source'], item['link']] for item in news_items])
                    print("[OK] Roteiro extenso gerado com sucesso via Gemini AI!")
                    return data
        except Exception as e:
            print(f"[!] Aviso na API do Gemini: {e}. Utilizando gerador didático aprofundado de fallback.")

    # Fallback didático e estruturado
    print("[+] Montando roteiro de fallback didático...")
    first_clean_title = clean_topic_title(news_items[0]['title']) if news_items else 'Tecnologia e Inovação'
    title = f"Destaques: {first_clean_title}"
    summary = f"Neste episódio do {podcast_title}, {h1_name} e {h2_name} conversam sobre os tópicos essenciais de tecnologia para impulsionar seus conhecimentos!"
    
    chapters = [["00:00", "Intro & Destaques do Dia"]]
    sources = []
    
    script_lines = [
        "[00:00] INTRODUÇÃO",
        f"{h1_name}: Olá, pessoal! Sejam muito bem-vindos ao {podcast_title}, o seu espaço diário sobre tecnologia, inovação e desenvolvimento!",
        f"{h2_name}: Fala, gente! Eu sou a {h2_name} e hoje preparamos um episódio super completo sobre os tópicos que mais geram dúvidas.",
        f"{h1_name}: É isso mesmo, {h2_name}! Vamos descomplicar cada assunto sem jargões difíceis. Peguem seu café e venham com a gente!"
    ]
    
    for idx, item in enumerate(news_items[:3]):
        clean_title = clean_topic_title(item['title'])
        sources.append([item['source'], item['link']])
        
        script_lines.extend([
            f"\n[00:00] BLOCO {idx+1}: {clean_title.upper()}",
            f"{h1_name}: {h2_name}, hoje vamos conversar sobre {clean_title}. O que esse conceito significa na prática para quem quer aprender?",
            f"{h2_name}: Excelente pergunta, {h1_name}! Para entender {clean_title}, vale a pena usar uma analogia do cotidiano. {item['summary']} Na prática, isso traz exatamente a organização e a eficiência de que precisamos.",
            f"{h1_name}: Incrível! E qual é a melhor forma de aplicar isso no dia a dia?",
            f"{h2_name}: Comece aplicando em pequenos projetos práticos. Divida o problema em etapas simples e resolva uma de cada vez. A constância é a chave do sucesso!"
        ])
        
    script_lines.extend([
        "\n[00:00] RECAPITULAÇÃO E DICAS DE ESTUDO",
        f"{h2_name}: E assim chegamos ao final do nosso episódio de hoje! Lembrem-se: aprender tecnologia é uma maratona constante.",
        f"{h1_name}: Com certeza! Todos os links das matérias citadas estão nas show notes do episódio. Nos vemos no próximo programa!",
        f"{h2_name}: Até lá, pessoal, bons estudos!"
    ])
    
    chapters.append(["19:00", "Recapitulação & Dicas Finais"])
    
    return {
        "title": title,
        "summary": summary,
        "chapters": chapters,
        "sources": sources,
        "script": "\n".join(script_lines)
    }
