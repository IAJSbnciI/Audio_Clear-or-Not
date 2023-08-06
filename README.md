# �����t�@�C���N���A�I�ʃv���O����

## �T�v

���̃v���O�����́A�w�肳�ꂽ�t�H���_���̉����t�@�C������͂��A�N���A�i���ꂢ�Ȃ�����̂Ȃ��j�ȉ���������I�ʂ��ĕʂ̃t�H���_�Ɉړ����܂��B�N���A�ȉ�����RMS�iRoot Mean Square�j���v�Z���Ĕ��肵�܂��B

## �K�v�ȃ��C�u����

- pydub
- pyaudio

�C���X�g�[�����@�ipip���g�p����ꍇ�j�F

pip install pydub pyaudio


## �g�p���@

1. `input`�t�H���_�ɃN���A�ȉ����t�@�C���ƁA����ȊO�̉����t�@�C����p�ӂ��܂��B�������A�N���A�ȉ����t�@�C����RMS�l��`3000`�ȏ�Ƃ��Ă��������i�K�v�ɉ����ăR�[�h�𒲐����Ă��������j�B

2. `test.py`�t�@�C�������s���܂��B

python test.py

    �v���O���������s����Aoutput�t�H���_�ɃN���A�ȉ����t�@�C�����ړ�����܂��B

    output�t�H���_���ɃN���A�ȉ����t�@�C�����ړ����ꂽ���Ƃ��m�F���Ă��������B

���ӎ���

    ���̃v���O������Python 3�œ��삵�܂��B
    �N���A�ȉ����̔����RMS�l�Ɋ�Â��Ă��܂��BRMS�l��臒l��K�؂ɒ������Ă��������i�f�t�H���g�ł�5000�j�B
    pyaudio�͉����t�@�C���̉�͂Ɏg�p����܂����A�C���X�g�[���ɂ͒��ӂ��K�v��������܂���i����Windows���j�B

���C�Z���X

MIT���C�Z���X�̂��ƂŔz�z����Ă��܂��B�ڍׂ�LICENSE�t�@�C�����Q�Ƃ��Ă��������B



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