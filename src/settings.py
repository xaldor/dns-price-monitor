from starlette.config import Config
from pydantic import PostgresDsn


env = Config()

# NOTE: APP_TITLE is used in OpenAPI documentation, but it's also just nice to have a project named :)
APP_TITLE: str = env("APP_TITLE")

# NOTE: POSTGRES_URL is constructed from its parts (scheme, user, etc.) in runtime.
# It seems a little bit complicated, but still useful in case we need to get database URL components separatly.
POSTGRES_URL: PostgresDsn = PostgresDsn(
    f"{env('POSTGRES_SCHEME')}://{env('POSTGRES_USER')}:{env('POSTGRES_PASSWORD')}@{env('POSTGRES_HOST')}:{env('POSTGRES_PORT')}/{env('POSTGRES_DB')}",
    scheme=env("POSTGRES_SCHEME"),
)

PRICE_UPDATE_INTERVAL_IN_MINUTES: int = env(
    "PRICE_UPDATE_INTERVAL_IN_MINUTES", cast=int
)
