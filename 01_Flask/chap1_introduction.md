# Flask installation

## Installation 

Dans un premier temps créer un dossier myapp sur votre bureau et créez le fichier suivant :

app.py

```python
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"
```

### Windows 

Dans un terminale sur votre bureau et dans un dossier où vous souhaitez démarrer le projet

```bash
python -m venv myapp
```

Dans un powershell, toujours dans le dossier myapp

```bash
.\mon_env\Scripts\Activate
```

Dans l'invite de commande 

```bash
myapp\Scripts\activate

# installation de Flask
pip install flask
```

Commandes utiles 

Démarrer le serveur sur le port 5000 en localhost :

```bash
flask run
```

Puis, on installa Flask dans le dossier virtualisé, notez que les dépendances suivantes seront également installées :

- **Werkzeug** implements WSGI, the standard Python interface between applications and servers.

- **Jinja** is a template language that renders the pages your application serves.

- **MarkupSafe** comes with Jinja. It escapes untrusted input when rendering templates to avoid injection attacks.

- **ItsDangerous** securely signs data to ensure its integrity. This is used to protect Flask’s session cookie.

- **Click** is a framework for writing command line applications. It provides the flask command and allows adding custom management commands.

- **Blinker** provides support for Signals.

### Sous Mac ou Linux

Résumé des commandes 

```bash
python3 -m venv .venv
. .venv/bin/activate
pip install flask

flask run 
```

## Désactivation de la virtualisation 

Attention, pour chaque session de votre console vous devez lancer l'environement pour l'activer.

Pour désactiver et supprimer l'environement tapez la commande suivante :

```bash

# Mac ou Linux
deactivate

# Dans cmder pour Windows
.\\Scripts\\deactivate.bat

# Suppression du dossier d'environement
rm -rf env

# Pour désactiver l'environement
deactivate

# Dans cmder pour Windows
.\\Scripts\\deactivate.bat

```

### Création d'un fichier de dépendance

Afin de préciser les dépendances utilisées dans votre projet vous devez créer le fichier suivant, cela permettra de partager vos projets et de les migrer facilement sur un autre poste de travail.

Rentrez dans votre environement virtualisé

```bash

# commande permettant d'écrire les dépendances dans ce fichier avec leurs versions.
pip freeze > requirements.txt

# Sous Windows
pip list > requirements.txt
```

Nous allons maintenant créer une petite application pour découvrir un peu mieux le micro-framework Flask

### Organisation des dossiers

- Un dossier "static" pour les assets.
- Un dossier "templates" pour les vues.
- Un dossier "tests" pour les tests.

## Création des templates et fichiers statiques

Nous allons partir de données d'exemple, créez le fichier users.py dans le dossier Data dans notre projet myapp.

Data/users.py

```python
users = [
    {
        "id": 0,
        "name": "John Doe",
        "email": "john@example.com",
        "age": 30,
        "bio": "Développeur Python passionné. Amateur de jeux vidéo."
    },
    {
        "id": 1,
        "name": "Alice Smith",
        "email": "alice@example.com",
        "age": 28,
        "bio": "Ingénieure logiciel avec une expertise en Python. Aime la randonnée."
    },
    {
        "id": 2,
        "name": "Bob Johnson",
        "email": "bob@example.com",
        "bio": "Étudiant en informatique, aime coder en Python. Fan de musique."
    },
    {
        "id": 3,
        "name": "Eva Wilson",
        "email": "eva@example.com",
        "age": 35,
        "bio": "Développeuse Python senior. Passionnée de photographie."
    }
]
``` 

### 01 Exercice configuration

Dans le dossier static créez le fichier bootstrap.min.css, puis dans le fichier app.py importez le module **render_template**. Créez les deux fichiers index.html et base.html :

- les templates 

**base.html**

```html
<!doctype html>
<title>{% block title %}{% endblock %} - Flask</title>
<link rel="stylesheet" href="{{ url_for('static', filename='bootstrap.min.css') }}">
<nav>
  <ul>
  </ul>
</nav>
<section class="content">
  <header>
    {% block header %}{% endblock %}
  </header>
 
  {% block content %}{% endblock %}
</section>
```

**index.html** ce fichier est étendu du fichier base.html

```html
{% block header %}
<h1>List</h1>
{% endblock %}

{% block content %}
<table class="table table-dark">
    <thead>
        <tr>
            <th scope="col">#</th>
            <th scope="col">Name</th>
            <th scope="col">email</th>
            <th scope="col">age</th>
        </tr>
    </thead>
    <tbody>
        {% for user in users %}
            TODO : affichez les informations suivantes Name, email et age si cette information existe.
        {% endfor %}
    </tbody>
</table>
{% endblock %}
```

- fichier app.py

```python
from flask import Flask, render_template
from Data import users

app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template('index.html', users=users)
```

Pour la suite pensez à taper la commande suivante pour surveiller les changements dans les fichiers et être en mode dévelloppement.

```bash
flask run --reload --extra-files 'templates/*.html' --debug
```

### 02 Exercice afficher les données users

Affichez les données users dans le dictionnaire **users** pour la route "/".

### 03 Exercice la bio de chaque user dans un nouveau fichier 

La route sera dynamique dans le template

```python
<a href="user/{{user['id']}}">{{ user['name'] }}</a>
```

Dans le fichier app.py vous décorez une route dynamique avec la syntaxe suivante :

```python
@app.route('/user/<id>')
def user(id):
    pass
```

## Route POST 

Pensez à importer le module request

Nous allons voir comment maintenant traiter les routes POST ou GET, dans l'exemple qui suit vous avez les deux verbes possibles HTTP passés en paramètre de la méthode route :

```python 
@app.route('/add', methods=['GET', 'POST'])
def addUser():
    if request.method == 'POST':
        pass
    else:
        pass
```

### 01 TP ajouter un user

Créez une page permettant d'ajouter un utilisateur à notre dictionnaire.

Utilisez la fonction flash de Flask pour vérifier l'existence d'un utilisateur, faites la gestion des erreurs.

Aidez de la documentation pour faire cela.

