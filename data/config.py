from environs import Env

env = Env()
env.read_env()

BOT_TOKEN = env.str("BOT_TOKEN")
ADMINS = env.list("ADMINS")
PGHOST = env.str("PGHOST")
PG_USER = env.str("PG_USER")
POSTGRES_PASSWORD = env.str("POSTGRES_PASSWORD")

POSTGRES_URI = f"postgresql://{PG_USER}:{POSTGRES_PASSWORD}@{PGHOST}"
