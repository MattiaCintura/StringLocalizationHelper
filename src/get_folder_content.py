import os
import json
from pick import pick
from rich.console import Console
from rich.table import Table
from pathlib import Path

class GetFolderContent:
    def __init__(self, current_path: Path) -> None:
        self.console = Console()
        self.current_path = current_path
        self.json_file_list = list()

    def open_cuttent_folder(self) -> None:
        lang_dict = {
            "it": "🇮🇹 ",
            "en": "🇬🇧 ",
            "es": "🇪🇸 ",
            "fr": "🇫🇷 ",
            "de": "🇩🇪 ",
            "zh": "🇨🇳 ",
            "zh-TW": "🇹🇼 ",
            "jo": "🇯🇵 ",
            "ko": "🇰🇷 "
        }
        for file in sorted(os.listdir(self.current_path)):
            if ".json" in file:
                flag_emoji = lang_dict[file.split(".")[0]]
                self.json_file_list.append(f"{flag_emoji} {file}")

        selected_file, index = pick(self.json_file_list, indicator="->")

        with open(selected_file[4:], "r") as string_file:
            dict_from_json = json.load(string_file)

        table = Table(show_header= True, title= selected_file, width=60, header_style="bold cyan")
        table.add_column("Title")
        table.add_column("Value")
        for row in dict_from_json:
            table.add_row(row, "*")

        self.console.print(table)
