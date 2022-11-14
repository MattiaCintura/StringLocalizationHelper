from googletrans import Translator

class TranslateString:
    def __init__(self, current_lang: str):
        self.translator = Translator()
        self.current_lang = current_lang

    def translate_one(self, text: str, lang: str):
        return self.translator.translate(text, dest=lang, src=self.current_lang).text

    def translate_more(self, text: str, lang: list):
        output_map = list()
        for l in lang:
           out = self.translator.translate(text, dest=l, src=self.current_lang)
           def_text = out.text.split(';')[0]
           output_map.append((def_text, l))
        return output_map
           

trans = TranslateString('it')
lang_list = ['en', 'es', 'de', 'fr', 'zh-tw', 'ja', 'ko', 'hi', 'th']
out = trans.translate_more('accedi', lang_list)
for _ in out:
    print(f'{_[0]} -> {_[1]}')
