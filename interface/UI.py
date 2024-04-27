import streamlit as st
from inference import get_answer
from interface.get_answer_horoscope import get_answer_horoscope
import sys
import os
import random
sys.path.insert(1, os.getcwd())

# App title
st.set_page_config(page_title="🔮💬Astrology Bot: AI Clairvoyant")


st.title('🔮💬Astrology Bot: AI Clairvoyant')
st.caption("🚀 A streamlit chatbot powered by Llama-2-7b")


menu = ["Home", "Horoscope","Tarot"]

choice = st.sidebar.selectbox("Menu", menu)
if choice == "Home":
    st.subheader("Home")
    st.write("This is the home page.")
elif choice == "Horoscope":
    st.image('./images/astrology-horoscope-circle.jpg.webp', caption=None, width=None, use_column_width=None, clamp=False, channels="RGB", output_format="auto")
    if "messages" not in st.session_state:
        st.session_state["messages"] = [{"role":  "AI Clairvoyant", "content": "Greetings, dear seeker. I am Estelle, the clairvoyant, and your cosmic guide. What do they call you and what is your question?"}]
        
    for msg in st.session_state.messages:
        st.chat_message(msg["role"]).write(msg["content"])
    if prompt_horoscope := st.chat_input():
        st.session_state.messages.append({"role": "user", "content": prompt_horoscope})
        st.chat_message("user").write(prompt_horoscope)
        answer_horoscope = get_answer_horoscope(question = prompt_horoscope)
        msg_horoscope = f"The answer of your question is \n {answer_horoscope}."
        st.session_state.messages.append({"role":  "AI Clairvoyant", "content": msg_horoscope})
        st.chat_message("AI Clairvoyant").write(msg_horoscope)

elif choice == "Tarot":
    
    st.image('images/tarot.jpg', caption=None, width=None, use_column_width=None, clamp=False, channels="RGB", output_format="auto")
    if "messages" not in st.session_state:
        st.session_state["messages"] = [{"role":  "AI Clairvoyant", "content": "Greetings, dear seeker. I am Estelle, the clairvoyant, and your cosmic guide. What do they call you and what is your question? Please select 3 cards below."}]

    for msg in st.session_state.messages:
        st.chat_message(msg["role"]).write(msg["content"])
        all_cards = ['fool', 'magician', 'high priestess', 'empress', 'emperor', 'hierophant', 'lovers', 
                        'chariot', 'strength', 'hermit', 'wheel of fortune', 'justice', 'hanged-man', 'death',
                        'temperance', 'devil', 'tower', 'star', 'moon', 'sun', 'judgement', 'world',
                        'ace-of-pentacles', 'two-of-pentacles', 'three-of-pentacles', 'four-of-pentacles',
                                                'five-of-pentacles', 'six-of-pentacles', 'seven-of-pentacles', 'eight-of-pentacles',
                                                'nine-of-pentacles', 'ten-of-pentacles', 'page-of-pentacles', 'knight-of-pentacles',
                                                'queen-of-pentacles', 'king-of-pentacles',
                    'ace-of-swords', 'two-of-swords', 'three-of-swords', 'four-of-swords', 'five-of-swords',
                                            'six-of-swords', 'seven-of-swords', 'eight-of-swords', 'nine-of-swords', 'ten-of-swords',
                                            'page-of-swords', 'knight-of-swords', 'queen-of-swords', 'king-of-swords',
                    'ace-of-wands', 'two-of-wands', 'three-of-wands', 'four-of-wands', 'five-of-wands',
                                        'six-of-wands', 'seven-of-wands', 'eight-of-wands', 'nine-of-wands', 'ten-of-wands',
                                        'page-of-wands', 'knight-of-wands', 'queen-of-wands', 'king-of-wands',
                    'ace-of-cups', 'two-of-cups', 'three-of-cups', 'four-of-cups', 'five-of-cups',
                                        'six-of-cups', 'seven-of-cups', 'eight-of-cups', 'nine-of-cups', 'ten-of-cups',
                                        'page-of-cups', 'knight-of-cups', 'queen-of-cups', 'king-of-cups']
        cards = st.multiselect("Select 3-5 cards", all_cards, key="cards")
        position = ['upright', 'reversed']
        cards_final = [c+'_'+position[random.randint(0, 1)] for c in cards]

    if prompt_tarot := st.chat_input():
        st.session_state.messages.append({"role": "user", "content": prompt_tarot})
        st.chat_message("user").write(prompt_tarot)
        answer, context = get_answer(question = prompt_tarot, cards = cards_final)
        msg1 = answer[0].split('\",')[0].strip('\"')
        st.session_state.messages.append({"role":  "AI Clairvoyant", "content": msg1})
        st.chat_message("AI Clairvoyant").write(msg1)
        msg2 = f"I generated the response based on the following context from Tarot.com: \n{context}"
        st.session_state.messages.append({"role":  "AI Clairvoyant", "content": msg2})
        st.chat_message("AI Clairvoyant").write(msg2)