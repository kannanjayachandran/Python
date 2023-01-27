# Interactive Dictionary

This is a simple interactive dictionary that allows you to search for a word and get its definition. If the word is not found, it will suggest a similar word. At present it uses a json file as the database. In the future, I will be adding a database to it. Or may be using a dictionary API.

## How to use

1. Download the files and run the `main.py` file.
2. Enter a word and press enter.
3. If the word is found, it will display the definition.
4. If the word is not found, it will suggest a similar word.
5. If no similar word is found, it will display a message saying so.

## How to add a word

1. Open the `data.json` file.
2. Add a new word in the following format:

```
"word": {
    "definition": "definition of the word"
}
```

3.Save the file.
