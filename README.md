# String localization helper
This is a CLI tool to speed up the process of string localization built with Python.

## About the project
I got the idea to create this tool while I was working on a large Angular project featuring multiple JSON files containing lables, after adding a new label to a JSON file i found myself repeating the same action again and again to feature the same label in the other files.
So i came up with an idea, instead of going through this process every time i had to implement a new label I could have just created a single JSON file and later on generating as many file as I needed authomatically translated in multiple languages using an authomation.

## Built with
This CLI tool has been entirely developed using Python 3.11 equipped with [Rich](https://pypi.org/project/googletrans/) and [Googletrans](https://github.com/Textualize/rich).

## Getting Started
To lauch the script, the only command you need to run is the following
```
python3 string_localization_helper.py -f <your_json_file_path> -l <your_file_language> -tr <language_for_translation>
```
After a few moments you will find a new JSON file in the same directory as the file you used as a template 🚀

As of today there is a total **9 supported languages**.

| Emojy | Language  | Code |
|-------|-----------|------|
|  🇮🇹   | Italian   | it   |
|  🇬🇧   | English   | en   |
|  🇪🇸   | Spanish   | es   |
|  🇫🇷   | French    | fr   |
|  🇩🇪   | German    | de   |
|  🇨🇳   | Simplified Chinese | zh-CN |
|  🇹🇼   | Traditional Chinese | zh-TW |
|  🇯🇵   | Japanese | ja |
|  🇰🇷   | Korean   | ko |

Use the codes you see in this table to set the language.

