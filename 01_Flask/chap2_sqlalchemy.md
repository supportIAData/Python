# SQLAlchemy

## Installation Windows

récupérez les sources de SQLlite : https://www.sqlite.org/download.html

sqlite-dll-win64-x64-xxxxxxx.zip

Ajoutez dans les variables d'environnement le chemin vers 

Lancez votre terminale et testez si SQLite est disponible 

```bash
sqlite3 --version
```

## Installation Mac

Si ce n'est pas déjà installée sur votre machine, vérifiez avant dans un terminale :

```bash
sqlite3 --version
```

Vous pouvez le faire avec brew https://brew.sh/

Puis :

```bash
brew install sqlite
```

## Mise en place de SQLAlchemy dans un projet Flask