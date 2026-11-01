import asyncio
import json
import logging
import os
from typing import Any

_LOGGER = logging.getLogger(__name__)


def _load_devices(conf_file: str) -> dict[Any, Any]:
    device_dict: dict[Any, Any] = {}

    if not os.path.exists(conf_file):
        # File does not exist, create an empty file
        open(conf_file, "w", encoding="utf-8").close()
        return device_dict

    with open(conf_file, encoding="utf-8") as f:
        for line in f:
            device = json.loads(line)
            device_dict[device[0]] = device

    return device_dict


async def load_devices(conf_dir: str) -> dict[Any, Any]:
    conf_file = os.path.join(conf_dir, "neviweb130.json")
    device_dict = await asyncio.to_thread(_load_devices, conf_file)
    _LOGGER.debug("Loading device: %s", device_dict)
    return device_dict


def _save_devices(conf_file: str, data) -> None:
    with open(conf_file, "w", encoding="utf-8") as f:
        for device in data.values():
            try:
                f.write(json.dumps(device) + "\n")
            except Exception as e:
                _LOGGER.error("Failed to write device data %s: %s", device, e)


async def save_devices(conf_dir: str, data):
    """Saving devices energy data to file neviweb130.json"""
    conf_file = os.path.join(conf_dir, "neviweb130.json")
    try:
        _LOGGER.info("Saving energy stat data %s to CONF_FILE %s", data, conf_file)
        await asyncio.to_thread(_save_devices, conf_file, data)
    except Exception as e:
        _LOGGER.error("Failed to open or write to file %s: %s", conf_file, e)
