# 音声ファイルクリア選別プログラム

## 概要

このプログラムは、指定されたフォルダ内の音声ファイルを解析し、クリア（きれいなこもりのない）な音声だけを選別して別のフォルダに移動します。クリアな音声はRMS（Root Mean Square）を計算して判定します。

## 必要なライブラリ

- pydub
- pyaudio

インストール方法（pipを使用する場合）：

pip install pydub pyaudio


## 使用方法

1. `input`フォルダにクリアな音声ファイルと、それ以外の音声ファイルを用意します。ただし、クリアな音声ファイルのRMS値は`3000`以上としてください（必要に応じてコードを調整してください）。

2. `test.py`ファイルを実行します。

python test.py

    プログラムが実行され、outputフォルダにクリアな音声ファイルが移動されます。

    outputフォルダ内にクリアな音声ファイルが移動されたことを確認してください。

注意事項

    このプログラムはPython 3で動作します。
    クリアな音声の判定はRMS値に基づいています。RMS値の閾値を適切に調整してください（デフォルトでは5000）。
    pyaudioは音声ファイルの解析に使用されますが、インストールには注意が必要かもしれません（特にWindows環境）。

ライセンス

MITライセンスのもとで配布されています。詳細はLICENSEファイルを参照してください。



# Audio File Clear Selection Program

## Overview

This program analyzes audio files in the specified folder and selectively moves only clear (noise-free) audio files to another folder. The clarity of the audio is determined based on the Root Mean Square (RMS) value.

## Required Libraries

- pydub
- pyaudio

To install the required libraries (using pip):

pip install pydub pyaudio


## Usage

1. Prepare clear audio files and other audio files in the `input` folder. However, ensure that the RMS value of clear audio files is greater than `3000` (adjust as needed in the code).

2. Run the `test.py` file:

python test.py

    The program will run and move the clear audio files to the output folder.

    Check the output folder to verify that the clear audio files have been moved.

Notes

    This program works with Python 3.
    Clear audio is determined based on the RMS value threshold (default is 3000). Adjust it as needed.
    Pyaudio is used for audio file analysis. Please be mindful of the installation, especially on Windows environments.

License

Distributed under the MIT License. See LICENSE file for more information.