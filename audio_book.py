from gtts import gTTS
import os

def create_audio_book(text_file, output_file):
    with open(text_file, 'r', encoding='utf-8') as file:
        text = file.read()

    tts = gTTS(text=text, lang='en')
    tts.save(output_file)
    print(f"Audiobook saved as {output_file}")

text_file = 'audio_book.txt'
outputfile = 'audiobook.mp3'

create_audio_book(text_file, outputfile)
# use os.system(f"start {outputfile}") on windows, open is for macOS
os.system(f"open {outputfile}")