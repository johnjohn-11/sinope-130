## Home Assistant Neviweb130 Custom Components
[🇫🇷 Version française](doc/readme_fr.md)
> 💛 **Enjoying this integration?**  
> If you'd like to support its ongoing development, you can contribute here:
> [![Support via PayPal](https://cdn.rawgit.com/twolfson/paypal-github-button/1.0.0/dist/button.svg)](https://www.paypal.me/phytoressources/) or 
> [![Donate via Interac](https://img.shields.io/badge/Interac-Don-orange?style=for-the-badge)](doc/Donations.md)

Custom integration to support [Neviweb](https://neviweb.com/) devices in [Home Assistant](http://www.home-assistant.io) (HA).
Neviweb is the Sinopé Technologies platform for their smart devices: thermostats, light switches and dimmers, load controllers, plugs, valves, water leak detectors and more.

Neviweb130 (Sinope Neviweb130 in HACS) manages the Zigbee devices connected to Neviweb through the GT130 gateway, and the Wi-Fi devices connected directly to Neviweb. It is almost up to date with Neviweb, but some information is still missing from Sinopé. New Sinopé devices are added as they are launched. If you have a device that is not supported yet, please open an issue and it will be added quickly.

Report a problem or suggest an improvement: [Open an issue](https://github.com/claudegel/sinope-130/issues/new/choose)

## Table of contents

- [Supported devices](#supported-devices)
- [Prerequisite](#prerequisite)
- [Installation](#installation)
- [Configuration](#configuration)
- [Migrating from version 4.x](#migrating-from-version-4x)
- [Sedna valve](#sedna-valve)
- [GT130](#gateway-gt130)
- [Update system](#updater-system)
- [Request counter](#neviweb-daily-request-counter)
- [Services / Actions](#custom-services)
- [Eco-Sinopé](#catch-éco-sinopé-signal-for-peak-period)
- [Energy and water statistics](#energy-and-water-statistics)
- [Localisation (language)](#localisation)
- [Troubleshooting](#troubleshooting)
- [Customization](#customization)
- [Device hard reset](#device-hard-reset)
- [TO DO](#to-do)

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
Your devices must be added to your Neviweb portal before they can be used in Home Assistant:
- Zigbee devices through a GT130 gateway,
- Wi-Fi devices directly,
- some Zigbee devices through a Sedna valve, which is itself connected to Neviweb.

Please refer to the instruction manual of your device or visit [Neviweb support](https://support.sinopetech.com/).

Wi-Fi devices can be in the same Neviweb location (network) as the GT130 Zigbee devices or in a separate one. Neviweb130 supports up to three locations per Neviweb account.

Four custom components let you manage Sinopé devices, through Neviweb or locally:
- [**neviweb**](https://github.com/claudegel/sinope-1) (HACS: Sinope Neviweb), for MiWi devices through the Neviweb portal.
- [**sinope**](https://github.com/claudegel/sinope-gt125) (HACS: Sinope GT125), for devices managed directly through your GT125 gateway.
- [**neviweb130**](https://github.com/claudegel/sinope-130) (HACS: Sinope Neviweb130), this integration, for Zigbee and Wi-Fi devices through the Neviweb portal.
- [**sinope-zha**](https://github.com/claudegel/sinope-zha), new Sinopé quirks for ZHA before they are merged into zha-device-handlers. With a Zigbee coordinator such as the ConBee II USB dongle, ZHA manages your Zigbee devices locally. Copy the sinope-zha files into your HA setup to test new quirks: ZHA loads them in place of the standard Sinopé quirks.

They can all be used at the same time. Zigbee devices managed directly through ZHA must be removed from Neviweb, as a device cannot be on two Zigbee networks at the same time.

## Installation
There are two ways to install this custom component:
- With HACS:
  - This repository is compatible with the Home Assistant Community Store ([HACS](https://community.home-assistant.io/t/custom-component-hacs/121727)).
  - After installing HACS, install 'Sinope Neviweb130' from the store, restart Home Assistant and add the integration (see Configuration).
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

## Configuration

Neviweb130 is configured from the Home Assistant UI. Configuration in `configuration.yaml` is obsolete. If you are upgrading from version 4.x, see [Migrating from version 4.x](#migrating-from-version-4x).

### Adding a Neviweb account

Go to Settings → Devices & services. At the bottom of the page, click **Add integration** and search for **Sinope Neviweb130**. A window opens to enter your Neviweb connection settings.

![new configuration](www/nouveau_pont.jpg)

Then Neviweb130 loads and starts retrieving your Neviweb devices.

To control another Neviweb account, add the integration again with a different **prefix**.

### Parameters

Location names are the names shown at the top of the first page after logging into Neviweb. If you have more than one location, click on the icon at the top to see all of them. Zigbee (GT130) and Wi-Fi devices of a same group must be in the same location. MiWi devices (GT125) are not supported. For them, install the [Neviweb](https://github.com/claudegel/sinope-1) custom component, which can run alongside this one.

![network](www/network.jpg)

| key               | required | default                                | description                                                                                                                                                                       |
|-------------------|----------|----------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **prefix**        | no       | default                                | Name of the Neviweb account. Needed only if you add more than one Neviweb account. Each account needs a different prefix, without spaces or accented characters.                |
| **username**      | yes      |                                        | The email address you use to log into Neviweb.                                                                                                                                    |
| **password**      | yes      |                                        | Your Neviweb password.                                                                                                                                                            |
| **network**       | no       | 1st location found                     | Name of the Neviweb location where your Zigbee or Wi-Fi devices are registered. Leave empty for auto detection, or set to `_` to block detection.                               |
| **network2**      | no       | 2nd location found                     | Name of the second location to control. Leave empty if you have only one location.                                                                                               |
| **network3**      | no       | 3rd location found                     | Name of the third location to control. Leave empty if you have only one or two locations.                                                                                        |
| **scan_interval** | no       | 420                                    | Number of seconds between each Neviweb poll to update device states, from 300 to 600. Sinopé asks for a minimum of 5 minutes between polls. Above 600 the session expires.      |
| **homekit_mode**  | no       | False                                  | Adds support for HomeKit specific values. Not needed if you don't use HomeKit.                                                                                                   |
| **ignore_miwi**   | no       | False                                  | Set to True if a selected location also contains MiWi devices (GT125). Without it, you get a warning saying the location contains unsupported MiWi devices.                     |
| **stat_interval** | no       | 1800                                   | Number of seconds between each Neviweb poll for energy statistics, from 300 to 1800.                                                                                             |
| **notify**        | no       | both                                   | How device errors are reported: `nothing`, `logging`, `notification` or `both`.                                                                                                  |
| **safe_mode**     | no       | -                                      | Comma separated list of device IDs to poll in safe mode, or `-` for none. In safe mode, attributes not supported by the device firmware are skipped. A device that returns `DVCATTRNSPTD` is added automatically and you get a notification. |

If you also have a GT125 connected to Neviweb, enter the location name, otherwise the GT125 location could be picked up by mistake. Unused locations can be left empty, or set to `_` so Neviweb130 does not search for them. A third location must be activated by Sinopé. If you enter names, write them exactly as in Neviweb, including capitalization. Accented letters are refused.

### Managing the integration

Everything is under Settings → Devices & services → Neviweb130:

![options](www/options.jpg)

From there you can:
- add another Neviweb account,
- change the integration options with **Configure** (see below),
- change the account parameters with **Reconfigure**.

Changes apply without restarting Home Assistant: Neviweb130 reloads itself. A session manager closes and reopens the Neviweb connections as needed, which avoids the ACCSESSEXC errors seen when Home Assistant restarts often.

*Available configuration options*:

![configuration options](www/configuration.jpg)

*Reconfiguration*:

![reconfiguration](www/reconfigurer.jpg)

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

### Attribute entities

Each device has its own page under Settings → Devices & services → Neviweb130, and Neviweb130 creates an entity for most device attributes:
- sensor, for numeric values such as temperature, voltage and energy statistics,
- binary_sensor, for on/off states such as leak sensors,
- button, to reset an on/off or alarm attribute,
- number, to change a numeric value (minimum/maximum temperature, away temperature, etc.),
- switch, to enable or disable an attribute,
- select, for attributes with a list of choices. Choices are translated and converted to and from Neviweb values automatically.

These entities update with the device and can be used directly in automations and in the Energy dashboard, so template sensors on attributes are no longer needed. Entities, services and attributes are translated in English or French according to your Home Assistant language. If an attribute entity is missing, open an issue.

Sample device page:

![Page appareil](www/page_appareil.jpg)
![Page appareil suite](www/page_appareil_suite.jpg)

## Migrating from version 4.x

At the first startup of version 5, Neviweb130:
- imports the `neviweb130:` configuration from `configuration.yaml` into the UI configuration,
- converts `unique_id`s to text (int to str),
- converts device model numbers to text (int to str).

These changes are required by Home Assistant and are done automatically. Device names are kept and attributes are still available.

After the first startup:
- remove or comment out the `neviweb130:` block in `configuration.yaml`,
- check your automations, scripts and dashboards. They keep working, but the new attribute entities can replace your template sensors,
- device icons are provided by the integration through the `icon_type` attribute and the entity picture (see [Customization](#customization)), so Custom-UI is no longer needed.

<details>
<summary>Legacy configuration.yaml reference (version 4.x)</summary>

#### Single account

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

#### Multi-account configuration
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

#### Running more than one instance of neviweb130 to manage different Neviweb connections
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

</details>

## Sedna valve
There are two ways to connect a Sedna valve to Neviweb:
- Wi-Fi direct connection. Leak sensors are connected directly to the Sedna valve, which closes when a leak is detected.
- Through the GT130 in Zigbee mode. Leak sensors are also connected to the GT130, but a leak detection is not passed to the valve. You need an automation in Neviweb or HA to close the Sedna valve when a sensor detects a leak.

Both modes are supported by this custom component.

## Gateway GT130
The `gateway_status` binary sensor of the GT130 tells you whether the gateway is online or offline in Neviweb.

## Updater system

Neviweb130 includes its own update entity:
- **Update check**, every 6 hours by default (update_check_interval option). It detects new versions, pre-releases (versions containing b0, -beta, rc1, etc.) and breaking changes found in the release notes. Pre-releases and breaking changes get a special icon and a label in the update card title.
- **SHA-256 validation**: the update zip file is checked against the official SHA-256 from GitHub. On a mismatch, the update is cancelled and you are notified.
- **Automatic rollback**: if an error occurs during the update, the previous version is restored and you are notified.
- **Backup**: a backup is made before the update, set by the backup_mode and backup_folders options (see [Integration options](#integration-options)).
- **Notifications** on success ("Update successful"), failure ("Update fail, rollback performed") and SHA-256 error ("Update aborted for security").
- **Release notes**: a link on the update card opens the GitHub release notes.

The update entity also has these attributes:
- check_interval: value of the update_check_interval option (default 6h),
- last_check and next_check: date and time of the last and next version check,
- last_update_success: date and time of the last successful update,
- update_status: steps performed during the update,
- rollback_status: result of the rollback if an update failed,
- update_percentage: progress of the update.

To avoid two update cards (one from HACS, one from Neviweb130), hide the HACS one:
1. Go to Settings → Devices & services → HACS.
2. On the Sinope Neviweb130 line, turn off the pre-release switch if it is on.
3. Click the three-dot menu at the end of the line, then **2 entities**.
4. Select the update entity, click the settings button and turn off **Visible**.

You can still update or redownload Neviweb130 manually through HACS. You can also do step 4 from the HACS update card the next time one appears.

## Neviweb daily request counter
Neviweb limits each account to 30000 requests per day. Above that limit, you are disconnected until midnight, which is a problem with many devices or during development.

Neviweb130 counts its daily requests (updates, statistics, error checks, etc.) in the `sensor.neviweb130_daily_requests` sensor. The count survives HA restarts and is reset to 0 at midnight. It helps you choose a shorter scan_interval without going over the limit. A notification is sent when the count goes over the request_limit option (default 25000).

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
Neviweb130 is translated in English and French: entities, services, attributes, errors and notifications. The language follows your Home Assistant language. Other languages can be added by translating the `en.json` file in the translations folder.

After changing translation files, restart Home Assistant. Reloading the integration is not enough for HA to load the new translations.

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

### Log file
Neviweb130 writes all its log messages to its own file, `neviweb130_log.txt`, in your config directory, not to `home-assistant.log`. By default the file is cleared each time the integration starts (log_reset_on_start), rotated when it reaches 2 MB (log_max_bytes) and 2 rotated files are kept (log_backup_count). These settings and the log level are in the integration options.

To help debugging, add relevant snippet of this file to any issue you may report.

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

Neviweb sometimes drops attributes during an update, even if they are listed for the device. A notification lists those missing attributes and their value is set to `[not supported]`. Known cases are listed below. Please open an issue to report new ones.

| Device          | Missing attributes              |
|-----------------|---------------------------------|
| **TH1123ZB-G2** | coldLoadPickup, heatLockoutTemp |
| **TH1124ZB-G2** | coldLoadPickup, heatLockoutTemp |
| **TH6250WF**    | backlight                       |

## Customization
Custom-UI is no longer needed. Neviweb130 sets the entity picture of thermostats, sensors and valves itself, and the examples below use modern Lovelace cards.

Prerequisites:
- Copy the icons into `config/www/neviweb130/` (served as `/local/neviweb130/` in HA). See [Device and weather icons](#device-and-weather-icons) for the file names.
- For the Mushroom examples, install these cards with HACS: card-mod, Mushroom and stack-in-card.

Neviweb130 exposes the icon path in these attributes:
- **icon_type**: heat level for thermostats, leak status for leak sensors, valve state for valves,
- **battery_icon**: battery level for sensors, monitors and valves,
- **leak_icon**: leak status for valves.

You can read them with a template, for example:

Heat level: `{{ state_attr('climate.neviweb130_climate_th1124wf', 'icon_type') }}`

Leak detection: `{{ state_attr('sensor.neviweb130_sensor_wl2010', 'icon_type') }}`

Battery level: `{{ state_attr('sensor.neviweb130_sensor_wl2010', 'battery_icon') }}`

These templates return a path in `/local/neviweb130/`.

Old style (many examples):

![icons](icon_view2.png)

New style based on Mushroom and Tile cards:

![icons](icon_view3.jpg)

(Feel free to improve the icons and share them.)

Here is the code for a Tile card, a Mushroom template card and a Mushroom climate card. Edit your dashboard, add the card, then edit its code like this:

- Tile card:
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
- Mushroom template card:
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
- Mushroom climate card:
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
You can group the cards in a vertical stack card or a stack-in-card.
Since the entity picture is set for all thermostats, valves and sensors, you can also add the devices directly in a vertical stack card.
Icons update automatically with the heat level, battery level, etc.
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

## Customization for leak sensors, monitors and valves

Same as above:
- leak status: **icon_type** for leak sensors, **leak_icon** for valves,
- battery level: **battery_icon**,
- valve state: **icon_type** for valves.

## Device and weather icons

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

### Weather icons

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
