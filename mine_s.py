import streamlit as st
import time

# Page setup
st.set_page_config(page_title="For My Love Susri 💌", page_icon="💖", layout="centered")

# Background and floating hearts
page_bg = """
<style>
[data-testid="stAppViewContainer"] {
    background-image: url("https://i.imgur.com/0ZfBqOT.jpeg");
    background-size: cover;
    background-position: center;
    overflow: hidden;
}
h1, h2, h3, p {
    color: #ff007f;
    text-align: center;
    font-family: "Comic Sans MS", cursive, sans-serif;
    margin: 10px auto;
    word-wrap: break-word;
    max-width: 90%;
}
.love {
    font-size: 2em;
    animation: glow 1.5s ease-in-out infinite alternate;
}
@keyframes glow {
    from { text-shadow: 0 0 10px #ff6699, 0 0 20px #ff99cc; }
    to { text-shadow: 0 0 20px #ff33aa, 0 0 40px #ff66cc; }
}

/* Floating hearts */
@keyframes float {
    0% { transform: translateY(100vh) scale(0.5); opacity: 0; }
    50% { opacity: 1; }
    100% { transform: translateY(-10vh) scale(1); opacity: 0; }
}
.heart {
    position: fixed;
    bottom: 0;
    left: 50%;
    font-size: 22px;
    animation: float 6s ease-in-out infinite;
}
.heart:nth-child(2) { left: 20%; animation-duration: 7s; font-size: 18px; }
.heart:nth-child(3) { left: 70%; animation-duration: 8s; font-size: 20px; }
.heart:nth-child(4) { left: 40%; animation-duration: 5s; font-size: 16px; }
.heart:nth-child(5) { left: 80%; animation-duration: 6.5s; font-size: 21px; }

button[kind="primary"] {
    background-color: #ff4b9b !important;
    color: white !important;
    border-radius: 12px !important;
    padding: 0.6em 1.2em !important;
    font-size: 1.1em !important;
}
</style>

<div class="heart">💖</div>
<div class="heart">💘</div>
<div class="heart">💞</div>
<div class="heart">💓</div>
<div class="heart">💗</div>
"""
st.markdown(page_bg, unsafe_allow_html=True)

# Title
st.markdown("<h1>💖 Hey My Sweet Susri 💖</h1>", unsafe_allow_html=True)
st.markdown("<h3>I have something truly special for you...</h3>", unsafe_allow_html=True)

# Typewriter animation
def typewriter(message, speed=0.08):
    placeholder = st.empty()
    full_text = ""
    for char in message:
        full_text += char
        placeholder.markdown(f"<h2 style='text-align:center;'>{full_text}</h2>", unsafe_allow_html=True)
        time.sleep(speed)

# Reveal button
if st.button("Tap Here My Love 💌"):
    # Play music on button click
    music_html = """
    <audio autoplay>
        <source src="https://cdn.pixabay.com/audio/2023/03/03/audio_4cc1bb1531.mp3" type="audio/mpeg">
    </audio>
    """
    st.markdown(music_html, unsafe_allow_html=True)

    with st.spinner("Just for you, my dearest Susri... 💞"):
        time.sleep(1.5)
    st.balloons()
    typewriter("I LOVE YOU, SUSRI ❤", speed=0.12)
    time.sleep(0.5)
    st.markdown("<h2 class='love'>You’re my heartbeat, my happiness, my forever 💫</h2>", unsafe_allow_html=True)
    st.markdown("<h3>💋 💖 🌹 😘 💕 💞 💓 💗 💝 💘 💌</h3>", unsafe_allow_html=True)

# Footer
st.markdown("<br><hr><p style='text-align:center; font-size:14px;'>Made with 💗 only for you, Susri</p>", unsafe_allow_html=True)
