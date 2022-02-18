from ting_file_management.file_management import txt_importer
import sys


def process(path_file, instance):
    for i in range(len(instance.data)):
        if path_file == instance.search(i)["nome_do_arquivo"]:
            return None

    file = txt_importer(path_file)
    result = {
        "nome_do_arquivo": path_file,
        "qtd_linhas": len(file),
        "linhas_do_arquivo": file,
    }

    instance.enqueue(result)
    sys.stdout.write(str(result))


def remove(instance):
    """Aqui irá sua implementação"""


def file_metadata(instance, position):
    """Aqui irá sua implementação"""
