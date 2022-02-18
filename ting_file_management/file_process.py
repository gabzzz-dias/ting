from ting_file_management.queue import Queue
from ting_file_management.file_management import txt_importer
import sys


def search(path_file, instance):
    if instance.__len__():
        for i in instance._data:
            return i['nome_do_arquivo'] == path_file
    else:
        return False


def process(path_file, instance):
    process_file = txt_importer(path_file)
    result = {
        "nome_do_arquivo": path_file,
        "qtd_linhas": len(process_file),
        "linhas_do_arquivo": process_file
    }
    repeated = search(path_file, instance)

    if repeated is False:
        instance.enqueue(result)

    sys.stdout.write(f'{result}\n')


def remove(instance):
    """Aqui irá sua implementação"""


def file_metadata(instance, position):
    """Aqui irá sua implementação"""


queue = Queue()
process('statics/arquivo_teste.txt', queue)
process('statics/arquivo_teste.txt', queue)

remove(queue)
