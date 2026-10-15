import sys
import os
import webview

HTML_NAME = "番茄钟.html"


def resource_path(name):
    # PyInstaller 打包后资源在 _MEIPASS；未打包时在同目录
    base = getattr(sys, "_MEIPASS", os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base, name)


def main():
    html_path = resource_path(HTML_NAME)
    with open(html_path, "r", encoding="utf-8") as f:
        html = f.read()
    webview.create_window("茉莉花猪の番茄钟", html=html, width=420, height=640)
    webview.start()


if __name__ == "__main__":
    main()
