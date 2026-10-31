# Options de l’intégration Neviweb130

Cette page décrit les options accessibles avec **Configurer** sur la page de l’intégration Neviweb130.

---

## 🔧 Paramètres disponibles

### **Nom du compte Neviweb (prefix)**
Nom du compte Neviweb. Sert à distinguer plusieurs comptes Neviweb dans Home Assistant. Sans espace, caractères ASCII seulement, et chaque compte doit avoir son propre préfixe.

### **Niveau de journalisation (log_level)**
Niveau du fichier de log de neviweb130, `config/neviweb130_log.txt` :
- debug
- info
- warning (défaut)
- error
- critical

Neviweb130 n’écrit pas dans `home-assistant.log`. La section `logger:` de `configuration.yaml` n’a aucun effet sur ce fichier.

### **Taille maximale du journal (log_max_bytes)**
Taille maximale du fichier de log avant rotation.

### **Nombre de fichiers de sauvegarde (log_backup_count)**
Nombre de fichiers de log conservés lors de la rotation.

### **Réinitialisation du journal au démarrage (log_reset_on_start)**
Efface le fichier de log au démarrage de l’intégration.

### **Télécharger le journal (download_log)**
Copie le fichier de log vers `/local/neviweb130.log` pour le télécharger depuis le navigateur. Une notification donne le lien. La copie est effacée après 30 minutes.

### **Recharger l’intégration (reload)**
Recharge l’intégration sans redémarrer Home Assistant.

### **Migrer les unique_id numériques (migrate)**
Convertit les anciens unique_id numériques en unique_id textuels, comme l’exige Home Assistant.

### **Limite de sécurité des requêtes (request_limit)**
Nombre de requêtes par jour vers Neviweb avant l’envoi d’une notification (défaut 25000). La limite de Neviweb est de 30000 requêtes par jour. Le compte courant est affiché par le capteur compteur de requêtes.

### **Intervalle de vérification des mises à jour (update_check_interval)**
Fréquence à laquelle l’entité de mise à jour vérifie sur GitHub s’il y a une nouvelle version : 1h, 3h, 6h (défaut), 12h ou 24h.

### **Mode de sauvegarde (backup_mode)**
Sauvegarde faite par l’entité de mise à jour avant d’installer une nouvelle version :
- **full** : sauvegarde complète de Home Assistant (`hassio.backup_full`)
- **partial** : sauvegarde partielle (`hassio.backup_partial`) des dossiers de backup_folders

Les deux nécessitent une installation Home Assistant avec le Supervisor.

### **Dossiers de sauvegarde (backup_folders)**
Dossiers inclus dans une sauvegarde partielle (défaut `config`, soit la configuration de Home Assistant).

---

## 🔑 Champs saisis à l’ajout ou à la reconfiguration

### **ignore_miwi**
À mettre à True si un emplacement Neviweb choisi contient aussi des appareils MiWi (GT125). Sinon, un avertissement indique que l’emplacement contient des appareils MiWi non supportés.

### **safe_mode**
Liste d’ID d’appareils séparés par des virgules à interroger en mode sécuritaire, ou `-` pour aucun. En mode sécuritaire, les attributs non supportés par le micrologiciel de l’appareil sont ignorés. Un appareil qui retourne `DVCATTRNSPTD` est ajouté automatiquement et une notification est envoyée.

---

## 📘 Voir aussi
- [Index de la documentation](doc_index.md)
