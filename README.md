# 🎙️ Auto Podcast Generator - Crie seu Podcast 100% Automático com IA & GitHub Actions

> **Crie, personalize e publique o seu próprio podcast diário sem gastar R$ 1,00!**  
> Este repositório é um **Template Pronto** onde você define o nome do seu podcast, os nomes dos apresentadores, as vozes e os tópicos de notícias em um único arquivo de configuração. A Inteligência Artificial cuida da curadoria, geração do roteiro, síntese das vozes e publicação diária no **Spotify**, **Apple Podcasts** e num **Site Web Interativo com Vídeo de Fundo**.

---

## ✨ Principais Recursos

- 🤖 **Curadoria & Roteiro com IA:** Coleta notícias reais em tempo real via RSS e gera roteiros didáticos e envolventes usando a API gratuita do **Google Gemini AI**.
- 🗣️ **Vozes Neurais de Alta Fidelidade:** Diálogos realistas entre 2 apresentadores usando vozes neurais da Microsoft Azure (`edge-tts`).
- 📡 **Feed RSS 2.0 Nativo:** Gera automaticamente o feed `rss.xml` 100% compatível com **Spotify for Podcasters**, Apple Podcasts, Amazon Music e Google Podcasts.
- ⚡ **Automação Diária Gratuita:** Executado automaticamente todos os dias às 07:00 AM (horário de Brasília) via **GitHub Actions** sem gastar servidor ou precisar deixar o PC ligado.
- 🎥 **Site Web com Vídeo de Fundo (60 FPS):** Player web responsivo em `index.html` com equalizador de áudio reativo, partículas de código flutuantes, capítulos clicáveis e controle ON/OFF.

---

## 📋 Pré-requisitos (100% Gratuitos)

