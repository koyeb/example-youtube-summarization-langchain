import streamlit as st

from download import download_audio_from_url
from summarize import summarize_transcript
from transcribe import transcribe_audio

# Set page title
st.set_page_config(page_title="YouTube Video Summarization", page_icon="📜", layout="wide")


# Set title
st.title("YouTube Video Summarization", anchor=False)
st.header("Summarize YouTube videos with AI", anchor=False)

# Input URL
st.divider()
url = st.text_input("Enter YouTube URL", value="")

# Download audio
st.divider()
if url:
    with st.status("Processing...", state="running", expanded=True) as status:
        st.write("Downloading audio file from YouTube...")
        audio_file, length = download_audio_from_url(url)
        st.write("Transcribing audio file..")
        transcript = transcribe_audio(audio_file)
        st.write("Summarizing transcript...")
        with open("transcript.txt", "w") as f:
            f.write(transcript)
        summary = summarize_transcript("transcript.txt")
        status.update(label="Finished", state="complete")

    # Play Audio
    st.divider()
    st.audio(audio_file, format='audio/mp3')

    # Show Summary
    st.subheader("Summary:", anchor=False)
    st.write(summary)
