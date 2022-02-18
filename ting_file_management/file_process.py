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
    if not instance.__len__():
        sys.stdout.write('Não há elementos\n')

    deleted = instance.dequeue()['nome_do_arquivo']
    sys.stdout.write(f"Arquivo {deleted} removido com sucesso\n")


def file_metadata(instance, position):
    """Aqui irá sua implementação"""
