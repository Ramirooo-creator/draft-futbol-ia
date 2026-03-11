import streamlit as st
import random

# Configuración inicial
st.set_page_config(page_title="Draft de Fútbol 11", layout="centered")
st.title("⚽ El Mejor 11: Duelo de Managers")

# Base de datos precaria de clubes (puedes agregar más)
CLUBES = ["Real Madrid", "Man City", "Boca Juniors", "Liverpool", "Bayern", "PSG", "Inter", "Arsenal", "FC Barcelona", "River Plate", "Napoli", "Chelsea", "Milan", "Atletico Madrid"]

# Inicializar estados de juego
if 'ronda' not in st.session_state:
    st.session_state.ronda = 0
    st.session_state.equipo_jugador = []
    st.session_state.clubes_sorteados = random.sample(CLUBES, 11)

# 1. Elegir Formación
formacion = st.sidebar.selectbox("Elige tu formación", ["4-3-3", "4-4-2", "3-5-2", "5-3-2"])

# 2. Mecánica del Juego
if st.session_state.ronda < 11:
    club_actual = st.session_state.clubes_sorteados[st.session_state.ronda]
    st.subheader(f"Ronda {st.session_state.ronda + 1} de 11")
    st.info(f"Club sorteado: **{club_actual}**")
    
    jugador = st.text_input(f"¿A quién eliges del {club_actual}?", key=f"input_{st.session_state.ronda}")
    
    if st.button("Confirmar Jugador"):
        if jugador:
            st.session_state.equipo_jugador.append({"club": club_actual, "jugador": jugador})
            st.session_state.ronda += 1
            st.rerun()
else:
    # 3. Resultado Final
    st.success("¡Tu 11 está completo!")
    for item in st.session_state.equipo_jugador:
        st.write(f"- {item['jugador']} ({item['club']})")
    
    # 4. Simulación del Ganador (IA "Simple")
    if st.button("¿Quién gana? (Consultar a la IA)"):
        # Aquí simulamos la lógica: en un entorno real usarías la API de Gemini
        st.write("### El veredicto de la IA:")
        st.write("Analizando químicas, defensa y ataque...")
        ganador = "¡Tu equipo es una locura! Ganarías por peso histórico." if "Boca Juniors" in str(st.session_state.equipo_jugador) else "Tu amigo tiene un mediocampo más sólido."
        st.balloons()
        st.info(ganador)
        
    if st.button("Reiniciar Juego"):
        st.session_state.clear()
        st.rerun()
