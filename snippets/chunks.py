import pprint

pp = pprint.PrettyPrinter(indent=2)

def chunks(lst: list, size: int):
    return [lst[i:i + size] for i in range(0, len(lst), size)]

def gen_chunks(lst: list, size: int):
    for i in range(0, len(lst), size):
        yield lst[i:i + size]

l = [i for i in range(25)]

print("Split into chunks in one go!")
pp.pprint(chunks(l, 10))

print("Loop through each generated chunk!")
for chunk in gen_chunks(l, 10):
    pp.pprint(chunk)
