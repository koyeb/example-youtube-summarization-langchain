from decouple import config
from deepgram import Deepgram

DEEPGRAM_API_KEY = config('DEEPGRAM_API_KEY')


def transcribe_audio(filename):
    dg_client = Deepgram(DEEPGRAM_API_KEY)
    with open(filename, 'rb') as audio:
        source = {'buffer': audio, 'mimetype': 'audio/mp3'}
        response = dg_client.transcription.sync_prerecorded(source,
                                                            model='nova-2-ea',
                                                            smart_format=True)
        transcript = response['results']['channels'][0]['alternatives'][0]['transcript']
        return transcript
