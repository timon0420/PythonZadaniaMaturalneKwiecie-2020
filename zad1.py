with open('zadanie maturalne kwiecień 2020\przyklad.txt', 'r') as f: txt = [x.rstrip() for x in f]
lst = [abs(int(txt[x])-int(txt[x+1])) for x in range(len(txt)-1)]
print(min(lst))
print(max(lst))
w = 0
q = []
for x in range(len(txt)-2):
    if abs(int(txt[x])-int(txt[x+1])) == abs(int(txt[x+1])-int(txt[x+2])):
        w += 1
    else:
        w = 0
    q.append(w)
print(q)
print(max(q)+2)