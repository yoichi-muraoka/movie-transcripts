import os
from moviepy import VideoFileClip
import whisper

# Set the paths
video_folder = "mov"
video_filename = "test.mp4"  # Replace with your actual video file name
video_path = os.path.join(video_folder, video_filename)

audio_folder = "aud"
output_audio_path = os.path.join(audio_folder, "temp_audio.mp3")

text_folder = "transcripts"  # 保存先フォルダ
output_text_path = os.path.join(text_folder, "transcription.txt")  # 保存先ファイル

# フォルダが存在しない場合は作成
os.makedirs(audio_folder, exist_ok=True)
os.makedirs(text_folder, exist_ok=True)

# Extract audio from the video
video = VideoFileClip(video_path)
video.audio.write_audiofile(output_audio_path)

# Load the Whisper ASR model
model = whisper.load_model("small")

# Transcribe the extracted audio
result = model.transcribe(output_audio_path)

# 保存: テキストファイルに書き込み
with open(output_text_path, "w", encoding="utf-8") as f:
    f.write(result["text"])

print(f"Transcription saved to {output_text_path}")

# Remove the temporary audio file
os.remove(output_audio_path)