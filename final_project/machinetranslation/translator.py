'''Translation instance (IBM Watson) and translation functions

Written: 1st February 2023

'''
import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)

language_translator.set_service_url(url)

def english2french(english_text):
    '''Translation function, English to French
    
    Args:
        english_text(str): string with English text

    Return:
        french_text(str): string with French text translation

    '''
    translation = language_translator.translate(
        text=english_text,
        model_id='en-fr').get_result()
    french_text = translation['translations'][0]['translation']
    return french_text

def french2english(french_text):
    '''Translation function, French to English
    
    Args:
        french_text(str): string with French text

    Return:
        english_text(str): string with English text translation

    '''
    translation = language_translator.translate(
        text=french_text,
        model_id='fr-en').get_result()
    english_text = translation['translations'][0]['translation']
    return english_text    