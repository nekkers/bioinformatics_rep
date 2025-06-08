from json import *
from Bio import Align


def initailize(path1, path2):
    """
    Загружает данные из двух JSON-файлов.

    Параметры:
    path1 (str): Путь к первому JSON-файлу
    path2 (str): Путь ко второму JSON-файлу

    Возвращает:
    tuple: Кортеж из двух элементов:
        - gd (dict): Словарь из первого файла
        - md (dict): Словарь из второго файла
    """
    with open(path1, 'r') as js:
        gd = load(js)
    with open(path2, 'r') as js:
        md = load(js)
    return gd, md


def convert(gd, md):
    """
    Конвертирует словари в списки значений.

    Параметры:
    gd (dict): Входной словарь 1
    md (dict): Входной словарь 2

    Возвращает:
    tuple: Кортеж из двух элементов:
        - gl (list): Список значений из gd
        - ml (list): Список значений из md
    """
    gl, ml = [], []
    for k1, v1 in gd.items():
        gl.append(v1)
    for k2, v2 in md.items():
        ml.append(v2)
    return gl, ml


def align_two(s1, s2):
    """
    Выполняет попарное локальное выравнивание двух строк.

    Параметры:
    s1 (str): Первая биологическая последовательность
    s2 (str): Вторая биологическая последовательность

    Возвращает:
    Align.PairwiseAlignments: Объект с результатами выравнивания
    """
    aligner = Align.PairwiseAligner()
    aligner.mode = 'local'
    alignments = aligner.align(s1, s2)
    return alignments


def align_full(gl, ml):
    """
    Выполняет попарное выравнивание всех комбинаций строк из двух списков.

    Параметры:
    gl (list): Список первых последовательностей
    ml (list): Список вторых последовательностей

    Возвращает:
    list: Список строк и объектов выравнивания в формате:
        ['Aligned: строка1 и строка2', obj_align1, obj_align2, ...]
    """
    fl = []
    for g in gl:
        for m in ml:
            fl.append('Aligned: ' + g + ' and ' + m + "\n")
            als = align_two(g, m)
            for a in als:
                fl.append(a)
    return fl


def writing(expath, fl):
    """
    Записывает результаты выравнивания в текстовый файл.

    Параметры:
    expath (str): Путь к выходному файлу
    fl (list): Список с результатами выравнивания (строки и объекты)
    """
    f = open(expath, 'w')
    for el in fl:
        f.write(str(el))
    f.close()
