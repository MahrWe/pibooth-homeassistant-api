# -*- coding: utf-8 -*-

"""pibooth plugin for interacting with homeassistant api"""

import os
import hassapi import Hass

import pibooth
from pibooth.utils import LOGGER


__version__ = "0.1.0"

SECTION = "Homeassistant"


@pibooth.hookimpl
def pibooth_configure(cfg):
    """Declare the new configuration options"""
    cfg.add_option(SECTION, "hass_url", "http://localhost:8123", "Homeassistant url")
    cfg.add_option(SECTION, "hass_token", "", "Homeassistant token")
    cfg.add_option(SECTION, "light_entity", "", "light entity to be toggled")


@pibooth.hookimpl
def pibooth_startup(app, cfg):
    """initialize the endpoint connection"""
    hass_url = cfg.get(SECTION, "hass_url")
    hass_token = cfg.get(SECTION, "hass_token")

     if not hass_token:
        LOGGER.error(
            "Homeassistant Token not defined in ["
            + SECTION
            + "][hass_token], uploading deactivated"
        )
    else:
        LOGGER.info("Initializing homeassistant api")
        app.hass = Hass(hassurl=hass_url, token=hass_token, verify=False)

@pibooth.hookimpl
def state_preview_enter(app, cfg):
    """Turn light on when preview starts"""
    if hasattr(app, "hass"):
        entity = cfg.get(SECTION, "light_entity")
        try:
            hass.turn_on(entity)
            LOGGER.info("Turned on: " + str(entity))
        except:
            LOGGER.error("Something went wrong")

@pibooth.hookimpl
def state_capture_exit(app, cfg):
    """Turn light off when done"""
    if hasattr(app, "hass"):
        entity = cfg.get(SECTION, "light_entity")
        try:
            hass.turn_off(entity)
            LOGGER.info("Turned off: " + str(entity))
        except:
            LOGGER.error("Something went wrong")
