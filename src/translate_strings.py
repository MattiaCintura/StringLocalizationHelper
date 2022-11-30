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

    def get_all_keys(self, d: dict):
        for key, value in d.items():
            yield key
            if isinstance(value, dict):
                yield from self.get_all_keys(value)
    
    def translate_dict(self, data: dict, lang: str = 'en') -> dict:
        new_data = data
        for first_key in data:
            for k, v in data[first_key].items():
                new_value = self.translate_one(v, lang)
                new_data[first_key][k] = new_value.capitalize()
        return new_data
