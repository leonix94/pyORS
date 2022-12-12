# PyORSClient

## INTRO

Questo Client utilizza le API fornite da OpenRouteService per calcolare le distanze tra due punti fornendo le coordinate geografiche (latitudine e longitudine) tramite il file input.csv.

Restituisce in Output due file:

- **output.csv** : è il file di input con l'aggiunta della colonna degli id e delle distanze
- **map.html** : la mappa dei tracciati con relativo id di riferimento del record e della distanza

## INSTALL

è consigliabile eseguire l'installazione dei moduli necessari allo script in un ambiente dedicato, per crearlo e attivarlo
`python3 -m venv ors-env && ors-env\Scripts\activate.bat`

Per l'installazione è necessario avere installate nell'environment python i moduli contenuti nel file requirements.txt tramite il comando

`$ pip install -r requirements.txt`

oppure se si utilizza conda, è possibile creare un nuovo ambiente e installare i moduli necessari:

`conda create --name my-env-name --file requirements.txt --channel default`

nel caso si vuole utilizzare un'istanza locale dell'ORS engine, è possibile avviarla in un container docker con un file OSM del centro italia, per avviarla è necessario lanciare il comando nella directory "docker"

`docker compose up`

ed eseguire poi lo script con l'argomento

`python script.py local`

una volta avviato il container, in base ai profiles attivi nel file *ors-config.json* esso genera, nel caso non vi siano già, dei file per ciascun profilo attivo nella cartella *graph*. Il servizio non risulterà disponibile finchè la generazione dei grafi non sarà completata.

Per maggiori informazioni sui parametri che è possibile inserire nel body message request, vedere [qui](https://openrouteservice.org/dev/#/api-docs/v2/directions) 

## UTIL

- [osmconvert64](https://wiki.openstreetmap.org/wiki/Osmconvert) permette di interagire e manipolare file .pbf 
- le mappe possono essere scaricate da [Geofabriq](https://download.geofabrik.de/europe/italy/centro.html)

## TODO

- Dotare lo script di una GUI per aggiungere e modificare i parametri dello script
- Aggiungere la possibilità di creare percorsi con diverse tipologie di trasporto e graficarli nella mappa
- Dare la possibilità di inserire un API Key diverso per le API pubbliche
- Poter aggiungere una rotta ad un server desiderato (locale o remoto) dove è installato il servizio OSR 