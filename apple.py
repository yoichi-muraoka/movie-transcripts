import os
from moviepy import VideoFileClip
import whisper

# フォルダのパス設定
video_folder = "mov"
audio_folder = "aud"
text_folder = "transcripts"

# フォルダが存在しない場合は作成
os.makedirs(audio_folder, exist_ok=True)
os.makedirs(text_folder, exist_ok=True)

# Whisper モデルをロード（最初に一度だけ）
model = whisper.load_model("small")

# `mov` フォルダ内のすべての mp4 ファイルを処理
for video_filename in os.listdir(video_folder):
    if video_filename.lower().endswith(".mp4"):  # .mp4ファイルのみ対象
        video_path = os.path.join(video_folder, video_filename)
        audio_path = os.path.join(audio_folder, "temp_audio.mp3")
        text_filename = os.path.splitext(video_filename)[0] + ".txt"  # 拡張子を .txt に変更
        text_path = os.path.join(text_folder, text_filename)

        print(f"Processing: {video_filename}")

        try:
            # 動画から音声を抽出
            video = VideoFileClip(video_path)
            video.audio.write_audiofile(audio_path)

            # 音声をテキストに変換
            result = model.transcribe(audio_path)

            # 結果をテキストファイルに保存
            with open(text_path, "w", encoding="utf-8") as f:
                f.write(result["text"])

            print(f"Transcription saved to {text_path}")

        except Exception as e:
            print(f"Error processing {video_filename}: {e}")

        finally:
            # 一時的な音声ファイルを削除
            if os.path.exists(audio_path):
                os.remove(audio_path)

print("All videos processed successfully!")