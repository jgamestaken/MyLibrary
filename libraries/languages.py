## MyLibrary - Handle Language Packs
## Currently supported:
## - Dutch
## - English
## All client facing UI uses language packs
############################################
## Start of script

import json
import os
from jinja2 import Template
from libraries.environhelper import get_safe_env

## Define language table

languages = {}
language_folder = "langpacks"

## Loader function

def _loadLanguage(name="en.json", folder="langpacks"):
    with open(folder+"/"+name) as langfile:
        lang_raw = langfile.read()
        lang_json = json.loads(lang_raw)

        lang_id = name.removesuffix(".json")

        languages[lang_id] = lang_json

## Find all language packs

language_files = [f for f in os.listdir(language_folder) if os.path.isfile(os.path.join(language_folder, f))]

## Import all language packs

for l in language_files:
    _loadLanguage(l)

############################################
## Language class

class Language:
    @staticmethod
    def getPreferredLanguage(): # Get the preferred language
        try:
            return os.getenv("LANGUAGE")
        except:
            return "en"
    
    @staticmethod
    def getLanguageString(page="index", id="welcome", lang=None): # Get a language string
        lang = lang or Language.getPreferredLanguage()
        lstring = languages[lang][page][id] # Get the correct language string

        return Template(lstring).render(env=get_safe_env())



