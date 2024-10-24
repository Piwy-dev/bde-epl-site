Site web officiel pour le BDE (bureau des étudiants) de l'[Ecole Polytechnique de Louvain](https://uclouvain.be/fr/facultes/epl).

Vous pouvez visiter le site via [ce lien](https://bde-epl.uclouvain.be)

Ce site utilise la librairie python [Flask](https://flask.palletsprojects.com/en/3.0.x/).

Il est entièrement open-source sous licence [GNU General Public License v3.0](https://github.com/Piwy-dev/bde-epl-site/blob/main/LICENSE).

## Contribuer
Si vous voulez apporter des modifications au site voici les démarches à suivre :

### Cloner le dépot
Vérifiez que vous avez bien configuéré une clé SSH pour votre compte (alternativement vous pouvez copier avec HTTP). Ensuite, exécutez la comande suivant dans le dossier de destination voulu.
```console
git clone git@github.com:Piwy-dev/bde-epl-site.git
```

### Créer un environnement python
Attention, pour cette étape vous devez avoir python installé sur votre machine. Si ce n'est pas le cas vous pouvez suivre les [instuctions d'installation](https://www.python.org/downloads/).

Vous pouvez créer un environnemnt python local via la commande suivante :
```console
python3 -m venv .venv
```

### Activer l'environement local
Maintenant, vous pouvez activer votre environement python local via la commande suivante :
```console
. .venv/bin/activate
```

### Installer Flask
Utilisez cette commande pour installer flask dans votre environnement python :
```
pip install Flask
```

### Lancer le site en local
> Assurez-vous que votre environnement est correctement configuré avant de lancer le site. Des erreurs peuvent survenir si des dépendances sont manquantes ou mal installées.

Vous pouvez maintenant lancer le site sur votre machine. L'URL local sera affichée en output.
```code
flask run --debug
```
