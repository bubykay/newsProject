from keywords import gen_keyword

with open('text.txt') as k:
    b=k.read()
    gen = gen_keyword(b)
    print(gen)