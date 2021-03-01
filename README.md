# MSPR3D
 ## Prerequis
### Installation de Kivy (To ingore)
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

###  Deploying to Android with Buildozer

Step 1) Download Virtualbox https://www.virtualbox.org/wiki/Downloads

Step 2) Download an Ubuntu 18.04 image https://ubuntu.com/download/desktop

Step 3) Make sure your phone is in Developer mode by going to Settings -- About Phone -- Software -- tap on 'Build Number' 7 times quickly. Now go to Settings -- Developer Options and enable Stay Awake and USB Debugging.

Step 4) Connect your phone to your computer and make sure to Always Allow USB Debugging when your phone connects.

Step 5) Set up a new virtual machine in Virtualbox using the image from step 2. I allocated 2048 MB of memory and 20 GB of disk space.

Step 6) Install Ubuntu on the virtual machine

Step 7) Open the Terminal in your virtual machine and run the following commands:

Sudo apt install git

git clone https://github.com/kivy/buildozer.git

cd buildozer

sudo apt-get install python3.6

sudo apt-get install -y python3-setuptools

sudo python3 setup.py install 

cd ..

git clone https://github.com/MohamedC7/MSPR3D.git

cd MSPR3D

buildozer init

sudo apt update

sudo apt install -y git zip unzip openjdk-8-jdk python3-pip autoconf libtool pkg-config zlib1g-dev libncurses5-dev libncursesw5-dev libtinfo5 cmake libffi-dev

pip3 install --user --upgrade cython virtualenv

Sudo apt-get install cython

buildozer android debug deploy run
