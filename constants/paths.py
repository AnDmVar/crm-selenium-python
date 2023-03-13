from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parent.parent
CONFIG_DIR = Path(ROOT_DIR / 'config/')
DATABASES_DIR = Path(ROOT_DIR / 'databases/')
MYSQL_DIR = Path(DATABASES_DIR / 'mysql/')
MYSQL_RESOURCES_DIR = Path(MYSQL_DIR / 'resources/')
