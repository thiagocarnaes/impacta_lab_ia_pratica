import streamlit as st
import uuid
from moviepy.editor import AudioFileClip

import convert_mp3_to_text_aai as convert


def mp4_to_mp3(mp4_filename, mp3_filename):
    file_to_convert = AudioFileClip(mp4_filename)
    file_to_convert.write_audiofile(mp3_filename)
    file_to_convert.close()


st.title("Automação de atas")

st.write("Criando uma ferramenta de automação de atas")


uploaded_file = st.file_uploader(
    "Selecione o seu arquivo", accept_multiple_files=False, type=['mp4'])

if uploaded_file:

    mp3_filename = ""
    with st.spinner("Convertendo de mp4 para mp3"):
        mp4_filename = uploaded_file.name
        mp3_filename = mp3_filename = '{filename}.mp3'.format(
            filename=uuid.uuid4().hex)

        tempfile = open(mp4_filename, 'wb')
        tempfile.write(uploaded_file.read())

        mp4_to_mp3(mp4_filename, mp3_filename)

        st.text(mp3_filename)

    with st.spinner("Convertendo de mp3 para texto"):

        text = convert.transcribe(mp3_filename)

        for line in text:

            st.write(f"Pessoa {line[0]}: ", line[1])
