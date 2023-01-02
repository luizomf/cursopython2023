# ZIP - Compactando / Descompactando arquivos com zipfile.ZipFile
import os
import shutil
from pathlib import Path
from zipfile import ZipFile

# Caminhos
CAMINHO_RAIZ = Path(__file__).parent
CAMINHO_ZIP_DIR = CAMINHO_RAIZ / 'aula_186_diretorio_zip'
CAMINHO_COMPACTADO = CAMINHO_RAIZ / 'aula186_compactado.zip'
CAMINHO_DESCOMPACTADO = CAMINHO_RAIZ / 'aula186_descompactado'

shutil.rmtree(CAMINHO_ZIP_DIR, ignore_errors=True)
Path.unlink(CAMINHO_COMPACTADO, missing_ok=True)
shutil.rmtree(str(CAMINHO_COMPACTADO).replace('.zip', ''), ignore_errors=True)
shutil.rmtree(CAMINHO_DESCOMPACTADO, ignore_errors=True)

# raise Exception()

# Cria o diretório para a aula
CAMINHO_ZIP_DIR.mkdir(exist_ok=True)


def criar_arquivos(qtd: int, zip_dir: Path):
    for i in range(qtd):
        texto = 'arquivo_%s' % i
        with open(zip_dir / f'{texto}.txt', 'w') as arquivo:
            arquivo.write(texto)


criar_arquivos(10, CAMINHO_ZIP_DIR)

# Criando um zip e adicionando arquivos
with ZipFile(CAMINHO_COMPACTADO, 'w') as zip:
    for root, dirs, files in os.walk(CAMINHO_ZIP_DIR):
        for file in files:
            # print(file)
            zip.write(os.path.join(root, file), file)

# Lendo arquivos de um zip
with ZipFile(CAMINHO_COMPACTADO, 'r') as zip:
    for arquivo in zip.namelist():
        print(arquivo)

# Extraindo arquivos de um zip
with ZipFile(CAMINHO_COMPACTADO, 'r') as zip:
    zip.extractall(CAMINHO_DESCOMPACTADO)
