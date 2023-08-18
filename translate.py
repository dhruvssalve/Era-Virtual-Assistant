from googletrans import Translator, LANGUAGES
# import googletrans 
def lang_translate(text, language):
    if language in LANGUAGES.values():
        translator = Translator()
        result = translator.translate(text, dest=language)
        return result
    else:
        return "None"

print(lang_translate("तुम्हारा नाम क्या हे","english").text)