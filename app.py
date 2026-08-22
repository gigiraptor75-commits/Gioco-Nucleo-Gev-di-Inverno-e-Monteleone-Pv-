import streamlit as st

# Configurazione pagina
st.set_page_config(page_title="GEV Inverno e Monteleone", page_icon="🌲")

# Titolo e introduzione
st.title("🌲 GEV Inverno e Monteleone - The Game")
st.subheader("Sei pronto a diventare una Guardia Ecologica Volontaria?")

st.write(
    "Benvenuto! Indossa la divisa e pattuglia il territorio tra Inverno e Monteleone. "
    "Rispondi alle domande per guadagnare punti ecologia e proteggere l'ambiente locale."
)

# Gestione dello stato del gioco
if "punteggio" not in st.session_state:
    st.session_state.punteggio = 0
if "step" not in st.session_state:
    st.session_state.step = 0

# Lista delle domande/scenario di gioco
domande = [
    {
        "scenario": "🚨 Durante una pattuglia lungo i sentieri campestri verso Monteleone, noti dei rifiuti abbandonati (macerie e plastica). Cosa fai?",
        "opzioni": [
            "Ignori il problema, non è di tua competenza.",
            "Scatti delle foto, geolocalizzi l'area e scrivi una segnalazione agli organi competenti.",
            "Dai fuoco ai rifiuti per smaltirli subito."
        ],
        "corretta": 1,
        "spiegazione": "Corretto! Le GEV monitorano il territorio e segnalano gli illeciti ambientali agli enti responsabili."
    },
    {
        "scenario": "🍄 È autunno. Incontri un cittadino nei boschi locali che sta raccogliendo funghi senza tesserino e usando un sacchetto di plastica chiuso. Cosa gli spieghi?",
        "opzioni": [
            "Gli dici che il sacchetto di plastica impedisce la dispersione delle spore e che serve la cesta in vimini.",
            "Gli fai i complimenti per l'ottimo raccolto.",
            "Gli dici che nei boschi si può raccogliere qualsiasi cosa senza limiti."
        ],
        "corretta": 0,
        "spiegazione": "Esatto! I funghi vanno raccolti in contenitori traforati (come le ceste) per permettere la diffusione delle spore."
    },
    {
        "scenario": "🔥 Un contadino sta bruciando delle sterpaglie vicino al margine del bosco in un periodo di grave secca. Cosa fai?",
        "opzioni": [
            "Informi subito il cittadino sui divieti regionali per il rischio incendi e contatti i Vigili del Fuoco se necessario.",
            "Ti fermi a scaldarti le mani.",
            "Gli versi sopra della benzina."
        ],
        "corretta": 0,
        "spiegazione": "Ottimo! La prevenzione degli incendi boschivi è fondamentale nei periodi di secca."
    }
]

# Logica di avanzamento del gioco
if st.session_state.step < len(domande):
    q = domande[st.session_state.step]
    st.markdown(f"### Scenario {st.session_state.step + 1}")
    st.info(q["scenario"])
    
    scelta = st.radio("Cosa decidi di fare?", q["opzioni"], key=f"q_{st.session_state.step}")
    
    if st.button("Conferma Scelta"):
        indice_scelta = q["opzioni"].index(scelta)
        if indice_scelta == q["corretta"]:
            st.success(f"✅ {q['spiegazione']}")
            st.session_state.punteggio += 10
        else:
            st.error("❌ Scelta sbagliata! Questo comportamento danneggia l'ambiente.")
        
        st.session_state.step += 1
        st.button("Prossimo Scenario ➡️")

else:
    st.balloons()
    st.header("🏆 Pattuglia Completata!")
    st.write(f"Il tuo punteggio finale è: **{st.session_state.punteggio} / {len(domande) * 10} punti**.")
    
    if st.session_state.punteggio == len(domande) * 10:
        st.success("Complimenti! Sei un'eccellente Guardia Ecologica Volontaria di Inverno e Monteleone!")
    else:
        st.warning("Hai fatto un buon lavoro, ma ripassa il regolamento ambientale prima della prossima pattuglia.")

    if st.button("Rigioca"):
        st.session_state.punteggio = 0
        st.session_state.step = 0
        st.rerun()
