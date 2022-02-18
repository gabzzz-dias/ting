import sys


def txt_importer(path_file):
    if not path_file.endswith(".txt"):
        sys.stderr.write("Formato inválido\n")
        return

    try:
        with open(path_file, mode="rt") as file:
            readingFile = file.read()
            return readingFile.split("\n")

    except FileNotFoundError:
        return sys.stderr.write(f"Arquivo {path_file} não encontrado\n")
