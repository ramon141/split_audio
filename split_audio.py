#!/usr/bin/env python3
"""
Script para dividir arquivos de áudio longos em segmentos menores.
Divide um arquivo de áudio de 1 hora em segmentos de 4 minutos cada.
Usa librosa e soundfile para compatibilidade com Python 3.13.
"""

import os
import sys
import numpy as np
from pathlib import Path
import librosa
import soundfile as sf
from pydub import AudioSegment

def verificar_dependencias():
    """Verifica se as dependências necessárias estão instaladas."""
    try:
        import librosa
        import soundfile
        from pydub import AudioSegment
        print("✓ librosa, soundfile e pydub estão instalados")
        return True
    except ImportError as e:
        print(f"❌ Dependências não encontradas: {e}")
        print("Execute: pip install librosa soundfile pydub")
        return False

def criar_pasta_saida(nome_arquivo_original):
    """Cria uma pasta para os arquivos divididos."""
    nome_base = Path(nome_arquivo_original).stem
    pasta_saida = f"{nome_base}_dividido"
    
    if not os.path.exists(pasta_saida):
        os.makedirs(pasta_saida)
        print(f"✓ Pasta criada: {pasta_saida}")
    else:
        print(f"✓ Pasta já existe: {pasta_saida}")
    
    return pasta_saida

def dividir_audio(arquivo_entrada, duracao_segmento_min=4):
    """
    Divide um arquivo de áudio em segmentos menores.
    
    Args:
        arquivo_entrada (str): Caminho para o arquivo de áudio
        duracao_segmento_min (int): Duração de cada segmento em minutos
    """
    try:
        print(f"🎵 Carregando arquivo: {arquivo_entrada}")
        
        # Carrega o arquivo de áudio
        audio_data, sample_rate = librosa.load(arquivo_entrada, sr=None)
        
        # Informações do arquivo
        duracao_total_segundos = len(audio_data) / sample_rate
        duracao_total_minutos = duracao_total_segundos / 60
        
        print(f"📊 Taxa de amostragem: {sample_rate} Hz")
        print(f"📊 Duração total: {duracao_total_minutos:.2f} minutos")
        print(f"📊 Duração total: {duracao_total_segundos:.2f} segundos")
        
        # Calcula a duração de cada segmento em amostras
        duracao_segmento_amostras = int(duracao_segmento_min * 60 * sample_rate)
        
        # Cria a pasta de saída
        pasta_saida = criar_pasta_saida(arquivo_entrada)
        
        # Calcula quantos segmentos serão criados
        num_segmentos = int(len(audio_data) / duracao_segmento_amostras) + 1
        
        print(f"📁 Criando {num_segmentos} segmentos de {duracao_segmento_min} minutos cada")
        print(f"📁 Salvando em: {pasta_saida}/")
        
        # Divide o áudio em segmentos
        for i in range(num_segmentos):
            inicio_amostra = i * duracao_segmento_amostras
            fim_amostra = min((i + 1) * duracao_segmento_amostras, len(audio_data))
            
            # Extrai o segmento
            segmento = audio_data[inicio_amostra:fim_amostra]
            
            # Nome do arquivo de saída
            nome_base = Path(arquivo_entrada).stem
            extensao = Path(arquivo_entrada).suffix
            
            # Sempre salvar como M4A para manter consistência
            extensao_saida = '.m4a'
            nome_arquivo = f"{nome_base}_parte_{i+1:02d}{extensao_saida}"
            caminho_saida = os.path.join(pasta_saida, nome_arquivo)
            
            # Converter numpy array para AudioSegment e salvar como M4A
            # Primeiro, normalizar o áudio para o formato correto
            if segmento.dtype != np.float32:
                segmento = segmento.astype(np.float32)
            
            # Converter para AudioSegment
            audio_segment = AudioSegment(
                segmento.tobytes(),
                frame_rate=sample_rate,
                sample_width=4,  # 32-bit float
                channels=1 if len(segmento.shape) == 1 else segmento.shape[1]
            )
            
            # Salvar como M4A
            audio_segment.export(caminho_saida, format="mp4")
            
            # Informações do segmento
            duracao_segmento_atual = len(segmento) / sample_rate
            print(f"✓ Parte {i+1:02d}: {nome_arquivo} ({duracao_segmento_atual:.1f}s)")
        
        print(f"\n🎉 Divisão concluída! {num_segmentos} arquivos criados em '{pasta_saida}'")
        
    except FileNotFoundError:
        print(f"❌ Erro: Arquivo não encontrado: {arquivo_entrada}")
        return False
    except Exception as e:
        print(f"❌ Erro ao processar o arquivo: {str(e)}")
        return False
    
    return True

def main():
    """Função principal do script."""
    print("🎵 Divisor de Arquivos de Áudio")
    print("=" * 40)
    
    # Verifica dependências
    if not verificar_dependencias():
        sys.exit(1)
    
    # Verifica se foi fornecido um arquivo
    if len(sys.argv) < 2:
        print("\n📝 Uso: python split_audio.py <arquivo_de_audio>")
        print("📝 Exemplo: python split_audio.py arquivo1h.m4a")
        print("\n💡 O script dividirá o arquivo em segmentos de 4 minutos cada.")
        sys.exit(1)
    
    arquivo_entrada = sys.argv[1]
    
    # Verifica se o arquivo existe
    if not os.path.exists(arquivo_entrada):
        print(f"❌ Erro: Arquivo não encontrado: {arquivo_entrada}")
        sys.exit(1)
    
    # Verifica se é um arquivo de áudio
    extensoes_validas = ['.mp3', '.wav', '.m4a', '.aac', '.flac', '.ogg', '.wma']
    extensao_arquivo = Path(arquivo_entrada).suffix.lower()
    
    if extensao_arquivo not in extensoes_validas:
        print(f"⚠️  Aviso: Extensão '{extensao_arquivo}' pode não ser suportada.")
        print(f"   Extensões recomendadas: {', '.join(extensoes_validas)}")
    
    print(f"\n🎯 Processando: {arquivo_entrada}")
    print("-" * 40)
    
    # Executa a divisão
    sucesso = dividir_audio(arquivo_entrada)
    
    if sucesso:
        print("\n✅ Processo concluído com sucesso!")
    else:
        print("\n❌ Processo falhou!")
        sys.exit(1)

if __name__ == "__main__":
    main()