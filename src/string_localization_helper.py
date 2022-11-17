import argparse
from rich.console import Console

from duplicate_file import DuplicateFile
from translate_strings import TranslateString

lang_dict = {
    "it": "🇮🇹 ",
    "en": "🇬🇧 ",
    "es": "🇪🇸 ",
    "fr": "🇫🇷 ",
    "de": "🇩🇪 ",
    "zh-CN": "🇨🇳 ",
    "zh-TW": "🇹🇼 ",
    "ja": "🇯🇵 ",
    "ko": "🇰🇷 "
}

parser = argparse.ArgumentParser(
    description=""
)

parser.add_argument(
    "-f", "--file",
    help="File that wil be used as a template",
    type=str, required=True
)

parser.add_argument(
    "-l", "--file_language",
    help="Language of the choosen file", 
    type=str, required=True
)

parser.add_argument(
    "-tr", "--translate",
    help="Language used to translate the given file, if not provided the default language is english",
    type=str, required=False
)

console = Console()

if __name__ == "__main__":
    with console.status('[bold green]Working on tasks...') as status:
        args = parser.parse_args()
        dup = DuplicateFile(args.file)
        trans = TranslateString(args.file_language)
        file = dup.open_file()
        new_data = trans.translate_dict(file, args.translate)
        dup.save_file(new_data, f'{args.translate}.json')
        console.print(f'📄 {lang_dict[args.translate]} File [cyan]{args.translate}.json[/cyan] creato con successo!')

