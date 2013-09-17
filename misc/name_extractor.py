import zgoogle

head = lambda x: x[0]
last = lambda x: x[-1]

def normalize_text(text):
    text = text.lower()
    text = text.replace('.', ' . ').replace(',', ' , ').replace('-', ' - ').replace('|', ' | ') # make tokenizer
    return text

def get_freq_dict(text):
    res = {}
    dels = [' ', '.', ',', '-', '|']
    for x in filter(lambda x: x not in dels, text.split()):
        if x not in res:
            res[x] = 0.0
        res[x] += 1
    return res

def filter_good_name(dct):
    lst = [(dct[x], x) for x in dct]
    lst.sort()
    lst.reverse()
    max = lst[0][0]
    max_length = 6
    return map(last, filter(lambda x: x[0] >= (max/2), lst[:max_length]))

if __name__ == '__main__':
    #data = zgoogle.google_it('4710937382310', 20)
    data = zgoogle.google_it('4605922006695', 20)
    text = reduce(lambda x, y: x + y, map(normalize_text, map(head, data)))

    dct = get_freq_dict(text)
    lst = [(dct[x], x) for x in dct]
    lst.sort()
    print lst
    for x in filter_good_name(dct): print x
