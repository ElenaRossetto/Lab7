import streamlit as st

# Titolo dell'applicazione
st.title("La mia prima applicazione Streamlit!")

# Messaggio di benvenuto
st.write("Benvenuti nella mia applicazione! Ecco un semplice esempio con Streamlit.")

# Aggiungi un'interazione
name = st.text_input("Come ti chiami?")
if name:
    st.write(f"Ciao, {name}! Grazie per aver provato Streamlit.")
