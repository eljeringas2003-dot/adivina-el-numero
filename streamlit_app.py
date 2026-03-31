import streamlit as st
import random

st.set_page_config(page_title="Adivina el Número", page_icon="🎯")
st.title("🎯 ¡Adivina el Número, Nico!")
st.write("He pensado un número entre 1 y 100. ¿Traes la puntería de un CNC?")

if 'numero_secreto' not in st.session_state:
    st.session_state.numero_secreto = random.randint(1, 100)
    st.session_state.intentos = 0

tiro = st.number_input("Tu número:", min_value=1, max_value=100, step=1)

if st.button("Probar suerte"):
    st.session_state.intentos += 1
    if tiro < st.session_state.numero_secreto:
        st.warning("¡Más arriba! Súbele al torque.")
    elif tiro > st.session_state.numero_secreto:
        st.info("Te pasaste de revoluciones. Más abajo...")
    else:
        st.success(f"¡A HUEVO! Lo lograste en {st.session_state.intentos} intentos.")
        st.balloons()
