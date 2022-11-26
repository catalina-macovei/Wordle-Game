# :books: Wordle Game 

Aplicația funcționeaza pe baza metodei Client-Sever. În aceasta structura, Clientul are rolul de a interacționa cu utilizatorul, oferind o interfață grafică (UI) sugestiv și de a facilita interacțiunea utilizatorului cu aplicația. În același timp, serverul are rolul de a prelucra datele primite de la utilizator si de a răspunde dinamic cererilor primite de la Client. În aceeași ordine de idei,  pastrează cuvântul secret si setul de date pentru fiecare sesiune de joc.

 Componenta client este construita pe baza tehnologiilor web, utilizate pe front-end HTML, CSS si JavaScript. In timp ce Serverul este creat pe baza frameworkului Flask, care la rândul său se bazează pe limbajului de programare Python.


### :pushpin: Obiectivul jocului
 Wordle Game determină utilizatorul să ghicească un cuvânt de cinci litere, introduse de la tastatură. În esență, jocul se bazează pe două mecanisme, primul este de a ghici cuvântul dintr-un număr nelimitat de încercări, iar al doilea ar fi de a ghici cuvântul, folosind lista de sugestii, unde e indicată cea mai bună opțiune, respectiv cuvântul cu entropia maximă. 
 #### :alarm_clock: Optimizare & Entropie:
 Optimizarea procesului de ghicire a cuvantului secret a fost realizata prin implementarea in Python  a unor functii ce au la baza criteriul entropiei. Astfel, se calculeaza probabilitatea de aparitie in lista de cuvinte a fiecarei litere din alfabet, care este apoi folosita pentru a determina entropia fiecarui cuvant din lista. Folosind feedback-ul primit in urma unei incercari de ghicire, lista de cuvinte din care este aleasa urmatoarea incercare este filtrata astfel incat sa mai contina doar cuvinte cat mai apropiate de forma cuvantului secret. Mai specific, doar cuvintele care:  

1. pastreaza literele a caror pozitie corecta in cuvant a fost ghicita 
2. contin literele care sunt in cuvantul secret, dar a caror pozitie nu a fost ghicita. Din acestea se aleg doar cele care nu incearca sa plaseze litera existenta pe aceeasi pozitie pe care au testat o incercarile precedente si care s a dovedit a fi incorecta 
3. nu contin literele care au primit feedback negativ in urma incercarii de ghicire 

##### Sugestia finala este cuvantul care indeplineste toate conditiile de mai sus si care are entropie maxima.
##### :zap: Numărul mediu de încercări pentru ghicirea tuturor cuvintelor - 4.58
 

### :scroll: Cerințe pentru rularea jocului:

Pentru a rula jocul, asigurați-vă că aveți instalată aplicația Visual Studio Code pentru un mediu de lucru corespunzător cu Python 3.11 și managerul de pachete Python pip. 

#### :zap:Instructiuni de rulare: :zap:

1. Clonați jocul din acest GitHub repository pe calculatorul local cu ajutorul terminalului.
2. Cu ajutorul terminalului acesati folderul **backend** si rulati managerul de pachete **pip** pentru a instala pachetul **Flask** si **Flask_cors** necesare lansarii serverului::
  2.1 ```pip install Flask```
  2.2 ```pip install flask_cors```
  
3. Dupa ce ați instalat pachetele necesare, treceți in backend directory și rulati în terminal comanda `flask --app main.py --debug run` pentru a porni serverul flask in development mode, (permite hot reload),  sau 3.2 ```flask --app main.py``` pentru a porni serverul in regim normal. 
4. Dupa ce serverul a pornit, accesati folderul frontend si lansati un server care ruleaza fisierul index.html (cel mai simplu server poate fi rulat folosind optiunea Go Live a IDE-lui VS Code) .
5. Enjoy our Wordle Game with entropy or without entropy.

#### Good luck :blush: !  
##### Echipa: Creative Team Name :zap:
###### grupa 142
1. Macovei Cătălina
2. Alexandra Toma
3. Popescu Pavel-Yanis
