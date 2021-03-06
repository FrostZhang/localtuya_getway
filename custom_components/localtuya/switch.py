"""Platform to locally control Tuya-based switch devices."""
import logging
from functools import partial

import voluptuous as vol
from homeassistant.components.switch import DOMAIN, SwitchEntity
import homeassistant.helpers.config_validation as cv

from .common import LocalTuyaEntity, async_setup_entry
from .const import (
    ATTR_CURRENT,
    ATTR_CURRENT_CONSUMPTION,
    ATTR_VOLTAGE,
    CONF_CURRENT,
    CONF_CURRENT_CONSUMPTION,
    CONF_VOLTAGE,
    CONF_CID_STRING,
)

_LOGGER = logging.getLogger(__name__)


def flow_schema(dps):
    """Return schema used in config flow."""
    return {
        vol.Optional(CONF_CURRENT): vol.In(dps),
        vol.Optional(CONF_CURRENT_CONSUMPTION): vol.In(dps),
        vol.Optional(CONF_VOLTAGE): vol.In(dps),
        vol.Required(CONF_CID_STRING): cv.string,
    }


class LocaltuyaSwitch(LocalTuyaEntity, SwitchEntity):
    """Representation of a Tuya switch."""

    def __init__(
        self,
        device,
        config_entry,
        switchid,
        cid,
        **kwargs,
    ):
        """Initialize the Tuya switch."""
        super().__init__(device, config_entry, switchid, cid, _LOGGER, **kwargs)
        self._state = None
        print("Initialized switch [{}]".format(self.name))

    @property
    def is_on(self):
        """Check if Tuya switch is on."""
        return self._state

    @property
    def extra_state_attributes(self):
        """Return device state attributes."""
        attrs = {}
        if self.has_config(CONF_CURRENT):
           attrs[ATTR_CURRENT] = self.dps(self._config[CONF_CURRENT])
        if self.has_config(CONF_CURRENT_CONSUMPTION):
            res = self.dps(self._config[CONF_CURRENT_CONSUMPTION])
            if res != None:
                attrs[ATTR_CURRENT_CONSUMPTION] = res / 10
        if self.has_config(CONF_VOLTAGE):
            res = self.dps(self._config[CONF_VOLTAGE])
            if res != None:
                attrs[ATTR_VOLTAGE] = res / 10
        attrs[CONF_CID_STRING] = self._cid
        return attrs

    async def async_turn_on(self, **kwargs):
        """Turn Tuya switch on."""
        await self._device.set_dp(True, self._dp_id, self._cid)

    async def async_turn_off(self, **kwargs):
        """Turn Tuya switch off."""
        await self._device.set_dp(False, self._dp_id, self._cid)

    def status_updated(self):
        """Device status was updated."""
        state = self.dps(self._dp_id)
        if state != None:
            self._state = state


async_setup_entry = partial(async_setup_entry, DOMAIN, LocaltuyaSwitch, flow_schema)
