import argparse
from rich.console import Console

from duplicate_file import DuplicateFile
from translate_strings import TranslateString

parser = argparse.ArgumentParser(
    description=""
)

parser.add_argument("-f", "--file", help="File that wil be used as a template", type=str)
parser.add_argument("-l", "--file_language", help="Language of the choosen file", type=str)
parser.add_argument("-tr", "--translate", help="Language used to translate", type=str)

console = Console()

if __name__ == "__main__":
    with console.status("[bold green]Working on tasks...") as status:
        args = parser.parse_args()
        dup = DuplicateFile(args.file)
        trans = TranslateString('it')
        file = dup.open_file()
        new_data = trans.translate_dict(file)
        dup.save_file(new_data, 'en.json')
        console.print('📄 File [blue]en.json[/blue] creato con successo!')

