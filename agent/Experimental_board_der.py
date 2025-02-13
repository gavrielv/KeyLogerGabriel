from KeyLoggerService import KeyLoggerService  
keyloger = KeyLoggerService()
keyloger.start_logging()
a = input()
print(keyloger.get_logged_keys())
a =input()
keyloger.stop_logging()


