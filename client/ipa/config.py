import RPi.GPIO as GPIO  #@UnresolvedImport


import K


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

  def UPLOAD_URL(self):
    """Ensures a trailing '/'."""
    url = self._cfg['upload_url']
    if url[-1] != '/':
      url += '/'
    return url
  def UPLOAD_USERNAME(self):
    return self._cfg['upload_username']
  def UPLOAD_PASSWORD(self):
    return self._cfg['upload_password']
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

  def HUAWEI_ENABLED(self):
    return int(self._cfg['huawei_enabled']) != 0

  def DOOR_ENABLED(self):
    return int(self._cfg['door_enabled']) != 0
  def DOOR_INPUT_PIN(self):
    return int(self._cfg['door_input_pin'])
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

  def LOGGING_LEVEL(self):
    return self._cfg['logging_level']
  def LOGGING_MAX_FILE_SIZE_KB(self):
    return int(self._cfg['logging_max_file_size_kb'])
  def LOGGING_BACKUP_COUNT(self):
    return int(self._cfg['logging_backup_count'])


C = Config()
