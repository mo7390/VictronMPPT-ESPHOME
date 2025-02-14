import esphome.codegen as cg
import esphome.config_validation as cv
from esphome.components import sensor
from esphome.const import (
    CONF_BATTERY_VOLTAGE,
    DEVICE_CLASS_CURRENT,
    DEVICE_CLASS_EMPTY,
    DEVICE_CLASS_POWER,
    DEVICE_CLASS_VOLTAGE,
    ICON_CURRENT_AC,
    ICON_EMPTY,
    ICON_FLASH,
    ICON_POWER,
    UNIT_AMPERE,
    UNIT_EMPTY,
    UNIT_VOLT,
    UNIT_WATT,
    UNIT_WATT_HOURS,
)

from . import CONF_VICTRON_ID, VictronComponent

DEPENDENCIES = ["victron"]

CODEOWNERS = ["@KinDR007"]

CONF_MAX_POWER_YESTERDAY = "max_power_yesterday"
CONF_MAX_POWER_TODAY = "max_power_today"
CONF_YIELD_TOTAL = "yield_total"
CONF_YIELD_YESTERDAY = "yield_yesterday"
CONF_YIELD_TODAY = "yield_today"
CONF_PANEL_VOLTAGE = "panel_voltage"
CONF_PANEL_POWER = "panel_power"
CONF_BATTERY_CURRENT = "battery_current"
CONF_DAY_NUMBER = "day_number"
CONF_CHARGING_MODE_ID = "charging_mode_id"
CONF_ERROR_CODE = "error_code"
CONF_WARNING_CODE = "warning_code"
CONF_TRACKING_MODE_ID = "tracking_mode_id"
CONF_DEVICE_MODE_ID = "device_mode_id"
CONF_LOAD_CURRENT = "load_current"
CONF_AC_OUT_VOLTAGE = "ac_out_voltage"
CONF_AC_OUT_CURRENT = "ac_out_current"

SENSORS = [
    CONF_BATTERY_VOLTAGE,
    CONF_AC_OUT_VOLTAGE,
    CONF_MAX_POWER_YESTERDAY,
    CONF_MAX_POWER_TODAY,
    CONF_YIELD_TOTAL,
    CONF_YIELD_YESTERDAY,
    CONF_YIELD_TODAY,
    CONF_PANEL_VOLTAGE,
    CONF_PANEL_POWER,
    CONF_BATTERY_CURRENT,
    CONF_AC_OUT_CURRENT,
    CONF_DAY_NUMBER,
    CONF_CHARGING_MODE_ID,
    CONF_ERROR_CODE,
    CONF_WARNING_CODE,
    CONF_TRACKING_MODE_ID,
    CONF_DEVICE_MODE_ID,
    CONF_LOAD_CURRENT,
]


CONFIG_SCHEMA = cv.Schema(
    {
        cv.GenerateID(CONF_VICTRON_ID): cv.use_id(VictronComponent),
        cv.Optional(CONF_MAX_POWER_YESTERDAY): sensor.sensor_schema(
            UNIT_WATT, ICON_POWER, 0, DEVICE_CLASS_POWER
        ),
        cv.Optional(CONF_MAX_POWER_TODAY): sensor.sensor_schema(
            UNIT_WATT, ICON_POWER, 0, DEVICE_CLASS_POWER
        ),
        cv.Optional(CONF_YIELD_TOTAL): sensor.sensor_schema(
            UNIT_WATT_HOURS, ICON_POWER, 0, DEVICE_CLASS_POWER
        ),
        cv.Optional(CONF_YIELD_YESTERDAY): sensor.sensor_schema(
            UNIT_WATT_HOURS, ICON_POWER, 0, DEVICE_CLASS_POWER
        ),
        cv.Optional(CONF_YIELD_TODAY): sensor.sensor_schema(
            UNIT_WATT_HOURS, ICON_POWER, 0, DEVICE_CLASS_POWER
        ),
        cv.Optional(CONF_PANEL_VOLTAGE): sensor.sensor_schema(
            UNIT_VOLT, ICON_FLASH, 3, DEVICE_CLASS_VOLTAGE
        ),
        cv.Optional(CONF_PANEL_POWER): sensor.sensor_schema(
            UNIT_WATT, ICON_POWER, 0, DEVICE_CLASS_POWER
        ),
        cv.Optional(CONF_BATTERY_VOLTAGE): sensor.sensor_schema(
            UNIT_VOLT, ICON_FLASH, 3, DEVICE_CLASS_VOLTAGE
        ),
        cv.Optional(CONF_AC_OUT_VOLTAGE): sensor.sensor_schema(
            UNIT_VOLT, ICON_FLASH, 3, DEVICE_CLASS_VOLTAGE
        ),
        cv.Optional(CONF_BATTERY_CURRENT): sensor.sensor_schema(
            UNIT_AMPERE, ICON_CURRENT_AC, 3, DEVICE_CLASS_CURRENT
        ),
        cv.Optional(CONF_AC_OUT_CURRENT): sensor.sensor_schema(
            UNIT_AMPERE, ICON_CURRENT_AC, 3, DEVICE_CLASS_CURRENT
        ),
        cv.Optional(CONF_DAY_NUMBER): sensor.sensor_schema(
            UNIT_EMPTY, ICON_EMPTY, 0, DEVICE_CLASS_EMPTY
        ),
        cv.Optional(CONF_CHARGING_MODE_ID): sensor.sensor_schema(
            UNIT_EMPTY, ICON_EMPTY, 0, DEVICE_CLASS_EMPTY
        ),
        cv.Optional(CONF_ERROR_CODE): sensor.sensor_schema(
            UNIT_EMPTY, ICON_EMPTY, 0, DEVICE_CLASS_EMPTY
        ),
        cv.Optional(CONF_WARNING_CODE): sensor.sensor_schema(
            UNIT_EMPTY, ICON_EMPTY, 0, DEVICE_CLASS_EMPTY
        ),
        cv.Optional(CONF_TRACKING_MODE_ID): sensor.sensor_schema(
            UNIT_EMPTY, ICON_EMPTY, 0, DEVICE_CLASS_EMPTY
        ),
        cv.Optional(CONF_DEVICE_MODE_ID): sensor.sensor_schema(
            UNIT_EMPTY, ICON_EMPTY, 0, DEVICE_CLASS_EMPTY
        ),
        cv.Optional(CONF_LOAD_CURRENT): sensor.sensor_schema(
            UNIT_AMPERE, ICON_CURRENT_AC, 3, DEVICE_CLASS_CURRENT
        ),
    }
)


def to_code(config):
    hub = yield cg.get_variable(config[CONF_VICTRON_ID])
    for key in SENSORS:
        if key in config:
            conf = config[key]
            sens = yield sensor.new_sensor(conf)
            cg.add(getattr(hub, f"set_{key}_sensor")(sens))
