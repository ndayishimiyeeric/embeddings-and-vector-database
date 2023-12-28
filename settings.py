import pathlib

from decouple import AutoConfig, Config, RepositoryEnv

BASE_DIR = pathlib.Path(__file__).parent

ENV_FILE_PATH = BASE_DIR / ".env"


def get_config() -> Config | AutoConfig:
    if ENV_FILE_PATH.exists():
        return Config(RepositoryEnv(ENV_FILE_PATH))
    else:
        from decouple import config as _decouple_config

        return _decouple_config


config = get_config()
