def palindromekeylong(a):
    lista = []
    x = 0
    y = 0
    for i in range(len(a)):
        w = a[i::]
        for j in range(len(w)+1):
            x = w[:j]
            if x[::-1] == w[:j] and len( w[:j]) != 1  and len( w[:j]) != 0:
                lista.append(w[:j])
    if len(lista)==0:
        return "No hay palindromo"
    return sorted(lista, key=len)[-1]

print(palindromekeylong("anitalavalatina"))
print(palindromekeylong("jklabcbareaba"))
print(palindromekeylong("asdeemxhhebnosokjahwejzmiebsjebxg"))
print(palindromekeylong("hola"))
