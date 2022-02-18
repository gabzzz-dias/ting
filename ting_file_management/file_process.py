from ting_file_management.queue import Queue
from ting_file_management.file_management import txt_importer
import sys


def process(path_file, instance):
    file = txt_importer(path_file)
    result = {
        "nome_do_arquivo": path_file,
        "qtd_linhas": len(file),
        "linhas_do_arquivo": file
    }

    if instance.__len__():
        for i in instance._data:
            repeated = i['nome_do_arquivo'] == path_file
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
process('statics/arquivo_teste.txt', queue)

remove(queue)
