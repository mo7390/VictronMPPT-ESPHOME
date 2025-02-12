import esphome.codegen as cg
import esphome.config_validation as cv
from esphome.components import text_sensor
from esphome.const import CONF_ID

from . import CONF_VICTRON_ID, VictronComponent

DEPENDENCIES = ["victron"]

CODEOWNERS = ["@KinDR007"]

CONF_CHARGING_MODE = "charging_mode"
CONF_ERROR = "error"
CONF_WARNING = "warning"
CONF_TRACKING_MODE = "tracking_mode"
CONF_DEVICE_MODE = "device_mode"
CONF_FIRMWARE_VERSION = "firmware_version"
CONF_DEVICE_TYPE = "device_type"

TEXT_SENSORS = [
    CONF_CHARGING_MODE,
    CONF_ERROR,
    CONF_WARNING,
    CONF_TRACKING_MODE,
    CONF_DEVICE_MODE,
    CONF_FIRMWARE_VERSION,
    CONF_DEVICE_TYPE,
]


CONFIG_SCHEMA = cv.Schema(
    {
        cv.GenerateID(CONF_VICTRON_ID): cv.use_id(VictronComponent),
        cv.Optional(CONF_CHARGING_MODE): text_sensor.TEXT_SENSOR_SCHEMA.extend(
            {cv.GenerateID(): cv.declare_id(text_sensor.TextSensor)}
        ),
        cv.Optional(CONF_ERROR): text_sensor.TEXT_SENSOR_SCHEMA.extend(
            {cv.GenerateID(): cv.declare_id(text_sensor.TextSensor)}
        ),
        cv.Optional(CONF_WARNING): text_sensor.TEXT_SENSOR_SCHEMA.extend(
            {cv.GenerateID(): cv.declare_id(text_sensor.TextSensor)}
        ),
        cv.Optional(CONF_TRACKING_MODE): text_sensor.TEXT_SENSOR_SCHEMA.extend(
            {cv.GenerateID(): cv.declare_id(text_sensor.TextSensor)}
        ),
        cv.Optional(CONF_DEVICE_MODE): text_sensor.TEXT_SENSOR_SCHEMA.extend(
            {cv.GenerateID(): cv.declare_id(text_sensor.TextSensor)}
        ),
        cv.Optional(CONF_FIRMWARE_VERSION): text_sensor.TEXT_SENSOR_SCHEMA.extend(
            {cv.GenerateID(): cv.declare_id(text_sensor.TextSensor)}
        ),
        cv.Optional(CONF_DEVICE_TYPE): text_sensor.TEXT_SENSOR_SCHEMA.extend(
            {cv.GenerateID(): cv.declare_id(text_sensor.TextSensor)}
        ),
    }
)


def to_code(config):
    hub = yield cg.get_variable(config[CONF_VICTRON_ID])
    for key in TEXT_SENSORS:
        if key in config:
            conf = config[key]
            sens = cg.new_Pvariable(conf[CONF_ID])
            yield text_sensor.register_text_sensor(sens, conf)
            cg.add(getattr(hub, f"set_{key}_text_sensor")(sens))
