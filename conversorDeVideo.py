import os
import time
import sys
from pytube import YouTube

def baixar_video(link):
    try:
        yt = YouTube(link)
        print("Baixando vídeo:", yt.title)
        stream = yt.streams.get_highest_resolution()
        download_path = os.path.join(os.path.expanduser("~"), "Downloads")
        temp_video_filename = f'{yt.title}_temp_video.mp4'
        temp_video_path = os.path.join(download_path, temp_video_filename)
        video_path = os.path.join(download_path, f'{yt.title}.mp4')
        stream.download(output_path=download_path, filename=temp_video_filename)
        os.rename(temp_video_path, video_path)
        print("Download do vídeo concluído!\nO vídeo foi salvo em:", video_path,"\nCom o nome de:",yt.title)
    except Exception as e:
        print("Ocorreu um erro:", str(e))

def baixar_audio(link):
    try:
        yt = YouTube(link)
        print("Baixando áudio de:", yt.title)
        audio_stream = yt.streams.filter(only_audio=True).first()
        download_path = os.path.join(os.path.expanduser("~"), "Downloads")
        temp_audio_filename = f'{yt.title}_temp_audio.mp3'
        temp_audio_path = os.path.join(download_path, temp_audio_filename)
        audio_path = os.path.join(download_path, f'{yt.title}.mp3')
        audio_stream.download(output_path=download_path, filename=temp_audio_filename)
        os.rename(temp_audio_path, audio_path)
        print("Download do áudio concluído!\nO áudio foi salvo em:", audio_path,"\nCom o nome de:",yt.title)
    except Exception as e:
        print("Ocorreu um erro:", str(e))

print("Seja bem vindo ao 'baixador de vídeo', você quer baixar o vídeo em mp4(vídeo) ou mp3 (áudio) ?")
print("1- MP4")
print("2- MP3")
escolha = int(input("Selecione a opção:"))
if escolha == 1:
    if __name__ == "__main__":
        link = input("Insira o link do vídeo do YouTube: ")
        baixar_video(link)
else:
    if __name__ == "__main__":
        link = input("Insira o link do vídeo do YouTube: ")
        baixar_audio(link)
print("Finalizando ...")
time.sleep(4)
sys.exit()