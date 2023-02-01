from starlette.config import Config


env = Config()

# NOTE: APP_TITLE is used in OpenAPI documentation, but it's also just nice to have a project named :)
APP_TITLE: str = env("APP_TITLE")
