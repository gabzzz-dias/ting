def search(word, arr):
    res = []
    for i, j in enumerate(arr):
        if word in j:
            res.append({'linha': i + 1})

    return res


    def search_cont(word, arr):
        res = []
        for i, j in enumerate(arr):
            x = re.findall(word, j, re.IGNORECASE)
            if len(x):
                res.append({'linha': i + 1, "conteudo": j})

        return res


def exists_word(word, instance):
    result = []

    for i in instance.data:
        file_lines = search(word, i['linhas_do_arquivo'])

        if len(file_lines):
            result.append({
                'palavra': word,
                'arquivo': i['nome_do_arquivo'],
                'ocorrencias': file_lines
            })

    return result


def search_by_word(word, instance):
    arr = []
    for i in instance.data:
        file_lines = search_cont(word, i['linhas_do_arquivo'])
        if len(file_lines):
            arr.append({
                'palavra': word,
                'arquivo': i['nome_do_arquivo'],
                'ocorrencias': file_lines
            })

    return arr
