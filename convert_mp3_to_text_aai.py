import assemblyai as aai
import streamlit as st

aai.settings.api_key = st.secrets["assembly_ai"]

# URL of the file to transcribe
# FILE_URL = "./151693ab1b424fc681cd546258737d51.mp3"

config = aai.TranscriptionConfig(
    speaker_labels=True, speakers_expected=2, language_code="pt")


def transcribe(filename):
    transcriber = aai.Transcriber()
    transcript = transcriber.transcribe(filename, config=config)

    if transcript.status == aai.TranscriptStatus.error:
        print("error")
        print(transcript.error)
        exit(0)

    text = list()
    for sentence in transcript.utterances:
        # print(f"Pessoa {sentence.speaker}: {sentence.text}")

        text.append((f"{sentence.speaker}", sentence.text))

    return text
