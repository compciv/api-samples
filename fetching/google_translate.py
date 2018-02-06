# https://cloud.google.com/translate/docs/reference/libraries#client-libraries-install-python
from google.cloud import translate
from os import environ
environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'google-cloud-creds.json'


# Instantiates a client
translate_client = translate.Client()

# The text to translate
text = 'Hello, world!'
# The target language
target = 'ru'

# Translates some text into Russian
translation = translate_client.translate(
    text,
    target_language=target)

print('Text: {}'.format(text))
print('Translation: {}'.format(translation['translatedText']))
