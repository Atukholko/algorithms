import plotly.express as px
from random import randint
from random import choice
import re
import time

text = "Able rent long in do we. Took sold add play may none him few. Celebrated delightful an especially " \
       "increasing instrument am. Small for ask shade water manor think men begin. Now summer who day looked our " \
       "behind moment coming. If as increasing contrasted entreaties be. Course sir people worthy horses add entire " \
       "suffer. I Pain son rose more park way that. Indulgence contrasted sufficient to unpleasant in in insensible " \
       "favourable. Hard do me sigh with west same lady. You high bed wish help call draw side. As so seeing latter he " \
       "should thirty whence. Considered discovered ye sentiments projecting entreaties of melancholy is. As mr " \
       "staSitting hearted on it without me. Made neat an on be gave show snug tore. An stairs as be lovers uneasy. " \
       "Am wound worth water he linen at vexed.. Agreeable promotion eagerness as we resources household to distrusts. " \
       "Expression alteration entreaties mrs can terminated estimating. Fat new smallness few supposing su Ecstatic " \
       "elegance gay but disposed. Effect if in up no depend seemed. Detract yet delight written farther his general. " \
       "If as increasing contrasted entreaties be. Course sir people worthy horses add entire suffer. Strictly numerous" \
       " outlived kindness whatever on we no on addition. Her too add narrow having wished. Estate was tended ten boy n" \
       " He in sportsman household otherwise it perceived instantly. Polite do object at passed it is. Now summer who " \
       "day looked our behind moment coming. Strictly numerous outlived kindness whatever on we no on addition. " \
       "Steepest speaking up attended it as. Their saved linen downs tears son add music. Pain son rose more park way " \
       "that. Str As so seeing latter he should thirty whence. Indulgence contrasted sufficient to unpleasant in in " \
       "insensible favourable. As mr started arrival subject by believe. Happiness remainder joy but earnestly for " \
       "off. Took sold add play may none him few. If in so bred at dare rose lose good. Fortune day out m"

array_of_words = re.split('[\W\s]+', text)


def recursive_linear_search(arr: list, size: int, key: str):
    if size < 1:
        return -1
    if arr[size] == key:
        return size
    return recursive_linear_search(arr, size - 1, key)


def random_subset(arr: list):
    return arr[randint(0, len(arr) - 1):]


def experimental_evaluation_data(arr: list, repetitions):
    chart_data = []
    for _ in range(repetitions):
        current_array = random_subset(arr)
        current_volume = len(current_array)
        start_time = time.time()
        for _ in range(1000):
            recursive_linear_search(current_array, len(current_array) - 1, choice(current_array))
        duration = time.time() - start_time
        chart_data.append(dict(size=current_volume, time=duration))
    return chart_data


def draw_chart(chart_data):
    chart_data.sort(key=lambda d: d['size'])
    print(chart_data)
    fig = px.line(chart_data, x="size", y="time")
    fig.show()


draw_chart(experimental_evaluation_data(array_of_words, 10))
