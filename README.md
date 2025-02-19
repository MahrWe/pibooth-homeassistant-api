pibooth-homeassistant-api
=================

[![Python 3.6+](https://img.shields.io/badge/python-3.6+-red.svg)](https://www.python.org/downloads)
[![PyPi package](https://badge.fury.io/py/pibooth-homeassistant-api.svg)](https://pypi.org/project/pibooth-homeassistant-api)
[![PyPi downloads](https://img.shields.io/pypi/dm/pibooth-homeassistant-api?color=purple)](https://pypi.org/project/pibooth-homeassistant-api)

`pibooth-homeassistant-api` is a plugin for the [pibooth](https://pypi.org/project/pibooth) application.

Install
-------

    $ pip3 install pibooth-homeassistant-api

Configuration
-------------

Below are the new configuration options available in the [pibooth](https://pypi.org/project/pibooth) configuration. **The keys and their default values are automatically added to your configuration after first** [pibooth](https://pypi.org/project/pibooth) **restart.**

``` {.ini}
[Homeassistant]

# Homeassistant URL (inkl. Port)
hass_url =

# Long-lived token
hass_token =

# Entity to toggle on and off
light_entity =

```

### Note

Edit the configuration by running the command `pibooth --config`.
