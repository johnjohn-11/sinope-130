# Neviweb130 Integration Options

This page describes the options reached with **Configure** on the Neviweb130 integration page.

---

## 🔧 Available parameters

### **Account prefix (prefix)**
Name of the Neviweb account. Used to distinguish several Neviweb accounts in Home Assistant. No spaces, ASCII characters only, and each account needs its own prefix.

### **Log level (log_level)**
Level of the neviweb130 log file `config/neviweb130_log.txt`:
- debug
- info
- warning (default)
- error
- critical

Neviweb130 does not write to `home-assistant.log`. The `logger:` section of `configuration.yaml` has no effect on this file.

### **Maximum log size (log_max_bytes)**
Maximum size of the log file before rotation.

### **Backup count (log_backup_count)**
Number of rotated log files to keep.

### **Reset log on startup (log_reset_on_start)**
Clears the log file when the integration starts.

### **Download log (download_log)**
Copies the log file to `/local/neviweb130.log` so you can download it from your browser. A notification gives the link. The copy is deleted after 30 minutes.

### **Reload integration (reload)**
Reloads the integration without restarting Home Assistant.

### **Migrate numeric unique_id (migrate)**
Converts old numeric unique_id to the text unique_id required by Home Assistant.

### **Request safety limit (request_limit)**
Daily number of requests to Neviweb before a notification is sent (default 25000). Neviweb's own limit is 30000 requests per day. The current count is shown by the request counter sensor.

### **Update check interval (update_check_interval)**
How often the update entity checks GitHub for a new neviweb130 release: 1h, 3h, 6h (default), 12h or 24h.

### **Backup mode (backup_mode)**
Backup made by the update entity before installing a new version:
- **full**: full Home Assistant backup (`hassio.backup_full`)
- **partial**: partial backup (`hassio.backup_partial`) of the folders in backup_folders

Both need a Home Assistant installation with the Supervisor.

### **Backup folders (backup_folders)**
Folders included in a partial backup (default `config`, which means the Home Assistant configuration).

---

## 🔑 Fields set when adding or reconfiguring the integration

### **ignore_miwi**
Set to True if a selected Neviweb location also contains MiWi devices (GT125). Without it, you get a warning telling you the location contains unsupported MiWi devices.

### **safe_mode**
Comma separated list of device IDs to poll in safe mode, or `-` for none. In safe mode, attributes not supported by the device firmware are skipped. A device that returns `DVCATTRNSPTD` is added automatically and you get a notification.

---

## 📘 See also
- [Documentation index](doc_index_en.md)
