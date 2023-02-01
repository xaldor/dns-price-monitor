from src.settings import env


SELENIUM_TIMEOUT_IN_SECONDS: int = env("SELENIUM_TIMEOUT_IN_SECONDS", cast=int)
