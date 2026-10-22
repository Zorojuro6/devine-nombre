def deviner(secret, bas=1, haut=100):
    essais = 0
    while bas <= haut:
        milieu = (bas + haut) // 2
        essais += 1
        if milieu == secret:
            return essais
        elif milieu < secret:
            bas = milieu + 1
        else:
            haut = milieu - 1

def pire_cas(bas=1, haut=100):
    pire = 0
    for secret in range(bas, haut + 1):
        essais = deviner(secret, bas, haut)
        if essais > pire:
            pire = essais
    return pire

if __name__ == "__main__":
    print(deviner(92))
    print(pire_cas())