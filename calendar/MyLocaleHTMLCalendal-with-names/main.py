#!/usr/bin/env python3

#
# DATY IMIENIN: http://www.sawicki.cc/DATY%20IMIENIN.htm
#
# w danych nie zaznaczyłem dat które występują w kalendarzach z trzema imionami
# widać to w PDF: http://www.sawicki.cc/Spis%20Imion.pdf
#
# http://www.kalbi.pl/kalendarz-imienin
# http://www.kalbi.pl/kalendarz-2017
#

data = '''Achacego 8 V, Achillesa 12 V, Adalberta 23 IV, Adama 24 XII, Adelajdy 5 II, Adeli 23 XI, Adeliny 28 VIII, Adolfa 19 IV, 17 VI, Adriana 5 III, Adrianny 5 III, 8 IX, Ady 12 XII, Agapita 18 VIII, Agatona 10 I, Agaty 5 II, Agenora 22 VI, Agnieszki 21 I, 20 IV, Agrypiny 23 VI, 6 VII, Aidy 28 VII, Aiszy 11 IX, Alana 14 X, Alberta 15 XI, Albina 1 III, 15 IX, Albiny 16 XII, Albrechta 25 VI, Aldony 11 X,  Alego 14 X, Aleksandra 26 II, 12 XII, Aleksandry 18 V, Aleksego 17 VII, Alfonsa 1 VIII, 2 VIII, Alfreda 14 VIII, 14 XII, Alfredy 19 VII, Alicji 21 VI, Aliny 16 VI, Almy 10 VII, Alojzego 21 VI, Amadei 10 VIII, Amadeusza 27 IX, Amalii 20 IV, Amandy 18 VI, Amaty 5 I, Ambrożego 7 XII, Amelii 30 III, Amina 2 VI, Anastazego 22 I, Anastazji 27 II, 15 IV, Anatola 3 VII, 20 XI, Anatolii 9 XI, Androna 16 X, Andrzeja 4 II, 16 V, 21 VII, 30 XI, Anety 16 VI, 17 VII, Angela 6 II, Angeli 27 I, Angeliki 4 I, Angeliny 29 IV, Anicety 17 IV, Anieli 4 I, 28 III, 31 V, Anity 26 VII, 17 VIII, Anny 26 VII, Antoniego 17 I, 13 VI, 5 VII, 7 XI, Antonina 10 V, Antoniny 1 III, 3 V, Anzelma 21 IV, Apolinarego 23 VII, 23 VIII, Apolla 9 III, Apolonii 9 II, Apoloniusza 18 IV, Arety 24 X, Ariadny 7 VI, Ariela 16 IX, Arkadiusza 12 I, Arletty 3 I, 13 II, Arnolda 15 I, 19 II, 9 X, Arona 2 IV, 13 V, Artura 6 X, Aspazji 29 XII, Atanazego 2 V, Atanazji 14 VIII, Augusta 7 V, 3 VIII, Augustyna 28 V, 28 VIII, Augustyny 9 IX, Aurelego 27 VII, Aureliana 4 VII, Aurelii 25 IX, 2 XII, Aureliusza 27 VII, 13 IX, Aurory 15 X, Axela 2 IX

Balbina 21 XII, Balbiny 31 III, 2 XII, Baltazara 6 I, Barabasza 11 VI, Barbary 4 XII, Barnaby 11 VI, Bartłomieja 24 VIII, 11 XI, Bartolomei 26 VII, Bartosza 21 IV, 24 VIII, Bazylego 2 I, 20 V, 14 VI, Beatrycze 29 VII, Beatusa 31 VII, Beaty 8 III, 6 IX, Beginy 9 V, Benedykta 21 III, 11 VII, Benedykty 6 V, Beniamina 31 III, Benity 16 VII, Benona 16 VI, Bereniki 14 IV, 20 IV, Bernadetty 16 IV, Bernarda 12 III, 20 VIII, 14 IX, Bernadety 18 II, Bernardyna 20 V, Bernardyny 14 IV, Berny 4 XII, Bertolda 29 III, Bertranda 9 VI, Berty 15 V, Bibianny 2 XII, Biruty 5 II, Bjorna 18 VI, Blanki 1 XII, Błażeja 3 II, 29 XI, Bogdana 19 III, 17 VII, Bogdany 6 II, Bogny 20 VI, 23 VIII, Bogumiła 10 VI, Bogumiły 13 I, 20 XII, Bogusława 22 III, 23 IX, 18 XII, Bogusławy 18 IV, Bogusza 24 II, Bohdana 6 II, 31 VIII, Bohdany 2 XI, Bolesława 19 VIII, Bolesławy 22 VII, Bonawentury 14 VII, 15 VII, Bonifacego 14 V, 5 VI, Borysa 10 VIII, Borysława 25 V, Borzysława 19 VI, Borzysławy 2 VIII, Bożeny 13 III, Bożydara 9 V, Bożymierza 9 I, Bratumiła 8 IX, Bratumiły 4 XII, Brodzisława 1 VIII, Bronimira 20 V, Bronisława 18 VIII, Bronisławy 1 IX, Bruna 17 V, Brunona 6 X, Brygidy 1 II, 23 VII, 8 X, Budzisława 3 III, Budzisławy 10 X

Cecyla 16 IV, Cecyliana 16 IV, Cecylii 22 XI, Cecyliusza 16 IV, Celestyna 6 IV, 27 VII, Celestyny 6 IV, Celiny 15 XII, Cezara 25 IX, Cezarego 25 II, 22 VIII, Cezariusza 27 VIII, Cezaryny 8 IV, Chrystiana 4 XII, Chwalimira 8 VII, Chwalisława 3 XI, Chwalisławy 30 IV, Ciechosława 13 V, Cieszymira 24 VIII, Cypriana 10 III, 16 IX, 26 IX, Cyriaka 8 VIII, Cyrusa 31 I, Cyryla 14 II, 18 III, Czcibora 12 XI, Czcisława 19 II, Czesława 20 IV, 20 VII, Czesławy 12 I

Dagmary 12 XII, Dagny 11 IX, Dalidy 21 VII, Dalii 29 X, Damazego 11 XII, Damiana 23 II, 26 IX, 27 IX, Daniela 21 VII, 10 X, Danieli 10 XII, Danuty 3 I, 16 II, 24 VI, 1 X, Darii 25 X, Dariusza 19 XII, Dawida 26 VI, 29 XII, Delfina 9 XII, Delfiny 26 XI, Demetrii 21 VI, Demetriusza 8 X, Dezyderego 11 II, Dezyderii 8 V, Dezyderiusza 23 V, Diany 13 VIII, Diny 20 VI, Diogenesa 6 IV, Diomedy 11 VIII, Dionizego 8 IV, 9 X, 26 XII, Dionizji 2 X, Ditty 6 V, Dobiegniewa 30 I, Dobiesława 14 V, Dobiesławy 14 II, Dobrawy 15 I, Dobrochny 1 II, Dobrogosta 14 VII, Dobromierza 31 III, Dobromiła 21 X, Dobromiły 11 X, Dobromira 5 VI, Dobrosława 10 I, Dobrosławy 9 IV, Dolores 15 IX, Domarada 16 VIII, Domiceli 12 V, Domicjana 12 V, Dominika 4 VIII, 8 VIII, 20 XII, Dominiki 6 VII, Domisławy 7 IX, Domosława 15 I, Donalda 15 VII, Donata 17 II, 7 IV, 22 X, Donaty 7 VIII, Doriana 22 I, Doris 7 VIII, Doroty 6 II, 5 IX, Dragomira 9 XI, Duszana 26 III, Dymitra 9 IV, Dymitriusza 26 X, Dyzmy 25 III, Dzierżykraja 17 VII, Dzierżysława 16 VII, Dzierżysławy 24 III

Edgara 8 VII, Edmunda 16 XI, 20 XI, Edwarda 18 III, 13 X, Edwina 4 X, Edyty 16 IX, Egberta 24 IV, Egona 15 VII, Eleonory 21 II, Eliasza 20 VII, Eligiusza 1 XII, Elizy 14 VI, Elwiry 10 II, Elżbiety 18 VI, 4 VII, 8 VII, 5 XI, 17 XI, 19 XI, Emanuela 26 III, Emila 11 X, Emiliana 8 VIII, Emiliany 5 I, 30 VI, Emilii 30 VI, 24 VIII, Emiliusza 14 XI, Emmy 24 XI, Epifaniego 21 I, Epifaniusza 12 V, Erazma 2 VI, 25 XI, Erazmy 3 IX, Erharda 8 I, Ernesta 27 III, 13 VII, Ernesty 31 VII, Erwina 18 VII, Erwiny 25 IV, Eryka 18 V, Eryki 9 II, Estery 24 V, 7 VII, Eudoksji 1 III, Eudoksjusza 2 XI, Eufemii 20 III, Euforyzmy 3 IX, Eugenii 7 II, 13 IX, Eugeniusza 4 I, 6 IX, 30 XII, Eulalii 12 II, Eustachego 29 III, 16 VII, 20 IX, 12 X, Euzebii 29 X, Euzebiusza 5 III, 14 VIII, Ewalda 7 VII, 3 X, Ewarysta 26 X, Eweliny 26 V, 24 XII, Ewy 24 XII

Fabiana 20 I, Fabioli 27 XII, Fausta 16 VII, Faustyna 15 II, Faustyny 20 IX, Felicjana 9 VI, 29 X, Felicji 24 I, 27 IV, Felicysma 6 VIII, Felicyty 7 III, 23 XI, Feliksa 14 I, 30 V, 6 XI, Ferdynanda 30 V, Fidelisa 24 IV, Filemona 21 III, Filipa 11 IV, 1 V, 26 V, 23 VIII, Filipiny 20 IX, Filomeny 10 VIII, Flawiana 18 II, 22 XII, Flawii 5 X, Flawiusza 22 VI, Florencjusza 27 X, Florentego 7 XI, Florentyna 23 II, Florentyny 20 VI, 16 X, Floriana 4 V, Flory 24 XI, Floryna 17 XI, Fortunata 21 II, Fortunaty 15 XII, Franciszka 24 I, 29 I, 2 IV, 4 VI, 17 IX, 4 X, 10 X, 3 XII, Franciszki 9 III, Fryderyka 5 III, 29 XI, Fryderyki 6 X, Frydy 19 X

Gabora 24 III, Gabriela 27 II, 24 III, 29 IX, Gabrieli 19 XII, Gajusza 22 IV, Galla 16 X, Gandy 30 VIII, Gardenii 10 V, Gaspara 25 IX, Gaudencji 30 VIII, Gaudentego 22 I, Gawła 16 X, Gedeona 28 III, Genowefy 3 I, Georginy 15 II, Geralda 13 X, Gerarda 24 IX, Germana 28 V, Gertrudy 16 XI, Gerwazego 19 VI, Gilberta 4 II, Gildy 19 I, Gizeli 7 V, Glikerii 22 X, Glorii 13 V, Gniewomira 8 II, Godfryda 8 XI, Godzimierza 31 X, Godzimira 31 X, Godzisława 28 XII, Gorzysława 9 II, Gosława 29 XII, Gościmiła 4 VI, Gościmira 15 III, Gościrada 28 XI, Gościsława 18 IV, Gotarda 6 VII, Gotfryda 8 XI, Gracjana 18 XII, Gracjany 1 VI, Gracji 13 VI, Grażyny 1 IV, 26 VII, Grety 12 I, Gryzeldy 22 XII, Grzegorza 13 II, 12 III, 9 V, 25 V, 3 IX, 17 XI, Grzymisława 12 X, Gustawa 2 VIII, Gustawy 7 V, Gwalberta 12 VII, Gwido 31 III, 12 IX, Gwidona 12 IX

Hadriana 5 III, 8 XI, Haliny 1 VII, Halki 22 X, Halszki 2 III, Hanny 5 I, 26 VII, Heleny 2 III, 22 V, Heliodora 3 VII, 3 X, Helmuta 29 III, Henryka 19 I, 13 VII, 15 VII, Henryki 2 III, 16 III, Herakliusza 17 IV, Herberta 16 III, Herkulana 25 IX, Herkulesa 5 IX, Hermana 7 IV, 24 IX, Hermenegilda 13 IV, Hermenegildy 13 IV, Hermesa 31 XII, Herminii 24 XII, Hiacynty 30 I, Hieronima 20 VII, 30 IX, Hilarego 14 I, 16 III, 21 X, Hilarii 12 VIII, Hildegardy 17 IX, Hipolita 3 II, 13 VIII, Honoraty 11 I, 22 XII, Honoriusza 30 IX, Honoryny 27 II, Horacego 24 IV, Horacjusza 24 IV, Hortensji 1 VI, Hortensjusza 1 VI, Huberta 3 XI, Hugo 1 IV, Hugona 1 IV, Humberta 13 IX

Idalii 15 XI, Idy 4 IX, Idziego 1 IX, Ifigenii 21 IX, Igi 11 V, Ignacego 1 II, 31 VII, Ignacji 23 X, Igora 5 X, Ildefonsa 23 I, Ilii 2 VII, Ilony 18 VIII, Ilzy 8 V, Inez 21 I, Ingeborgi 25 X, Ingi 25 X, Ingridy 6 VI, Innocentego 28 VII, Ireneusza 28 VI, Ireny 5 IV, 5 V, 20 X, Iriny 18 V, Irminy 24 XII, 30 XII, Irmy 18 IX, Irwina 13 VII, Irydiona 21 IV, Irydy 5 V, Isaury 17 VI, Ismeny 29 I, Ity 6 V, Iwa 19 V, Iwana 12 IV, 27 XII, Iwetty 29 VI, Iwony 23 V, 27 X, Iwy 1 XII, Izaaka 19 X, 12 XI, Izabeli 16 III, 3 IX, Izoldy 6 IV, Izydora 2 I, 4 IV, 10 V, 14 XII

Jacentego 10 II, Jacka 3 VII, 17 VIII, 11 IX, Jacława 15 VIII, Jadwigi 17 VII, 15 X, 16 X, Jagody 2 VII, Jakobiny 24 VII, 16 IX, Jakuba 1 VI, 25 VII, 6 VIII, Jana 31 I, 27 V, 24 VI, 26 VI, 12 VII, 29 VIII, 20 X, 27 XII, Janiny 12 VI, Janisława 24 VI, Januarego 19 IX, Janusza 21 XI, Jaremy 6 XII, Jarmiły 14 III, Jarogniewa 6 XII, Jaromira 28 V, Jarosława 25 IV, Jarosławy 21 I, Jaśminy 24 II, Jeremiasza 1 V, Jeremiego 1 V, Jerzego 23 IV, 24 IV, 24 VIII, Jędrzeja 16 V, Joachima 26 VII, 16 VIII, Joanny 24 V, 30 V, 21 VIII, 12 XII, Jolanty 15 VI, Jonasza 21 IX, Jordana 6 III, Jowity 15 II, Józefa 19 III, 1 V, 25 VIII, 27 VIII, 18 IX, Józefata 12 XI, Józefiny 12 III, Józefy 3 X, Judyty 6 V, Juliana 7 I, 19 VIII, 2 IX, 18 X, Julianny 16 II, Julietty 17 VII, Julii 16 IV, 22 V, 10 XII, Julity 30 VII, Juliusza 12 IV, 27 V, Juranda 6 V, Juraty 12 IV, Justyna 1 VI, 1 VIII, Justyniana 5 II, Justyny 16 VI, 26 IX

Kacpra 6 I, Kai 22 IV, Kajetana 7 VIII, Kalasantego 27 VIII, Kaliksta 14 X, Kaliny 11 VII, Kamelii 3 VIII, Kamila 14 VII, 18 VII, Kamili 16 IX, Kandyda 11 III, Kareny 9 V, Kariny 2 VIII, Karola 4 VI, 4 XI, Karolina 5 VIII, Karoliny 5 VII, Kasjana 13 VIII, Kaspra 6 I, Katarzyny 13 II, 9 III, 22 III, 24 III, 29 IV, 30 IV, 25 XI, Kazimiery 21 VIII, Kazimierza 4 III, Kiejstuta 21 II, Kingi 24 VII, Kiry 20 III, Kiryła 22 VI, Klary 11 VIII, 12 VIII, Klarysy 1 VII, 12 VIII, Klaudiana 6 III, Klaudii 20 III, Klaudiusza 26 IV, 7 VII, Klaudyny 18 XI, Klemencji 21 X, Klemensa 15 III, 23 XI, Klementa 8 XII, Klementyna 23 XI, Klementyny 8 IX, Kleofasa 25 IX, Kleopatry 20 X, Klotyldy 3 VI, Kolety 6 III, Kolombiny 10 I, Kondrata 23 III, Konrada 19 II, 21 XI, 26 XI, Konradyna 2 XI, Konstancji 19 IX, Konstancjusza 18 II, Konstantego 11 III, Konstantyna 29 VII, Kordiana 22 X, Korduli 22 X, Kornela 16 IX, Kornelego 31 III, Kornelii 31 III, 6 IV, Korneliusza 16 IX, Kosmy 26 IX, 27 IX, Kryspina 21 V, 25 X, Kryspiny 5 XII, Krystiana 4 XII, Krystiany 15 XII, Krystyna 13 XI, Krystyny 13 III, 24 VII, Krzesimira 11 I, Krzesisława 28 III, Krzysztofa 25 VII, Ksawerego 3 XII, Ksawery 22 XII, Ksaweryny 22 XII, Kseni 16 IV, Kunegundy 3 III, Kwiatosławy 8 XII, Kwiryna 30 III, Kwiryny 4 VI

Lamberta 17 IX, Larysy 26 III, Laurencji 18 XII, Laurencjusza 3 VI, Laurentego 6 VI, Laurentyny 3 VI, Laury 17 VI, Lecha 12 VIII, Lechosława 26 XI, Lechosławy 26 XI, Ledy 5 II, Lenarta 6 XI, Leny 10 XI, Leokadii 9 XII, Leona 20 II, 14 III, 11 IV, 28 VI, Leonarda 6 XI, Leonardy 27 XI, Leoncjusza 19 II, Leonida 15 IV, 22 IV, Leonidy 15 VI, Leonii 22 IV, Leontyny 19 IV, 6 XII, Leony 15 VI, Leoparda 30 IX, Leopolda 15 XI, Lesława 28 XI, Lesławy 28 XI, Leszka 3 VI, Liberata 23 XI, Lidii 27 III, 3 VIII, Ligii 11 VIII, Lili 14 II, Liliany 14 II, Lilianny 4 IX, Lilli 27 VII, Lindy 13 II, Liwii 14 X, Liwiusza 23 IX, Lizy 8 V, Lolity 15 IX, Longina 15 III, Loretty 10 XII, Lubomierza 21 III, Lubomira 21 III, Lubomiry 21 III, Lubora 13 IX, Lubosława 12 IV, Luby 28 IX, Lucjana 7 I, 13 VI, Lucji 4 III, 13 XII, Lucjoli 3 III, Lucjusza 11 II, Lucylii 31 X, Lucyny 30 VI, Ludgarda 16 VI, Ludmiły 7 V, 30 VII, 16 IX, Ludomiła 20 II, Ludomiły 7 V, Ludomira 10 XI, Ludomiry 31 VII, Ludosława 11 III, Ludwika 25 VIII, Ludwiki 31 I, 15 III, Ludwiny 15 IV, Luizy 25 VIII, Lukrecji 9 VII, Lutogniewa 11 V,  Lutomira 28 II, Lutosława 29 II, Lwa 13 I

Ładysława 25 IX, Łazarza 17 XII, Łucjana 26 X, Łucji 4 III, 25 VI, 13 XII, Łukasza 22 IV, 10 IX, 18 X

Macieja 30 I, 24 II, 14 V, Madleny 25 V, Magdaleny 29 V, 22 VII, Magdy 25 V, Mai 9 IV, Makarego 2 I, 28 II, 10 III, 10 IV, Maksyma 8 VI, 13 VIII, Maksymiliana 14 VIII, 12 X, Maksymina 29 V, Maliny 24 VIII, Malkolma 28 III, Malwina 4 VII, 1 X, Malwiny 4 VII, Małgorzaty 18 I, 22 II, 10 VI, 16 X, 16 XI, Mamerta 11 V, Manfreda 4 X, Mansweta 19 II, Marcela 16 I, 10 III, Marcelego 16 I, 10 III, Marceli 31 I, 28 VII, Marcelina 26 IV, 14 VII, Marceliny 9 I, Marcina 24 X, 11 XI, 7 XII, Marcjala 30 VI, Marcjana 17 VI, Marcjanny 9 I, Margarety 13 VII, Mariana 30 IV, 1 VII, Marianny 2 VI, 12 IX, Marietty 31 V, Marii 1 I, 2 II, 11 II, 24 III, 3 V, 16 VII, 22 VII, 15 VIII, 26 VIII, 8 IX, 12 IX, 7 X, 16 XI, 8 XII, Mariki 16 VII, Mariny 18 VI, Marioli 25 III, Marity 17 X, Mariusza 19 I, Marka 24 III, 25 IV, 18 VI, 7 X, 22 XI, Marleny 16 VI, 23 X, Marty 22 II, 29 VII, Martyniana 2 VII, Martyny 30 I, Maryli 27 VI, Maryny 3 III, Marzanny 2 VI, Marzeny 26 IV, Mateusza 21 IX, Matyldy 11 I, 14 III, Maura 15 I, 22 XI, Maury 30 XI, Maurycego 22 IX, Mauryna 10 VI, Medarda 8 VI, Melanii 31 XII, Melchiora 6 I, 7 IX, Metodego 14 II, Metody 7 VII, Michaliny 29 IX, Michała 10 IV, 29 IX, Mieczysława 1 I, Mieszka 1 I, Mikołaja 10 IX, 13 XI, 6 XII, Milenii 22 VII, Mileny 24 I, 24 V, Miłosława 2 II, Miłosza 25 I, Mirabelii 27 IX, Mirandy 11 V, Mirelli 7 X, Miromira 26 VI, Mirona 17 VIII, Mirosława 26 II, Mirosławy 26 II, 26 VII, Miry 11 V, Modesta 12 II, Modesty 5 IX, Moniki 4 V, 27 VIII, Mścibora 10 IX, Mścisława 8 I, Mścisławy 9 III, Mściwoja 4 XI, Myślibora 18 V

Nadii 1 VIII, Nadziei 15 V, Namysława 25 VIII, Napoleona 15 VIII, Narcyza 18 III, 29 X, Narcyzy 18 III, Natalii 27 VII, 1 XII, Nataszy 9 XII, Neli 10 XI, Nestora 8 IX, Niemira 14 II, Nikifora 9 II, Nikity 10 VI, Nikodema 15 IX,  Nikoli 19 V, Nimfy 10 XI, Niny 15 XII, Noego 24 XII, Nony 5 VIII, Norberta 6 VI, Normana 6 I, Nory 12 II

Odona 4 VII, 18 XI, Odila 2 II, Odilli 23 X, Ody 27 XI, Odyseusza 1 I, Ofelii 13 V, Oksany 12 IV, Oktawiana 23 III, Oktawii 16 III, Oktawiusza 20 XI, Olafa 29 VII, Olecha 8 VIII, Olega 20 IX, Oleny 11 IV, Olgi 11 VII, Olgierda 4 XI, Olimpii 17 XII, Oliwiera 21 XI, Oliwii 5 III, Onufrego 12 VI, Orchidei 1 VIII, Orestesa 23 XI, Orfeusza 27 II, Oriany 7 I, Oskara 3 II, Ostapa 20 II, Oswalda 5 VIII, Otmara 16 XI, Ottona 1 VII, 18 XI, Otylii 13 XII, Ozanny 9 IX

Pafnucego 19 IV, Palomy 19 IX, Pameli 12 VII, Pankracego 3 IV, 12 V, Pantaleona 27 VII, Parysa 17 III, Paschalisa 17 V, Patrycego 17 IV, Patrycji 28 VIII, Patrycjusza 9 VII, Patryka 17 III, Pauli 26 I, Paulina 22 VI, Pauliny 26 V, 10 X, 2 XII, Pawła 15 I, 25 I, 7 III, 28 IV, 26 VI, 29 VI, Pelagii 9 VI, 8 X, Pelagiusza 23 III, Petroneli 31 V, Petroniusza 6 IX, Pii 19 I, Piotra 18 I, 8 II, 29 IV, 19 V, 29 VI, 19 X, Piusa 11 VII, 21 VIII, Placyda 5 X, Polikarpa 26 I, 23 II, Pompejusza 10 IV, Praksedy 21 VII, Prokopa 8 VII, Prospera 23 VI, Prota 11 IX, Protazego 19 VI, 4 VIII, Przecława 7 IV, Przecławy 7 IV, Przemysława 13 IV, 30 X, Przesława 3 IX, Przybysława 27 I, Przybysławy 27 I, 22 X, Pulcherii 10 IX

Racibora 29 VIII, Racisława 2 VI, Radka 25 VIII, Radomiła 11 VI, Radomiły 13 VIII, Radomira 28 I, Radomysła 27 XII, Radosława 1 III, Radosławy 9 IX, Radowida 27 V, Radzimierza 12 II, Radzimira 12 IX, Radzisława 16 X, Rafaela 20 VI, Rafała 29 IX, 24 X, Rainera 30 XII, Rajmunda 7 I, 23 I, 31 VIII, Rajnolda 9 II, Ramona 4 VII, Ramony 31 VIII, Rebeki 30 VIII, Reginy 7 IX, Remigiusza 1 X, Rene 18 X, Renaty 12 XI, Reny 17 III, Rity 29 IV, Roberta 17 IV, 7 VI, Roberty 13 V, Rocha 16 VIII, Roderyka 13 III, Rodryga 13 III, Rogera 14 XI, Roksany 14 IX, Rolanda 9 VIII, Romana 28 II, 29 II, 9 VIII, 18 XI, Romany 23 II, Romea 7 II, Romualda 7 II, 19 VI, 9 VIII, Romy 23 II, 22 V, Ronalda 18 VIII, Rościsława 17 I, Rozalii 4 IX, 4 X, Rozanny 14 IX, Rozyny 11 III, Róży 6 III, 30 VIII, Rudolfa 17 IV, 12 X, Rudolfiny 17 IV, 21 VI, Rufina 7 IV, Rufiny 10 VII, Rufusa 27 VIII, Ruperta 24 IX, Ruprechta 27 III, Ruty 16 II, Ryszarda 7 II, 3 IV, Ryszardy 7 IX

Sabina 30 XII, Sabiny 29 VIII, 27 X, Saby 5 XII, Salezego 29 I, Salomei 17 XI, 19 XI, Salomona 28 IX, Sambora 25 X, Samuela 16 II, 20 VIII, Samueli 20 VIII, Samsona 28 VII, Sandry 18 V, 26 VIII, Sary 13 VII, Saturnina 31 X, 29 XI, Sawy 7 V, Scholastyki 10 II, Sebastiana 20 I, Serafina 14 XI, Serafiny 29 VII, Sergiusza 24 II, 9 IX, Serwacego 13 V, Sewera 8 XI, Seweriana 8 XI, Sewery 20 VII, 13 VIII, Seweryna 8 I, 23 X, Seweryny 19 XI, Sędzimira 20 XI, Sędziwoja 8 XI, Skarbimierza 19 X, Skarbimira 19 X, Sławoja 9 VI, Sławomira 17 V, 5 XI, Sławomiry 23 XII, Sławosza 23 VII, Sławy 6 VIII, Sobiesława 20 VIII, Sobiesławy 1 XII, Soni 30 IX, Sotera 22 IV, Stanisława 8 V, 18 IX, 13 XI, Stanisławy 5 VIII, Stefana 16 VIII, 2 IX, Stefanii 18 IX, Stelli 15 VIII, Sulibora 17 XI, Sulimiery 30 V, Sulimierza 30 V, Sulimira 30 V, Sulisława 2 XII, Sulisławy 17 X, Swetłany 13 II, Sybilli 9 X, Sykstusa 28 III, 7 VIII, Sylwana 18 II, Sylwany 10 VII, Sylweriusza 20 VI, Sylwestra 26 XI, 31 XII, Sylwii 3 XI, Sylwina 17 II, Sylwiusza 8 VIII, Symeona 18 II, Symplicjusza 2 III, Szarloty 5 VII, Szczepana 26 XII, Szczęsnego 30 VIII, Szymona 18 VII, 3 IX, 28 X, Szymonety 16 V

Ścibora 9 IX, Światozara 8 XII, Świętopełka 1 VI, Świętosława 31 VIII, Świętosławy 3 V

Tacjany 12 I, Tadeusza 28 X, Taidy 1 III, Tamary 3 VI, Tatiany 25 I, Tekli 23 IX, Telesfora 5 I, Telimeny 3 II, Teobalda 1 VII, Teodora 19 IX, 24 IX, 9 XI, Teodory 1 IV, Teodozji 29 V, Teodozjusza 11 I, 25 X, Teofila 27 IV, 2 X, Teofili 28 XII, Terencjusza 23 IV, Teresy 1 X, 3 X, 15 X, Tezeusza 11 I, Tobiasza 2 XI, Tomasza 28 I, 7 III, 3 VII, 22 IX, 21 XII, 29 XII, Tomiła 10 X, Tomira 24 IX, Tomiry 24 V, Tomisława 21 XII, Toski 18 V, Tristana 28 XI, Tyberiusza 12 VIII, Tyburcjusza 14 IV, Tycjana 3 III, Tymona 19 IV, Tymoteusza 24 I, 26 I, Tytusa 4 I, 26 I

Ubalda 16 V, Ulryka 14 VII, Urbana 2 VII, 31 X, Ursyna 9 XI, Urszuli 21 X

Wacława 4 IV, 28 IX, Wacławy 15 IV, Wadima 9 IV, Waldemara 5 V, 11 XII, Walentego 14 II, Walentyna 13 XI, Walentyny 25 VII, Walerego 28 I, 29 I, Waleriana 14 IV, 27 XI, Walerii 28 IV, 5 VI, Waleriusza 28 I, Waltera 8 IV, 5 VI, Wandy 23 VI, Wasyla 20 III, Wawrzyńca 5 IX, Wenesy 24 V, Wernera 18 IV, Weroniki 13 I, 4 II, 9 VII, Wery 30 IX, Wespazjana 18 VII, Wiaczesława 18 II, Wieńczysława 25 III, Wiesława 7 VI, 9 XII, Wiesławy 22 V, Wiktora 25 II, 21 V, 28 VII, 17 X, Wiktorii 23 XII, Wiktoryna 29 III, Wilhelma 10 I, 25 VI, Wilhelminy 25 X, Wilmy 5 XII, Wincentego 22 I, 8 III, 5 IV, 19 VII, 27 IX, 9 X, Wincenty 5 V, Wińczysława 25 III, Wioletty 29 X, Wioli 15 VI, Wirgiliusza 27 XI, Wirginii 8 XII, Wirginiusza 5 VIII, 8 XII, Wisława 7 VI, Wita 15 VI, Witaliana 25 I, Witalisa 10 VII, Witolda 12 XI, Witomiła 27 X, Witomira 2 V, Witosława 4 III, Witosławy 4 III, Wiwanny 2 XII, Władymira 9 I, Władysława 2 IV, 27 VI, Włodzimierza 16 I, 15 VII, Włodzisława 19 VII, Włodzimira 13 XI, Wodzisława 19 VII, Wojciecha 23 IV, Wojmira 11 XII, Wojsława 8 X, Wolfganga 31 X, Wszebora 27 VII, Wyszomira 28 VIII

Zachariasza 5 XI, Zawiszy 17 VIII, Zbigniewa 17 III, 1 IV, Zbisława 23 III, Zbysława 17 XI, Zdobysława 30 VII, Zdzisława 29 I, 28 XI, Zdzisławy 16 XII, Zefira 26 VIII, Zefiryna 20 XII, Zefiryny 26 VIII, Zelmiry 21 IV, Zenobii 30 X, Zenobiusza 24 XII, Zenona 23 VI, 22 XII, Ziemisława 13 X, Ziemowita 19 X, Zofii 15 V, Zoriana 15 X, Zory 19 VI, Zuzanny 24 V, 11 VIII, Zygfryda 15 II, 22 VIII, Zygmunta 2 V, Zyty 27 IV

Żakliny 8 II, 23 VII, Żaliny 23 VII, Żanety 27 XII, Żanny 17 VIII, Żegoty 1 II, Żelisława 23 VII, Żytomira 7 XI, Żywii 21 III, Żywisława 27 IV
'''

