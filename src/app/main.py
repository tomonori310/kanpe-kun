# ************************************************************
# メインアプリケーションのエントリーポイント
# ************************************************************

# 標準ライブラリおよびサードパーティライブラリのインポート
import customtkinter as ctk


# ============================================================
# メイン関数の定義
# ============================================================
def main():
    # 設定を読み込む
    from config import WINDOW_DATA, UI_DATA
    from commons.debug import log_print

    log_print("アプリケーション起動")

    # アプリケーションの初期化
    ctk.set_appearance_mode(UI_DATA["appearance_mode"])
    ctk.set_default_color_theme(UI_DATA["color_theme"])
    app = ctk.CTk()

    # ウィンドウの各種設定
    app.title(WINDOW_DATA["title"])                 # タイトルを設定
    app.geometry(WINDOW_DATA["geometry"])           # 初期サイズを設定
    app.resizable(False, False)                     # サイズを固定
    app.configure(bg=UI_DATA["appearance_mode"])    # 背景色を設定
    app.option_add("*Font", "Helvetica 12")         # フォントを設定
    if WINDOW_DATA["min_width"] > 0 and WINDOW_DATA["min_height"] > 0:
        app.minsize(WINDOW_DATA["min_width"], WINDOW_DATA["min_height"])
    if WINDOW_DATA["max_width"] > 0 and WINDOW_DATA["max_height"] > 0:
        app.maxsize(WINDOW_DATA["max_width"], WINDOW_DATA["max_height"])
    app.eval('tk::PlaceWindow . center')            # 中央配置

    app.mainloop()


# スクリプトが直接実行された場合の処理
if __name__ == '__main__':
    main()
