# ************************************************************
# 設定ファイルの読み込みと管理を行うモジュール
# ************************************************************

# 標準ライブラリのインポート
import json
import os


# 設定ファイルのパスを定義する
CONFIG_FILE_PATH = os.path.join(
    os.path.dirname(__file__),
    "resources",
    "default_conf.json"
)


# ============================================================
# 設定ファイルを読み込む関数を定義する
# ============================================================
def load_config():
    with open(CONFIG_FILE_PATH, "r", encoding="utf-8") as f:
        return json.load(f)


# 設定を読み込む
_config = load_config()


# ウィンドウ関連の設定データを取得
WINDOW_DATA = {
    "title": _config.get("window", {}).get("title", "かんぺくん"),
    "icon": _config.get("window", {}).get("icon", ""),
    "geometry": _config.get("window", {}).get("geometry", "800x600"),
    "min_width": _config.get("window", {}).get("min_width", 400),
    "min_height": _config.get("window", {}).get("min_height", 300),
    "max_width": _config.get("window", {}).get("max_width", 0),
    "max_height": _config.get("window", {}).get("max_height", 0)
}

# UIデータ取得
UI_DATA = {
    "appearance_mode": _config.get("ui", {}).get("appearance_mode", "dark"),
    "color_theme": _config.get("ui", {}).get("color_theme", "blue")
}
