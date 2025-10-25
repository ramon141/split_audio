# 🎵 Split Audio - Divisor de Arquivos de Áudio

<div align="center">

![Python](https://img.shields.io/badge/Python-3.13+-blue.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)
![Status](https://img.shields.io/badge/Status-Production%20Ready-brightgreen.svg)

**Uma ferramenta Python elegante para dividir arquivos de áudio longos em segmentos menores e transcrever usando IA**

[🚀 Instalação](#-instalação) • [📖 Como Usar](#-como-usar) • [🎯 Funcionalidades](#-funcionalidades) • [🔧 Solução de Problemas](#-solução-de-problemas)

</div>

---

## 📋 Sobre o Projeto

O **Split Audio** é uma ferramenta Python desenvolvida para dividir arquivos de áudio longos em segmentos menores de 4 minutos cada e transcrever usando IA (Whisper). Ideal para podcasts, aulas, músicas longas ou qualquer conteúdo de áudio que precise ser segmentado e transcrito para facilitar o compartilhamento ou processamento.

### ✨ Por que usar o Split Audio?

- 🎯 **Precisão**: Divide arquivos com precisão de segundos
- 🎨 **Interface Amigável**: Mensagens coloridas e informativas
- 🔧 **Robusto**: Tratamento completo de erros
- 📁 **Organizado**: Cria automaticamente pastas para os arquivos divididos
- 🌐 **Compatível**: Suporta múltiplos formatos de áudio
- ⚡ **Rápido**: Processamento eficiente usando bibliotecas otimizadas
- 🤖 **IA Integrada**: Transcrição automática usando Whisper
- 📝 **Multilíngue**: Suporta transcrição em português e outros idiomas

---

## 🎯 Funcionalidades

<table>
<tr>
<td width="50%">

---

## 🚀 Instalação

### Pré-requisitos

- Python 3.13 ou superior
- pip (gerenciador de pacotes Python)

### Instalação Rápida

1. **Clone o repositório**

   ```bash
   git clone https://github.com/seu-usuario/split_audio.git
   cd split_audio
   ```
2. **Crie um ambiente virtual**

   ```bash
   python -m venv venv
   source venv/bin/activate  # No Windows: venv\Scripts\activate
   ```
3. **Instale as dependências**

   ```bash
   pip install -r requirements.txt
   ```

### Instalação Manual

```bash
pip install librosa soundfile numpy pydub openai-whisper torch tqdm
```

---

## 📖 Como Usar

### Uso Básico

```bash
python split_audio.py arquivo_de_audio.extensao
```

### Exemplos Práticos

```bash
# Dividir um podcast de 1 hora
python split_audio.py podcast_1h.mp3

# Dividir uma aula de música
python split_audio.py aula_musica.wav

# Dividir um arquivo M4A
python split_audio.py gravacao.m4a
```

### 🎤 Funcionalidades de Transcrição

```bash
# Apenas dividir (funcionalidade original)
python split_audio.py arquivo_de_audio.m4a

# Dividir + transcrever cada segmento individualmente
python split_audio.py arquivo_de_audio.m4a --transcrever

# Apenas transcrever arquivo completo
python split_audio.py arquivo_de_audio.m4a --apenas-transcrever

# 🚀 NOVA FUNCIONALIDADE: Dividir + transcrever tudo em um arquivo único
python split_audio.py arquivo_de_audio.m4a --transcrever-completa

# Usar modelo específico do Whisper
python split_audio.py arquivo_de_audio.m4a --transcrever --modelo base

# Alterar duração dos segmentos (padrão: 4 minutos por segmento)
python split_audio.py arquivo_de_audio.m4a --transcrever-completa --segmentos 5

# Modelos disponíveis: tiny, base, small, medium, large
python split_audio.py arquivo_de_audio.m4a --transcrever-completa --modelo small
```

### Estrutura de Saída

```
projeto/
├── arquivo_original.mp3
├── split_audio.py
└── arquivo_original_dividido/
    ├── arquivo_original_parte_01.m4a
    ├── arquivo_original_parte_01.txt      # Transcrição da parte 1
    ├── arquivo_original_parte_02.m4a
    ├── arquivo_original_parte_02.txt      # Transcrição da parte 2
    ├── arquivo_original_parte_03.m4a
    ├── arquivo_original_parte_03.txt      # Transcrição da parte 3
    ├── arquivo_original_transcricao_completa.txt     # 🎯 Transcrição completa em um arquivo
    └── arquivo_original_transcricao_detalhada.txt    # 🎯 Informações detalhadas por segmento
```

---

## 🎬 Exemplo de Execução

```bash
$ python split_audio.py arquivo1h.m4a --transcrever-completa --modelo base

🎵 Divisor de Arquivos de Áudio com Transcrição
==================================================
✓ librosa, soundfile, pydub, whisper e tqdm estão instalados

🎯 Processando: arquivo1h.m4a
----------------------------------------
🤖 Carregando modelo Whisper 'base'...
✓ Modelo Whisper 'base' carregado com sucesso
🎵 Carregando arquivo: arquivo1h.m4a
📊 Taxa de amostragem: 48000 Hz
📊 Duração total: 69.05 minutos
📊 Duração total: 4142.95 segundos
✓ Pasta criada: arquivo1h_dividido
📁 Preparando 18 segmentos de 4 minutos cada
📁 Arquivos serão salvos em formato WAV para melhor transcrição

🎤 Iniciando transcrição completa de 18 segmentos...
============================================================

🎵 Transcrevendo: 100%|████████████████████| 18/18 [45:30<00:00, 151.68s/segmento]

🔄 Processando segmento 01/18...
✅ Segmento 01: O resto é seguir uma lógica dentro de 1901 para a gente poder...

🔄 Processando segmento 02/18...
✅ Segmento 02: Continuando com a explicação sobre documentação...

🔄 Processando segmento 03/18...
✅ Segmento 03: Agora vamos falar sobre os procedimentos...

...

🎉 Transcrição completa finalizada!
📄 Arquivo principal: arquivo1h_transcricao_completa.txt
📄 Arquivo detalhado: arquivo1h_transcricao_detalhada.txt
📊 Total de segmentos processados: 18

🎉 Processo completo finalizado!
📁 Todos os arquivos salvos em: arquivo1h_dividido

✅ Processo concluído com sucesso!
```

---

## 📊 Formatos Suportados

| Formato        | Entrada | Saída | Notas               |
| -------------- | ------- | ------ | ------------------- |
| **MP3**  | ✅      | ✅     | Formato mais comum  |
| **WAV**  | ✅      | ✅     | Qualidade máxima   |
| **M4A**  | ✅      | ✅     | Formato de saída padrão |
| **AAC**  | ✅      | ✅     | Alta qualidade      |
| **FLAC** | ✅      | ✅     | Lossless            |
| **OGG**  | ✅      | ✅     | Open source         |
| **WMA**  | ✅      | ✅     | Windows Media       |

> **Nota**: Todos os arquivos são salvos em formato M4A para manter consistência e boa compressão.

---

## 🔧 Solução de Problemas

### ❌ Erro de Dependências

```bash
# Solução: Reinstalar dependências
pip install --upgrade librosa soundfile numpy pydub openai-whisper torch tqdm
```

### ❌ Arquivo Não Encontrado

```bash
# Verifique se o arquivo existe
ls -la arquivo_de_audio.mp3

# Use caminho completo se necessário
python split_audio.py /caminho/completo/para/arquivo.mp3
```

### ❌ Formato Não Suportado

- O script tenta carregar qualquer formato de áudio
- Formatos proprietários podem não funcionar
- Converta para MP3 ou WAV antes de usar

### ❌ Erro de Memória

- Para arquivos muito grandes (>2GB), considere usar um computador com mais RAM
- O script carrega o arquivo inteiro na memória

### ❌ Problemas de Transcrição

- **Transcrição vazia**: O áudio pode não conter fala clara ou ser música instrumental
- **Modelo muito lento**: Use `--modelo tiny` para testes rápidos
- **Qualidade ruim**: Use `--modelo large` para melhor qualidade (mais lento)
- **Arquivo M4A**: O script converte automaticamente para WAV para melhor compatibilidade

### ❌ Whisper não funciona

- Primeira execução baixa o modelo (~100-300MB)
- Certifique-se de ter conexão com internet na primeira vez
- Modelos maiores precisam de mais RAM

### ❌ Problemas com --transcrever-completa

- **Barra de progresso não aparece**: Certifique-se de que o tqdm está instalado
- **Arquivos não salvos**: Verifique se há espaço suficiente no disco
- **Transcrição vazia**: Use modelos maiores (base, small, medium) para melhor qualidade
- **Processo muito lento**: Use modelo `tiny` para testes rápidos

---

## 🛠️ Desenvolvimento

### Estrutura do Projeto

```
split_audio/
├── split_audio.py      # Script principal
├── requirements.txt     # Dependências
├── README.md           # Documentação
├── .gitignore          # Arquivos ignorados
└── venv/               # Ambiente virtual
```

### Contribuindo

1. Fork o projeto
2. Crie uma branch para sua feature (`git checkout -b feature/AmazingFeature`)
3. Commit suas mudanças (`git commit -m 'Add some AmazingFeature'`)
4. Push para a branch (`git push origin feature/AmazingFeature`)
5. Abra um Pull Request

---

## 📄 Licença

Este projeto está sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.

---

## 👨‍💻 Autor

**Ramon** - Desenvolvedor Python

- GitHub: [@ramon141
  ](https://github.com/ramon141)

---

## 🙏 Agradecimentos

- [librosa](https://librosa.org/) - Biblioteca de análise de áudio
- [soundfile](https://pysoundfile.readthedocs.io/) - Biblioteca de leitura/escrita de áudio
- [numpy](https://numpy.org/) - Computação numérica

---

<div align="center">

**⭐ Se este projeto foi útil para você, considere dar uma estrela! ⭐**

Feito com ❤️ em Python

</div>
