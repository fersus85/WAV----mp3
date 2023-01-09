# import required modules
from pathlib import Path
from pydub import AudioSegment


def convert_to_mp3(inlet: str, output):
    # Define input and output file
    input_file = Path(inlet)
    output_file = f'{output.stem}.mp3'

    # convert mp3 file to converters file
    sound = AudioSegment.from_wav(input_file)
    sound.export(output_file, format='mp3')
