#De lengte van de ID's van de boeken
LEN_ID = 9
#Pad naar books.db file vanaf root
PATH_DB = r"./resources/databases/books.db"
#Pad naar books_back_up.db file vanaf root
PATH_DB_BACK = r"./resources/databases/books_back_up.db"
#URL van de bibliotheek in Gent om een boek te zoeken. Voeg een zoekterm in na de URL om te zoeken(spatie=%20).
URL_GENTBIB = r'https://gent.bibliotheek.be/catalogus?q='
#Attributes van boek in volgorde van DB
ATTRIBUTES_BOEK = ['book_id','title','author','year','genre','description','language','pages','score','status','tags','date_gelezen']
#Aantal resultaten te verkrijgen van de gent_bib. Max 20.
AANTAL_RESULTS = 3