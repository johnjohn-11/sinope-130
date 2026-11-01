## Home Assistant Neviweb130 Custom Components
[🇬🇧 English version](../README.md)

Intégration personnalisée pour utiliser les appareils [Neviweb](https://neviweb.com/) dans [Home Assistant](http://www.home-assistant.io) (HA). Neviweb est la plateforme de Sinopé Technologies pour ses appareils intelligents : thermostats, interrupteurs et gradateurs, contrôleurs de charge, prises, valves, détecteurs de fuite d’eau et autres.

Neviweb130 (Sinope Neviweb130 dans HACS) gère les appareils Zigbee connectés à Neviweb par la passerelle GT130, et les appareils Wi-Fi connectés directement à Neviweb. Les nouveaux appareils Sinopé sont ajoutés à mesure qu’ils sortent. Si votre appareil n’est pas encore pris en charge, [ouvrez une issue](https://github.com/claudegel/sinope-130/issues/new/choose) et il sera ajouté rapidement.

> 💛 **Vous aimez cette intégration?** Vous pouvez soutenir son développement :
> [![Support via PayPal](https://cdn.rawgit.com/twolfson/paypal-github-button/1.0.0/dist/button.svg)](https://www.paypal.me/phytoressources/) ou
> [![Faire un don via Interac](https://img.shields.io/badge/Interac-Don-orange?style=for-the-badge)](Donations.md)

## Table des matières

- **Démarrage**
  - [Avant de commencer](#avant-de-commencer)
  - [Installation](#installation)
  - [Ajouter un compte Neviweb](#ajouter-un-compte-neviweb)
  - [Paramètres du compte](#paramètres-du-compte)
  - [Options de l’intégration](#options-de-lintégration)
  - [Passer de la version 4.x](#passer-de-la-version-4x)
- **Utiliser Neviweb130**
  - [Appareils et entités](#appareils-et-entités)
  - [Statistiques d’énergie et d’eau](#statistiques-dénergie-et-deau)
  - [Périodes de pointe Éco Sinopé](#périodes-de-pointe-éco-sinopé)
  - [Actions (services)](#actions-services)
  - [Valve Sedna](#valve-sedna)
  - [Compteur de requêtes quotidiennes](#compteur-de-requêtes-quotidiennes)
  - [Mises à jour](#mises-à-jour)
  - [Langue](#langue)
- **Tableaux de bord**
  - [Icônes d’appareils et météo](#icônes-dappareils-et-météo)
  - [Exemples de cartes](#exemples-de-cartes)
- **Aide**
  - [Dépannage](#dépannage)
  - [Réinitialisation d’un appareil](#réinitialisation-dun-appareil)
  - [Appareils pris en charge](#appareils-pris-en-charge)

# Démarrage

## Avant de commencer

- Vos appareils doivent déjà être ajoutés à votre portail Neviweb : les appareils Zigbee par une passerelle GT130, les appareils Wi-Fi directement, et certains appareils Zigbee par une valve Sedna. Consultez le manuel de votre appareil ou [l’assistance Neviweb](https://support.sinopetech.com/).
- Vérifiez que vos appareils sont dans la liste des [appareils pris en charge](#appareils-pris-en-charge).
- Les appareils MiWi (GT125) ne sont pas pris en charge par cette intégration. Utilisez une des autres intégrations Sinopé ci-dessous, elles peuvent toutes fonctionner en même temps.

<details>
<summary>Autres intégrations Sinopé</summary>

- [**neviweb**](https://github.com/claudegel/sinope-1) (HACS : Sinope Neviweb), pour les appareils MiWi par le portail Neviweb.
- [**sinope**](https://github.com/claudegel/sinope-gt125) (HACS : Sinope GT125), pour les appareils gérés directement par votre passerelle GT125.
- [**neviweb130**](https://github.com/claudegel/sinope-130) (HACS : Sinope Neviweb130), cette intégration, pour les appareils Zigbee et Wi-Fi par le portail Neviweb.
- [**sinope-zha**](https://github.com/claudegel/sinope-zha), les nouveaux quirks Sinopé pour ZHA avant leur ajout à zha-device-handlers. Avec un coordinateur Zigbee comme la clé USB ConBee II, ZHA gère vos appareils Zigbee en local. Copiez les fichiers sinope-zha dans votre installation HA pour tester les nouveaux quirks : ZHA les charge à la place des quirks Sinopé standards.

Les appareils Zigbee gérés directement par ZHA doivent être retirés de Neviweb, car un appareil ne peut pas être sur deux réseaux Zigbee en même temps.

</details>

## Installation

**Avec HACS (recommandé) :** cherchez **Sinope Neviweb130** dans HACS, installez-le et redémarrez Home Assistant.

<details>
<summary>Installation manuelle</summary>

1. Téléchargez le fichier zip de ce dépôt avec le bouton vert Code.
2. Décompressez-le et copiez le dossier `custom_components/neviweb130` dans le dossier `custom_components` du répertoire `config` de Home Assistant (celui qui contient `configuration.yaml`).
3. Redémarrez Home Assistant.

Votre répertoire de configuration devrait ressembler à ceci :

```
config/
  configuration.yaml
  custom_components/
    neviweb130/
      __init__.py
      binary_sensor.py
      button.py
      climate.py
      config_flow.py
      const.py
      coordinator.py
      devices.py
      exceptions.py
      helpers.py
      light.py
      manifest.json
      number.py
      schema.py
      select.py
      sensor.py
      services.yaml
      session_manager.py
      strings.json
      switch.py
      update.py
      valve.py
      translations/en.json
      translations/fr.json
```

</details>

Pour afficher les images des appareils et de la météo dans vos tableaux de bord, copiez aussi les icônes (voir [Icônes d’appareils et météo](#icônes-dappareils-et-météo)).

## Ajouter un compte Neviweb

1. Allez dans Paramètres → Appareils et services.
2. Cliquez sur **Ajouter une intégration** et cherchez **Sinope Neviweb130**.
3. Entrez votre courriel et votre mot de passe Neviweb. Les autres champs peuvent habituellement rester tels quels (voir [Paramètres du compte](#paramètres-du-compte)).

![nouvelle configuration](../www/nouveau_pont.jpg)

Neviweb130 se charge ensuite et récupère vos appareils Neviweb.

**Plus d’un compte Neviweb :** ajoutez l’intégration de nouveau pour chaque compte, avec un **prefix** différent. Chaque compte Neviweb ne peut être ajouté qu’une seule fois.

## Paramètres du compte

Ils sont demandés à l’ajout d’un compte. Pour les changer ensuite, utilisez **Reconfigurer** sur la page de l’intégration.

| Paramètre         | Défaut                 | Description |
|-------------------|------------------------|-------------|
| **prefix**        | default                | Nom du compte. À changer seulement si vous ajoutez plus d’un compte Neviweb. Chaque compte doit avoir un préfixe différent, sans espace ni accent. |
| **username**      |                        | Le courriel utilisé pour vous connecter à Neviweb. Obligatoire. |
| **password**      |                        | Votre mot de passe Neviweb. Obligatoire. |
| **network**       | 1er emplacement trouvé | Nom de l’emplacement Neviweb à gérer. Vide pour la détection automatique. |
| **network2**      | 2e emplacement trouvé  | Deuxième emplacement à gérer. Vide si vous n’en avez qu’un. |
| **network3**      | 3e emplacement trouvé  | Troisième emplacement à gérer. Un troisième emplacement doit être activé par Sinopé. |
| **scan_interval** | 420                    | Secondes entre deux mises à jour des appareils, de 300 à 600. Sinopé demande au moins 5 minutes entre deux lectures. |
| **stat_interval** | 1800                   | Secondes entre deux mises à jour des statistiques d’énergie, de 300 à 1800. |
| **homekit_mode**  | False                  | Ajoute les valeurs propres à HomeKit. Inutile si vous n’utilisez pas HomeKit. |
| **ignore_miwi**   | False                  | À mettre à True si un emplacement choisi contient aussi des appareils MiWi (GT125), pour éviter l’avertissement d’appareils non pris en charge. |
| **notify**        | both                   | Façon de signaler les erreurs d’appareil : `nothing`, `logging`, `notification` ou `both`. |
| **safe_mode**     | -                      | ID d’appareils séparés par des virgules à lire en mode sécuritaire, ou `-` pour aucun. En mode sécuritaire, les attributs non pris en charge par le micrologiciel sont ignorés. Un appareil qui retourne `DVCATTRNSPTD` est ajouté automatiquement et une notification est envoyée. |

<details>
<summary>À propos des emplacements (network, network2, network3)</summary>

Les noms d’emplacements sont affichés en haut de la première page après la connexion à Neviweb. Si vous avez plusieurs emplacements, cliquez sur l’icône en haut pour les voir tous.

![network](../www/network.jpg)

- Les appareils Zigbee (GT130) et Wi-Fi peuvent être dans le même emplacement ou dans des emplacements séparés. Neviweb130 gère jusqu’à trois emplacements par compte.
- Si vous avez aussi un GT125 dans Neviweb, entrez vos noms d’emplacements, sinon l’emplacement du GT125 pourrait être pris par erreur.
- Mettez un emplacement inutilisé à `_` pour que Neviweb130 ne le cherche pas.
- Écrivez les noms exactement comme dans Neviweb, majuscules comprises. Les lettres accentuées sont refusées.

</details>

## Options de l’intégration

Tout se trouve dans Paramètres → Appareils et services → Neviweb130. Cliquez sur **Configurer** pour changer ces options. Les changements s’appliquent sans redémarrer Home Assistant.

![options](../www/options.jpg)

| Option | Défaut | Description |
|--------|--------|-------------|
| **log_level** | info | Niveau des messages écrits dans le fichier journal. Mettez `debug` pour analyser un problème. |
| **log_max_bytes**, **log_backup_count**, **log_reset_on_start** | 2 Mo, 2, activé | Taille, rotation et remise à zéro au démarrage du fichier journal (voir [Dépannage](#dépannage)). |
| **download_log** | | Copie le fichier journal vers `/local/neviweb130.log` pour le télécharger dans votre navigateur. La copie est effacée après 30 minutes. |
| **reload** | | Recharge Neviweb130 sans redémarrer Home Assistant. |
| **migrate** | | Relance la migration des unique_id. Elle se fait déjà automatiquement au démarrage. |
| **request_limit** | 25000 | Limite de sécurité des requêtes envoyées à Neviweb par jour (la limite de Neviweb est de 30000). |
| **update_check_interval** | 6h | Fréquence de vérification des nouvelles versions sur GitHub : 1h, 3h, 6h, 12h ou 24h. |
| **backup_mode**, **backup_folders** | full, config | Sauvegarde faite avant l’installation d’une mise à jour. `full` appelle `hassio.backup_full`, `partial` appelle `hassio.backup_partial` avec les dossiers listés. Nécessite une installation Home Assistant avec le Supervisor. |

Voir aussi [doc/options.md](options.md).

<details>
<summary>Captures des fenêtres d’options et de reconfiguration</summary>

![options de configuration](../www/configuration.jpg)

![reconfiguration](../www/reconfigurer.jpg)

</details>

## Passer de la version 4.x

Rien à faire au départ : au premier démarrage de la version 5, Neviweb130 importe le bloc `neviweb130:` de `configuration.yaml` dans l’interface, une entrée par compte (le format `accounts:` est pris en charge). Il convertit aussi les `unique_id` et les numéros de modèle des appareils en texte, comme l’exige Home Assistant. Les noms d’entités sont conservés.

Après ce premier démarrage :
- retirez ou commentez le bloc `neviweb130:` de `configuration.yaml`,
- vérifiez vos automatisations, scripts et tableaux de bord. Ils continuent de fonctionner, mais les nouvelles [entités d’attributs](#appareils-et-entités) peuvent remplacer vos capteurs template,
- retirez vos personnalisations Custom-UI pour Neviweb130, l’intégration définit maintenant elle-même les images des appareils.

Si vous utilisiez une copie de l’intégration sous un autre nom (par exemple `neviweb131`) pour gérer un deuxième compte, ajoutez plutôt ce compte à Neviweb130 (voir [Ajouter un compte Neviweb](#ajouter-un-compte-neviweb)).

<details>
<summary>Référence de l’ancienne configuration configuration.yaml (version 4.x)</summary>

Un seul compte :

```yaml
neviweb130:
  username: '«votre courriel Neviweb»'
  password: '«votre mot de passe Neviweb»'
  network: '«nom de l’emplacement du GT130 dans Neviweb»'
  network2: '«nom du deuxième emplacement»'
  network3: '«nom du troisième emplacement»'
  scan_interval: 360
  homekit_mode: False
  ignore_miwi: False
  stat_interval: 1800
  notify: "both"
  safe_mode: "-"
```

Plusieurs comptes (depuis la 3.1.0). `location` et `network` sont équivalents, et les paramètres globaux s’appliquent à tous les comptes :

```yaml
neviweb130:
  accounts:
    - username: 'votre_courriel@example.com'
      password: 'votre_mot_de_passe'
    - username: 'courriel_parents@example.com'
      password: 'mot_de_passe_parents'
      location: 'Chalet'
      prefix: 'parents'
  scan_interval: 360
  homekit_mode: False
  ignore_miwi: False
  stat_interval: 1800
  notify: "both"
  safe_mode: "-"
```

Les noms des paramètres sont en anglais et ne doivent pas être traduits.

</details>

# Utiliser Neviweb130

## Appareils et entités

Chaque appareil a sa page dans Paramètres → Appareils et services → Neviweb130. En plus de l’entité principale (climate, light, switch, valve ou sensor), Neviweb130 crée une entité pour la plupart des attributs :
- **sensor**, pour les valeurs numériques comme la température, la tension et les statistiques d’énergie,
- **binary_sensor**, pour les états on/off comme les détecteurs de fuite et le `gateway_status` du GT130 (en ligne ou hors ligne dans Neviweb),
- **button**, pour réinitialiser un attribut on/off ou une alarme,
- **number**, pour changer une valeur numérique (température minimum/maximum, température d’absence, etc.),
- **switch**, pour activer ou désactiver un attribut,
- **select**, pour les attributs à choix multiples.

Ces entités s’utilisent directement dans les automatisations et le tableau de bord Énergie. Les capteurs template sur les attributs ne sont plus nécessaires. S’il manque une entité d’attribut, ouvrez une issue.

<details>
<summary>Exemple de page d’appareil</summary>

![Page appareil](../www/page_appareil.jpg)
![Page appareil suite](../www/page_appareil_suite.jpg)

</details>

## Statistiques d’énergie et d’eau

Les appareils qui rapportent leur consommation dans Neviweb ont ces capteurs, en kWh, prêts pour le tableau de bord Énergie de HA :
- **Énergie totale** (`total_kwh_count`, total_increasing),
- énergie **mensuelle**, **quotidienne** et **horaire** (`monthly_kwh_count`, `daily_kwh_count`, `hourly_kwh_count`, total).

Les valves Sedna 2e génération avec capteur de débit ont le même ensemble pour l’eau, en litres : **Débit total** (`total_flow_count`) et les comptes mensuel, quotidien et horaire.

Les statistiques sont lues dans Neviweb toutes les `stat_interval` secondes (défaut 1800). Les attributs `hourly_kwh`, `daily_kwh` et `monthly_kwh` restent exposés sur les entités climate, light et switch, et `hourly_flow`, `daily_flow` et `monthly_flow` sur les entités valve.

## Périodes de pointe Éco Sinopé

Si au moins un thermostat ou un contrôleur de charge est inscrit au programme Éco Sinopé, vous pouvez savoir quand Neviweb annonce une période de pointe. Suivez l’attribut **eco_status** : il passe de «off» à «on» au début de la période de préchauffage. Créez une automatisation sur ce changement pour préparer vos autres appareils HA.

<details>
<summary>Tous les attributs Éco Sinopé</summary>

- Thermostats :
  - **eco_status** : «off» en temps normal, passe à «on» au début de la période de préchauffage.
  - **eco_setpoint** : passe à «on» pendant la pointe si l’appareil est géré par Éco Sinopé.
  - **eco_optout** : passe à «on» si quelqu’un change la consigne pendant la pointe.
  - **eco_power_relative** : température minimale, relative à la consigne, à laquelle le thermostat se rallume automatiquement pour la protection contre le gel.
  - **eco_power_absolute** : limite pi_heating_demand entre 1 et 100% pendant la pointe.
  - **eco_setpoint_status** : passe à «on» si la consigne est changée par Éco Sinopé.
  - **eco_setpoint_delta** : 0 en temps normal, entre -10 et +10 pendant la pointe. Positif pour le préchauffage, négatif pour la pointe. Il s’ajoute à la consigne : -10 = consigne réduite de 10°C.
- Contrôleurs de charge :
  - **eco_status** : comme pour les thermostats.
  - **eco_onoff** : passe à «on» pendant la pointe si l’appareil est géré par Éco Sinopé. L’appareil est éteint pendant la pointe. Rien n’est fait pendant le préchauffage.
  - **eco_optout** : passe à «on» si quelqu’un rallume l’appareil pendant la pointe.
- Multicontrôleur MC3100ZB :
  - **eco_status** : comme pour les thermostats.
  - **eco_setpoint** : aucun changement pendant la pointe.
  - **eco_optout** : passe à «on» si quelqu’un change l’état on/off pendant la pointe.
  - **eco_power_relative** : température minimale, relative à la température ambiante, à laquelle le MC3100ZB se rallume automatiquement pour la protection contre le gel.
  - **eco_power_absolute** : usage inconnu.

</details>

## Actions (services)

Neviweb130 ajoute des actions (services) pour changer les réglages que les actions standards de HA ne couvrent pas : verrouillage du clavier, minuteries, affichage, limites de consigne, alertes, options Éco Sinopé, réglages des thermopompes et des valves, et plus. Trouvez-les dans Outils de développement → Actions en tapant `neviweb130.`, ou dans la liste des actions de l’éditeur d’automatisations. Chaque action a une description et ses champs dans l’interface.

Les actions marquées « Equipment configuration should be performed by a professional » modifient le fonctionnement de l’équipement CVC. Utilisez-les seulement si vous connaissez votre installation.

<details>
<summary>Liste complète des actions</summary>

- neviweb130.set_second_display, pour faire afficher la température extérieure au lieu de la consigne sur le deuxième affichage du thermostat. À envoyer une seule fois par appareil.
- neviweb130.set_climate_keypad_lock, pour verrouiller le clavier d’un thermostat.
- neviweb130.set_light_keypad_lock, pour verrouiller le clavier d’un interrupteur ou gradateur.
- neviweb130.set_switch_keypad_lock, pour verrouiller le clavier d’un appareil switch.
- neviweb130.set_light_timer, pour régler une minuterie en secondes (0 à 10800) après laquelle la lumière s’éteint.
- neviweb130.set_switch_timer, pour régler une minuterie en secondes (0 à 10800) après laquelle le switch ou le multicontrôleur s’éteint.
- neviweb130.set_switch_timer2, pour régler la minuterie 2 en secondes (0 à 10800) après laquelle le multicontrôleur s’éteint.
- neviweb130.set_led_indicator, pour changer la couleur et l’intensité du voyant des appareils d’éclairage pour les états «on» et «off». N’importe quelle couleur RGB peut être envoyée avec les paramètres red, green et blue.
- neviweb130.set_time_format, pour afficher l’heure en 12h ou 24h sur les thermostats.
- neviweb130.set_temperature_format, pour afficher la température en Celsius ou en Fahrenheit sur les thermostats.
- neviweb130.set_backlight, pour régler l’intensité du rétroéclairage des thermostats à l’état «on» ou «off».
- neviweb130.set_wattage, pour régler wattageOverload des appareils d’éclairage.
- neviweb130.set_auxiliary_load, pour régler l’état et la charge du chauffage d’appoint.
- neviweb130.set_setpoint_min, pour régler la consigne minimale des thermostats.
- neviweb130.set_setpoint_max, pour régler la consigne maximale des thermostats.
- neviweb130.set_cool_setpoint_min, pour régler la consigne minimale de climatisation du TH1134ZB-HC.
- neviweb130.set_cool_setpoint_max, pour régler la consigne maximale de climatisation du TH1134ZB-HC.
- neviweb130.set_floor_limit_low, pour régler la consigne minimale des thermostats de plancher (5 à 34°C, 0 = off).
- neviweb130.set_floor_limit_high, pour régler la consigne maximale des thermostats de plancher (7 à 36°C, 0 = off).
- neviweb130.set_sensor_leak_alert, pour régler l’alerte de fuite du détecteur de fuite.
- neviweb130.set_sensor_temp_alert, pour régler l’alerte de basse température du détecteur de fuite.
- neviweb130.set_sensor_closure_action, pour régler l’action de fermeture de la valve en cas de fuite, seulement pour les détecteurs connectés directement à la valve Sedna.
- neviweb130.set_valve_alert, pour régler l’alerte de batterie faible.
- neviweb130.set_valve_temp_alert, pour régler l’alerte de basse température de la valve Sedna.
- neviweb130.set_early_start, pour activer ou désactiver le démarrage anticipé des thermostats Wi-Fi.
- neviweb130.set_air_floor_mode, pour choisir entre la sonde de plancher et la sonde ambiante pour contrôler la température.
- neviweb130.set_floor_air_limit, pour régler la limite de température de l’air des thermostats de plancher.
- neviweb130.set_phase_control, pour régler le mode de contrôle de phase du gradateur DM2550ZB (reverse ou forward).
- neviweb130.set_hvac_dr_options, pour activer ou réinitialiser les options de période DR dans Neviweb pour les thermostats.
- neviweb130.set_hvac_dr_setpoint, pour régler la réduction de consigne des thermostats pendant la période DR, de 100 à -100 (°C × 10). 0 fait seulement clignoter la petite icône.
- neviweb130.set_load_dr_options, pour activer ou réinitialiser les options de période DR dans Neviweb pour les contrôleurs de charge.
- neviweb130.set_cycle_output, pour régler la durée du cycle principal des thermostats basse tension, en minutes.
- neviweb130.set_aux_cycle_output, pour régler la durée du cycle d’appoint des thermostats basse tension, en minutes.
- neviweb130.set_control_onoff, pour changer l’état des sorties 1 et 2 du multicontrôleur de la valve Sedna.
- neviweb130.set_battery_type, pour choisir le type de pile du détecteur de fuite, alcaline ou lithium.
- neviweb130.set_tank_size, pour régler la capacité du chauffe-eau du Calypso RM3500ZB.
- neviweb130.set_low_temp_protection, pour activer ou non la protection de température d’eau du chauffe-eau. Sous 45°C, le chauffage redémarre automatiquement.
- neviweb130.set_controlled_device, pour changer le nom de l’appareil contrôlé par le contrôleur de charge RM3250ZB.
- neviweb130.set_flow_meter_model, pour changer le modèle de débitmètre connecté à la valve Sedna 2e génération et activer ou arrêter la protection contre les fuites par le débitmètre.
- neviweb130.set_flow_meter_delay, pour régler le délai avant la fermeture de la valve quand le débitmètre détecte une fuite.
- neviweb130.set_flow_meter_options, pour régler l’action du débitmètre : fermer la valve (oui/non) et envoyer une alerte (oui/non), ou ne rien faire.
- neviweb130.set_tank_type, pour choisir le type de réservoir du LM4110-ZB, propane ou mazout.
- neviweb130.set_gauge_type, pour choisir le type de jauge du LM4110-ZB sur un réservoir de propane, modèle 5-95 ou 10-80.
- neviweb130.set_low_fuel_alert, pour régler le seuil de niveau bas du réservoir de propane, 0 (off), 10, 20 ou 30%.
- neviweb130.set_tank_height, pour régler la hauteur du réservoir de mazout du LM4110-ZB, 0 (off), 23, 24, 35, 38, 47, 48, 50.
- neviweb130.set_fuel_alert, pour activer ou désactiver l’alerte de carburant du LM4110-ZB.
- neviweb130.set_power_supply, pour choisir l’alimentation de la valve Sedna : batterie, acups-01 ou les deux.
- neviweb130.set_battery_alert, pour activer ou désactiver l’alerte de batterie du LM4110-ZB.
- neviweb130.set_input_output_names, pour nommer les entrées 1 et 2 et les sorties 1 et 2 du MC3100ZB.
- neviweb130.set_activation, pour activer ou bloquer la lecture d’un appareil dans Neviweb.
- neviweb130.set_sensor_type, pour choisir le type de sonde, 10k ou 12k.
- neviweb130.set_remaining_time, pour régler l’attribut coldLoadPickupRemainingTime.
- neviweb130.set_on_off_input_delay, pour régler le délai «on» ou «off» en secondes des entrées 1 et 2 du MC3100ZB.
- neviweb130.set_em_heat, pour activer ou désactiver le chauffage d’appoint des thermostats de plancher et basse tension. Remplace turn_aux_heat_on et turn_aux_heat_off, retirés par HA.
- neviweb130.set_display_config, pour allumer ou éteindre l’affichage de la thermopompe.
- neviweb130.set_sound_config, pour activer ou désactiver le son de la thermopompe.
- neviweb130.set_heat_pump_operation_limit, pour régler la température minimale de fonctionnement de la thermopompe.
- neviweb130.set_heat_lockout_temperature, pour régler la température extérieure maximale à laquelle le chauffage peut fonctionner.
- neviweb130.set_cool_lockout_temperature, pour régler la température extérieure minimale à laquelle la climatisation peut fonctionner.
- neviweb130.set_hc_second_display, pour régler le deuxième affichage du TH1134ZB-HC.
- neviweb130.set_language, pour choisir la langue d’affichage du TH1134ZB-HC.
- neviweb130.set_neviweb_status, pour régler le statut global Neviweb, maison ou absent, par le capteur du GT130.
- neviweb130.set_climate_neviweb_status, pour régler le statut global Neviweb, maison ou absent, par n’importe quel thermostat.
- neviweb130.set_refuel_alert, pour recevoir une alerte quand le réservoir de propane est rempli.
- neviweb130.set_accessory_type, pour choisir le type d’accessoire (humidificateur, déshumidificateur, échangeur d’air) connecté au TH6500WF ou TH6250WF.
- neviweb130.set_schedule_mode, pour choisir le mode d’horaire, manuel ou auto, du TH6500WF ou TH6250WF.
- neviweb130.set_flow_alarm_disable_timer, pour désactiver l’alarme de débit anormal de 1 seconde à 24 heures.
- neviweb130.set_heatcool_setpoint_delta, pour régler l’écart entre la consigne de chauffage et celle de climatisation, de 1 à 5°C en mode auto, pour TH6xxxWF.
- neviweb130.set_fan_filter_reminder, pour régler le délai entre deux nettoyages du filtre du ventilateur, de 1 à 12 mois, pour TH6xxxWF.
- neviweb130.set_temperature_offset, pour corriger la sonde de température de -2 à 2°C par pas de 0,5°C, pour TH6xxxWF.
- neviweb130.set_aux_heating_source, pour choisir le type de chauffage d’appoint utilisé par TH6xxxWF.
- neviweb130.set_fan_speed, pour régler la vitesse du ventilateur, on ou auto, pour TH6xxxWF.
- neviweb130.set_min_time_on, pour régler la durée minimale de marche avant l’arrêt (run-on) pour TH6500WF et TH6250WF.
- neviweb130.set_min_time_off, pour régler la durée minimale d’arrêt avant le redémarrage (cooldown) pour TH6500WF et TH6250WF.
- neviweb130.set_heat_interstage_delay et set_cool_interstage_delay, pour régler la durée minimale de chauffage ou de climatisation avant de passer à l’étage suivant pour TH6500WF et TH6250WF.
- neviweb130.set_heat_dissipation_time et set_cool_dissipation_time, pour régler la durée de purge en chauffage ou en climatisation pour TH6xxxWF.
- neviweb130.set_reversing_valve_polarity, pour régler la polarité de la valve d’inversion de la thermopompe pour TH6500WF et TH6250WF.
- neviweb130.set_humidity_mode, pour régler le mode de consigne d’humidité pour TH6500WF et TH6250WF.
- neviweb130.set_room_setpoint_away, pour régler la consigne d’absence des thermostats Wi-Fi.
- neviweb130.set_cool_setpoint_away, pour régler la consigne de climatisation en absence pour TH6xxxWF et HP6000WF.
- neviweb130.set_pump_protection, pour activer ou désactiver la protection de pompe des thermostats basse tension.
- neviweb130.set_led_on_intensity et set_led_off_intensity, pour régler l’intensité du voyant à l’état «on» ou «off».
- neviweb130.set_light_min_intensity, pour régler l’intensité minimale du gradateur.
- neviweb130.set_key_double_up, pour activer ou désactiver l’action du double appui vers le haut du DM2550ZB.
- neviweb130.set_switch_power_timer, pour régler la minuterie du RM3250ZB, off ou de 1 min à 24 h. L’appareil s’éteint après ce délai.
- neviweb130.set_switch_temp_alert, pour régler l’alerte de basse température du MC3100ZB.

</details>

## Valve Sedna

Une valve Sedna peut être connectée à Neviweb de deux façons, toutes deux prises en charge :
- **En Wi-Fi direct.** Les détecteurs de fuite sont connectés à la valve, qui se ferme d’elle-même quand une fuite est détectée.
- **Par le GT130 en mode Zigbee.** Les détecteurs de fuite sont connectés au GT130 et une fuite n’est pas transmise à la valve. Il faut une automatisation dans Neviweb ou HA pour fermer la valve quand un détecteur signale une fuite.

## Compteur de requêtes quotidiennes

Neviweb limite chaque compte à 30000 requêtes par jour. Au-delà, vous êtes déconnecté jusqu’à minuit.

Le capteur `sensor.neviweb130_daily_requests` compte les requêtes envoyées par Neviweb130 depuis minuit. Le compte survit aux redémarrages de HA et revient à 0 à minuit. Une notification est envoyée quand il dépasse l’option **request_limit** (défaut 25000). Servez-vous-en pour vérifier qu’un scan_interval plus court reste sous la limite.

## Mises à jour

Neviweb130 a sa propre entité de mise à jour. Elle vérifie GitHub toutes les 6 heures par défaut (option **update_check_interval**) et signale les préversions et les changements incompatibles avec une icône et une mention spéciales. Quand vous installez une mise à jour, elle :
- fait d’abord une sauvegarde (options **backup_mode** et **backup_folders**),
- compare le fichier zip au SHA-256 officiel de GitHub et annule s’ils diffèrent,
- restaure l’ancienne version si une erreur survient,
- envoie une notification avec le résultat.

Un lien sur la carte de mise à jour ouvre les notes de version.

<details>
<summary>Attributs de l’entité de mise à jour</summary>

- check_interval : valeur de l’option update_check_interval,
- last_check et next_check : date et heure de la dernière et de la prochaine vérification,
- last_update_success : date et heure de la dernière mise à jour réussie,
- update_status : étapes effectuées pendant la mise à jour,
- rollback_status : résultat du retour arrière si une mise à jour a échoué,
- update_percentage : progression de la mise à jour.

</details>

<details>
<summary>Masquer la carte de mise à jour de HACS</summary>

Pour éviter deux cartes de mise à jour (une de HACS, une de Neviweb130) :
1. Allez dans Paramètres → Appareils et services → HACS.
2. Sur la ligne Sinope Neviweb130, désactivez l’option préversion si elle est active.
3. Cliquez sur le menu à trois points au bout de la ligne, puis sur **2 entités**.
4. Choisissez l’entité de mise à jour, cliquez sur le bouton de paramètres et désactivez **Visible**.

Vous pouvez toujours mettre à jour ou retélécharger Neviweb130 manuellement par HACS.

</details>

## Langue

Les entités, actions, attributs, erreurs et notifications sont traduits en français et en anglais, selon la langue de Home Assistant. D’autres langues peuvent être ajoutées en traduisant `translations/en.json`. Après avoir modifié les fichiers de traduction, redémarrez Home Assistant : recharger l’intégration ne suffit pas.

# Tableaux de bord

## Icônes d’appareils et météo

Neviweb130 définit lui-même l’image des thermostats, capteurs et valves. Custom-UI et `customize.yaml` ne sont plus nécessaires. L’image s’affiche seulement si le fichier png existe, sinon l’icône par défaut de HA est utilisée.

Pour avoir les images, copiez les icônes de ce dépôt dans le répertoire `config` de Home Assistant :
- les icônes d’appareils du dossier [www](../www) dans `config/www/neviweb130/`,
- les icônes météo du dossier [www/icons](../www/icons) dans `config/www/neviweb130/weather/`.

Les noms de fichiers sont sensibles à la casse. Au démarrage, Neviweb130 envoie une notification si le dossier météo est absent ou vide.

Le chemin de l’image est aussi exposé dans ces attributs, pour vos propres cartes :
- **icon_type** : niveau de chauffe des thermostats, état de fuite des détecteurs, état des valves,
- **battery_icon** : niveau de batterie des capteurs, moniteurs et valves,
- **leak_icon** : état de fuite des valves.

Par exemple, `{{ state_attr('climate.neviweb130_climate_th1124wf', 'icon_type') }}` retourne un chemin dans `/local/neviweb130/`.

<details>
<summary>Noms des fichiers d’icônes d’appareils</summary>

| Appareil                     | Fichiers                                                                                  |
|------------------------------|-------------------------------------------------------------------------------------------|
| Thermostats                  | `heat-off.png`, `heat-0.png` à `heat-5.png`, `heat-auto-0.png` à `heat-auto-5.png`        |
| Thermostats de plancher      | `floor-off.png`, `floor-0.png` à `floor-5.png`, `floor-auto-0.png` à `floor-auto-5.png`   |
| Détecteurs de fuite          | `drop.png`, `leak.png`                                                                    |
| Niveau de batterie           | `battery-unknown.png`, `battery-1.png` à `battery-5.png`                                  |
| Valves                       | `valve-open.png`, `valve-close.png`, `leak.png`                                           |
| Réservoir propane (LM4110-ZB)| `propane-unknown.png`, `propane-0.png` à `propane-8.png`                                  |

Le niveau des thermostats suit la demande de chauffage : 0 sous 1%, puis un niveau par tranche de 20%. `-off` est utilisé quand le thermostat est éteint et `-auto-` quand il est en mode auto.

</details>

<details>
<summary>Noms des fichiers d’icônes météo</summary>

Le capteur **icône météo** des thermostats compatibles donne un code météo de Neviweb. Correspondance code et fichier (`WEATHER_ICON_MAP` dans `schema.py`) :

| Code | Fichier            | Code | Fichier            | Code | Fichier             |
|------|--------------------|------|--------------------|------|---------------------|
| 0    | Hide.png           | 11   | Cloudlightning.png | 22   | Cloudsnow5.png      |
| 1    | Sun.png            | 12   | Cloudlightning2.png| 23   | Cloudrainmoon.png   |
| 2    | Sun2.png           | 13   | Cloudsnow.png      | 24   | Cloudrainmoon2.png  |
| 3    | Cloudsun.png       | 14   | Cloudsnow2.png     | 25   | Cloudrainmoon3.png  |
| 4    | Cloudsun2.png      | 15   | Cloudsnow3.png     | 26   | Cloudsnow6.png      |
| 5    | Cloud.png          | 16   | Cloudsnow4.png     | 28   | Cloudrain2.png      |
| 6    | Cloudrainsun.png   | 17   | Cloudfog.png       | 29   | Cloudrain3.png      |
| 7    | Cloudrainsun2.png  | 18   | Moonstar.png       | 30   | Cloudrainsun3.png   |
| 8    | Cloud2.png         | 19   | Cloudmoon.png      | 31   | Cloudrainmoon4.png  |
| 9    | Cloud3.png         | 20   | Cloudmoon2.png     | 32   | Cloudrainsun4.png   |
| 10   | Cloudrain.png      | 21   | Cloudmoon3.png     | 33   | Cloudrainmoon5.png  |

</details>

## Exemples de cartes

Comme l’image de l’entité est définie, le plus simple est d’ajouter vos appareils à une carte entités ou Tile : les images changent automatiquement avec le niveau de chauffe, le niveau de batterie, etc.

![icons](../icon_view4.jpg)

Les exemples Mushroom ci-dessous nécessitent card-mod, Mushroom et stack-in-card de HACS. (N’hésitez pas à améliorer les icônes et à les partager.)

![icons](../icon_view3.jpg)

<details>
<summary>Carte Tile</summary>

```yaml
type: tile
entity: climate.neviweb130_climate_th1124wf
show_entity_picture: true
vertical: false
grid_options:
  columns: 12
  rows: 1
```

</details>

<details>
<summary>Carte Mushroom template</summary>

```yaml
type: custom:mushroom-template-card
entity: climate.neviweb130_climate_th1124wf
primary: |
  Cave ({{ state_attr(entity, 'temperature') }} °C)
secondary: |
  {{ states(entity) }} – ({{ state_attr(entity, 'hvac_action') }})
  Actuellement : {{ state_attr(entity, 'current_temperature') }} °C
picture: |
  {{ state_attr(entity, 'icon_type') }}
grid_options:
  columns: 12
  rows: 1
```

</details>

<details>
<summary>Carte Mushroom climate</summary>

```yaml
type: custom:mushroom-climate-card
entity: climate.neviweb130_climate_th1124wf
hvac_modes: []
fill_container: true
primary_info: name
secondary_info: state
tap_action:
  action: more-info
card_mod:
  style:
    mushroom-shape-icon$: |
      .shape {
        background-color: transparent !important;
        background: url("{{ state_attr('climate.neviweb130_climate_th1124wf', 'icon_type') }}");
        background-size: cover;
        background-position: center;
        border-radius: 50%;
      }
    .: |
      ha-state-icon {
        display: none !important;
      }
```

</details>

<details>
<summary>Exemples de l’ancien style</summary>

![icons](../icon_view2.png)

</details>

# Aide

## Dépannage

### Fichier journal et messages de débogage

Neviweb130 écrit ses messages dans son propre fichier, `config/neviweb130_log.txt`, et non dans `home-assistant.log`. La section `logger:` de `configuration.yaml` n’a aucun effet sur ce fichier. Par défaut, il est vidé à chaque démarrage, renommé à 2 Mo et 2 fichiers de rotation sont conservés (voir [Options de l’intégration](#options-de-lintégration)).

Pour obtenir les messages de débogage :
1. Sur la page de l’intégration Neviweb130, cliquez sur **Configurer** et mettez **log_level** à `debug`.
2. Reproduisez le problème.
3. Utilisez **download_log** dans les mêmes options pour télécharger le fichier, ou lisez directement `config/neviweb130_log.txt`.
4. Remettez ensuite le niveau à `info`, le journal debug grossit vite.

Joignez un extrait de ce fichier à toute issue.

### Mon appareil n’est pas détecté

Si votre appareil apparaît dans le journal mais pas dans la liste des entités, son numéro de modèle doit être ajouté au code. Dans le journal, cherchez ces lignes :

```
[custom_components.neviweb130] Received gateway data: [{'id': 100225, 'identifier': '500b91400001f750', 'name': 'Chargeur auto', 'family': '2506',...
[custom_components.neviweb130] Received signature data: {'signature': {'model': 2506, 'modelCfg': 0, 'softBuildCfg': 0, 'softVersion': {'minor': 9, 'middle': 2, 'major': 1}, 'hardRev': 2, 'protocol': 'sinopcom'}}
```

`'family': '2506'` et `'model': 2506` donnent le numéro de modèle. [Ouvrez une issue](https://github.com/claudegel/sinope-130/issues/new/choose) avec ce numéro.

### Des attributs affichent `[not supported]`

Neviweb laisse parfois tomber des attributs lors d’une mise à jour, même s’ils sont listés pour l’appareil. Une notification les liste et leur valeur devient `[not supported]`. Cas connus :

| Appareil        | Attributs manquants             |
|-----------------|---------------------------------|
| **TH1123ZB-G2** | coldLoadPickup, heatLockoutTemp |
| **TH1124ZB-G2** | coldLoadPickup, heatLockoutTemp |
| **TH6250WF**    | backlight                       |

Ouvrez une issue pour en signaler de nouveaux.

### Messages d’erreur de Neviweb

<details>
<summary>Codes d’erreur et quoi faire</summary>

- ACCDAYREQMAX : nombre maximal de requêtes par jour atteint (30000). Réduisez la fréquence de lecture.
- ACCRATELIMIT : trop de tentatives de connexion. Attendez quelques minutes avant de réessayer.
- ACCSESSEXC : trop de sessions ouvertes en même temps. C’est fréquent après plusieurs redémarrages de Home Assistant ou quand Neviweb est aussi ouvert ailleurs.
- DVCACTNSPTD : action non prise en charge par l’appareil.
- DVCATTRNSPTD : attribut non pris en charge. Le micrologiciel de l’appareil ne prend pas en charge certains attributs. L’appareil passe automatiquement en mode sécuritaire (voir safe_mode). Attendez une mise à jour du micrologiciel dans Neviweb, ou ouvrez une issue pour qu’une exception soit ajoutée.
- DVCBUSY : Neviweb fait une mise à jour et les appareils ne sont pas disponibles. Réessayez plus tard.
- DVCCOMMTO : délai de communication dépassé. L’appareil n’a pas répondu à temps, ou il est lu trop souvent.
- DVCERR : la commande ou l’attribut a été refusé par l’appareil.
- DVCNOTSYNC : appareil non synchronisé avec Neviweb.
- DVCUNVLB : appareil non disponible. Neviweb ne peut pas joindre l’appareil, surtout les appareils Wi-Fi.
- MAINTENANCE : Neviweb est temporairement indisponible pour maintenance. Réessayez plus tard.
- SVCERR : service non disponible. Réessayez plus tard.
- SVCINVREQ : requête invalide envoyée à Neviweb. Le service n’existe pas ou la requête est mal formée.
- SVCUNAUTH : requête refusée par le serveur Neviweb, l’action n’est pas autorisée pour cet appareil.
- USRBADLOGIN : nom d’utilisateur ou mot de passe Neviweb invalide.
- USRSESSEXP : session expirée. Réduisez scan_interval.
- VALINVLD : valeur invalide envoyée à Neviweb.
- ReadTimeout : la requête a été envoyée mais l’appareil n’a pas répondu. Problème de réseau.
- TimeoutError : délai de la requête dépassé. Réessayez plus tard.

</details>

### Obtenir de l’aide

- [Ouvrez une issue](https://github.com/claudegel/sinope-130/issues/new/choose) pour un bogue, une trace d’erreur dans le journal ou un appareil manquant.
- Posez votre question dans l’un de ces fils : [Sinopé line voltage thermostats](https://community.home-assistant.io/t/sinope-line-voltage-thermostats/17157), [Sinopé light switch and dimmer](https://community.home-assistant.io/t/adding-support-for-sinope-light-switch-and-dimmer/38835).

## Réinitialisation d’un appareil

- Thermostats :
  1. Montez la température jusqu’à ce que l’affichage change.
  2. Appuyez sur les deux boutons jusqu’à ce que CLR s’affiche.
  3. Appuyez une fois sur le bouton du haut pour afficher YES.
  4. Appuyez sur les deux boutons en même temps et relâchez aussitôt. DONE devrait s’afficher.
  5. Le thermostat redémarre avec les réglages d’usine.
- Thermostats G2 :
  1. Montez la température jusqu’à ce que l’affichage change.
  2. Maintenez les deux boutons enfoncés jusqu’à ce que RST s’affiche.
  3. Attendez que l’appareil redémarre.

## Appareils pris en charge

En gros, tout ce qui peut être ajouté dans Neviweb. Les appareils Wi-Fi n’ont pas besoin de GT130.

<details>
<summary>Thermostats et thermopompes</summary>

- Thermostats Zigbee :
  - Sinopé TH1123ZB, thermostat de ligne 3000W
  - Sinopé TH1124ZB, thermostat de ligne 4000W
  - Sinopé TH1123ZB, thermostat de ligne pour aires publiques 3000W
  - Sinopé TH1124ZB, thermostat de ligne pour aires publiques 4000W
  - Sinopé TH1123ZB-G2, thermostat deuxième génération 3000W
  - Sinopé TH1124ZB-G2, thermostat deuxième génération 4000W
  - Sinopé TH1134ZB-HC, pour le verrouillage chauffage/climatisation
  - Sinopé TH1300ZB, thermostat de plancher chauffant 3600W
  - Sinopé TH1320ZB-04, thermostat de plancher chauffant
  - Sinopé TH1400ZB, thermostat basse tension
  - Sinopé TH1500ZB, thermostat bipolaire 3600W
  - Nordik TH1420ZB-01, thermostat de plancher hydronique radiant basse tension
  - Ouellet OTH3600-GA-ZB, thermostat de plancher
  - Ouellet OTH4000-ZB, thermostat de ligne 4000W
- Thermostats Wi-Fi :
  - Sinopé TH1123WF, thermostat de ligne Wi-Fi 3000W
  - Sinopé TH1124WF, thermostat de ligne Wi-Fi 4000W
  - Sinopé TH1133WF, thermostat de ligne Wi-Fi édition Lite 3000W
  - Sinopé TH1133CR, thermostat de ligne Sinopé Evo édition Lite 3000W
  - Sinopé TH1134WF, thermostat de ligne Wi-Fi édition Lite 4000W
  - Sinopé TH1134CR, thermostat de ligne Sinopé Evo édition Lite 4000W
  - Sinopé THEWF01, thermostat Wi-Fi édition Lite
  - Sinopé TH1143WF et TH1144WF, thermostats Wi-Fi 3000W et 4000W, deux fils, écran couleur
  - Sinopé TH1145WF, thermostat Wi-Fi 4000W, deux fils, écran couleur
  - Sinopé TH1300WF, TH1310WF, TH1315WF et TH1325WF, thermostats de plancher Wi-Fi 3600W
  - Sinopé TH1400WF, thermostat basse tension Wi-Fi
  - Sinopé TH1500WF, thermostat bipolaire Wi-Fi 3600W
  - Sinopé TH6500WF, TH6510WF, TH6250WF, TH6250WF-PRO et TH6251WF-PRO, chauffage/climatisation Wi-Fi (préliminaire, bénévoles recherchés pour tester)
  - Flextherm Concerto Connect FLP55, thermostat de plancher (le FLP55 ne fournit pas de statistiques d’énergie dans Neviweb)
  - Flextherm True Comfort, thermostat de plancher
  - SRM40, thermostat de plancher
- Contrôleurs de thermopompe :
  - Sinopé HP6000ZB-GE, pour thermopompe Ouellet avec connecteur Gree
  - Sinopé HP6000ZB-GE-RS485, pour thermopompe Tosot avec connecteur Gree
  - Sinopé HP6000ZB-MA, pour thermopompe Ouellet Convectair avec connecteur Midea
  - Sinopé HP6000ZB-HS, pour thermopompe Hisense, Haxxair et Zephyr
  - Sinopé HP6000WF-MA, pour thermopompe Ouellet Convectair avec connecteur Midea, Wi-Fi
  - Sinopé HP6000WF-TCL, pour thermopompe Runtru/Ameristar, Wi-Fi
  - Sinopé HP6000WF-HA, pour thermopompe Hotpoint, Wi-Fi

</details>

<details>
<summary>Éclairage, contrôleurs de charge et prises</summary>

- Éclairage Zigbee :
  - Sinopé SW2500ZB, interrupteur
  - Sinopé SW2500ZB-G2, interrupteur
  - Sinopé DM2500ZB, gradateur
  - Sinopé DM2500ZB-G2, gradateur
  - Sinopé DM2550ZB, gradateur
  - Sinopé DM2550ZB-G2, gradateur
  - SW2500ZB-VA, DM2500ZB-VA et DM2550ZB-VA connectés à une valve Sedna
- Contrôle spécialisé Zigbee :
  - Sinopé RM3250ZB, contrôleur de charge 50A
  - Sinopé RM3500ZB, contrôleur de charge Calypso 20,8A pour chauffe-eau
  - Sinopé SP2610ZB, prise murale
  - Sinopé SP2600ZB, prise portable intelligente
  - Sinopé MC3100ZB, multicontrôleur de valve Sedna pour système d’alarme
  - RM3250ZB-VA, SP2610ZB-VA, SP2600ZB-VA et MC3100ZB-VA connectés à une valve Sedna
- Contrôle spécialisé Wi-Fi :
  - Sinopé RM3500WF, contrôleur de charge Calypso 20,8A pour chauffe-eau
  - Sinopé RM3510WF, contrôleur de charge Calypso 20,8A pour chauffe-eau
  - Sinopé RM3250WF, contrôleur de charge 40A

</details>

<details>
<summary>Valves, détecteurs de fuite, capteurs de débit et moniteurs de réservoir</summary>

- Détecteurs de fuite et valves :
  - Sinopé VA4201WZ, valve Sedna 1 pouce, Wi-Fi
  - Sinopé VA4200WZ, valve Sedna 3/4 pouce, Wi-Fi
  - Sinopé VA4200ZB, valve Sedna 3/4 pouce, Zigbee
  - Sinopé VA4220WZ, valve Sedna 2e gén. 3/4 pouce
  - Sinopé VA4220WF, valve Sedna 2e gén. 3/4 pouce, Wi-Fi
  - Sinopé VA4220ZB, valve Sedna 2e gén. 3/4 pouce, Zigbee
  - Sinopé VA4221WZ, valve Sedna 2e gén. 1 pouce
  - Sinopé VA4221WF, valve Sedna 2e gén. 1 pouce, Wi-Fi
  - Sinopé VA4221ZB, valve Sedna 2e gén. 1 pouce, Zigbee
  - Sinopé WL4200, détecteur de fuite
  - Sinopé WL4200S, détecteur de fuite avec sonde déportée
  - Sinopé WL4200C, détecteur de fuite à câble périmétrique
  - Sinopé WL4200ZB, détecteur de fuite
  - Sinopé WL4210, détecteur de fuite
  - Sinopé WL4210S, détecteur de fuite avec sonde déportée
  - Sinopé WL4210C, détecteur de fuite à câble périmétrique
  - Sinopé WL4210ZB, détecteur de fuite
  - Sinopé WL4200ZB, connecté à une valve Sedna
  - Sinopé ACT4220WF-M, VA4220WF-M, valve Sedna multirésidentielle maîtresse 2e gén. 3/4 pouce, Wi-Fi
  - Sinopé ACT4220ZB-M, VA4220ZB-M, valve Sedna multirésidentielle secondaire 2e gén. 3/4 pouce, Zigbee
  - Sinopé ACT4221WF-M, VA4221WF-M, valve Sedna multirésidentielle maîtresse 2e gén. 1 pouce, Wi-Fi
  - Sinopé ACT4221ZB-M, VA4221ZB-M, valve Sedna multirésidentielle secondaire 2e gén. 1 pouce, Zigbee
- Capteurs de débit (par les valves Sedna 2e génération) :
  - Sinopé FS4220, capteur de débit 3/4 pouce
  - Sinopé FS4221, capteur de débit 1 pouce
- Moniteurs de niveau de réservoir :
  - Sinopé LM4110-ZB, moniteur de niveau de réservoir de propane
  - Sinopé LM4110-LTE, moniteur de niveau de réservoir de propane, LTE, plusieurs réservoirs

</details>

<details>
<summary>Passerelles et alimentation</summary>

- Passerelles :
  - GT130
  - GT4220WF et GT4220WF-M, passerelle mesh pour les valves
- Alimentation :
  - Sinopé ACUPS-01, batterie de secours pour valve Sedna

</details>
