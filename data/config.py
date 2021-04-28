from environs import Env

env = Env()
env.read_env()

BOT_TOKEN = env.str("BOT_TOKEN")
ADMINS = env.list("ADMINS")
PGHOST = env.str("PGHOST")
DATABASE = env.str("DATABASE")
PGUSER = env.str("PG_USER")
PGPASSWORD = env.str("PG_PASSWORD")

POSTGRES_URI = f"postgresql://{PGUSER}:{PGPASSWORD}@{PGHOST}/{DATABASE}"
