import os
from yt_dlp import YoutubeDL

# Configuração do diretório de saída
DOWNLOAD_DIR = "Downloads"
if not os.path.exists(DOWNLOAD_DIR):
    os.makedirs(DOWNLOAD_DIR)

# Configurações padrão do yt-dlp
YDL_OPTIONS = {
    'format': 'bestvideo+bestaudio/best',  # Melhor qualidade disponível
    'outtmpl': os.path.join(DOWNLOAD_DIR, '%(uploader)s/%(playlist_title)s/%(title)s.%(ext)s'),  # Organiza em pastas
    'noplaylist': False,  # Permite baixar playlists
    'quiet': False,
    'progress_hooks': [lambda d: print(f"[{d['status'].capitalize()}] {d.get('filename', '')}")],
}

def download_from_youtube(url):
    try:
        with YoutubeDL(YDL_OPTIONS) as ydl:
            print(f"[+] Iniciando o download de: {url}")
            ydl.download([url])
            print("[✔] Download concluído.")
    except Exception as e:
        print(f"[!] Erro ao baixar {url}: {e}")

def main():
    print("Bem-vindo ao Downloader do YouTube")
    while True:
        print("\n[1] Baixar um único vídeo")
        print("[2] Baixar uma playlist")
        print("[3] Sair")
        choice = input("Escolha uma opção: ").strip()

        if choice == "1":
            video_url = input("Digite a URL do vídeo do YouTube: ").strip()
            YDL_OPTIONS['noplaylist'] = True  # Força a desativação de playlists
            download_from_youtube(video_url)

        elif choice == "2":
            playlist_url = input("Digite a URL da playlist do YouTube: ").strip()
            YDL_OPTIONS['noplaylist'] = False  # Ativa a opção de playlist
            download_from_youtube(playlist_url)

        elif choice == "3":
            print("Saindo do programa. Até mais!")
            break

        else:
            print("[!] Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()