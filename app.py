import streamlit as st
import random

st.set_page_config(page_title="GEV Inverno e Monteleone - Infiniti Scenari", page_icon="🌲")

st.title("🌲 GEV Inverno e Monteleone - Generatore Infinito")
st.subheader("Pattuglia virtuale con scenari generati automaticamente")

# Inizializzazione dello stato di gioco
if "punteggio" not in st.session_state:
    st.session_state.punteggio = 0
if "domanda_corrente" not in st.session_state:
    st.session_state.domanda_corrente = None
if "domande_fatte" not in st.session_state:
    st.session_state.domande_fatte = 0

# Modelli per la generazione automatica delle domande
LUOGHI = ["lungo i sentieri verso Monteleone", "vicino alle rogge di Inverno", "ai margini dei boschi comunali", "in prossimità di un campo agricolo", "lungo la strada vicinale"]
SOGGETTI = ["Un escursionista", "Un residente locale", "Un gruppo di giovani", "Un agricoltore", "Un ciclista"]

TEMATICHE = [
    {
        "categoria": "🗑️ Rifiuti",
        "azione": "sta abbandonando sacchi di plastica con rifiuti domestici",
        "corretta": "Contesti l'abbandono di rifiuti, compili il verbale e richiedi la bonifica.",
        "sbagliate": ["Aiuti la persona a nascondere i sacchi tra le siepi.", "Fai finta di nulla perché sono pochi rifiuti."]
    },
    {
        "categoria": "🔥 Incendi",
        "azione": "sta accendendo un piccolo falò con sterpaglie in un periodo di secca",
        "corretta": "Informi del divieto regionale per rischio incendi e chiedi l'immediato spegnimento.",
        "sbagliate": ["Ti fermi a scaldarti le mani.", "Suggerisci di spostare il fuoco più vicino agli alberi."]
    },
    {
        "categoria": "🐶 Fauna",
        "azione": "lascia correre dei cani senza guinzaglio che disturbano gli uccelli nidificanti",
        "corretta": "Richiedi di legare i cani al guinzaglio come previsto dalle norme di tutela fauna.",
        "sbagliate": ["Complimenti la persona per la vivacità dei cani.", "Suggerisci di lasciarli liberi anche nelle riserve."]
    },
    {
        "categoria": "🚗 Veicoli",
        "azione": "sta percorrendo con una moto da cross un sentiero pedonale interdetto",
        "corretta": "Annoti la targa in sicurezza per la segnalazione delle norme sulla viabilità agro-silvo-pastorale.",
        "sbagliate": ["Ti lanci davanti alla moto per fermarla.", "Chiedi di fare un giro come passeggero."]
    },
    {
        "categoria": "🍄 Sottobosco",
        "azione": "raccoglie funghi usando buste di plastica chiuse invece di ceste traforate",
        "corretta": "Spieghi l'obbligo di usare contenitori rigidi e traforati per far disperdere le spore.",
        "sbagliate": ["Confischi i funghi per mangiarli a cena.", "Dici che la plastica mantiene i funghi più freschi."]
    }
]

def genera_nuova_domanda():
    luogo = random.choice(LUOGHI)
    soggetto = random.choice(SOGGETTI)
    tema = random.choice(TEMATICHE)
    
    scenario = f"Durante una pattuglia {luogo}, noti che {soggetto.lower()} {tema['azione']}. Cosa fai?"
    
    opzioni = [tema['corretta']] + tema['sbagliate']
    random.shuffle(opzioni)
    
    return {
        "categoria": tema['categoria'],
        "scenario": scenario,
        "opzioni": opzioni,
        "corretta": opzioni.index(tema['corretta'])
    }

# Genera prima domanda se non esiste
if st.session_state.domanda_corrente is None:
    st.session_state.domanda_corrente = genera_nuova_domanda()

q = st.session_state.domanda_corrente

st.markdown(f"### Domanda #{st.session_state.domande_fatte + 1} | {q['categoria']}")
st.info(q["scenario"])

scelta = st.radio("Seleziona l'intervento corretto:", q["opzioni"], key=f"rnd_{st.session_state.domande_fatte}")

if st.button("Conferma Scelta"):
    idx_scelta = q["opzioni"].index(scelta)
    if idx_scelta == q["corretta"]:
        st.success("✅ Intervento corretto! Hai dimostrato ottime competenze GEV.")
        st.session_state.punteggio += 10
    else:
        st.error("❌ Decisione errata! Questo comportamento viola le norme ambientali.")
    
    st.session_state.domande_fatte += 1

if st.button("Prossimo Scenario Generato ➡️"):
    st.session_state.domanda_corrente = genera_nuova_domanda()
    st.rerun()

st.divider()
st.metric("Punteggio Accumulato", f"{st.session_state.punteggio} pt", f"{st.session_state.domande_fatte} scenari affrontati")
