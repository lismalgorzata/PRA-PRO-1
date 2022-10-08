import json

book={"tytul":"Zatracenie",
      "autor":"Osamu Dazai",
      "kraj":"Japonia",
      "nurt":"dekadentyzm",
      "opinia":"bardzo lubie"
      }


with open('favourite.json','w') as file:
    json.dump(book, file,indent=4)
    #ident-formatuje tekst i daje nam wciecia itp fajne