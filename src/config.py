import os
from dataclasses import dataclass

from dotenv import load_dotenv

load_dotenv()


@dataclass(frozen=True, kw_only=True)
class Config:
    rpc_url: str


def load_env_var(var_name: str) -> str:
    """Loads and validates environment variables."""
    return os.getenv(var_name, default="")


# Initialize configuration
config = Config(
    rpc_url=load_env_var("RPC_URL"),
)
