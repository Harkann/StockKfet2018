# Application de gestion des stocks de la KFET de l'ENS Cachan

## Déploiement :

### Dépendances : 
	- python3
	- uwsgi
	- uwsgi-plugin-python3
	- nginx

### Installation :
	- cloner ce dépot ``` git clone git@gitlab.crans.org:paulon/stock_kfet_2017.git ```
	- créer la base de données stock propriété de l'utilisateur kfet (ou éditer le fichier de configuration)
	- créer les symlink nécessaires :
		``` ln -s stock_kfet_nginx.conf /etc/nginx/sites-enabled/. ```
		``` ln -s stock_kfet_uwsgi.ini /etc/uwsgi/sites-enabled/. ```
 
