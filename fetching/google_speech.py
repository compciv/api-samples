from google.cloud import speech
from google.cloud.speech import enums
from google.cloud.speech import types
from os import environ
environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'google-cloud-creds.json'

client = speech.SpeechClient()

# InvalidArgument: 400 Request payload size exceeds the limit: 10485760 bytes.
# tmp $ ffmpeg -i full-audio.wav -ss 00:00:02 -t 00:00:07 -ar 16000 -ac 1 audio.wav

with open('audio.wav', 'rb') as sf:
    soundbytes = sf.read()
    audio = types.RecognitionAudio(content=soundbytes)

auconfig = types.RecognitionConfig(
                enable_word_time_offsets=True,
                language_code='en-US')

response = client.recognize(auconfig, audio)

# for result in response.results:
print('Transcript: {}'.format(result.alternatives[0].transcript))
