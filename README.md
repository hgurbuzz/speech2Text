1) pip install -U openai-whisper

    Alternatively, the following command will pull and install the latest commit from this repository, along with its Python dependencies:

    pip install git+https://github.com/openai/whisper.git 

2) pip install --upgrade --no-deps --force-reinstall git+https://github.com/openai/whisper.git

3) https://www.gyan.dev/ffmpeg/builds/ adresinden ffmpeg-release-essentials.zip dosyası indirilir. Ortam değişkenlerine eklenir

4) whisper test.wav --language Turkish --model tiny
output olarak .txt, .srt dosyaları oluşur.

5) Size	Parameters	English-only model	Multilingual model	Required VRAM	Relative speed
tiny	39 M	tiny.en	tiny	~1 GB	~10x
base	74 M	base.en	base	~1 GB	~7x
small	244 M	small.en	small	~2 GB	~4x
medium	769 M	medium.en	medium	~5 GB	~2x
large	1550 M	N/A	large	~10 GB	1x
turbo	809 M	N/A	turbo	~6 GB	~8x

6) To translate speech into English, use:
whisper japanese.wav --model medium --language Japanese --task translate
