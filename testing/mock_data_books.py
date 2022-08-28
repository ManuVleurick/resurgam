from domain.book import Book
title,author,year,genre,description,language,ISBN,pages,score,status = 'Nieuwe dinges','Mr. Bruh',2018,'Horror','Een langedescription lksdmfqfs+9546','Engels','169-50-522545-05',206,7.52,'Read'
review_score,review,bib_place,tags,date_gelezen = 4.58,'Goeie booek','1de 25.5 bruh','Horror Poezie','1992-12-26'
book = Book(title=title,author=author,year=year,genre=genre,description=description,language=language,ISBN=ISBN,pages=pages,score=score,status=status,review_score=review_score,review=review,bib_place=bib_place,tags=tags,date_gelezen=date_gelezen)