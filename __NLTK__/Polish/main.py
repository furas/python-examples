text = '''tzn ja myslalem o czyms takim zeby zliczal tylko slowa ktore najczesciej sie powtarzaja
i ktore maja wiecej niz 4 litery
zeby nie zliczal mi spojnikow
i tak wlasnie sie zastanawialem czy jest cos takiego by ignorowal koncowki
zeby mial tolerancje
ze np jezeli sa takie same litery do ktoregos miejsca to by je liczyl jako jedno
np zeby liczyl samochod-y, samochod-em, samochod-ami
jako jedno samochod
chyba ze moze Ty masz jakis lepszy sposob na to co chce zrobic
bo chodzi o to ze jak od pracodawcy dostaje teksty to musze do nich znalezc zdjecia no i zdjecia szukam ze tak powiem przez slowa kluczowe
tylko ze robiac to recznie robie to tak ze np majac dziedzine motoryzacje to wiadomo kojarzy sie z tym samochod no i teraz wpisuje sobie w jednej rubryce np samochod jezeli tytul ma cos zwiazanego z tym, jezeli jest w tytule cos o pociagach to pisze sobie kolej itd itd
ale majac np 2tys tekstow troche sie z tym schodzi i myslalem o czyms co by pokazywalo najczesciej powtarzajace sie slowo
motoryzacja.xlsx
o tak to dostaje
tutaj jakas mala ilosc
i zeby w kolumnach C D i E wypisywal slowa
albo zrobic jakas beze i zeby samo wpisywalo slowa jezeli znajdzie dane slowo w tekscie
albo po prostu za bardzo juz kombinuje z tym wszystkim'''

# stopwords -> ~/nltk_data/corpora/stopwords/polish
# https://raw.githubusercontent.com/bieli/stopwords/master/polish.stopwords.txt
# https://www.ranks.nl/stopwords/polish

# corpus
# http://nkjp.pl/
# http://clip.ipipan.waw.pl/NationalCorpusOfPolish
# http://sgjp.pl/morfeusz/

# http://programowalnasiec.blogspot.com/2012/11/analiza-tekstow-w-jezyku-polskim.html
# http://plwordnet.pwr.wroc.pl/wordnet/
# https://github.com/morfologik/morfologik-stemming/tree/master/morfologik-polish/src/main/resources/morfologik/stemming/polish

import nltk
from nltk.corpus import stopwords

nltk.download('punkt')
nltk.download('pl196x')
nltk.download('wordnet')

words = nltk.word_tokenize(text)
print(len(words))

stops = set(nltk.corpus.stopwords.words('polish'))

words = [word for word in words if word not in stops]
print(len(words))

import nltk.stem

s = nltk.stem.WordNetLemmatizer()
for word in words:
    print(s.lemmatize(word))

for word in ['samochód', 'samochody', 'samochodowy']:
    print(s.lemmatize(word))

#nltk.corpus.reader.Pl196xCorpusReader(root='/home/furas/nltk_data/corpora/pl196x', fileids='textids.txt')
r = nltk.corpus.reader.NKJPCorpusReader(root='/home/furas/Pulpit/NKJP-PodkorpusMilionowy-1.0/')
#print(len(r.words()))

