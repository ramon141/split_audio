# 🎵 Split Audio - Divisor de Arquivos de Áudio

<div align="center">

![Python](https://img.shields.io/badge/Python-3.13+-blue.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)
![Status](https://img.shields.io/badge/Status-Production%20Ready-brightgreen.svg)

**Uma ferramenta Python elegante para dividir arquivos de áudio longos em segmentos menores**

[🚀 Instalação](#-instalação) • [📖 Como Usar](#-como-usar) • [🎯 Funcionalidades](#-funcionalidades) • [🔧 Solução de Problemas](#-solução-de-problemas)

</div>

---

## 📋 Sobre o Projeto

O **Split Audio** é uma ferramenta Python desenvolvida para dividir arquivos de áudio longos em segmentos menores de 4 minutos cada. Ideal para podcasts, aulas, músicas longas ou qualquer conteúdo de áudio que precise ser segmentado para facilitar o compartilhamento ou processamento.

### ✨ Por que usar o Split Audio?

- 🎯 **Precisão**: Divide arquivos com precisão de segundos
- 🎨 **Interface Amigável**: Mensagens coloridas e informativas
- 🔧 **Robusto**: Tratamento completo de erros
- 📁 **Organizado**: Cria automaticamente pastas para os arquivos divididos
- 🌐 **Compatível**: Suporta múltiplos formatos de áudio
- ⚡ **Rápido**: Processamento eficiente usando bibliotecas otimizadas

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
pip install librosa soundfile numpy pydub
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

### Estrutura de Saída

```
projeto/
├── arquivo_original.mp3
├── split_audio.py
└── arquivo_original_dividido/
    ├── arquivo_original_parte_01.m4a
    ├── arquivo_original_parte_02.m4a
    ├── arquivo_original_parte_03.m4a
    └── ...
```

---

## 🎬 Exemplo de Execução

```bash
$ python split_audio.py arquivo1h.m4a

🎵 Divisor de Arquivos de Áudio
========================================
✓ librosa e soundfile estão instalados

🎯 Processando: arquivo1h.m4a
----------------------------------------
🎵 Carregando arquivo: arquivo1h.m4a
📊 Taxa de amostragem: 48000 Hz
📊 Duração total: 69.05 minutos
📊 Duração total: 4142.95 segundos
✓ Pasta criada: arquivo1h_dividido
📁 Criando 18 segmentos de 4 minutos cada
📁 Salvando em: arquivo1h_dividido/
✓ Parte 01: arquivo1h_parte_01.wav (240.0s)
✓ Parte 02: arquivo1h_parte_02.wav (240.0s)
✓ Parte 03: arquivo1h_parte_03.wav (240.0s)
...
✓ Parte 18: arquivo1h_parte_18.wav (63.0s)

🎉 Divisão concluída! 18 arquivos criados em 'arquivo1h_dividido'

✅ Processo concluído com sucesso!
```

---

## 📊 Formatos Suportados

| Formato        | Entrada | Saída | Notas               |
| -------------- | ------- | ------ | ------------------- |
| **MP3**  | ✅      | ✅     | Formato mais comum  |
| **WAV**  | ✅      | ✅     | Qualidade máxima   |
| **M4A**  | ✅      | ✅     | Convertido para WAV |
| **AAC**  | ✅      | ✅     | Alta qualidade      |
| **FLAC** | ✅      | ✅     | Lossless            |
| **OGG**  | ✅      | ✅     | Open source         |
| **WMA**  | ✅      | ✅     | Windows Media       |

> **Nota**: Arquivos M4A são automaticamente convertidos para WAV na saída para garantir máxima compatibilidade.

---

## 🔧 Solução de Problemas

### ❌ Erro de Dependências

```bash
# Solução: Reinstalar dependências
pip install --upgrade librosa soundfile numpy
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
