## Home Assistant Neviweb130 Custom Components
[🇫🇷 Version française](doc/readme_fr.md)
> 💛 **Enjoying this integration?**  
> If you'd like to support its ongoing development, you can contribute here:
> [![Support via PayPal](https://cdn.rawgit.com/twolfson/paypal-github-button/1.0.0/dist/button.svg)](https://www.paypal.me/phytoressources/) or 
> [![Donate via Interac](https://img.shields.io/badge/Interac-Don-orange?style=for-the-badge)](doc/Donations.md)

Custom components to support [Neviweb](https://neviweb.com/) devices in [Home Assistant](http://www.home-assistant.io) (HA). 
Neviweb is a platform created by Sinopé Technologies to interact with their smart devices like thermostats, light 
switches/dimmers , load controllers, plug, valves and water leak detector etc. 

Neviweb130 (Sinope Neviweb130 in HACS) will manage the Zigbee devices connected to Neviweb via the GT130 gateway and the new Wi-Fi devices connected 
directly to Neviweb. It is presently almost up to date with Neviweb but some information are still missing from Sinopé. 
As new devices are launched by Sinopé, they are added to this custom-component. If you have a device that is not supported 
yet, please open an issue and I'll add it quickly.

Report a problem or suggest an improvement: [Open an issue](https://github.com/claudegel/sinope-130/issues/new/choose)

## Table of contents

- [Announcement](#announcement)
- [Supported devices](#supported-devices)
- [Prerequisite](#prerequisite)
- [Installation](#installation)
- [Configuration](#legacy-configuration)
- [Multi_accounts configuration](#multi-account-configuration)
- [V2 configuration](#v2-configuration)
- [Sedna valve](#sedna-valve)
- [GT130](#gateway-gt130)
- [Update system](#updater-system)
- [Request counter](#neviweb-daily-request-counter)
- [Multi instance (obsolete)](#running-more-than-one-instance-of-neviweb130-to-manage-different-neviweb-connections)
- [Services / Actions](#custom-services)
- [Debugging](#logging-for-debugging)
- [Eco-Sinopé](#catch-eco-sinope-signal-for-peak-period)
- [Energy and water statistics](#energy-and-water-statistics)
- [Localisation (language)](#localisation)
- [Troubleshooting](#troubleshooting)
- [Customization](#customization)
- [Device hard reset](#device-hard-reset)
- [TO DO](#to-do)

## Announcement

### Neviweb130-V2 is almost there

neviweb130 v5.0.0b0 is ready for testing.

## Supported Devices
Here is the list of currently supported devices. Basically, it's everything that can be added in Neviweb.
- Zigbee thermostats:
  - Sinopé TH1123ZB 3000W line voltage thermostat
  - Sinopé TH1124ZB 4000W line voltage thermostat
  - Sinopé TH1123ZB 3000W thermostat for public areas
  - Sinopé TH1124ZB 4000W thermostat for public areas
  - Sinopé TH1123ZB-G2 3000W thermostat, second generation
  - Sinopé TH1124ZB-G2 4000W thermostat, second generation
  - Sinopé TH1134ZB-HC for heating/cooling interlocking
  - Sinopé TH1300ZB 3600W floor heating thermostat
  - Sinopé TH1320ZB-04 floor heating thermostat
  - Sinopé TH1400ZB low voltage thermostat
  - Sinopé TH1500ZB 3600W double pole thermostat
  - Nordik TH1420ZB-01 low voltage radiant hydronic floor thermostat
  - Ouellet OTH3600-GA-ZB floor thermostat
  - Ouellet OTH4000-ZB 4000W line voltage thermostat
- Wi-Fi thermostats (no GT130 needed):
  - Sinopé TH1123WF Wi-Fi 3000W line voltage thermostat
  - Sinopé TH1124WF Wi-Fi 4000W line voltage thermostat
  - Sinopé TH1133WF Wi-Fi 3000W line voltage thermostat lite
  - Sinopé TH1133CR Sinopé Evo 3000W line voltage thermostat lite
  - Sinopé TH1134WF Wi-Fi 4000W line voltage thermostat lite
  - Sinopé TH1134CR Sinopé Evo 4000W line voltage thermostat lite
  - Sinopé THEWF01 Wi-Fi thermostat lite
  - Sinopé TH1143WF and TH1144WF Wi-Fi 3000W and 4000W thermostats, two wire connection, color screen
  - Sinopé TH1145WF Wi-Fi 4000W thermostat, two wire connection, color screen
  - Sinopé TH1300WF, TH1310WF, TH1315WF and TH1325WF Wi-Fi 3600W floor thermostats
  - Sinopé TH1400WF Wi-Fi low voltage thermostat
  - Sinopé TH1500WF Wi-Fi 3600W double pole thermostat
  - Sinopé TH6500WF, TH6510WF, TH6250WF, TH6250WF-PRO and TH6251WF-PRO Wi-Fi heat/cool (preliminary, volunteers needed to test)
  - Flextherm Concerto Connect FLP55 floor thermostat (the FLP55 does not provide energy stats in Neviweb)
  - Flextherm True Comfort floor thermostat
  - SRM40 floor thermostat
- Heat pump controllers:
  - Sinopé HP6000ZB-GE for Ouellet heat pump with Gree connector
  - Sinopé HP6000ZB-GE-RS485 for Tosot heat pump with Gree connector
  - Sinopé HP6000ZB-MA for Ouellet Convectair heat pump with Midea connector
  - Sinopé HP6000ZB-HS for Hisense, Haxxair and Zephyr heat pump
  - Sinopé HP6000WF-MA for Ouellet Convectair heat pump with Midea connector, Wi-Fi
  - Sinopé HP6000WF-TCL for Runtru/Ameristar heat pump, Wi-Fi
  - Sinopé HP6000WF-HA for Hotpoint heat pump, Wi-Fi
- Zigbee lighting:
  - Sinopé SW2500ZB light switch
  - Sinopé SW2500ZB-G2 light switch
  - Sinopé DM2500ZB dimmer
  - Sinopé DM2500ZB-G2 dimmer
  - Sinopé DM2550ZB dimmer
  - Sinopé DM2550ZB-G2 dimmer
  - SW2500ZB-VA, DM2500ZB-VA and DM2550ZB-VA connected to a Sedna valve
- Zigbee specialized control:
  - Sinopé RM3250ZB load controller 50A
  - Sinopé RM3500ZB Calypso load controller 20.8A for water heater
  - Sinopé SP2610ZB in-wall outlet
  - Sinopé SP2600ZB smart portable plug
  - Sinopé MC3100ZB Sedna valve multi-controller for alarm system
  - RM3250ZB-VA, SP2610ZB-VA, SP2600ZB-VA and MC3100ZB-VA connected to a Sedna valve
- Wi-Fi specialized control:
  - Sinopé RM3500WF Calypso load controller 20.8A for water heater
  - Sinopé RM3510WF Calypso load controller 20.8A for water heater
  - Sinopé RM3250WF load controller 40A
- Water leak detectors and valves:
  - Sinopé VA4201WZ, Sedna valve 1 inch, Wi-Fi
  - Sinopé VA4200WZ, Sedna valve 3/4 inch, Wi-Fi
  - Sinopé VA4200ZB, Sedna valve 3/4 inch, Zigbee
  - Sinopé VA4220WZ, Sedna 2nd gen 3/4 inch
  - Sinopé VA4220WF, Sedna 2nd gen 3/4 inch, Wi-Fi
  - Sinopé VA4220ZB, Sedna 2nd gen 3/4 inch, Zigbee
  - Sinopé VA4221WZ, Sedna 2nd gen 1 inch
  - Sinopé VA4221WF, Sedna 2nd gen 1 inch, Wi-Fi
  - Sinopé VA4221ZB, Sedna 2nd gen 1 inch, Zigbee
  - Sinopé WL4200, water leak detector
  - Sinopé WL4200S, water leak detector with sensor
  - Sinopé WL4200C, perimeter cable water leak detector
  - Sinopé WL4200ZB, water leak detector
  - Sinopé WL4210, water leak detector
  - Sinopé WL4210S, water leak detector with sensor
  - Sinopé WL4210C, perimeter cable water leak detector
  - Sinopé WL4210ZB, water leak detector
  - Sinopé WL4200ZB, connected to a Sedna valve
  - Sinopé ACT4220WF-M, VA4220WF-M, Sedna multi-residential master valve 2nd gen 3/4 inch, Wi-Fi
  - Sinopé ACT4220ZB-M, VA4220ZB-M, Sedna multi-residential slave valve 2nd gen 3/4 inch, Zigbee
  - Sinopé ACT4221WF-M, VA4221WF-M, Sedna multi-residential master valve 2nd gen 1 inch, Wi-Fi
  - Sinopé ACT4221ZB-M, VA4221ZB-M, Sedna multi-residential slave valve 2nd gen 1 inch, Zigbee
- Flow sensors (supported through the 2nd gen Sedna valves):
  - Sinopé FS4220, 3/4 inch flow sensor
  - Sinopé FS4221, 1 inch flow sensor
- Tank level monitors:
  - Sinopé LM4110-ZB, propane tank level monitor
  - Sinopé LM4110-LTE, propane tank level monitor, LTE, multiple tanks
- Gateways:
  - GT130
  - GT4220WF and GT4220WF-M, mesh gateway for valves
- Power supply:
  - Sinopé ACUPS-01, battery backup for Sedna valve

## Prerequisite
You need to connect your devices to a GT130 web gateway and add them in your Neviweb portal before being able to 
interact with them within Home Assistant. Wi-Fi devices must be connected directly to Neviweb. Some Zigbee devices 
can be connected directly to a Sedna valve which is connected to Neviweb directly. Please refer to 
the instructions manual of your device or visit [Neviweb support](https://support.sinopetech.com/)

Wi-Fi devices can be connected in the same network (location) then the GT130 Zigbee devices or in a separate network.
**Neviweb130** support up to three networks in neviweb.

There are four custom components giving you the choice to manage your devices via the neviweb portal or directly via local 

- [**neviweb**](https://github.com/claudegel/sinope-1) (HACS: Sinope Neviweb) custom component to manage your devices via Neviweb portal.
- [**sinope**](https://github.com/claudegel/sinope-gt125) (HACS: Sinope GT125) custom component to manage your devices directly via
  your GT125 web gateway.
- **Zigbee gateway**:
  - [**neviweb130**](https://github.com/claudegel/sinope-130) (HACS: Sinope Neviweb130) this custom component, to manage your devices
    via neviweb portal.
  - [**sinope-zha**](https://github.com/claudegel/sinope-zha) where I put all new Sinopé devices quirks before they are merged
    into zha-device-handlers. Buy a Zigbee gateway like Dresden ConBee II usb dongle and manage your Zigbee device locally
    via ZHA component. I'm adding support for Sinopé Zigbee in zha-device-handlers. You can test new Sinopé devices quirks
    in HA by coping the sinope-zha files directly in your HA setup. ZHA will load them in place of the standard sinopé quirks.

You need to install only one of them but all can be used at the same time on HA. Zigbee devices managed directly via 
ConBee II must be removed from Neviweb as they cannot be on two Zigbee networks at the same time.

## Installation
There are two ways to install this custom component:
- With HACS:
  - This repository is compatible with the Home Assistant Community Store ([HACS](https://community.home-assistant.io/t/custom-component-hacs/121727)).
  - After installing HACS, install 'sinope-130' from the store, restart Home Assistant and add the integration (see Configuration).
- Manually:
  - Download the zip file of this repository with the green Code button.
  - Extract the zip file on your computer, then copy the entire `custom_components` folder into your Home Assistant `config` directory (where your `configuration.yaml` file is).
  - Your config directory should look like this:

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
      www/
        neviweb130/
          heat-0.png ... (device icons, see Device and weather icons)
          weather/
            Sun.png ... (weather icons)
      ...
    ```

    Upon the first startup of HA, Neviweb130-V2 will perform the following operations:
    - import the V1 configuration from `configuration.yaml` into the `config_flow` (HA's modern configuration method).
    - convert `unique_id`s to an alphanumeric format (int to str).
    - convert device model numbers to an alphanumeric format (int to str).
  These changes are required by HA. No action is required on the part of users.

## Legacy configuration

To enable Neviweb130 management in your installation, add the following to your `configuration.yaml` file, then restart 
Home Assistant.

```yaml
# Example configuration.yaml entry
neviweb130:
  username: '«your Neviweb username»'
  password: '«your Neviweb password»'
  network: '«your gt130 location name in Neviweb»'   # gt130 emplacement dans Neviweb
  network2: '«your second location name in Neviweb»' # 2e emplacement
  network3: '«your third location name in Neviweb»'  # 3e emplacement
  scan_interval: 360
  homekit_mode: False
  ignore_miwi: False
  stat_interval: 1800
  notify: "both"
  safe_mode: "-"
```
Networks names are the names found on top of first page after logging into Neviweb. If you have more then one network, 
just click on icon on top to find all networks names. Select the one used for Zigbee GT130 or Wi-Fi devices. Both devices types 
must be on same network to work in neviweb130. If you have two networks for two GT130 or two Wi-Fi groups then you can 
add network2 parameter in your configuration.yaml. See below. You can't mix miwi devices and Zigbee/Wi-Fi devices on the 
same network. For miwi devices install [Neviweb](https://github.com/claudegel/sinope-1) 
custom_component which can run along with this custom_component in HA.

![network](www/network.jpg)

**Configuration options:**  

| key               | required | default                                                                                                            | description                                                                                                                                                                                                                  |
|-------------------|----------|--------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **username**      | yes      |                                                                                                                    | Your email address used to log in Neviweb.                                                                                                                                                                                   |
| **password**      | yes      |                                                                                                                    | Your Neviweb password.                                                                                                                                                                                                       |
| **network**       | no       | if not specified, 1st location found is used. Write the name of the GT130 location in Neviweb you want to control. | Network name is the location name in Neviweb written on top center of first page, where your Wi-Fi or Zigbee devices are registered.                                                                                         |
| **network2**      | no       | 2nd location found                                                                                                 | The name of the second location you want to control (Zigbee and/or Wi-Fi only). Don't add it if you have only one network.                                                                                                   |
| **network3**      | no       | 3rd location found                                                                                                 | The name of the third location you want to control (Zigbee and/or Wi-Fi only). Don't add it if you have only one network.                                                                                                    |
| **scan_interval** | no       | 420                                                                                                                | The number of seconds between each access to Neviweb to update device state. Sinopé asked for a minimum of 5 minutes between polling now so you can reduce scan_interval to 300. Don't go over 600, the session will expire. |
| **homekit_mode**  | no       | False                                                                                                              | Add support for Homekit specific values. Not needed if you don't use homekit.                                                                                                                                                |
| **ignore_miwi**   | no       | False                                                                                                              | Ignore miwi devices if present in same location then Zigbee and/or Wi-Fi devices. Warns if the wrong Neviweb location is set.                                                                                                     |
| **stat_interval** | no       | 1800                                                                                                               | The number of seconds between each access to Neviweb for energy statistic update. Scan will start after 5 minutes from HA startup and will be updated at every 300 to 1800 seconds.                                          |
| **notify**        | no       | both                                                                                                               | The method to send notification in case of device error. value option are `nothing`, `logging`, `notification`, `both`.   |                                                                        
| **safe_mode**     | no       | -                                                                                                                  | Safe mode is used to run device update in a way that won't crash in case of bad or missing parameters. If a device receive DVCATTRNSPTD error, safe_mode will fire automatically for that device to detect faulty attribute and allow device update to complete. Default value is "-". If you want to test device attributes put your device ID in safe_mode value ex. "12345".                                             |

If you have a GT125 also connected to Neviweb the network parameter is mandatory, or it is possible that during the 
setup, the GT125 network will be picked up accidentally. If you have only two GT130/Wi-Fi network, you can omit there 
names as during setup, the first two network found will be picked up automatically. If you prefer to add networks names 
make sure that they are written «exactly» as in Neviweb. (first letter capitalized or not). Avoid also accented letters 
as Home Assistant will remove them and location name won't match preventing custom_component loading.

## Multi-Account Configuration
(New in v3.1.0)

If you need to control devices from **multiple Neviweb accounts** (e.g., your home and a neighbor's), you can now use the new multi-account configuration format. This eliminates the need to duplicate the custom component folder.

```yaml
# Multi-account configuration example
neviweb130:
  accounts:
    # Account with multiple locations (home + chalet)
    - username: 'your_email@example.com'
      password: 'your_password'
      # location was called network in previous versions.
      #
      # Optional: you can target up to 3 locations for this account:
      #   location / location2 / location3 (or network / network2 / network3)
      #
      # If you omit all locations, the integration will automatically use the first 1–3 locations
      # returned by Neviweb for this account.
    
    # Separate account for parents (using 'network' - works the same as 'location')
    - username: 'parents_email@example.com'
      password: 'parents_password'
      location: '5678'           # Optional: location id/name (or use 'network')
      prefix: 'parents'          # Optional: account alias (used in entity naming)
  
  # Global settings (apply to all accounts)
  scan_interval: 360
  homekit_mode: False
  ignore_miwi: False
  stat_interval: 1800
  notify: "both"
  safe_mode: "-"
```

> **⚠️ Important: Entity Name Conflicts in Multi-Account Setup**
> 
> Entity names are built from the integration domain (`neviweb130`), plus optional `prefix` and/or `location` values.
> 
> **Problem:** If you omit both `prefix` and `location` for multiple accounts, and both accounts have devices with similar names (e.g., both have a thermostat called "LivingRoom"), Home Assistant may auto-suffix entity_ids:
> - `climate.neviweb130_livingroom`
> - `climate.neviweb130_livingroom_2`  ← Collision handled by HA
> 
> **Solution:** Provide either a unique `prefix` (account alias), or explicit `location` names/ids, to keep entity_ids stable and readable:
> ```yaml
> accounts:
>   - username: 'user1@example.com'
>     password: 'pass1'
>     location: 'Home'
>     prefix: 'me'          # ← account alias
>   - username: 'user2@example.com'
>     password: 'pass2'
>     location: 'Chalet'
>     prefix: 'parents'     # ← different account alias
> ```
> Example: `climate.neviweb130_parents_chalet_climate_livingroom`.

**Multi-account configuration options:**

| key | required | default | description
| --- | --- | --- | ---
| **accounts** | yes (for multi-account) | | List of accounts to connect to
| **username** | yes | | Your email address for this Neviweb account
| **password** | yes | | The password for this Neviweb account
| **location** (or **network**) | no | first location found | Location id/name for this account (network #1).
| **location2** (or **network2**) | no | second location found | Location id/name for this account (network #2).
| **location3** (or **network3**) | no | third location found | Location id/name for this account (network #3).
| **prefix** | no | (empty) | Optional account alias used in entity naming to distinguish accounts.

**Notes:**
- `prefix` is optional. If omitted, it is not included in the entity name (Home Assistant may auto-suffix entity_ids if collisions occur).
- If your `location` names/ids are already unique across your accounts (e.g., you use an address, site code, or other unique label), you can omit `prefix` entirely and rely on `location` to distinguish entities.
- Each account maintains its own independent connection to Neviweb.
- **Multiple locations per account**:
  - If you omit all locations, the integration will automatically use the first 1–3 locations returned by Neviweb.
  - Or you can explicitly set `location2` and `location3`.
- Both `location*` and `network*` are accepted as aliases in the new format for consistency with the legacy format.
- Global settings (`scan_interval`, `homekit_mode`, etc.) apply to all accounts.
- The legacy single-account configuration format (shown above) remains fully supported for backward compatibility.

**Example entity names:**
- **Legacy single-account config (backward compatible naming)**:
  - 1st location → `climate.neviweb130_climate_bedroom`
  - 2nd location → `climate.neviweb130_climate_2_bedroom`
  - 3rd location → `climate.neviweb130_climate_3_bedroom`
- **Multi-account config (`accounts:`)**:
  - With prefix + location → `climate.neviweb130_parents_chalet_climate_living_room`
  - With location only (no prefix) → `climate.neviweb130_chalet_climate_living_room`

## V2 Configuration
(new since version 5.0.0)

Neviweb130 V2 is version v5.0.0 of the current Neviweb130. An update will be released as soon as the final compatibility 
tests for the migration from Neviweb130 to Neviweb130-V2 are complete. Version V2 has been designed to meet the latest 
Home Assistant standards. Configuration via **configuration.yaml** is now obsolete.

- **Via the neviweb130 update**:

  The configuration from `configuration.yaml` is migrated to the `config_flow`, which is the modern HA approach. Options in
  `configuration.yaml` can be safely removed or commented out. Device names are preserved, and attributes remain accessible.
  The configuration can be found under Settings > Devices & Services > Neviweb130. All devices are listed there, and each one
  now has a dedicated graphical configuration page. Neviweb130-V2 now supports French or English, depending on your HA
  configuration; services, entities, and attributes are all automatically translated.

  The configuration for the Neviweb130-V2 can be found here:

  ![options](www/options.jpg)

  Here, in order, you can:

  - Add a new Neviweb account (gateway). Up to 3 accounts can be managed.
  - Modify certain neviweb130 options (see below).
  - Modify the neviweb130-V2 configuration (see below). Up to three locations can be supported for each
    Neviweb account. Permission must be requested from Sinopé to activate the third location.

  It is no longer necessary to restart HA after changing settings; Neviweb130-V2 reloads automatically.
  A connection manager (Session_manager) handles closing connections to Neviweb and establishing new ones as needed.
  This eliminates the ACCSESSEXC errors received from Neviweb when restarting HA too frequently.

  *Available configuration options*:

  ![configuration options](www/configuration.jpg)

  *Neviweb130-V2 configuration, imported from Neviweb130-V1*:

  ![reconfiguration](www/reconfigurer.jpg)

- **Via a clean installation**:

  For a fresh installation, install Neviweb130-V2 via HACS (Sinopé neviweb130), minimum version v5.0.0. Then go to Settings /
  Devices & Services. At the bottom of the page, click **Add integration** and search for **Sinopé Neviweb130**.
  A configuration window will appear on the screen for entering your Neviweb connection settings.

  ![new configuration](www/nouveau_pont.jpg)

  The settings are:
- Neviweb account name; the first one is named **default**. You can keep it, replace it, or even leave this field blank to
  use the same device names as in Neviweb130-V1.
- Neviweb email
- Neviweb password
- First location
- Second location
- Third location

  These fields are optional if you do not have a Miwi device. Otherwise, you must enter the location name. Unused locations
  can be left blank, or you can enter "_" to instruct Neviweb130-V2 not to search for them.
- Scan_interval, default 420 seconds (300 to 600).
- HomeKit support, optional
- Ignore Miwi devices, optional
- Stat_interval, default 1800 seconds
- Notifications for device disconnections, 4 options:
  - nothing: no notification
  - logging: logs only
  - Notification: receive a notification upon device disconnection
  - Both: "Notification" plus "logging"
- Device ID to update in safe mode. For problematic devices (Wi-Fi?)

Then, Neviweb130-V2 is reloaded and will begin retrieving the Neviweb devices.

The major difference between V1 and V2 is that it is no longer necessary to create sensors to track specific attributes 
of your devices. For all devices, neviweb130-V2 automatically creates attribute entities.

- sensor, for numeric attributes to be monitored, such as temperature, voltage, and energy statistics.
- binary_sensor, for binary attributes, such as leak sensors.
- button, to modify or reset the value of an on/off or alarm-type attribute.
- number, to change the numeric value of an attribute (e.g., minimum/maximum temperature, away temperature, etc.).
- switch, to enable or disable an attribute.
- select, for attributes with a choice of options. All options are translated, so it is no longer necessary to enter
  numeric values ​​for intervals like 15 seconds, 15 minutes, etc. Neviweb130-V2 automatically handles the conversion
  when sending values ​​to Neviweb and receiving values ​​from Neviweb.

You can find all these attribute entities on each device's page (Settings > Devices & Services > Neviweb130).
They are updated in real-time by HA. These entities can be used directly in your automations or with the Energy dashboard.
If you install neviweb130-V2 via an update, you will need to re-validate your automations. They will remain functional, but
by using the new attribute entities, you can eliminate your separate sensors and simplify your automations.

A few attribute entities may be missing. They can easily be added once I am notified.

Here is a sample device page:

![Page appareil](www/page_appareil.jpg)
![Page appareil suite](www/page_appareil_suite.jpg)

### Integration options

Click on Configure on the neviweb130 integration page to reach these options (see also [doc/options_en.md](doc/options_en.md)):
- **prefix**: Neviweb account name.
- **log_level**, **log_max_bytes**, **log_backup_count**, **log_reset_on_start**: settings of the neviweb130 log file (see Troubleshooting).
- **download_log**: copies the log file to `/local/neviweb130.log` so you can download it from your browser. It is deleted after 30 minutes.
- **reload**: reloads neviweb130 without restarting Home Assistant.
- **migrate**: migrates old numeric unique_id to the new text unique_id required by HA.
- **request_limit** (default 25000): daily safety limit of requests sent to Neviweb. Neviweb's own limit is 30000 per day. A notification is sent when the request counter sensor goes over this value.
- **update_check_interval** (1h, 3h, 6h, 12h or 24h, default 6h): how often the update entity checks GitHub for a new neviweb130 release.
- **backup_mode** (full or partial) and **backup_folders** (default `config`): backup made by the update entity before installing a new version. `full` calls `hassio.backup_full`. `partial` calls `hassio.backup_partial` with the folders listed in backup_folders (`config` means the Home Assistant configuration). Both need a Home Assistant installation with the Supervisor.

## Sedna valve
There are two ways to connect a Sedna valve to Neviweb:
- Wi-Fi direct connection. Leak sensors are connected directly to the Sedna valve, which closes when a leak is detected.
- Through the GT130 in Zigbee mode. Leak sensors are also connected to the GT130, but a leak detection is not passed to the valve. You need an automation in Neviweb or HA to close the Sedna valve when a sensor detects a leak.

Both modes are supported by this custom component.

## Gateway GT130
The `gateway_status` binary sensor of the GT130 tells you whether the gateway is online or offline in Neviweb.

## Updater system

Neviweb130 now include a complete update system that include:
- Automatic update check every 6 hours by default (update_check_interval option):
  - New update available.
  - Pre-release available.
  - Breaking changes.
  - Version notes.

- SHA-256 validation:
  - Get official SHA-256 from GitHub.
  - Download update zip file.
  - Validate SHA-256.
  - If mismatch, cancel update and notify.

- Auto Rollback if error detected during update:
  - Restore old version automatically.
  - Notify user of the problem.
 
- Persistent notifications on:
  - Success: "Update successful".
  - Fail: "Update fail, rollback performed".
  - SHA-256 error: "Update aborted for security".
 
- Breaking changes detection:
  The updator scan version notes from GitHub. If breaking changes are detected:
  - Add special icon in updater card.
  - Add (Breaking changes) in updater title.
 
- Pre-release detection if version contain, b0, -beta or rc1 etc:
  The updator scan update version from GitHub. If pre-release version is detected:
  - Add special icon in updater card.
  - Add (Pre-release) in updater title.

- Backup option:
  A backup is made before the update, set by the backup_mode and backup_folders options (see Integration options).

- Version notes can be viewed via link provided on the update card that point to GitHub releases motes.

- Updater have many attributes to help user:
  - check_interval: set by the update_check_interval option (default 6h).
  - last_check: date/time of last available version check.
  - next_check: date/time of next available version check.
  - last_update_success: Last date/time an update was done.
  - update_status: list all step performed during update.
  - rollback_status: If an update fail, last active version will be rolled back.
  - update_percentage: Show a slider for update process followup.

You will need to deactivate HACS update card or you will get two updates notifications with two updates cards. 
This can be done in parameters / devices & services / HACS. Pick 'Sinope Neviweb130' line and deactivate 
the pre-release button if set. Locate the Sinope Neviweb130 integration and click on the three vertical 
dots on the right end of the line. There are two options: `2 entities` and `deactivate the device`. Clic on `2 entities`.
Then select update. Click on the configuration button and deactivate option `Visible`. It will still be possible to 
do manual update or redownload neviweb130 via HACS.

You can also wait for a new update and select HACS update card. Then clic on the configuration button and deactivate the 
`Visible` option.

## Neviweb daily request counter
As Sinopé is becoming more picky about request number per day, limit fixed to 30000. If you reach that limit you 
will be disconnected until midnight. This is very bad if you have many devices or doing development on neviweb130.
I've added a daily Neviweb request counter that is reset to 0 at midnight and suvive HA restart. It create a 
sensor sensor.neviweb130_daily_requests that increase at each request: update, stats polling, error status, etc.
The sensor survive HA restart and is set back to 0 at midnight every days.

This way it is possible to improve your scan_interval to get the higher frequency without busting the limit.
When reaching 25000 requests, neviweb130 will send a notification. This warning limit is set with the request_limit option.

## Running more than one instance of neviweb130 to manage different Neviweb connections
> This section is still working but as Neviweb130 now support multi account directly, it become obsolete.
>
>It is possible to run two instance of neviweb130, but you need to use two different username (email) and password to 
>connect to Neviweb.
>Steps to achieve this:
>
>- Create another directory in config/custom_components like neviweb131.
>- Copy all files from directory neviweb130 to new directory neviweb131.
>- In neviweb131, edit file manifest.json to change the line #2, "domain": "neviweb130",
>and change it to the same name as the directory you just create. "domain": "neviweb131",
>- Add a second configuration in configuration.yaml like this:
>```yaml
># Example configuration.yaml entry for a second neviweb130 instance named neviweb131.
>neviweb131:
>   username: 'your Neviweb username for second connection'
>   password: 'your Neviweb password for second connection'
>   network: 'your gt130 location name in second Neviweb' (gt130 emplacement dans Neviweb)
>   network2: 'your second location name in second Neviweb' (2e emplacement)
>   network3: 'your third location name in second Neviweb' (3e emplacement)
>   scan_interval: 360
>   homekit_mode: False
>   ignore_miwi: False
>   stat_interval: 1800
>   notify: "both"
>```
>- Restart Home Assistant
>
>All devices on this second instance will have a name like `climate.neviweb131_climate_office_thermostat`.

## Custom services
Automations use actions (services) to send commands, e.g. light.turn_on. For Sinopé devices connected through neviweb130, custom actions send specific information to devices or change device parameters. They are available in Developer tools → Actions and in automations:
- neviweb130.set_second_display, to change the thermostat second display from setpoint temperature to outdoor temperature. This needs to be sent only once to each device.
- neviweb130.set_climate_keypad_lock, to lock the keypad of the climate device.
- neviweb130.set_light_keypad_lock, to lock the keypad of the light device.
- neviweb130.set_switch_keypad_lock, to lock the keypad of the switch device.
- neviweb130.set_light_timer, to set a timer in seconds (0 to 10800) after which the light turns off.
- neviweb130.set_switch_timer, to set a timer in seconds (0 to 10800) after which the switch or multi-controller turns off.
- neviweb130.set_switch_timer2, to set timer 2 in seconds (0 to 10800) after which the multi-controller turns off.
- neviweb130.set_led_indicator, to change the LED indicator color and intensity of light devices for the «on» and «off» states. Any RGB color can be sent with the red, green and blue parameters.
- neviweb130.set_time_format to display time in 12h or 24h on thermostats.
- neviweb130.set_temperature_format to display temperature in Celsius or Fahrenheit format on thermostats.
- neviweb130.set_backlight to set backlight intensity in state «on» or «off» for thermostats.
- neviweb130.set_wattage to set wattageOverload for light devices.
- neviweb130.set_auxiliary_load to set the status and load of the auxiliary heating.
- neviweb130.set_setpoint_min to set minimum setpoint temperature for thermostats.
- neviweb130.set_setpoint_max to set maximum setpoint temperature for thermostats.
- neviweb130.set_cool_setpoint_min to set minimum cooling setpoint for TH1134ZB-HC.
- neviweb130.set_cool_setpoint_max to set maximum cooling setpoint for TH1134ZB-HC.
- neviweb130.set_floor_limit_low to set minimum setpoint temperature for floor thermostats. (5 to 34°C, 0 = off)
- neviweb130.set_floor_limit_high to set maximum setpoint temperature for floor thermostats. (7 to 36°C, 0 = off)
- neviweb130.set_sensor_leak_alert to set the leak alert of the water leak sensor.
- neviweb130.set_sensor_temp_alert to set the low temperature alert of the water leak sensor.
- neviweb130.set_sensor_closure_action to set the valve closure action on leak, only for leak sensors connected directly to the Sedna valve.
- neviweb130.set_valve_alert to set low battery alert status.
- neviweb130.set_valve_temp_alert to set the low temperature alert on the Sedna valve.
- neviweb130.set_early_start to set early heating on/off for Wi-Fi thermostats.
- neviweb130.set_air_floor_mode to switch between floor or ambient temperature sensor to control room temperature.
- neviweb130.set_floor_air_limit to set floor thermostat max air limit temperature.
- neviweb130.set_phase_control to set phase control mode for DM2550ZB dimmer (reverse or forward).
- neviweb130.set_hvac_dr_options to set or reset DR period option in Neviweb for thermostats.
- neviweb130.set_hvac_dr_setpoint to adjust the thermostat setpoint reduction during the DR period, 100 to -100 (°C × 10). 0 only makes the small icon flash.
- neviweb130.set_load_dr_options to set or reset DR period options in Neviweb for load controller.
- neviweb130.set_cycle_output to set main cycle length of low voltage thermostat in minutes.
- neviweb130.set_aux_cycle_output to set auxiliary cycle length of low voltage thermostats in minutes.
- neviweb130.set_control_onoff to change the status of outputs 1 and 2 of the Sedna valve multi-controller.
- neviweb130.set_battery_type to set the battery type, alkaline or lithium, for the water leak sensor.
- neviweb130.set_tank_size to set the water heater tank capacity for Calypso RM3500ZB.
- neviweb130.set_low_temp_protection to activate or not the water heater protection for water temperature. Below 45°C, heating restarts automatically.
- neviweb130.set_controlled_device to change the name of the device controlled by the RM3250ZB load controller.
- neviweb130.set_flow_meter_model to change the flow meter model connected to the 2nd gen Sedna valve and start/stop leak protection from flow meter.
- neviweb130.set_flow_meter_delay to set the leak delay before the valve closes when a leak is detected by the flow meter. 
- neviweb130.set_flow_meter_options to set the flow meter action: close the valve (yes/no) and to send alert message (yes/no), or just do nothing.
- neviweb130.set_tank_type to set tank type for LM4110-ZB, propane or oil.
- neviweb130.set_gauge_type to set gauge type for LM4110-ZB on propane tank, model 5-95 or 10-80.
- neviweb130.set_low_fuel_alert to set low fuel level limit for propane tank, 0 (off), 10, 20 or 30%.
- neviweb130.set_tank_height to set the oil tank height for LM4110-ZB sensor, 0 (off), 23, 24, 35, 38, 47, 48, 50.
- neviweb130.set_fuel_alert to set the fuel alert on/off for LM4110-ZB.
- neviweb130.set_power_supply to set the Sedna valve power source: battery, acups-01 or both.
- neviweb130.set_battery_alert to set battery alert on/off for LM4110-ZB.
- neviweb130.set_input_output_names to set name for input 1 and 2 and output 1 and 2 of MC3100ZB device.
- neviweb130.set_activation to activate or block Neviweb polling for a device.
- neviweb130.set_sensor_type to set the sensor type, 10k or 12k.
- neviweb130.set_remaining_time to set value for coldLoadPickupRemainingTime attribute.
- neviweb130.set_on_off_input_delay to set the «on» or «off» delay in seconds for input 1 and 2 of MC3100ZB.
- neviweb130.set_em_heat to turn auxiliary heat on or off for floor and low voltage thermostats. It replaces turn_aux_heat_on and turn_aux_heat_off, deprecated by HA.
- neviweb130.set_display_config to turn the heat pump display on or off.
- neviweb130.set_sound_config to turn the heat pump sound on or off.
- neviweb130.set_heat_pump_operation_limit to set the minimum operating temperature of the heat pump.
- neviweb130.set_heat_lockout_temperature to set maximum outside temperature limit to allow heating device operation.
- neviweb130.set_cool_lockout_temperature to set minimum outside temperature limit to allow cooling device operation.
- neviweb130.set_hc_second_display to set second display of TH1134ZB-HC thermostat.
- neviweb130.set_language to set display language on TH1134ZB-HC thermostats.
- neviweb130.set_neviweb_status, to set global Neviweb status, home / away, via the GT130 sensor.
- neviweb130.set_climate_neviweb_status, to set global Neviweb status, home / away, via any thermostat.
- neviweb130.set_refuel_alert, to get an alert when the propane tank is refueled.
- neviweb130.set_accessory_type, to set the accessory type (humidifier, dehumidifier, air exchanger) connected to TH6500WF or TH6250WF.
- neviweb130.set_schedule_mode, to set the schedule mode, manual or auto for TH6500WF or TH6250WF.
- neviweb130.set_flow_alarm_disable_timer, to disable the abnormal flow alarm for 1 second to 24 hours.
- neviweb130.set_heatcool_setpoint_delta, to set a temperature delta between heating setpoint and cooling setpoint from 1 to 5°C in auto mode for TH6xxxWF.
- neviweb130.set_fan_filter_reminder, to set the delay between each fan filter cleaning from 1 to 12 months, for TH6xxxWF.
- neviweb130.set_temperature_offset, to adjust temperature sensor from -2 to 2°C in 0.5°C steps, for TH6xxxWF.
- neviweb130.set_aux_heating_source, to select which type of auxiliary heating source is in use for TH6xxxWF.
- neviweb130.set_fan_speed, to set fan speed, on or auto for TH6xxxWF.
- neviweb130.set_min_time_on, to set the minimum time the device stays on before turning off (run-on time) for TH6500WF and TH6250WF.
- neviweb130.set_min_time_off, to set the minimum time the device stays off before turning on again (cooldown time) for TH6500WF and TH6250WF.
- neviweb130.set_heat_interstage_delay and set_cool_interstage_delay, to set the minimum heating or cooling time before going to the next stage for TH6500WF and TH6250WF.
- neviweb130.set_heat_dissipation_time and set_cool_dissipation_time, to set the heating or cooling purge time for TH6xxxWF.
- neviweb130.set_reversing_valve_polarity, to set the polarity of the heat pump reversing valve for TH6500WF and TH6250WF.
- neviweb130.set_humidity_mode, to set the humidity setpoint mode for TH6500WF and TH6250WF.
- neviweb130.set_room_setpoint_away, to set the away room setpoint for Wi-Fi thermostats.
- neviweb130.set_cool_setpoint_away, to set the away cooling setpoint for TH6xxxWF and HP6000WF.
- neviweb130.set_pump_protection, to set pump protection on/off for low voltage thermostats.
- neviweb130.set_led_on_intensity and set_led_off_intensity, to set the LED indicator intensity in «on» or «off» state.
- neviweb130.set_light_min_intensity, to set the dimmer minimum intensity.
- neviweb130.set_key_double_up, to activate or deactivate the double up key press action for DM2550ZB.
- neviweb130.set_switch_power_timer, to set the RM3250ZB timer, off or 1 min to 24 h. The device turns off after that delay.
- neviweb130.set_switch_temp_alert, to set the low temperature alert of the MC3100ZB.

Services marked «Equipment configuration should be performed by a professional» in Developer tools change how the HVAC equipment runs. Use them only if you know your installation.

## Logging for debugging
Neviweb130 writes all its log messages to its own file, `neviweb130_log.txt`, in your config directory, not to `home-assistant.log`. By default the file is cleared each time the integration starts (log_reset_on_start), rotated when it reaches 2 MB (log_max_bytes) and 2 rotated files are kept (log_backup_count). These settings and the log level are in the integration options.

To help debugging, add relevant snippet of this file to any issue you may report.

## Catch Éco Sinopé signal for peak period
If at least one thermostat or load controller is registered in the Éco Sinopé program, you can detect when Neviweb sends the pre-heating signal for thermostats or the turn-off signal for load controllers. These attributes tell you that a peak period is coming and how it is managed:

- For thermostats:
  - **eco_status**: «off» during normal operation, turns «on» at the beginning of the pre-heating period. This is the attribute to follow to detect a peak start.
  - **eco_setpoint**: «off» during normal operation, turns «on» during the peak period if the device is managed by Éco Sinopé.
  - **eco_optout**: «off» during normal operation and during the peak period, turns «on» if somebody changes the setpoint during the peak period.
  - **eco_power_relative**: «off» during normal operation. Used to set a minimum temperature, relative to the setpoint, at which the thermostat turns on automatically for frost protection.
  - **eco_power_absolute**: «off» during normal operation. Used to limit the pi_heating_demand level between 1 and 100% during the peak period.
  - **eco_setpoint_status**: «off» during normal operation, turns «on» if the device setpoint is changed by Éco Sinopé.
  - **eco_setpoint_delta**: 0 during normal operation, changes to a value between -10 and +10 during the peak period. The value is positive for pre-heating and negative for the peak period. It is a delta applied to the regular setpoint: -10 = setpoint reduced by 10°C, +2 = setpoint increased by 2°C.

- For load controllers:
  - **eco_status**: «off» during normal operation, turns «on» at the beginning of the pre-heating period. This is the attribute to follow to detect a peak start.
  - **eco_onoff**: «off» during normal operation, turns «on» during the peak period if the device is managed by Éco Sinopé. The device is turned off during the peak period. Nothing is done during the pre-heating period.
  - **eco_optout**: «off» during normal operation and during the peak period, turns «on» if somebody turns the device on during the peak period.

- For the MC3100ZB multi-controller:
  - **eco_status**: «off» during normal operation, turns «on» at the beginning of the pre-heating period. This is the attribute to follow to detect a peak start.
  - **eco_setpoint**: «off» during normal operation, no change during the peak period if the device is managed by Éco Sinopé.
  - **eco_optout**: «off» during normal operation, turns «on» if somebody changes the on/off value during the peak period.
  - **eco_power_relative**: «off» during normal operation. Used to set a minimum temperature, relative to the room temperature, at which the MC3100ZB turns on automatically for frost protection.
  - **eco_power_absolute**: «off» during normal operation, usage unknown.

You can then build an automation that prepares your HA devices for the peak period by following the eco_status change from «off» to «on».

## Energy and water statistics
Devices that report energy in Neviweb get these sensor entities, in kWh:
- **Total Energy** (`total_kwh_count`, total_increasing)
- **Monthly**, **Daily** and **Hourly** energy (`monthly_kwh_count`, `daily_kwh_count`, `hourly_kwh_count`, total)

2nd gen Sedna valves with a flow sensor get the same set for water, in liters: **Total Flow** (`total_flow_count`, total_increasing) and the monthly, daily and hourly flow counts (total).

These sensors have the energy or water device class and can be added directly to the HA Energy dashboard. No template sensor is needed. Statistics are polled from Neviweb every `stat_interval` seconds (default 1800).

The `hourly_kwh`, `daily_kwh` and `monthly_kwh` attributes (kWh used during the last hour, day and month) are still exposed on climate, light and switch entities, and `hourly_flow`, `daily_flow` and `monthly_flow` on valve entities.

## Localisation
Neviweb130 is now translated in French for the errors and notifications messages. The translation is done automatically based
on your HA configuration for language. Now French and English are supported. Any language can be added by translating 
en.json file located in the translations folder into other language.

If you modify translations files you will need to not only reload HA but also restart the HA server to force HA to reload 
translations properly.

## Troubleshooting
If your device appears in the log but not in the entity list, its model number must be added to the code. Open an issue with the model number so it can be added.

In the log, look for these lines:
```yaml
[custom_components.neviweb130] Received gateway data: [{'id': 100225, 'identifier': '500b91400001f750', 'name': 'Chargeur auto', 'family': '2506',...
[custom_components.neviweb130] Received signature data: {'signature': {'model': 2506, 'modelCfg': 0, 'softBuildCfg': 0, 'softVersion': {'minor': 9, 'middle': 2, 'major': 1}, 'hardRev': 2, 'protocol': 'sinopcom'}}
```
'family': '2506' and 'model': 2506 give the model number of your device. Model lists are in `const.py` (CLIMATE_MODEL, LIGHT_MODEL, SWITCH_MODEL, VALVE_MODEL, SENSOR_MODEL).

If you get a stack trace related to a Neviweb130 component in `neviweb130_log.txt` or `home-assistant.log`, you can file an issue in this repository.

You can also ask for help in one of these threads:
- https://community.home-assistant.io/t/sinope-line-voltage-thermostats/17157
- https://community.home-assistant.io/t/adding-support-for-sinope-light-switch-and-dimmer/38835

### Turning on Neviweb130 debug messages

Neviweb130 writes its messages to its own file, `config/neviweb130_log.txt`, not to `home-assistant.log`. The `logger:` section of `configuration.yaml` has no effect on it.

To get debug messages:
- Open the neviweb130 integration page, click on Configure and set **log_level** to `debug`.
- Reproduce the problem, then use **download_log** in the same options to get the file from your browser, or read `config/neviweb130_log.txt` directly.
- Put the log level back to `warning` afterwards, as the debug log grows fast.

Please provide a snippet of this file when you ask for help.

### Error messages received from Neviweb
You can get these messages from Neviweb in the log:
- ACCDAYREQMAX: maximum daily requests reached (30000 per day). Reduce the polling frequency.
- ACCRATELIMIT: too many login attempts. Wait a few minutes before retrying.
- ACCSESSEXC: too many open sessions at the same time. This is common after several Home Assistant restarts or when Neviweb is also open elsewhere.
- DVCACTNSPTD: device action not supported. This action is not available for that device.
- DVCATTRNSPTD: device attribute not supported. The device firmware does not support some attributes. The device is put in safe mode automatically (see safe_mode). Wait for a firmware update in Neviweb, or open an issue so an exception can be added.
- DVCBUSY: Neviweb is performing an update and devices are not available. Try later.
- DVCCOMMTO: device communication timeout. The device did not respond in time, or you are polling it too often.
- DVCERR: the command or attribute was rejected by the device.
- DVCNOTSYNC: device not synchronized with Neviweb.
- DVCUNVLB: device unavailable. Neviweb cannot reach the device, mostly Wi-Fi devices.
- MAINTENANCE: Neviweb is temporarily unavailable for maintenance. Retry later.
- SVCERR: service unavailable. Try later.
- SVCINVREQ: invalid request sent to Neviweb. The service does not exist or the request is malformed.
- SVCUNAUTH: request rejected by the Neviweb server, the action is not authorized for this device.
- USRBADLOGIN: invalid Neviweb username or password.
- USRSESSEXP: user session expired. Reduce scan_interval.
- VALINVLD: invalid value sent to Neviweb.
- ReadTimeout: the request was sent but no answer came back from the device. Network problem.
- TimeoutError: request timeout. Retry later.

### Missing attributes not returned by Neviweb during update

During device update it is possible that some attribute are just dropped by Neviweb even if they are listed as attribute
for a device. During Neviweb130-V2 startup, a notification will be sent to list those missing attributes and there value
will be set to 'not supported'. Please refer to this list and report new missing attributes by opening an issue.

| Devices	| missing attributes |
| --- | --- |
| **TH1123ZB-G2** |	coldLoadPickup, heatLockoutTemp |
| **TH1124ZB-G2** |	coldLoadPickup, heatLockoutTemp |
| **TH6250WF** | backlight |

## Customization
Custom-ui is almost deprecated and hard to configure. So I've switch to modern lovelace card to ease the process 
and get better results.

Prerequisites:
- The icons are located in www folder in this repo. Copy them in config/www/neviweb130/. You need to create the
  neviweb130 under config/www. (called /local in HA)
- Install via HACS the lovelace card: card-mod, mushroom and for stack-in-card.
- Make sure you have at least neviweb130 v4.1.2

Neviweb130 will manage the icon to show depending on heat level for thermostats via the **icon_type** attribute. For
sensors, monitors and valve, battery icon are managed via **battery_icon** attributes based on battery level.
You can retrieve the icon name with template like this example:

Heat level: `{{ state_attr('climate.neviweb130_climate_th1124wf', 'icon_type') }}`

leak detection: `{{ state_attr('sensor.neviweb130_sensor_wl2010', 'icon_type') }}`

battery level: `{{ state_attr('sensor.neviweb130_sensor_wl2010', 'battery_icon') }}`

Those template point directly to /local/neviweb130/(icons)

Old style: (Many examples)

![icons](icon_view2.png)

New style based on Mushroom and Tile cards:

![icons](icon_view3.jpg) 

(Feel free to improve my icons and let me know.) 

Here the code for tile card, mushroom template card and mushroom climate card. Edit your dashboard and add the card. 
Then edit the code like this:

- tile card:
```
type: tile
grid_options:
  columns: 12
  rows: 1
entity: climate.neviweb130_climate_th1124wf
name:
  - type: text
    text: Cuisine
  - type: text
    text: Tile card
show_entity_picture: true
vertical: false
features_position: bottom
```
Mushroom template:
```
type: custom:mushroom-template-card
entity: climate.neviweb130_climate_th1124wf
features_position: bottom
primary: |
  Cave (
  {{ state_attr(entity, 'temperature') }}
  °C)
  Mushroom template card
secondary: |
  {{ states(entity) }} – ({{ state_attr(entity, 'hvac_action') }})
  Currently: {{ state_attr(entity, 'current_temperature') }} °C
picture: |
  {{ state_attr(entity, 'icon_type') }}
grid_options:
  columns: 12
  rows: 1
```
- Mushroom Climate:
```
type: custom:mushroom-climate-card
entity: climate.neviweb130_climate_th1124wf
name: th1124wf Mushroom Climate card
hvac_modes: []
fill_container: true
primary_info: name
secondary_info: state
grid_options:
  columns: 12
  rows: 1
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
You can group the card in a vertical stack card, stack-in-card.
Since the entity_picture is defined for all thermostats, valve, sensors you can add the devices directly in a vertical stack card.
Icon will be dynamically updated for heat level, battery level etc
```
type: vertical-stack
cards:
  - type: entities
    entities:
      - entity: climate.neviweb130_climate_th1124wf
      - entity: climate.neviweb130_climate_office
      - entity: climate.neviweb130_climate_kitchen
      .....
```

![icons](icon_view4.jpg) 

## Customization for leak sensor

Same as above. 
For leak detected icon it is the **icon_type** attribute.
For battery level it's the same as above with **battery_icon**.

Icons are available from [www](https://github.com/claudegel/sinope-130/tree/master/www) sub-directory. 
Copy them in config/www/neviweb130 in your HA.

## Customization for battery level for monitor and valve

Same as above with attribute **battery_icon**, **leak_icon** and **icon_type**.

### Device and weather icons

Neviweb130 sets the entity picture itself. Custom-UI and `customize.yaml` are no longer needed. The picture is shown only if the png file exists, otherwise the default icon is used. The current path is also exposed in the `icon_type` attribute.

Copy the icons in `config/www/neviweb130/` (served as `/local/neviweb130/`). File names used by the code:

| Device                   | Files                                                                                     |
|--------------------------|-------------------------------------------------------------------------------------------|
| Thermostats              | `heat-off.png`, `heat-0.png` to `heat-5.png`, `heat-auto-0.png` to `heat-auto-5.png`      |
| Floor thermostats        | `floor-off.png`, `floor-0.png` to `floor-5.png`, `floor-auto-0.png` to `floor-auto-5.png` |
| Leak sensors             | `drop.png`, `leak.png`                                                                    |
| Battery level            | `battery-unknown.png`, `battery-1.png` to `battery-5.png`                                 |
| Valves                   | `valve-open.png`, `valve-close.png`, `leak.png`                                           |
| Propane tank (LM4110-ZB) | `propane-unknown.png`, `propane-0.png` to `propane-8.png`                                 |

The thermostat level follows the heating demand: 0 below 1%, then one step every 20%. `-off` is used when the thermostat is off and `-auto-` when it is in auto mode.

#### Weather icons

The **weather icon** sensor of supported thermostats gives a weather code from Neviweb. Its picture is taken from `config/www/neviweb130/weather/<name>.png`. At startup, neviweb130 sends a notification if this folder is missing or empty. Code to file name (from `WEATHER_ICON_MAP` in `schema.py`):

| Code | File               | Code | File               | Code | File                |
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

File names are case sensitive.

## Device hard reset
- Thermostats:
    - Raise the temperature until the display changes.
    - Press both buttons until CLR appears on the screen.
    - Press the upper button once to get YES on the display.
    - Press both buttons at the same time and release immediately. DONE should appear on the screen.
    - The thermostat restarts with factory settings.

- G2 thermostats:
    - Raise the temperature until the display changes.
    - Press and hold both buttons until RST appears on the screen.
    - Wait until the device restarts.

## TO DO
- Improve energy stat polling from Neviweb.
