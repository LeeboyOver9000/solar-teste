import os
from urllib.request import urlretrieve


def mkdir(path: str = os.getcwd(), directory_name: str = 'downloads') -> str:
    """Verifica se a pasta existe, caso não exista, cria uma nova pasta no caminho que foi especificado.

    Arguments:
        path (str) -- Caminho da pasta -- Defaults: Raíz do projeto atual
        directory_name (str) -- Nome da pasta -- Defaults: downloads

    Returns:
        str -- Caminho da pasta
    """
    path = f'{path}/{directory_name}'
    if not os.path.isdir(path):
        os.mkdir(path)
    return path


def download(url: str, output: str, filename: str):
    """Faz o download do arquivo que foi passado pela url.

    Arguments:
        url (str) -- URL para download
        output (str) -- Caminho do download
        filename (str) -- Nome do arquivo
    """
    urlretrieve(url, f'{output}/{filename}')
