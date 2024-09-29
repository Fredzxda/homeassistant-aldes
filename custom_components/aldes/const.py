"""Constants for aldes."""
from homeassistant.const import Platform

NAME = "Aldes"
DOMAIN = "aldes"
VERSION = "0.0.1"

CONF_USERNAME = "username"
CONF_PASSWORD = "password"

MANUFACTURER = "Aldes"
PLATFORMS: list[Platform] = [
    Platform.BINARY_SENSOR,
    Platform.SENSOR,
    Platform.CLIMATE,
    Platform.SELECT,
]

FRIENDLY_NAMES = {
    "TONE_AIR": "T.One® AIR",
    "EASY_HOME_CONNECT": "EASYHOME PureAir Compact CONNECT",
    "EASY_HOME_PREMIUM": "EASYHOME PureAir Compact PREMIUM",
}

TEXT_MODES = {
    "Holidays": "W",
    "Daily": "V",
    "Boost": "Y",
    "Guest": "X",
    "Air Prog": "Z",
}
MODES_TEXT = {
    "W": "Holidays",
    "V": "Daily",
    "Y": "Boost",
    "X": "Guest",
    "Z": "Air Prog",
}
POLLUANTS = {
    "hr": "Humidity",
    "co2": "CO2",
}
