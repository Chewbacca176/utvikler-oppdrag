

tekst = []


def HentTekst(filnavn):
    with open(filnavn, 'r') as fil:
        for linje in fil:

            tekst.append(linje)

def skriv_til_fil(filnavn):
    with open(filnavn, 'w') as txt_file:
        for line in tekst:
            txt_file.write(str(line) + '\n')

HentTekst('tekst.txt')
for line in tekst:
    print(line)





skriv_til_fil(tekst)