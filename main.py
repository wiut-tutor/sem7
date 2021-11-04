eng2uz = dict()
eng2uz2 = {}
eng2uz['one'] = "bir"
print(eng2uz)
print(eng2uz2)
print(eng2uz['one'])
print(len(eng2uz))
print('one' in eng2uz)
print('bir' in eng2uz)
vals = eng2uz.values()
print(vals)
print('bir' in vals)

myFinalMarks = {'CSF': 75, 'FunPro': 80, 'WT': 85}


# Task 7
def calculateAverage(finalMarks):
    total = 0

    for key in finalMarks:
        total = total + finalMarks[key]
    average = total / len(finalMarks)
    return average


print(calculateAverage(myFinalMarks))


def histogram(s):
    d = dict()
    for c in s:
        if c not in d:
            d[c] = 1
        else:
            d[c] += 1
    return d


h = histogram('brontosaurus')
print(h)

print(h.get('z', 0))

# Task 8
csf = {
    'cw1-weight': 0.4,
    'cw1-mark': 79,
    'exam-weight': 0.6,
    'exam-mark': 65
}

print(csf.get('cw1-weight') * csf.get('cw1-mark') + csf.get('exam-weight') * csf.get('exam-mark'))


def print_hist(h):
    for c in h:
        print(c, h[c])


h = histogram('parrot')
print_hist(h)

def reverse_lookup(d, v):
    for k in d:
        if d[k] == v:
            return k
    raise LookupError()


h = histogram('parrot')

key = reverse_lookup(h, 1)
print(key)
