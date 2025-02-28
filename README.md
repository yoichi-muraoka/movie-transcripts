# プロジェクト概要

このプロジェクトは、`OpenAI Whisper` を使用して `mov` フォルダ内のすべての `.mp4` 動画の音声をテキスト化し、`transcripts` フォルダに `.txt` ファイルとして保存するスクリプトです。

## 📂 プロジェクト構成
project_root/ <br>
　│── mov/ ← 🎥 動画フォルダ（ここに .mp4 を置く）<br>
　│── aud/ ← 🎵 一時音声フォルダ（処理後に削除）<br>
　│── transcripts/ ← 📝 生成されたテキストを保存 <br>
　│── apple.py ← 🐍 メインの Python スクリプト <br>
　│── app-runner.bat ← 🎯 ダブルクリックで実行できるバッチファイル <br>
　│── README.md ← 📖 この説明ファイル

## 🚀 動作環境
- Python 3.8 以上
- `ffmpeg` がインストールされていること
- 必要なライブラリ:
  - `moviepy`
  - `whisper`

## 🔧 インストール
1. **Python をインストール**（[公式サイト](https://www.python.org/downloads/) ）
2. **必要なライブラリをインストール**
  - [動画ファイルからテキスト抽出がWhisperを使えば数十分で実装できた話](https://qiita.com/ShinyaNakayama/items/8ab7a0033a99b2644066)
3. **`ffmpeg` をインストール**
  - [WindowsにFFmpegをインストールする方法](https://qiita.com/Tadataka_Takahashi/items/9dcb0cf308db6f5dc31b)

## ▶ 使い方
1. `mov` フォルダに `.mp4` 動画ファイルを入れる
2. **ダブルクリックで実行**（Windows）
   - `app-runner.bat` を **ダブルクリック** するだけ
3. transcripts フォルダに 動画名.txt のファイルが生成される
※ *apple.py*の15行目にあるモデルの設定を`small`から`medium`や`large`に変更することで、精度が上がりますが、変換に時間を要します。逆に`base`や`tiny`にすることで、精度を下げ、短時間で処理できるようになります。私の環境では、`small`設定で、計25分の動画に12分程度の変換時間を要しました。

## ⚠ 注意点
- ffmpeg がインストールされていないと動作しません。
- aud フォルダ内の .mp3 ファイルは処理後に自動で削除されます。
- whisper のモデルを初めて使う際は、ダウンロードに時間がかかることがあります。

## 参考
- [動画ファイルからテキスト抽出がWhisperを使えば数十分で実装できた話](https://qiita.com/ShinyaNakayama/items/8ab7a0033a99b2644066)
- [WindowsにFFmpegをインストールする方法](https://qiita.com/Tadataka_Takahashi/items/9dcb0cf308db6f5dc31b)
