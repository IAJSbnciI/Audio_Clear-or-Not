import os
from pydub import AudioSegment
import pyaudio
import wave

def is_clear_audio(audio_path):
    # 音声ファイルをロード
    audio = AudioSegment.from_wav(audio_path)

    # 音声のRMS（Root Mean Square）を計算
    rms = audio.rms

    # RMSが一定以上の値を持つ音声をクリアな音声として判定
    if rms > 5000:  # この値は調整してください
        return True
    else:
        return False

def move_clear_audios(input_folder, output_folder):
    # 出力フォルダが存在しなければ作成
    os.makedirs(output_folder, exist_ok=True)

    # inputフォルダ内の音声ファイルを処理
    for filename in os.listdir(input_folder):
        if filename.endswith(".wav"):
            audio_path = os.path.join(input_folder, filename)
            if is_clear_audio(audio_path):
                # クリアな音声ファイルをoutputフォルダに移動
                output_path = os.path.join(output_folder, filename)
                os.rename(audio_path, output_path)
                print(f"Moved: {filename}")

if __name__ == "__main__":
    input_folder = "input"   # 実際のinputフォルダのパスを指定
    output_folder = "output" # outputフォルダのパスを指定
    move_clear_audios(input_folder, output_folder)
