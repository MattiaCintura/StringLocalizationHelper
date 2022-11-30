import argparse
from rich.console import Console

from duplicate_file import DuplicateFile
from translate_strings import TranslateString
from util import Util

parser = argparse.ArgumentParser(
    description=""
)

parser.add_argument(
    "-f",
    help="File that wil be used as a template",
    type=str, required=True
)

parser.add_argument(
    "-l",
    help="Language of the choosen file", 
    type=str, required=True
)

parser.add_argument(
    "-tr",
    help="Language used to translate the given file, if not provided the default language is english",
    type=str, required=False
)

console = Console()

if __name__ == "__main__":
    with console.status('[bold green]Working on tasks...') as status:
        args = parser.parse_args()
        dup = DuplicateFile(args.f)
        trans = TranslateString(args.l)
        file = dup.open_file()
        new_data = trans.translate_dict(file, args.tr)
        new_filename = f'{args.tr}.json'
        dup.save_file(new_data, new_filename)
        console.print(f'📄 {Util.lang_dict[args.tr]} [cyan]{new_filename}[/cyan] succesfully created!')

