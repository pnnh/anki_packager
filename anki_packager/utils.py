import os
import platform

from anki_packager.logger import logger


def get_project_root():
    """
    Returns the project root directory (where setup.py is located).
    """
    current_file = os.path.abspath(__file__)
    # __file__ is in anki_packager/utils.py
    # project root is two levels up
    return os.path.dirname(os.path.dirname(current_file))


def get_user_config_dir():
    """
    Returns the platform-specific user configuration directory.

    - Windows: %APPDATA%/anki_packager
    - macOS/Linux: ~/.config/anki_packager
    """
    if platform.system() == "Windows":
        return os.path.join(os.environ.get("APPDATA", ""), "anki_packager")
    else:
        return os.path.expanduser("~/.config/anki_packager")


def get_config_dir():
    """
    Returns the configuration directory, preferring project directory over user config.

    Priority:
    1. Project directory (e.g., E:/Workspace/tools/anki_packager/)
       - If config/config.toml exists in project root
    2. User config directory (e.g., %APPDATA%/anki_packager or ~/.config/anki_packager)

    Returns the base config directory (not the 'config' subdirectory).
    """
    project_root = get_project_root()
    project_config_file = os.path.join(project_root, "config", "config.toml")

    # Check if project config exists
    if os.path.exists(project_config_file):
        logger.debug(f"使用项目配置目录: {project_root}")
        return project_root

    # Fall back to user config directory
    user_config = get_user_config_dir()
    logger.debug(f"使用用户配置目录: {user_config}")
    return user_config


def initialize_config():
    """
    Make sure config dir exists.

    Priority order:
    1. Use project directory if config/config.toml exists there
    2. Otherwise use user config directory

    Example structure:
    <config_dir>/
        ├── config/
        │   ├── config.toml
        │   ├── failed.txt
        │   └── vocabulary.txt
        └── dicts/
            ├── 单词释义比例词典-带词性.mdx
            ├── 有道词语辨析.mdx
            ├── stardict.7z
            ├── stardict.csv
            └── stardict.db
    """
    # Always ensure user config dir exists as fallback
    user_config_dir = get_user_config_dir()
    os.makedirs(user_config_dir, exist_ok=True)
    user_config_subdir = os.path.join(user_config_dir, "config")
    os.makedirs(user_config_subdir, exist_ok=True)
    user_dicts_dir = os.path.join(user_config_dir, "dicts")
    os.makedirs(user_dicts_dir, exist_ok=True)

    # Get the actual config directory to use (project dir if config exists, else user dir)
    config_dir = get_config_dir()
    config_subdir = os.path.join(config_dir, "config")
    os.makedirs(config_subdir, exist_ok=True)
    dicts_dir = os.path.join(config_dir, "dicts")
    os.makedirs(dicts_dir, exist_ok=True)

    # Default configuration in TOML format
    default_config = """
PROXY = ""
EUDIC_TOKEN = ""
EUDIC_ID = "0"
DECK_NAME = "anki_packager"

[[MODEL_PARAM]]
model = "gemini/gemini-2.5-flash"
api_key = "GEMINI_API_KEY"
rpm = 10                          # 每分钟请求次数

# [[MODEL_PARAM]]
# model = "openai/gpt-4o"
# api_key = "OPENAI_API_KEY"
# api_base = "YOUR_API_BASE"
# rpm = 200

"""

    config_path = os.path.join(config_subdir, "config.toml")
    if not os.path.exists(config_path):
        with open(config_path, "w", encoding="utf-8") as f:
            f.write(default_config)

    vocab_path = os.path.join(config_subdir, "vocabulary.txt")
    if not os.path.exists(vocab_path):
        with open(vocab_path, "w", encoding="utf-8") as f:
            f.write("")

    failed_path = os.path.join(config_subdir, "failed.txt")
    if not os.path.exists(failed_path):
        with open(failed_path, "w", encoding="utf-8") as f:
            f.write("")

    logger.info(f"配置文件位于 {config_path}")
