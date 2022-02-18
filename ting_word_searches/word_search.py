def search(word, arr):
    result = []
    for i, j in enumerate(arr):
        if word in j:
            result.append({'linha': i + 1})

    return result


def exists_word(word, instance):
    result = []

    for i in instance._data:
        file_lines = search(word, i['linhas_do_arquivo'])

        if len(file_lines):
            result.append({
                'palavra': word,
                'arquivo': i['nome_do_arquivo'],
                'ocorrencias': file_lines
            })

    return result


def search_by_word(word, instance):
    """Aqui irá sua implementação"""
