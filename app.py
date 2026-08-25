import streamlit as st

# Configurazione pagina
st.set_page_config(page_title="GEV Inverno e Monteleone", page_icon="🌲", layout="centered")

# Titolo e intestazione
st.title("🌲 GEV Inverno e Monteleone - Simulatore Pattuglia")
st.subheader("Sfida a 20 domande per aspiranti Guardie Ecologiche Volontarie")

# Inizializzazione dello stato di gioco
if "punteggio" not in st.session_state:
    st.session_state.punteggio = 0
if "step" not in st.session_state:
    st.session_state.step = 0
if "risposte" not in st.session_state:
    st.session_state.risposte = {}
        "categoria": "🗑️ Inquinamento e Rifiuti",
        "scenario": "1. Durante una perlustrazione nei pressi dei campi verso Monteleone, trovi un accumulo di macerie edilizie e plastica. Come intervieni?",
        "opzioni": [
            "Ignori il problema, la zona è isolata.",
            "Scatti foto, geolocalizzi l'area, compili il verbale di accertamento e inoltri la segnalazione alle autorità competenti.",
            "Dai fuoco ai rifiuti per liberare il passaggio."
        ],
        "corretta": 1,
        "spiegazione": "Le GEV hanno il compito di monitorare il territorio e verbalizzare gli illeciti ambientali inviandoli agli enti preposti."
    },
    {
        "categoria": "🍄 Fauna e Flora",
        "scenario": "2. Un cercatore di funghi nei boschi vicini usa un sacchetto di plastica sigillato. Cosa gli contesti?",
        "opzioni": [
            "Il sacchetto di plastica impedisce il rilascio delle spore; occorre un contenitore rigido e traforato (come un cestino di vimini).",
            "Niente, la plastica protegge i funghi dal deterioramento.",
            "Gli ordini di consegnarti tutti i funghi raccolti."
        ],
        "corretta": 0,
        "spiegazione": "L'uso di contenitori traforati è obbligatorio per consentire la dispersione delle spore nel sottobosco."
    },
    {
        "categoria": "🔥 Prevenzione Incendi",
        "scenario": "3. Un agricoltore sta bruciando residui vegetali al margine del bosco durante un periodo di alta pericolosità incendi regionale. Cosa fai?",
        "opzioni": [
            "Ti unisci a lui per finire prima.",
            "Informi l'agricoltore del divieto assoluto di abbruciamento in periodi a rischio e richiedi lo spegnimento immediato.",
            "Lasci fare purché sia presente un secchio d'acqua."
        ],
        "corretta": 1,
        "spiegazione": "Nei periodi dichiarati a rischio incendio dalla Regione Lombardia vige il divieto assoluto di abbruciamento."
    },
    {
        "categoria": "🐝 Tutela della Biodiversità",
        "scenario": "4. Incontrando degli apicoltori lungo un corso d'acqua, noti l'impiego di fitofarmaci vietati vicino alle arpie. Come agisci?",
        "opzioni": [
            "L'uso di prodotti chimici non rientra nelle mansioni delle GEV.",
            "Verifichi le etichette, raccogli elementi di prova e verfichi il rispetto dei coefficienti di rispetto delle acque e della fauna.",
            "Consigli un altro pesticida più efficace."
        ],
        "corretta": 1,
        "spiegazione": "Le GEV vigilano anche sull'impiego corretto e legale di prodotti chimici a tutela dell'ecosistema e degli impollinatori."
    },
    {
        "categoria": "🎣 Pesca e Acque",
        "scenario": "5. Un pescatore si trova lungo una roggia locale senza la licenza di pesca governativa. Qual è il comportamento corretto?",
        "opzioni": [
            "Procedere con il controllo dei documenti ed eventualmente elevare sanzione amministrativa per mancanza di titolo autorizzativo.",
            "Consigliargli di nascondersi se passa la Polizia Provinciale.",
            "Sequestrare la canna da pesca sul posto di tua iniziativa."
        ],
        "corretta": 0,
        "spiegazione": "Le GEV sono pubblici ufficiali nell'esercizio delle loro funzioni e possono accertare violazioni relative alle licenze di pesca."
    },
    {
        "categoria": "🐶 Animali d'Affetto",
        "scenario": "6. In un'area naturale protetta, un cittadino passeggia con un cane di grande taglia privo di guinzaglio che rincorre la fauna selvatica. Cosa fai?",
        "opzioni": [
            "Lo inviti a legare il cane ricordando le norme a tutela della fauna e il rischio di sanzione.",
            "Regali un biscotto al cane e lasci proseguire.",
            "Tiri una pietra al cane per allontanarlo."
        ],
        "corretta": 0,
        "spiegazione": "I cani liberi possono disturbare o uccidere la fauna selvatica, specie durante i periodi di nidificazione e riproduzione."
    },
    {
        "categoria": "🚗 Circolazione Fuoristrada",
        "scenario": "7. Un gruppo di moto da enduro sta percorrendo un sentiero pedonale o forestale interdetto ai mezzi a motore. Come ti comporti?",
        "opzioni": [
            "Ti metti al centro del sentiero per bloccarli fisicamente.",
            "Annoti targhe, orario e luogo in sicurezza e inoltri la segnalazione per la sanzione relativa alla viabilità agro-silvo-pastorale.",
            "Li rincorri con il tuo veicolo privato."
        ],
        "corretta": 1,
        "spiegazione": "La sicurezza viene prima di tutto: mai creare situazioni di pericolo fermando mezzi in corsa; prendere nota dei dati e sanzionare/segnalare."
    },
    {
        "categoria": "🌿 Flora Progetta",
        "scenario": "8. Noti un gruppo di escursionisti che sta sradicando esemplari di orchidee selvatiche lungo un prato umido. Come intervieni?",
        "opzioni": [
            "Spieghi che le orchidee spontanee sono specie protette dalla legge regionale e ne è vietata la raccolta e lo sradicamento.",
            "Chiedi se ne hanno una anche per te.",
            "Dire che possono raccoglierne al massimo 5 chilogrammi a testa."
        ],
        "corretta": 0,
        "spiegazione": "La legge regionale protegge rigorosamente la flora spontanea rara come le orchidee selvatiche lombarde."
    },
    {
        "categoria": "🦅 Fauna Selvatica in Difficoltà",
        "scenario": "9. Trovi un rapace ferito ai margini di una strada provinciale vicino a Inverno. Qual è la procedura adeguata?",
        "opzioni": [
            "Lo porti a casa e provi a curarlo con dei rimedi casalinghi.",
            "Contatti il CRAS (Centro Recupero Animali Selvatici) di riferimento e la Polizia Provinciale per il recupero professionale.",
            "Lo lasci lì confidando nella natura."
        ],
        "corretta": 1,
        "spiegazione": "La fauna selvatica ferita deve essere presa in carico da centri specializzati (CRAS) per la riabilitazione."
    },
    {
        "categoria": "🚜 Tutela del Suolo",
        "scenario": "10. Un cantiere sta scaricando terre e rocce da scavo su un terreno agricolo senza alcuna autorizzazione o piano di riutilizzo. Cosa fai?",
        "opzioni": [
            "Avvii l'accertamento per potenziale gestione illecita di rifiuti speciali e ne dai notizia all'ufficio tecnico comunale e ARPA.",
            "Pensi che stiano solo livellando il terreno e continui la pattuglia.",
            "Aiuti gli operai a stendere la terra."
        ],
        "corretta": 0,
        "spiegazione": "I materiali da scavo non autorizzati sono assimilati a rifiuti e possono contaminare i suoli agricoli."
    },
    {
        "categoria": "🧱 Patrimonio Ambientale",
        "scenario": "11. Trovi delle scritte vandaliche fatte con bombolette spray sui pannelli informativi del percorso naturalistico locale. Come procedi?",
        "opzioni": [
            "Scrivi 'GEV' sopra i graffiti per coprirli.",
            "Documenti il danno estetico/materiale al patrimonio pubblico e fai richiesta al Comune per il ripristino.",
            "Compri un altro pennarello per completare il disegno."
        ],
        "corretta": 1,
        "spiegazione": "Il danneggiamento delle strutture informative ostacola la fruizione pubblica e la valorizzazione del territorio."
    },
    {
        "categoria": "🏕️ Campeggio Abusivo",
        "scenario": "12. Un gruppo di persone ha allestito un campo tenda con tanto di falò acceso in un'area naturale protetta non adibita a campeggio. Cosa fai?",
        "opzioni": [
            "Controlli l'incolumità dell'area, spegni il fuoco improvvisato, contesti il campeggio abusivo e inviti allo sgombero.",
            "Ti fermi a dormire con loro per la notte.",
            "Chiedi una tassa di soggiorno in contanti."
        ],
        "corretta": 0,
        "spiegazione": "Il campeggio libero e l'accensione di fuochi sono vietati al di fuori delle aree attrezzate per prevenire incendi e degrado."
    },
    {
        "categoria": "🪵 Taglio Alberi",
        "scenario": "13. In un bosco ceduo trovi persone intenti ad abbattere alberi ad alto fusto senza la segnalazione/autorizzazione di taglio. Cosa richiedi?",
        "opzioni": [
            "Sospendi l'attività e richiedi l'esibizione dell'autorizzazione/denuncia di inizio attività selvicolturale (istanza di taglio).",
            "Chiedi loro di regalarti un carico di legna per l'inverno.",
            "Insegni loro ad usare meglio la motosega."
        ],
        "corretta": 0,
        "spiegazione": "I tagli boschivi sono regolati dalla normativa forestale regionale per garantire il rinnovo del bosco."
    },
    {
        "categoria": "💧 Tutela Idrica",
        "scenario": "14. Noti uno scarico di liquido schiumoso e maleodorante proveniente da una roggia che sfocia in un corso d'acqua. Qual è il primo passo?",
        "opzioni": [
            "Bere un sorso per capire di cosa si tratta.",
            "Effettuare rilievi fotografici, campionare l'orario e avvisare tempestivamente ARPA e Polizia Locale per l'individuazione della fonte.",
            "Mettere dei sassi davanti allo scarico per fermarlo."
        ],
        "corretta": 1,
        "spiegazione": "Gli sversamenti nei corsi d'acqua richiedono un pronto intervento delle agenzie di protezione ambientale (ARPA)."
    },
    {
        "categoria": "📜 Normativa GEV",
        "scenario": "15. Durante il servizio, un cittadino ti chiede se hai il potere di perquisirlo personalmente. Cosa rispondi?",
        "opzioni": [
            "Sì, posso perquisire chiunque in qualsiasi momento.",
            "No, la GEV ha qualifica di Pubblico Ufficiale e Polizia Amministrativa, non di Polizia Giudiziaria per perquisizioni personali.",
            "Sì, ma solo se c'è la luna piena."
        ],
        "corretta": 1,
        "spiegazione": "Le GEV hanno compiti di Polizia Amministrativa Ambientale; non possono effettuare perquisizioni personali, riservate alle Forze dell'Ordine."
    },
    {
        "categoria": "🐝 Specie Invasive",
        "scenario": "16. Durante una perlustrazione noti la presenza diffusa della Vespa velutina o della Nutria lungo i fossi. Come ti comporti?",
        "opzioni": [
            "Segnali la presenza secondo i piani di monitoraggio ed eradicazione delle specie esotiche invasive definiti dalla Regione.",
            "Provi a catturarle a mani nude.",
            "Le porti a casa come animali domestici."
        ],
        "corretta": 0,
        "spiegazione": "La segnalazione delle specie esotiche invasive è fondamentale per l'attuazione dei piani regionali di contenimento."
    },
    {
        "categoria": "🚜 Pesticidi in Agricoltura",
        "scenario": "17. Un trattore sta nebulizzando prodotti fitosanitari in presenza di forte vento vicino alle abitazioni del paese. Cosa fai?",
        "opzioni": [
            "Rilevi l'infrazione delle distanze di sicurezza e delle condizioni meteo non idonee previste dal PAN (Piano d'Azione Nazionale).",
            "Gli fai cenno che il vento fa spandere meglio il prodotto.",
            "Ti metti a correre dietro al trattore senza protezioni."
        ],
        "corretta": 0,
        "spiegazione": "L'uso di fitofarmaci in presenza di vento forte è vietato per evitare la deriva dei prodotti chimici verso zone abitate."
    },
    {
        "categoria": "🏛️ Educazione Ambientale",
        "scenario": "18. Un gruppo di studenti in visita guidata ti chiede quale sia il ruolo principale delle GEV nel comune di Inverno e Monteleone. Cosa rispondi?",
        "opzioni": [
            "Fare multe a tutti i cittadini senza spiegazioni.",
            "Promuovere l'educazione ambientale, prevenire gli illeciti e tutelare il patrimonio naturale del territorio.",
            "Tagliare l'erba nei giardini privati."
        ],
        "corretta": 1,
        "spiegazione": "L'educazione ambientale e la prevenzione sono pilastri fondamentali del servizio delle Guardie Ecologiche Volontarie."
    },
    {
        "categoria": "🦆 Caccia e Fauna Unifilare",
        "scenario": "19. Durante la stagione venatoria, senti sparare a distanza ravvicinata da una casa o da una strada asfaltata. Qual è la norma?",
        "opzioni": [
            "È consentito sparare ovunque purché si abbia la licenza.",
            "La legge sulla caccia impone distanze minime rigorose (es. 150m dalle abitazioni in direzione di sparo) per ragioni di sicurezza.",
            "Si può sparare solo dal balcone di casa."
        ],
        "corretta": 1,
        "spiegazione": "La legge 157/92 stabilisce distanze di sicurezza tassative da immobili, strade e ferrovie per la pratica venatoria."
    },
    {
        "categoria": "🚴 Fruizione dei Sentieri",
        "scenario": "20. Incontri un gruppo di ciclismo che ha abbandonato varie borracce e involucri di integratori lungo un sentiero naturalistico. Come intervieni?",
        "opzioni": [
            "Fai notare l'inciviltà del gesto, applichi la sanzione per abbandono di piccoli rifiuti e li inviti a raccoglierli.",
            "Chiedi se ti lasciano un integratore al gusto limone.",
            "Calpesti gli involucri per nasconderli nell'erba."
        ],
        "corretta": 0,
        "spiegazione": "L'abbandono di micro-rifiuti in natura è sanzionabile ed è un pessimo esempio per la fruizione sostenibile dei sentieri."
    }
]