1. Uma conta no [GitHub](https://github.com).
2. Uma chave de API gratuita do [Google Gemini AI Studio](https://aistudio.google.com/).
3. Uma conta gratuita no [Spotify for Podcasters](https://podcasters.spotify.com/).

---

## 🚀 Passo a Passo Completo de Configuração

### 1️⃣ Criar seu Repositório a partir deste Template

1. No topo desta página no GitHub, clique no botão verde **"Use this template"** (ou **"Fork"**).
2. Dê um nome para o seu repositório (ex: `meu-podcast-automating`).
3. Marque o repositório como **Public** (necessário para o GitHub Pages e Spotify lerem seu feed).
4. Clique em **"Create repository"**.

---

### 2️⃣ Obter a Chave da API do Gemini AI

1. Acesse o [Google AI Studio](https://aistudio.google.com/app/apikey).
2. Faça login com sua conta do Google.
3. Clique em **"Create API Key"** e copie o código gerado. *(É 100% gratuito e não exige cartão de crédito!)*

---

### 3️⃣ Configurar a Chave Secreta no GitHub

1. No seu repositório no GitHub, clique na aba **Settings** (Configurações).
2. No menu lateral esquerdo, vá em **Secrets and variables** > **Actions**.
3. Clique no botão **New repository secret**.
4. Preencha os campos:
   - **Name:** `GEMINI_API_KEY`
   - **Secret:** *(Cole a chave que você copiou no Google AI Studio)*
5. Clique em **Add secret**.

---

### 4️⃣ Personalizar o seu Podcast (`podcast_config.json`)

Edite o arquivo `podcast_config.json` direto pelo GitHub ou no seu computador para definir a identidade do seu programa:

```json
{
  "podcast": {
    "title": "Meu Podcast de TI & Tecnologia",
    "tagline": "Tudo sobre Programação, IA & Inovação Descomplicada",
    "description": "O podcast diário que traduz o 'tecniquês' em conversas leves sobre tecnologia.",
    "author": "Seu Nome ou Apresentadores",
    "email": "seu-email@exemplo.com",
    "link": "https://SEU_USUARIO.github.io/NOME_DO_REPOSITORIO",
    "category": "Technology",
    "language": "pt-br",
    "schedule_time_brt": "07:00 da manhã"
  },
  "hosts": {
    "host_1": {
      "name": "Tico",
      "voice": "pt-BR-AntonioNeural",
      "role": "O estudante curioso. Faz perguntas simples de quem está aprendendo do zero."
    },
    "host_2": {
      "name": "Tech",
      "voice": "pt-BR-FranciscaNeural",
      "role": "A especialista em TI. Explica conceitos com analogias simples e dicas de código."
    },
    "mascot": {
      "name": "Robô de IA",
      "role": "O assistente virtual que busca as notícias diárias."
    }
  },
  "feeds": [
    { "name": "freeCodeCamp PT", "url": "https://www.freecodecamp.org/portuguese/news/rss/" },
    { "name": "Blog Alura", "url": "https://www.alura.com.br/artigos/rss" },
    { "name": "TabNews", "url": "https://www.tabnews.com.br/rss" }
  ],
  "keywords": [
    "python", "sql", "programação", "tecnologia", "desenvolvimento", "ia", "dados", "carreira"
  ]
}
```

---

### 🗣️ Lista de Vozes Neurais Disponíveis (Microsoft Azure)

Você pode escolher qualquer uma destas vozes para os seus apresentadores no campo `"voice"`:

#### 🇧🇷 Português (Brasil)
- `pt-BR-AntonioNeural` *(Masculino - Tom jovem/conversacional)*
- `pt-BR-FranciscaNeural` *(Feminino - Tom claro/didático)*
- `pt-BR-HumbertoNeural` *(Masculino - Tom mais grave)*
- `pt-BR-ThalitaNeural` *(Feminino - Tom suave)*

#### 🇵🇹 Português (Portugal)
- `pt-PT-DuarteNeural` *(Masculino)*
- `pt-PT-RaquelNeural` *(Feminino)*

#### 🇺🇸 Inglês (EUA)
- `en-US-GuyNeural` *(Masculino)*
- `en-US-JennyNeural` *(Feminino)*

---

### 5️⃣ Ativar o GitHub Pages (Para Publicar o Site e o Feed RSS)

1. No seu repositório no GitHub, vá em **Settings** > **Pages**.
2. Em **Build and deployment** > **Source**, selecione **Deploy from a branch**.
3. Em **Branch**, escolha `main` e a pasta `/ (root)`.
4. Clique em **Save**.
5. Aguarde cerca de 1 a 2 minutos. A URL do seu site será:  
   `https://SEU_USUARIO.github.io/NOME_DO_REPOSITORIO/`  
   E a URL do seu Feed RSS será:  
   `https://SEU_USUARIO.github.io/NOME_DO_REPOSITORIO/rss.xml`

---

### 6️⃣ Cadastrar no Spotify for Podcasters

1. Acesse o [Spotify for Podcasters](https://podcasters.spotify.com/) e faça login.
2. Clique em **"Get Started"** / **"Add your podcast"** > **"I already have an RSS feed"**.
3. Cole a URL do seu Feed RSS:  
   `https://SEU_USUARIO.github.io/NOME_DO_REPOSITORIO/rss.xml`
4. O Spotify enviará um código de verificação para o e-mail cadastrado em `podcast_config.json`.
5. Insira o código e confirme. **Pronto!** O Spotify publicará seus episódios diariamente de forma automática.

---

### 🎨 7️⃣ Como Personalizar a Capa (`cover.jpg`)

Para alterar a imagem de capa do seu podcast:
1. Crie uma imagem quadrada (recomendado: **1400x1400 px** ou **3000x3000 px** em formato JPG).
2. Substitua o arquivo `cover.jpg` na raiz do repositório pela sua nova imagem.
3. Faça o commit da nova foto.

---

## 💻 Como Rodar e Testar Localmente

Se você deseja rodar ou testar o projeto no seu computador:

### 1. Clonar o repositório
```bash
git clone https://github.com/SEU_USUARIO/NOME_DO_REPOSITORIO.git
cd NOME_DO_REPOSITORIO
```

### 2. Instalar as dependências
```bash
pip install -r requirements.txt
```

### 3. Executar a Suíte de Testes
```bash
python test_all.py
```

### 4. Gerar um novo episódio manualmente
```bash
# Definir a variável de ambiente com sua API key (no PowerShell do Windows):
$env:GEMINI_API_KEY="sua_chave_aqui"

# Executar o gerador:
python main.py
```

---

## 📂 Arquitetura da Solução

```text
Auto-Podcast-Generator/
├── .github/
│   └── workflows/
│       └── daily_podcast.yml  # Automação diária no GitHub Actions
├── autopodcast/               # Pacote principal reutilizável
│   ├── __init__.py
│   ├── config_loader.py       # Leitor dinâmico do podcast_config.json
│   ├── news_fetcher.py        # Coletor de matérias de feeds RSS
│   ├── script_generator.py    # Gerador de roteiro com Gemini AI
│   ├── audio_generator.py     # Sintetizador de vozes neurais (edge-tts)
│   ├── rss_generator.py       # Gerador do feed XML para Spotify & Apple
│   └── pipeline.py            # Orquestrador mestre do fluxo
├── data/
│   └── episodes.json          # Banco de dados de histórico dos episódios
├── episodes/                  # Pasta onde os arquivos MP3 são salvos
├── podcast_config.json        # ARQUIVO DE CONFIGURAÇÃO CENTRAL
├── cover.jpg                  # Imagem de capa oficial do podcast
├── index.html                 # Player Web interativo com Vídeo Canvas 60 FPS
├── main.py                    # Entrada CLI do gerador (python main.py)
├── test_all.py                # Suíte de auditoria e testes automáticos
├── requirements.txt           # Dependências Python
└── README.md                  # Manual completo do projeto
```

---

## ❓ Solução de Problemas (Troubleshooting)

- **O GitHub Actions não está gerando episódios?**  
  Verifique se você cadastrou o Secret `GEMINI_API_KEY` corretamente em *Settings > Secrets and variables > Actions*.
- **O Spotify não encontra o RSS?**  
  Certifique-se de que o GitHub Pages está ativado na aba *Settings > Pages* e que o repositório é *Public*.
- **Como alterar o horário de publicação automática?**  
  Edite o arquivo `.github/workflows/daily_podcast.yml` e modifique a linha `cron: '0 10 * * *'`. *(Ex: `0 10` é 10:00 UTC, equivalente às 07:00 AM no Brasil).*

---

## 📄 Licença

Este projeto é open-source e disponibilizado sob a licença [MIT](LICENSE). Fique à vontade para usar, modificar e distribuir seu próprio podcast!
