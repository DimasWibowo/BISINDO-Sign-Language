import streamlit as st

def initialize_session_state():
    if 'current_question' not in st.session_state:
        st.session_state.current_question = 0
    if 'player_score' not in st.session_state:
        st.session_state.player_score = 0

def update_score(player_choice, correct_answer):
    if player_choice.lower() == correct_answer.lower():
        st.session_state.player_score += 1

def calculate_score(player_choice):
    correct_answer = quiz_questions[st.session_state.current_question]['answer']
    update_score(player_choice, correct_answer)
    st.session_state.current_question += 1

quiz_questions = [
    {
        'image_path': 'gambar_soal/gambar_A.jpg',
        'answer': 'A'
    },
    # Tambahkan pertanyaan lainnya di sini...
    {
        'image_path': 'gambar_soal/gambar_K.jpg',
        'answer': 'K'
    }
]

# CSS untuk pusatkan konten
centered_style = """
    <style>
    .centered {
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        height: 21vh;
        text-align: center;
    }
    </style>
"""

st.markdown(centered_style, unsafe_allow_html=True)

initialize_session_state()

ind = st.session_state.current_question

if ind < len(quiz_questions):
    current_question = quiz_questions[ind]
    image_path = current_question["image_path"]
    
    st.markdown("<div class='centered'><h1>Mini Game</h1></div>", unsafe_allow_html=True)
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.image(image_path, width=300, caption=f"Question {ind + 1}/{len(quiz_questions)}")  # Mengatur lebar gambar menjadi 300 piksel dan menambahkan keterangan
        
    player_choice = st.text_input("Your Answer", key=f"question_{ind}") 

    # Memposisikan tombol Submit di tengah
    col1, col2, col3 = st.columns([1, 1, 1])
    with col1:
        if st.button("Submit", key=f"submit_{ind}"):
            calculate_score(player_choice)
            
            if st.session_state.current_question < len(quiz_questions):
                st.experimental_rerun()

            if st.session_state.current_question >= len(quiz_questions):
                st.success("Kuis Telah Selesai")
                st.button("Cek Nilai Anda", on_click=initialize_session_state)
else:
    st.warning(f"Selamat anda telah menyelesaikan mini game. Nilai Anda:{st.session_state.player_score}")
    if st.button("Main Lagi"):
        st.session_state.current_question = 0
        st.session_state.player_score = 0