# Progress Bar
progresso = (st.session_state.step) / len(domande)
st.progress(progresso)
st.caption(f"Avanzamento: Domanda {st.session_state.step + 1} di {len(domande)}")

# Logica di presentazione domande
if st.session_state.step < len(domande):
    q = domande[st.session_state.step]
    
    st.markdown(f"#### {q['categoria']}")
    st.info(q["scenario"])
    
    scelta = st.radio("Seleziona la tua decisione:", q["opzioni"], key=f"q_{st.session_state.step}")
    
    col1, col2 = st.columns([1, 1])
    
    with col1:
        if st.button("Conferma Risposta ➔"):
            idx_scelta = q["opzioni"].index(scelta)
            if idx_scelta == q["corretta"]:
                st.success(f"✅ RISPOSTA CORRETTA!\n\n{q['spiegazione']}")
                st.session_state.punteggio += 10
            else:
                st.error(f"❌ RISPOSTA ERRATA!\n\n{q['spiegazione']}")
            
            st.session_state.step += 1
            st.rerun()

    with col2:
        if st.session_state.step > 0:
            if st.button("⬅️ Torna Indietro"):
                st.session_state.step -= 1
                st.rerun()

else:
    st.balloons()
    st.header("🏆 Pattuglia Completata!")
    punteggio_max = len(domande) * 10
    st.write(f"Il tuo punteggio finale è: **{st.session_state.punteggio} / {punteggio_max} punti**.")
    
    percentuale = (st.session_state.punteggio / punteggio_max) * 100
    
    if percentuale == 100:
        st.success("🥇 ECCELLENTE! Sei una Guardia Ecologica Volontaria modello per Inverno e Monteleone!")
    elif percentuale >= 70:
        st.info("🥈 BUON LAVORO! Hai una buona conoscenza del regolamento ambientale locale.")
    else:
        st.warning("🥉 SERVE RIPASSO! Rileggi le norme ambientali prima di tornare in pattuglia.")

    if st.button("🔄 Ricomincia il Gioco"):
        st.session_state.punteggio = 0
        st.session_state.step = 0
        st.rerun()
            {
        "categoria": "🐝 Apicoltura e Insetti Utili",
        "scenario": "21. Trovi dei favi naturali di api in un pilone vicino al Parco Giardino. Un cittadino vuole distruggerli con un insetticida. Come intervieni?",
        "opzioni": [
            "Lo aiuti a spruzzare l'insetticida per sicurezza.",
            "Spieghi che le api sono protette e fondamentali per l'ecosistema, invitando a contattare un apicoltore per il recupero sicuro.",
            "Dai fuoco al pilone."
        ],
        "corretta": 1,
        "spiegazione": "Le api e gli impollinatori sono tutelati; la rimozione o il recupero degli sciami deve essere effettuato da personale esperto senza abbatterle."
    },
    {
        "categoria": "🌊 Tutela Argini e Fiumi",
        "scenario": "22. Un residente ha scavato un fossato privato modificando il corso di un canale di scolo comunale senza permessi. Cosa fai?",
        "opzioni": [
            "Rilevi l'opera idraulica abusiva che modifica il regime delle acque e la segnali al Consorzio di Bonifica e al Comune.",
            "Gli chiedi di scavare un altro canale anche per il tuo giardino.",
            "Fai finta di niente, l'acqua scorre comunque."
        ],
        "corretta": 0,
        "spiegazione": "Le modifiche ai reticoli idrici superficiali richiedono specifiche autorizzazioni per prevenire rischi idrogeologici e allagamenti."
    },
    {
        "categoria": "🪵 Legna da Ardere",
        "scenario": "23. Un cittadino sta raccogliendo legna secca caduta all'interno di una riserva naturale regionale protetta. È consentito?",
        "opzioni": [
            "Sì, la legna caduta si può prendere liberamente ovunque.",
            "No, nelle aree protette anche il legno morto a terra costituisce habitat essenziale per insetti decompositori e biodiversità.",
            "Sì, purché la carichi a mano senza usare carri."
        ],
        "corretta": 1,
        "spiegazione": "Nelle aree a riserva naturale rigida la legna morta decomponendosi arricchisce il suolo e sostiene la catena alimentare."
    }
