
from random import randrange

seznam_vet =["Pohádky a psi mají jedno společné, jsou to věrní přátelé lidí a dělají jim radost.","Oblíbená autorka Zuzana Pospíšilová proto pro všechny milovníky psů a pohádkového čtení napsala dvacet původních pohádek o pejscích ras ušlechtilých i zcela neznámých.","V téhle knížce vyvádějí psi neuvěřitelné kousky.","Fenka Sisi zpívá, z pejska Fleka se stane malíř a kokršpaněl Bady se chce učit španělsky.","Nechte se poučit psí moudrostí, pobavit psí radostí a užijte si veselé ilustrace Michala Sušiny.","Haf!"]

rozpeti = seznam_vet[randrange(0,len(seznam_vet))]

samohlasky = ["a","á","e","é","i","í","o","ó","u","ú"]

souhlasky = ["b", "c", "č", "d", "ď", "f", "g", "h", "j", "k", "l", "m", "n", "ň", "p", "r", "ř", "s", "š", "t", "ť", "v", "z", "ž", "ch"]

print(f">>>{rozpeti}<<<\n")

pocet_samohlasek = 0
pocet_souhlasek = 0 
pocet_ostatnich = 0
pocet_slov = 1

for pismeno in rozpeti.lower():
  if pismeno in samohlasky:
    pocet_samohlasek +=1
  elif pismeno in souhlasky:
    pocet_souhlasek +=1
  elif pismeno.endswith(" "):
    pocet_slov +=1
  else: 
    pocet_ostatnich +=1
print(f"Pocet samohlasek ve vete je: {pocet_samohlasek}\nPocet souhlasek ve vete je: {pocet_souhlasek}\nPocet ostatnich znaku ve vete je: {pocet_ostatnich}\nPocet vsech vsech znaku ve vete je: {pocet_samohlasek + pocet_souhlasek + pocet_ostatnich}\nPocet slov ve vete je: {pocet_slov}")
