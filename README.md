# Wordle Game

Aplicația funcționeaza pe baza metodei Client-Sever. În aceasta structura, Clientul are rolul de a interacționa cu utilizatorul, oferind o interfață grafică (UI) sugestiv și de a facilita interacțiunea utilizatorului cu aplicația. În același timp, serverul are rolul de a prelucra datele primite de la utilizator si de a răspunde dinamic cererilor primite de la Client. În aceeași ordine de idei,  pastrează cuvântul secret si setul de date pentru fiecare sesiune de joc.

 Componenta client este construita pe baza tehnologiilor web, utilizate pe front-end HTML, CSS si JavaScript. In timp ce Serverul este creat pe baza frameworkului Flask, care la rândul său se bazează pe limbajului de programare Python.


### Obiectivul jocului
 Wordle Game determină utilizatorul să ghicească un cuvânt de cinci litere, introduse de la tastatură. În esență, jocul se bazează pe două mecanisme, primul este de a ghici cuvântul dintr-un număr nelimitat de încercări, iar al doilea ar fi de a ghici cuvântul, folosind lista de sugestii, unde e indicată cea mai bună opțiune, respectiv cuvântul cu entropia maximă. 

### Cerințe pentru rularea jocului:

Pentru a rula jocul, asigurați-vă că aveți instalată aplicația Visual Studio Code pentru un mediu de lucru corespunzător cu Python 3.11 și managerul de pachete Python pip. 

#### Instructiuni de rulare: :zap:

1. Clonați jocul din acest GitHub repository pe calculatorul local cu ajutorul terminalului.
2. Accesati folderul backend si rulati managerul de pachete *pip* pentru a instala pachetele necesare rularii serverului:
    2.1
3. Dupa ce ați instalat pachetele necesare, treceți in backend directory și rulati în terminal comanda `flask --app main.py --debug run` pentru a porni serverul flask in development mode, (permite hot reload),  sau 3.2 pentru a porni serverul. 
  
 
4. Dupa ce serverul a pornit, accesati folderul frontend si deschideti fisierul index.html în browser.
5. Enjoy our Wordle Game with entropy or without entropy.
#### Good luck :blush: !  
