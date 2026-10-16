# ************************************************************
# ファイル操作用のユーティリティ関数を提供するモジュール
# ************************************************************

# 標準ライブラリのインポート
import os


# ============================================================
# ファイルの存在確認関数
# ============================================================
def file_exists(file_path):
    """
    指定されたファイルが存在するかを確認する関数

    引数:
    file_path: 確認するファイルのパス

    戻り値:
    存在する場合は True、存在しない場合は False
    """
    return os.path.isfile(file_path)


# ============================================================
# ディレクトリの存在確認関数
# ============================================================
def directory_exists(directory_path):
    """
    指定されたディレクトリが存在するかを確認する関数

    引数:
    directory_path: 確認するディレクトリのパス

    戻り値:
    存在する場合は True、存在しない場合は False
    """
    return os.path.isdir(directory_path)


# ============================================================
# ファイルの読み込み関数
# ============================================================
def read_file(file_path):
    """
    指定されたファイルの内容を読み込む関数

    引数:
    file_path: 読み込むファイルのパス

    戻り値:
    ファイルの内容（文字列）
    """
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()


# ============================================================
# ファイルの書き込み関数
# ============================================================
def write_file(file_path, content, append=False):
    """
    指定されたファイルに内容を書き込む関数
    引数:
    file_path: 書き込むファイルのパス
    content: ファイルに書き込む内容
    append: True の場合は追記モードで書き込む（デフォルトは False）

    戻り値: なし
    """
    mode = 'a' if append else 'w'
    with open(file_path, mode, encoding='utf-8') as file:
        file.write(content)


# ============================================================
# ダイアログ表示してファイルを選択する関数
# ============================================================
def select_file_dialog(filetypes=(("All files", "*.*"),)):
    """
    ダイアログを表示してファイルを選択する関数

    引数:
    filetypes: 入力することで任意のファイル形式を指定できる
    ※ デフォルトでは全てのファイルが表示される
    """
    from tkinter import Tk
    from tkinter.filedialog import askopenfilename

    root = Tk()
    root.withdraw()  # メインウィンドウを表示しない
    file_path = askopenfilename(filetypes=filetypes)
    return file_path


# ============================================================
# ダイアログ表示してファイルを保存する関数
# ============================================================
def save_file_dialog(filetypes=(("All files", "*.*"),)):
    """
    ダイアログを表示してファイルを保存する関数

    引数:
    filetypes: 入力することで任意のファイル形式を指定できる
    ※ デフォルトでは全てのファイルが表示される
    """
    from tkinter import Tk
    from tkinter.filedialog import asksaveasfilename

    root = Tk()
    root.withdraw()  # メインウィンドウを表示しない
    file_path = asksaveasfilename(filetypes=filetypes)
    return file_path


# ============================================================
# ダイアログ表示してディレクトリを選択する関数
# ============================================================
def select_directory_dialog():
    """ダイアログを表示してディレクトリを選択する関数"""
    from tkinter import Tk
    from tkinter.filedialog import askdirectory

    root = Tk()
    root.withdraw()  # メインウィンドウを表示しない
    directory_path = askdirectory()
    return directory_path