swieta = {
    '1.1 Nowy Rok',
    '3.1 Trzech Króli',
    '21.1 Dzień Babci',
    '22.1 Dzień Dziadka',
    '4.2 Tłusty Czwartek',
    '10.2 Popielec',
    '14.2 Walentynki',
    '8.3 Dzień Kobiet',
    '27.3 Wielkanoc',
    '28.3 Poniedziałek Wielkanocny',
    '1.4 Prima Aprillis',
    '1.5 Święto Pracy',
    '3.5 Konstytucji 3 Maja',
    '26.5 Boże Ciało',
    '26.5 Dzień Matki',
    '1.6 Dzień Dziecka',
    '15.8 Wniebowzięcie NMP',
    '14.10 Dzień Nauczyciela',
    '1.11 Wszystkich Świętych',
    '11.11 Dzień Niepodległości',
    '30.11 Andrzejki',
    '24.12 Wigilia',
    '25.12 Boże Narodzenie',
    '31.12 Sylwestra',
}

def show(d, m):
    print('---', d, m, '---')
    print('\n'.join(names[m][d]))

names = {}
name = ''

month_numbers = [None, 'I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX', 'X', 'XI', 'XII']
for line in data.split('\n'):
    #line = line.strip()[:-1]
    if line:
        #print(line)
        for item in line.split(','):
            item = item.strip()

            if item[0].isdigit():
                n = name
                d, m = item.split()
            else:
                n, d, m = item.split()
                name = n

            d = int(d)
            m = month_numbers.index(m)

            if m not in names:
                names[m] = {}
            if d not in names[m]:
                names[m][d] = []
            names[m][d].append(n)

