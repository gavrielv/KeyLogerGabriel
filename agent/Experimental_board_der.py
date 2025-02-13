from KeyLoggerService import KeyLoggerService  

KeyLoggerService.start_logging()
print(KeyLoggerService.get_logged_keys())
KeyLoggerService.stop_logging()