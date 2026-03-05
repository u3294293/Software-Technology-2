def list_count(l):
    output = []
    seen = set()

    for n in l:
        if n not in seen:
            seen.add(n)
            n_count = l.count(n)
            output.append((n, n_count))

    return output

l = [1, 2, 2, 3, 4, 4, 5, 1]

set = set()

def test():
    p = []
    for i in l:
        if i not in set:
            set.add(i)
            p_count = l.count(i)
            p.append((i, p_count))
    return p

print(test())