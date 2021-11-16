"""
    This is a Translator that translate from English to French and vice-versa
"""
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

language_translator.set_service_url('https://api.us-south.language-translator.watson.cloud.ibm.com')

def english_to_french(english_text):
    """
        Translates from english to french
    """
    if english_text is None:
        return None
    translated = language_translator.translate(text=english_text, model_id='en-fr').get_result()
    return translated["translations"][0]["translation"]

def french_to_english(french_text):
    """
        Translates from french to english
    """
    if french_text is None:
        return None
    translated = language_translator.translate(text=french_text, model_id='fr-en').get_result()
    return translated["translations"][0]["translation"]
    