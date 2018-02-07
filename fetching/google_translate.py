# https://cloud.google.com/translate/docs/reference/libraries#client-libraries-install-python
from google.cloud import translate
from os import environ
environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'creds-google-cloud.json'


def helloworld():
    ## Quickie example:
    # Instantiates a client
    translate_client = translate.Client()

    # The text to translate
    text = 'Hello, world!'
    # The target language
    target = 'es'

    # Translates some text into Spanish
    translation = translate_client.translate(
        text,
        target_language=target)

    print('Text: {}'.format(text))
    print('Translation: {}'.format(translation['translatedText']))


def get_translation(text, target_lang, source_lang='en'):
    client  = translate.Client()
    translation = client.translate(text, target_language=target_lang,
                                         source_language=source_lang)
    return translation


def pick_random_languages(n=5, exclude_langs=['en']):
    client = translate.Client()
    languages = [t for t in translate_client.get_languages() if t['language'] not in exclude_langs]

    return random.sample(languages, n)

def telephone(start_text, n=5, source_lang='en'):
    results = []
    thetext = start_text
    orglang = thelang = source_lang
    randolangs = pick_random_languages(n)

    for lang in randolangs:
        nextlang = lang['language']
        result = get_translation(thetext,
                                source_lang=thelang,
                                target_lang=nextlang)

        thetext = result['translatedText']
        thelang = nextlang
        results.append(result)
    ## one more translation back into the source language:
    lastresult = get_translation(thetext,
                                source_lang=thelang,
                                target_lang=orglang)

    results.append(lastresult)

    return results
