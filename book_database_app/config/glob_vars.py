#De lengte van de ID's
LEN_ID = 10
#Pad naar books.db file vanaf root
PATH_DB_BOOK = r"./book_database_app/resources/databases/books.db"
#Pad naar books_back_up.db file vanaf root
PATH_DB_BOOK_BACK = r"./book_database_app/resources/backups/books_back_up.db"
#URL van de bibliotheek in Gent om een boek te zoeken. Voeg een zoekterm in na de URL om te zoeken(spatie=%20).
URL_GENTBIB = r'https://gent.bibliotheek.be/catalogus?q='
#Attributes van boek in volgorde van DB
ATTRIBUTES_BOEK = ['book_id','title','author','year','genre','description','language','pages','score','status','tags','date_gelezen']
#Aantal resultaten te verkrijgen van de gent_bib. Max 20.
AANTAL_RESULTS = 3