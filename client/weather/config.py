import RPi.GPIO as GPIO  #@UnresolvedImport


import K


class InvalidConfigException(Exception):

  def __init__(self, message):
    self._message = message

  def __str__(self):
    return 'Invalid config: %s' % self._message


class Config:

  _PUD_MAP = {'up': GPIO.PUD_UP,
              'down': GPIO.PUD_DOWN}

  def __init__(self):
    self._cfg = {}
    self._readFile();

  def _readFile(self):
    for line in open(K.CONFIG_FILENAME, 'r'):
      entry = [x.strip() for x in line.split('=', 1)]
      if len(entry) != 2 or not entry[0]:
        raise RuntimeError('invalid config file entry: %s' % line)
      self._cfg[entry[0]] = entry[1]

  def DEMO_MODE_ENABLED(self):
    return int(self._cfg['demo_mode_enabled']) != 0

  def UPLOAD_INTERVAL_SECONDS(self):
    return int(self._cfg['upload_interval_seconds'])
  def UPLOAD_MAX_SIZE_KB(self):
    return int(self._cfg['upload_max_size_kb'])

  def TEMPERATURE_SHUTDOWN_AT(self):
    return float(self._cfg['temperature_shutdown_at'])

  def TIMEOUT_SHUTDOWN_SECONDS(self):
    return int(self._cfg['timeout_shutdown_seconds'])
  def TIMEOUT_HTTP_REQUEST_SECONDS(self):
    return int(self._cfg['timeout_http_request_seconds'])

  def WIND_ENABLED(self):
    return int(self._cfg['wind_enabled']) != 0
  def WIND_DEBOUNCE_MILLIS(self):
    return int(self._cfg['wind_debounce_millis'])
  def WIND_INPUT_PIN(self):
    return int(self._cfg['wind_input_pin'])
  def WIND_PUD(self):
    return Config._PUD_MAP[self._cfg['wind_pud'].lower()]
  def WIND_EDGES_PER_REV(self):
    return int(self._cfg['wind_edges_per_revolution'])
  def WIND_HSF(self):
    return float(self._cfg['wind_high_speed_factor'])
  def WIND_LSF(self):
    return float(self._cfg['wind_low_speed_factor'])
  def WIND_MAX_ROTATION(self):
    return int(float(self._cfg['wind_max_rotation_seconds']) * 1000)
  def WIND_DIAMETER_MM(self):
    return float(self._cfg['wind_diameter_mm'])
  
  def RAIN_ENABLED(self):
    return int(self._cfg['rain_enabled']) != 0
  def RAIN_DEBOUNCE_MILLIS(self):
    return int(self._cfg['rain_debounce_millis'])
  def RAIN_INPUT_PIN(self):
    return int(self._cfg['rain_input_pin'])
  def RAIN_SIZE_LONG_MM(self):
    return float(self._cfg['rain_size_long_mm'])
  def RAIN_SIZE_WIDE_MM(self):
    return float(self._cfg['rain_size_wide_mm'])
  def RAIN_PUD(self):
    return Config._PUD_MAP[self._cfg['rain_pud'].lower()]
  def RAIN_DROPS(self):
    return int(self._cfg['rain_drops'])

  def DHT_ENABLED(self):
    return int(self._cfg['dht_enabled']) != 0
  def DHT_SENSOR(self):
    return int(self._cfg['dht_sensor'])
  def DHT_PIN(self):
    return int(self._cfg['dht_pin'])
  def DHT_RETRIES(self):
    return int(self._cfg['dht_retries'])

  def ADC_ENABLED(self):
    return int(self._cfg['adc_enabled']) != 0
  def ADC_CHANNELS(self):
    return [int(x) for x in self._cfg['adc_channels'].split(',') if x]
  def ADC_VREFS(self):
    return [float(x) for x in self._cfg['adc_vrefs'].split(',') if x]

  def HUAWEI_ENABLED(self):
    return int(self._cfg['huawei_enabled']) != 0

  def DOOR_ENABLED(self):
    return int(self._cfg['door_enabled']) != 0
  def DOOR_INPUT_PIN(self):
    return int(self._cfg['door_input_pin'])
  def DOOR_PUD(self):
    return Config._PUD_MAP[self._cfg['door_pud'].lower()]
  def DOOR_OPEN_STATE(self):
    return int(self._cfg['door_open_state'])
  def DOOR_DEBOUNCE_MILLIS(self):
    return int(self._cfg['door_debounce_millis'])

  def PILOTS_ENABLED(self):
    return int(self._cfg['pilots_enabled']) != 0
  def PILOTS_PLUS_INPUT_PIN(self):
    return int(self._cfg['pilots_plus_input_pin'])
  def PILOTS_MINUS_INPUT_PIN(self):
    return int(self._cfg['pilots_minus_input_pin'])
  def PILOTS_PLUS_TRIGGER_STATE(self):
    return int(self._cfg['pilots_plus_trigger_state'])
  def PILOTS_MINUS_TRIGGER_STATE(self):
    return int(self._cfg['pilots_minus_trigger_state'])
  def PILOTS_PLUS_DEBOUNCE_MILLIS(self):
    return int(self._cfg['pilots_plus_debounce_millis'])
  def PILOTS_MINUS_DEBOUNCE_MILLIS(self):
    return int(self._cfg['pilots_minus_debounce_millis'])
  def PILOTS_LED_OUTPUT_PIN(self):
    return int(self._cfg['pilots_led_output_pin'])
  def PILOTS_RESET_HOUR(self):
    return int(self._cfg['pilots_reset_hour'])

  def PRESSURE_ENABLED(self):
    return int(self._cfg['pressure_enabled']) != 0
  def PRESSURE_CS(self):
    return int(self._cfg['pressure_cs'])
  def PRESSURE_SCK(self):
    return int(self._cfg['pressure_sck'])
  def PRESSURE_SDI(self):
    return int(self._cfg['pressure_sdi'])
  def PRESSURE_SDO(self):
    return int(self._cfg['pressure_sdo'])

  def PLUVIO_ENABLED(self):
    return int(self._cfg['pluvio_enabled']) != 0
  def PLUVIO_INPUT_PIN(self):
    return int(self._cfg['pluvio_pin'])
  def PLUVIO_DROPS(self):
    return int(self._cfg['pluvio_drops'])
  def PLUVIO_SIZE_A(self): 
    return int(self._cfg['pluvio_size_a'])
  def PLUVIO_SIZE_B(self):
    return int(self._cfg['pluvio_size_b'])

  def LOGGING_LEVEL(self):
    return self._cfg['logging_level'].upper()
  def LOGGING_MAX_FILE_SIZE_KB(self):
    return int(self._cfg['logging_max_file_size_kb'])
  def LOGGING_BACKUP_COUNT(self):
    return int(self._cfg['logging_backup_count'])

  def CLIENT_VERSION(self):
    return self._cfg['client_version']

  def CAMERA_ENABLED(self):
    return int(self._cfg['camera_enabled']) != 0
  def CAMERA_RESOLUTION_HOR(self):
    return int(self._cfg['camera_resolution_hor'])
  def CAMERA_RESOLUTION_VER(self):
    return int(self._cfg['camera_resolution_ver'])
  
  def WIND_VANE_ENABLED(self):
    return int(self._cfg['wind_vane_enabled'])

C = Config()
