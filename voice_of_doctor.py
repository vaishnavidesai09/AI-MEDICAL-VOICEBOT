# voice_of_doctor.py (updated)

import os
from gtts import gTTS
import subprocess
import platform
from pydub import AudioSegment
from elevenlabs.client import ElevenLabs
from elevenlabs import play, save

# ———————————————————————————————
# gTTS setup (unchanged)
def text_to_speech_with_gtts(input_text, output_filepath):
    audioobj = gTTS(text=input_text, lang='en', slow=False)
    audioobj.save(output_filepath)
    os_name = platform.system()
    play_cmd = {
        "Windows": ['powershell', '-c', f'(New-Object Media.SoundPlayer "{output_filepath}").PlaySync();'],
        "Darwin": ['afplay', output_filepath],
        "Linux": ['aplay', output_filepath],
    }.get(os_name)
    if play_cmd:
        subprocess.run(play_cmd)

# ———————————————————————————————
# ElevenLabs setup (updated)

ELEVENLABS_API_KEY = os.getenv("ELEVENLABS_API_KEY", "sk_ffe36395a3a2bd0dccf00bea95f27dab57395387d1ec52f4")
client = ElevenLabs(api_key=ELEVENLABS_API_KEY)

def convert_mp3_to_wav(mp3_fp, wav_fp):
    audio = AudioSegment.from_mp3(mp3_fp)
    audio.export(wav_fp, format="wav")

def text_to_speech_with_eleven_labs(input_text, output_mp3, output_wav):
    # Use the new method from the official SDK
    result = client.text_to_speech.convert(
        text=input_text,
        voice_id="21m00Tcm4TlvDq8ikWAM",  # or use voice="Bella" or whichever voice ID
        model_id="eleven_multilingual_v2",
        output_format="mp3_22050_32"
    )
    save(result, output_mp3)

    convert_mp3_to_wav(output_mp3, output_wav)

    return output_mp3