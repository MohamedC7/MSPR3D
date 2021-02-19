# MSPR3D
 ## Prerequis
### Installation de Kivy
Kivy a de nombreuses dépendances, il est donc recommandé de l'installer dans un environnement virtuel Python. Vous pouvez utiliser la venvbibliothèque intégrée de Python ou le virtualenvpackage. Si vous n'avez jamais utilisé d'environnement virtuel Python auparavant, consultez Environnements virtuels Python: une introduction .

Voici comment vous pouvez créer un environnement virtuel Python:

`$ python3 -m venv my_project`
Cela copiera votre exécutable Python 3 dans un dossier appelé my_kivy_projectet ajoutera quelques autres sous-dossiers à ce répertoire.

Pour utiliser votre environnement virtuel, vous devez l'activer. Sur Mac et Linux, vous pouvez le faire en exécutant ce qui suit dans le my_projectdossier:

`$ source bin/activate`
La commande pour Windows est similaire, mais l'emplacement du script d'activation est à l'intérieur du Scriptsdossier au lieu de bin.

Maintenant que vous avez un environnement virtuel Python activé, vous pouvez exécuter pippour installer Kivy. Sous Linux et Mac, vous exécuterez la commande suivante:

`$ python -m pip install kivy`
Sous Windows, l'installation est un peu plus complexe. Consultez la documentation officielle pour savoir comment installer Kivy sur Windows . (Les utilisateurs de Mac peuvent également télécharger un dmgfichier et installer Kivy de cette façon.)