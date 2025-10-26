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
- 💾 **Salvamento Incremental**: Atualiza transcrição a cada segmento (segurança máxima)
- 📊 **Barra de Progresso**: Acompanhamento visual em tempo real

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

### 💡 Instalação com Pip (Recomendado)

```bash
# Clone o repositório
git clone https://github.com/seu-usuario/split_audio.git
cd split_audio

# Crie ambiente virtual
python -m venv venv
source venv/bin/activate  # Linux/Mac
# ou
venv\Scripts\activate     # Windows

# Instale dependências
pip install -r requirements.txt

# Execute
python split_audio.py arquivo_de_audio.m4a --transcrever-completa --modelo tiny
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

# 🚀 Dividir + transcrever tudo em um arquivo único com salvamento incremental
python split_audio.py arquivo_de_audio.m4a --transcrever-completa

# Usar modelo específico do Whisper
python split_audio.py arquivo_de_audio.m4a --transcrever --modelo base

# Alterar duração dos segmentos (padrão: 4 minutos por segmento)
python split_audio.py arquivo_de_audio.m4a --transcrever-completa --segmentos 5

# Modelos disponíveis: tiny, base, small, medium, large
python split_audio.py arquivo_de_audio.m4a --transcrever-completa --modelo small
```

### 💾 Salvamento Incremental

A funcionalidade `--transcrever-completa` salva a transcrição **a cada segmento processado**, garantindo que você sempre tenha a versão mais atualizada:

- ✅ **Segurança máxima**: Se o processo for interrompido, você não perde nada já processado
- ✅ **Acompanhamento em tempo real**: O arquivo é atualizado a cada minuto transcrito
- ✅ **Arquivo único**: Toda transcrição em um lugar organizado com timestamps
- ✅ **Status atualizado**: Mostra quantos segmentos foram processados
- ✅ **Recuperação automática**: Pode retomar de onde parou visualizando o arquivo

**Exemplo do arquivo durante o processamento:**
```bash
Status: 25/70 segmentos transcritos

[01] Texto do primeiro minuto...
[02] Texto do segundo minuto...
...
[25] Texto do vigésimo quinto minuto...
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
$ python split_audio.py arquivo1h.m4a --transcrever-completa --modelo tiny --segmentos 1

🎵 Divisor de Arquivos de Áudio com Transcrição
==================================================
✓ librosa, soundfile, pydub, whisper e tqdm estão instalados

🎯 Processando: arquivo1h.m4a
----------------------------------------
🤖 Carregando modelo Whisper 'tiny'...
✓ Modelo Whisper 'tiny' carregado com sucesso
🎵 Carregando arquivo: arquivo1h.m4a
📊 Taxa de amostragem: 48000 Hz
📊 Duração total: 69.05 minutos
📊 Duração total: 4142.95 segundos
✓ Pasta criada: arquivo1h_dividido
📁 Preparando 70 segmentos de 1 minutos cada
📁 Arquivos serão salvos em formato WAV para melhor transcrição

🎤 Iniciando transcrição completa de 70 segmentos...
============================================================

🎵 Transcrevendo: 100%|████████████████████| 70/70 [1:36:58<00:00, 83.12s/segmento]

🔄 Processando segmento 01/70...
✅ Segmento 01: É, Elery e Jean, esse aqui é o Wiggy e o Ramon...

🔄 Processando segmento 02/70...
✅ Segmento 02: Vamos lá, o que a gente faz como empresa?...

🔄 Processando segmento 03/70...
✅ Segmento 03: para a Marinha. A gente já tem uma relação direta...

...

🔄 Processando segmento 70/70...
✅ Segmento 70: Eu acredito que na semana que vem...

🎉 Transcrição completa finalizada!
📄 Arquivo principal: arquivo1h_transcricao_completa.txt
📄 Arquivo detalhado: arquivo1h_transcricao_detalhada.txt
📊 Total de segmentos processados: 70

🎉 Processo completo finalizado!
📁 Todos os arquivos salvos em: arquivo1h_dividido

✅ Processo concluído com sucesso!
```