#print(names)

#show(1, 11)
#show('24', 8)
#show('24', 2)

#s = set()
#for n, m in names.items():
#    print(n, len(m))
#    s |= set(m)

#print(len(s), s)

import calendar

class MyCal(calendar.LocaleHTMLCalendar):

    def formatday(self, day, weekday, month=1):
        """
        Return a day as a table cell.
        """
        if day == 0:
            return '<td class="noday">&nbsp;</td>' # day outside month
        else:
            if day in names[month]:
                txt = names[month][day]
                txt += ['&nbsp;'] * (8-len(txt))
                txt = '<br>'.join(txt)
            else:
                txt = '???'
            return '<td class="%s"><span>%d</span><br>%s</td>' % (
                    self.cssclasses[weekday],
                    day,
                    txt
                )

    def formatweek(self, theweek, month=1):
        """
        Return a complete week as a table row.
        """
        s = ''.join(self.formatday(d, wd, month) for (d, wd) in theweek)
        return '<tr>%s</tr>' % s

    def formatmonth(self, theyear, themonth, withyear=True):
        """
        Return a formatted month as a table.
        """
        v = []
        a = v.append
        a('<table border="0" cellpadding="0" cellspacing="0" class="month">')
        a('\n')
        a(self.formatmonthname(theyear, themonth, withyear=withyear))
        a('\n')
        a(self.formatweekheader())
        a('\n')
        for week in self.monthdays2calendar(theyear, themonth):
            a(self.formatweek(week, themonth))
            a('\n')
        a('</table>')
        a('\n')
        return ''.join(v)

    def formatweekday(self, day):
        with calendar.different_locale(self.locale):
            s = calendar.day_abbr[day].capitalize()
            return '<th class="%s">%s</th>' % (self.cssclasses[day], s)

    def formatmonthname(self, theyear, themonth, withyear=True):
        with calendar.different_locale(self.locale):
            s = calendar.month_name[themonth].capitalize()
            if withyear:
                s = '%s %s' % (s, theyear)
            return '<tr><th colspan="7" class="month">%s</th></tr>' % s

cal = MyCal()

print('''<head>
<meta charset="utf-8">
<style>
td{vertical-align:top; padding:5px;}
.month td{border:1px solid #eee; width:150px}
span{font-size: 150%;font-weight:bold; padding:5px; display:inline-block}
.sun{color:red}
</style>
</head>''')

print(cal.formatyear(2017, 1))

