# 茉莉花猪の番茄钟

一个简洁的番茄工作法（Pomodoro）计时器，支持专注 / 短休息 / 长休息三种模式，纯前端单文件实现，无需联网、无依赖。

## 功能

- 番茄专注计时（默认 25 分钟）与休息计时（短休息 5 分钟 / 长休息 15 分钟）
- 可视化环形进度，明暗主题自适应
- 阶段切换时桌面通知提醒
- 单文件 HTML，双击即用；同时提供打包好的 Windows 桌面程序

## 使用方式

### 网页版（任意系统）
直接用浏览器打开 [`番茄钟.html`](番茄钟.html) 即可，无需安装任何东西。

### 桌面版（Windows）
下载 [`茉莉花猪の番茄钟.exe`](茉莉花猪の番茄钟.exe) 双击运行。
> 桌面版基于系统 WebView2（Edge 内核）渲染，运行环境需已安装 Microsoft Edge / WebView2 运行时（Win10 / Win11 通常已自带）。

## 文件说明

| 文件 | 说明 |
| --- | --- |
| `番茄钟.html` | 网页版计时器 |
| `茉莉花猪の番茄钟.exe` | Windows 桌面版 |
| `app.py` / `make_icon.py` | 桌面版打包脚本与图标生成脚本（可自行重新打包） |

## 🛠 自行重新打包

```bash
pip install pywebview pyinstaller Pillow
python make_icon.py                 # 生成 tomato.ico
pyinstaller --onefile --windowed --name "茉莉花猪の番茄钟" --icon tomato.ico --add-data "番茄钟.html;." app.py
```

---

Made with 🍅
