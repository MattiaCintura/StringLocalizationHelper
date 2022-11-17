import json

class DuplicateFile:
    def __init__(self, file_path: str):
        self.file_path = file_path

    def open_file(self) -> dict:
        with open(self.file_path, "r") as f:
            return json.load(f)
        
    def save_file(self, data: dict, filename: str = 'new_file.json'):
        with open(f'../tests/{filename}', 'w', encoding='utf8') as nf:
            json.dump(data, nf, indent=2, ensure_ascii=False)
