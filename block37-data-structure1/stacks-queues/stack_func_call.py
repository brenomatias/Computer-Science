# a linguagem(python) mantém uma pilha com quais funções devem ser executadas após a execução de uma função.

def load_video(video_path):
    print('Carregando vídeo do caminho:', video_path)
    return 'fake vídeo'

def process_video(video_path):
    print('Carregando vídeo...')
    loaded_video = load_video(video_path)
    # Faz alguma coisa legal com o vídeo




# Se adicionarmos a função traceback.print_stack(file=sys.stdout) conseguimos ver quais os itens presentes na call stack do Python

import traceback
import sys


def load_video(video_path):
    print('Carregando vídeo do caminho:', video_path)
    traceback.print_stack(file=sys.stdout)
    return 'fake vídeo'

def process_video(video_path):
    print('Carregando vídeo...')
    loaded_video = load_video(video_path)
    # Faz alguma coisa legal com o vídeo


process_video('path/to/my/video')