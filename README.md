# Progetto n° 1
Progetto di gruppo n° 1 del Corso Python and Machine Learning di:
- [Davide Cognetta](https://github.com/cognettadavide97-afk)
- [Elisabetta Carella](https://github.com/eli-carella)
- [Gabriele Giuliani](https://github.com/giulianigabbo95/)
- [Maria Visone](https://github.com/mariavisone)

---

## Testo
Progettare un sistema a oggetti per un'officina che ripara elettrodomestici.  

Il programma deve modellare elettrodomestici, ticket di riparazione e operazioni dell'officina utilizzando incapsulamento, ereditarietà, polimorfismo, type() e metodi variatici (*args, **kwargs).
* Classe base Elettrodomestico:
	> Gabriele

    - Attributi privati (__ doppio underscore):
        - __marca (stringa)
        - __modello (stringa)
        - __anno_acquisto (intero)
        - __guasto (stringa)
    - Metodi:
        - __init__(self, marca, modello, anno_acquisto, guasto): costruttore
        - descriviElettrodomestico(self): restituisce stringa con marca, modello, anno, guasto
        - stimaCostoBase(self): restituisce un valore numerico (costo base diagnosi)
        - Getter e setter per tutti gli attributi (controllo: anno non può essere nel futuro)
    Regola 1 - Incapsulamento: attributi privati (__), accessibili solo tramite getter/setter.

* Classi derivate (Ereditarietà + Polimorfismo)
    Creare almeno tre sottoclassi di Elettrodomestico:
    1. Lavatrice:
        > Gabriele

        - Attributi aggiuntivi privati:
            - __capacita_kg (intero)
            - __giri_centrifuga (intero)
        - Override:
            - stimaCostoBase(self): costo maggiorato se la capacità è elevata
    2. Frigorifero:
        > Elisabetta
        - Attributi aggiuntivi privati:
            - __litri (intero)
            - __ha_freezer (booleano)
        - Override:
            - stimaCostoBase(self): costo modificato in base a presenza freezer e litri
    3. Forno:
        > Maria / Davide  
        - Attributi aggiuntivi privati:
            - __tipo_alimentazione (stringa: "elettrico", "gas")
            - __ha_ventilato (booleano)
        - Override:
            - stimaCostoBase(self): costo modificato in base a tipo alimentazione e presenza funzione ventilata
    Regola 2 - Ereditarietà: tutte le classi derivate devono chiamare super().__init__() nel costruttore.  
    Regola 3 - Polimorfismo: ogni sottoclasse implementa la propria versione di stimaCostoBase().

* Classe TicketRiparazione:
    > Maria / Davide

    Classe che rappresenta un ticket di riparazione aperto in officina.
    - Attributi privati (__):
        - __id_ticket (intero o stringa univoca)
        - __elettrodomestico (oggetto di tipo Elettrodomestico o sottoclasse)
        - __stato (stringa: "aperto", "in lavorazione", "chiuso")
        - __note (lista di stringhe, inizialmente vuota)
    - Metodi:
        - __init__(self, id_ticket, elettrodomestico): costruttore
        - aggiungiNota(self, testo): aggiunge una nota alla lista
        - calcolaPreventivo(self, *voci_extra): metodo variadico:
            - Utilizza elettrodomestico.stimaCostoBase() come costo di partenza
            - Somma tutte le voci extra passate come parametri (*voci_extra)
            - Restituisce il totale
        - Getter e setter per stato e note
    Nota: il metodo calcolaPreventivo() deve funzionare con qualsiasi sottoclasse di Elettrodomestico (polimorfismo su stimaCostoBase()).

* Classe Officina:
    > Elisabetta

    Classe che gestisce i ticket e gli elettrodomestici.
    - Attributi:
        - nome (stringa)
        - tickets (lista di oggetti TicketRiparazione)
    - Metodi:
        - aggiungiTicket(self, ticket): aggiunge un ticket alla lista
        - chiudiTicket(self, id_ticket): imposta lo stato del ticket su "chiuso"
        - stampaTicketAperti(self): mostra ID, tipo di elettrodomestico e stato
        - totalePreventivo(self): somma i preventivi di tutti i ticket

* Uso di type() e controllo degli oggetti:
    > Gabriele

    Implementare un metodo all'interno della classe Officina (o in una funzione separata): calcolaStatisticheTipo(self)  
    Questo metodo deve:
    - Iterare su tutti i ticket
    - Utilizzare type() (o isinstance()) per identificare se l'elettrodomestico associato al ticket è una Lavatrice, un Frigorifero o un Forno
    - Contare quanti ticket ci sono per ciascuna sottoclasse
    - Stampare un report del tipo:
        - text
        - Numero di lavatrici in riparazione: X
        - Numero di frigoriferi in riparazione: Y
        - Numero di forni in riparazione: Z
    Requisito: il metodo deve utilizzare type() (o varianti consigliate) per determinare il tipo reale degli oggetti.

---

## Linee Guida

### Come aggiungere Collaboratori:
Al fine di poter scrivere tutti sulla stessa repository è necessario che il proprietario aggiunga dei collaboratori, in modo che questi la vedano come propria e possano committare senza problemi.  
Per farlo, una volta aperta, cliccare su "Settings" e poi su "Collaborators and Teams", così da poter digitare nell'apposito box il nome utente o la mail di chi si intende aggiungere.  
Nel caso ciò non venga fatto, gli altri membri devono clonare la repository e possono lavorarci solo in locale senza poter committare.

### Come scrivere il codice:
Al fine di essere tutti coordinati e rendere il codice più leggile si è scelto di usare uno standard:
- Variabili:
    - italiano
    - sostantivo
    - minuscolo
    - trattino basso per separare le parole nel caso siano due o più
- Classi:
    - italiano
    - sostantivo
    - prima lettera di ogni parola maiuscola
    - nessun separatore tra le parole (nel caso siano più di una)
- Funzioni/Metodi (eccetto Getter e Setter):
    - italiano
    - prima parola: verbo imperativo minuscolo
    - parole successive alla prima: sostantivo con prima lettera maiuscola
    - nessun separatore tra le parole

### Come dividere

---

## Albero GitHub
![Albero](https://github.com/giulianigabbo95/Progetto1_CorsoPYML_DC-EC-GG-MV/blob/main/Albero_Commit-(Ultima_Modifica_2026-03-08).yEd.png)

### Specifiche (in costante aggiornamento):
- Creato con [yED](https://www.yworks.com/products/yed) (programma scaricabile da [qui](https://www.yworks.com/products/yed/download))
- File scaricabile da [qui](https://drive.google.com/file/d/1UymIbvs9AvrtxK7zTDUoMLo6rnIx1zWK/view?usp=sharing) (serve yED per aprirlo) oppure [qui](https://github.com/giulianigabbo95/Progetto1_CorsoPYML_DC-EC-GG-MV/blob/main/Albero_Commit-(Ultima_Modifica_2026-03-08).graphml)
- Alternativa online [qui](https://drive.google.com/file/d/1VutCebM29kgtEaHvPOyIaC-R-zhQ0F9m/view?usp=sharing) (serve [Draw.io](https://app.diagrams.net/) collegato a Drive per aprirlo), scaricabile in formato PDF da [qui]():  

Alcuni

### Legenda:
- Titolo (su Nodo): Nome Commit
- Etichetta (su Arco): Nome Branch
- Collegamenti:
    Freccia: ...
- Testo:
    - Grassetto: Commit Pushato
    - Corsivo: Commit NON Pushato
- Asterisco:
    - Assente: Commit Online
    - Presente: Commit su Fork, presente solo sul PC dell'autore (e quindi non sulla repository del proprietario) nel caso 
- Sfondo:
    - Verde: Task Completato
    - Grigio: Task NON Completato
- Bordo:
    - Arancione (#ff6600): Task di Gabriele -> Commit di Gabriele nel branch "MAIN/ORIGIN"
    - Bordeaux (#993366): Task di Elisabetta -> Commit di Elisabetta nel branch "MAIN/ORIGIN"
    - Celeste (#99ccff): Task di Davide -> Commit di Davide nel branch "MAIN/ORIGIN"
    - Giallo (#ffff00): Task di Gabriele -> Commit di Gabriele nel branch "Prova"
    - Lilla (#cc99ff): Task di Maria -> Commit di Maria nel branch "Branch_Maria"
    - Viola (#800080): Task di Elisabetta -> Commit di Elisabetta nel branch "Branch_Elisabetta"
    - Nero (#000000): Task da Dividere

---

## Video Utili
GitKraken
[Git e GitHub Fundamentals \[ITA\]](https://www.youtube.com/watch?v=tBReZ661Ps8)  
[Git e GitHub Basi \[ITA\]](https://www.youtube.com/watch?v=MnqHNRNBbcg)  
[Github Desktop e Github Pages \[ITA\]](https://www.youtube.com/watch?v=8sVu_02rZQU)  
[Git, GitHub, & GitHub Desktop per Principianti \[ENG\]](https://www.youtube.com/watch?v=8Dd7KRpKeaE)