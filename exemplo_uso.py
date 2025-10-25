#!/usr/bin/env python3
"""
Exemplo de uso do Split Audio
Este arquivo demonstra como usar o script split_audio.py
"""

import os
import subprocess
import sys

def exemplo_uso():
    """Demonstra como usar o split_audio.py"""
    
    print("🎵 Exemplo de Uso do Split Audio")
    print("=" * 40)
    
    # Verifica se o script existe
    if not os.path.exists("split_audio.py"):
        print("❌ Arquivo split_audio.py não encontrado!")
        return
    
    # Lista arquivos de áudio disponíveis
    extensoes_audio = ['.mp3', '.wav', '.m4a', '.aac', '.flac', '.ogg', '.wma']
    arquivos_audio = []
    
    for arquivo in os.listdir('.'):
        if any(arquivo.lower().endswith(ext) for ext in extensoes_audio):
            arquivos_audio.append(arquivo)
    
    if not arquivos_audio:
        print("📁 Nenhum arquivo de áudio encontrado no diretório atual.")
        print("💡 Coloque um arquivo de áudio (.mp3, .wav, .m4a, etc.) neste diretório.")
        return
    
    print(f"📁 Arquivos de áudio encontrados:")
    for i, arquivo in enumerate(arquivos_audio, 1):
        tamanho = os.path.getsize(arquivo) / (1024 * 1024)  # MB
        print(f"   {i}. {arquivo} ({tamanho:.1f} MB)")
    
    # Exemplo de uso
    arquivo_exemplo = arquivos_audio[0]
    print(f"\n🎯 Exemplo: Dividindo '{arquivo_exemplo}'")
    print(f"Comando: python split_audio.py {arquivo_exemplo}")
    
    # Pergunta se quer executar
    resposta = input("\n❓ Deseja executar o exemplo agora? (s/n): ").lower()
    
    if resposta in ['s', 'sim', 'y', 'yes']:
        try:
            print(f"\n🚀 Executando: python split_audio.py {arquivo_exemplo}")
            resultado = subprocess.run([sys.executable, "split_audio.py", arquivo_exemplo], 
                                    capture_output=False, text=True)
            
            if resultado.returncode == 0:
                print("\n✅ Exemplo executado com sucesso!")
            else:
                print("\n❌ Erro ao executar o exemplo.")
                
        except Exception as e:
            print(f"\n❌ Erro: {e}")
    else:
        print("\n💡 Para executar manualmente:")
        print(f"   python split_audio.py {arquivo_exemplo}")

if __name__ == "__main__":
    exemplo_uso()