### ⏱️ Tempos de Processamento (Baseado em Testes Reais)

| Modelo | 1 Minuto | 1 Hora | Notas |
|--------|----------|--------|-------|
| **tiny** | ~1-2 min | ~1-2h | ✅ Mais rápido, boa qualidade para testes |
| **base** | ~2-3 min | ~2-3h | ✅ Equilibrado, recomendado para uso geral |
| **small** | ~3-4 min | ~3-4h | ✅ Melhor qualidade, mais lento |
| **medium** | ~4-5 min | ~4-5h | ✅ Alta qualidade, lento |
| **large** | ~5-6 min | ~5-6h | ✅ Melhor qualidade, muito lento |

> **💡 Dica:** Use modelo `tiny` para testes rápidos e `base` para produção

## 🎯 Recomendações de Uso

### 📊 Baseado em Testes Reais (69 minutos de áudio)

| Cenário | Comando | Tempo Estimado | Recomendação |
|---------|---------|---------------|--------------|
| **Teste rápido** | `--modelo tiny --segmentos 1` | ~1-2h | ✅ Ideal para validar conteúdo |
| **Uso geral** | `--modelo base --segmentos 4` | ~2-3h | ✅ Equilibrado velocidade/qualidade |
| **Máxima qualidade** | `--modelo small --segmentos 4` | ~3-4h | ✅ Para conteúdo importante |
| **Arquivo pequeno** | `--modelo tiny --segmentos 1` | ~30-60min | ✅ Para arquivos < 30min |

### ⚡ Dicas de Performance

- **Segmentos menores** (1-2 min): Processamento mais rápido, mais arquivos
- **Segmentos maiores** (5-10 min): Processamento mais lento, menos arquivos
- **Modelo tiny**: 2x mais rápido que base, qualidade aceitável
- **Interrupção segura**: Sempre tem transcrição parcial salva

### 🔧 Para Arquivos Grandes (>1h)

1. **Use salvamento incremental**: `--transcrever-completa`
2. **Modelo recomendado**: `tiny` ou `base`
3. **Segmentos**: 1-4 minutos para melhor granularidade
4. **Monitoramento**: Acompanhe o progresso na barra e no arquivo

## ✅ Resultados de Teste Real

**Arquivo:** 69 minutos de áudio
**Configuração:** `--modelo tiny --segmentos 1`
**Tempo:** 1h36min para 70 segmentos
**Taxa:** ~1.4 minutos por minuto de áudio
**Sucesso:** 100% dos segmentos transcritos
**Salvamento:** Incremental funcionando perfeitamente

## 📄 Exemplo de Arquivo de Transcrição

**Durante o processamento:**
```bash
🎵 TRANSCRIÇÃO COMPLETA DO ÁUDIO (ATUALIZANDO...)
==================================================

Arquivo original: arquivo1h.m4a
Total de segmentos: 70
Segmentos processados: 35
Status: 35/70 segmentos transcritos

==================================================

[01] É, Elery e Jean, esse aqui é o Wiggy e o Ramon...
[02] Vamos lá, o que a gente faz como empresa?...
[03] para a Marinha. A gente já tem uma relação direta...
...
[35] [texto do trigésimo quinto minuto]...
```

**Após conclusão:**
```bash
🎵 TRANSCRIÇÃO COMPLETA DO ÁUDIO
==================================================

Arquivo original: arquivo1h.m4a
Total de segmentos: 70
Duração total: 4142.95 segundos
Status: ✅ COMPLETO - 70/70 segmentos transcritos

==================================================

[01] Texto do primeiro minuto...
[02] Texto do segundo minuto...
...
[70] Texto do último minuto...
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
- **Interrupção do processo**: Não se preocupe! O arquivo de transcrição já tem tudo processado até o momento
- **Modelo não carrega**: Primeira execução baixa o modelo (~100-300MB), certifique-se de ter internet

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
