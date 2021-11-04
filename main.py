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


csf = {
    'cw1-weight': 0.4,
    'cw1-mark': 79,
    'exam-weight': 0.6,
    'exam-mark': 65
}
print("Your nark for CSF:", csf.get('cw1-weight') * csf.get('cw1-mark') + csf.get('exam-weight') * csf.get('exam-mark'))

def calculate_mark(csf):
    return ("Your nark for CSF:", csf.get('cw1-weight') * csf.get('cw1-mark') + csf.get('exam-weight') * csf.get('exam-mark'))


def get_input():
    cw_weight = float(input("enter cw1 weight: "))
    cw_mark = int(input("enter mark mark: "))
    exam_weight = float(input("enter exam weight: "))
    exam_mark = int(input("enter exam mark: "))
    csf = {
        'cw1-weight': cw_weight,
        'cw1-mark': cw_mark,
        'exam-weight': exam_weight,
        'exam-mark': exam_mark
    }
    return csf


print(calculate_mark(get_input()))

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
