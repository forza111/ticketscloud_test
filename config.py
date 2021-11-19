from environs import Env

env = Env()
env.read_env()
USERNAME = env.str("USERNAME")
TOKEN = env.str("TOKEN")
HEADERS = env.json("HEADERS")