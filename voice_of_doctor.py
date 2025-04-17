#step1 set up TTS Text to speech with gtts 
import os 
from gtts import gTTS



def text_to_speech_with_gtts_old(input_text,output_filepath):
    language='en'

    audioobj=gTTS(
        text=input_text,
        lang=language,
        slow=False
    )
    audioobj.save(output_filepath)

input_text= 'Hi this AI with Vaishnavi'

#text_to_speech_with_gtts_old(input_text=input_text,output_filepath='gtts_testing.mp3')



#step1 set up TTS Text to speech with  eleven labs
import elevenlabs
from elevenlabs.client import ElevenLabs

#ELEVENLABS_API_KEY = os.environ.get('ELEVENLABS_API_KEY ')
ELEVENLABS_API_KEY="sk_d84250fc67ea276fb9343e43b9f230d5be9a8a665d4277b2"
def text_to_speech_with_eleven_labs_old(input_text,output_filepath):
    client = ElevenLabs(api_key=ELEVENLABS_API_KEY)
    audio= client.generate(

            text =input_text,
            voice= "Aria",
            output_format='mp3_22050_32' ,
            model= 'eleven_turbo_v2'

    )
    elevenlabs.save(audio,output_filepath)    
#text_to_speech_with_eleven_labs_old(input_text,output_filepath='elevenlabs_testing.mp3')


#step2 use model for text output to voice '

import subprocess
import platform
def text_to_speech_with_gtts(input_text,output_filepath):
    language='en'

    audioobj=gTTS(
        text=input_text,
        lang=language,
        slow=False
    )
    audioobj.save(output_filepath)
    audioobj.save(output_filepath)
    os_name = platform.system()
    try:
        if os_name == "Darwin":  # macOS
            subprocess.run(['afplay', output_filepath])
        elif os_name == "Windows":  # Windows
            subprocess.run(['powershell', '-c', f'(New-Object Media.SoundPlayer "{output_filepath}").PlaySync();'])
        elif os_name == "Linux":  # Linux
            subprocess.run(['aplay', output_filepath])  # Alternative: use 'mpg123' or 'ffplay'
        else:
            raise OSError("Unsupported operating system")
    except Exception as e:
        print(f"An error occurred while trying to play the audio: {e}")



#text_to_speech_with_gtts(input_text=input_text,output_filepath='gtts_autoplay_testing.mp3')

'''
def text_to_speech_with_eleven_labs(input_text,output_filepath):
    client = ElevenLabs(api_key=ELEVENLABS_API_KEY)
    audio= client.generate(

            text =input_text,
            voice= "Aria",
            output_format='mp3_22050_32' ,
            model= 'eleven_turbo_v2'

    )
    elevenlabs.save(audio, output_filepath)
    os_name = platform.system()
    try:
        if os_name == "Darwin":  # macOS
            subprocess.run(['afplay', output_filepath])
        elif os_name == "Windows":  # Windows
            subprocess.run(['powershell', '-c', f'(New-Object Media.SoundPlayer "{output_filepath}").PlaySync();'])
        elif os_name == "Linux":  # Linux
            subprocess.run(['aplay', output_filepath])  # Alternative: use 'mpg123' or 'ffplay'
        else:
            raise OSError("Unsupported operating system")
    except Exception as e:
        print(f"An error occurred while trying to play the audio: {e}")
   
text_to_speech_with_eleven_labs(input_text,output_filepath='elevenlabs_autoplay_testing.mp3')
'''
input_text="Hi, this is AI with Vaishnavi, autoplay testing"
from pydub import AudioSegment
def convert_mp3_to_wav(output_filepath, wav_filepath):
    """ Convert MP3 file to WAV """
    audio = AudioSegment.from_mp3(output_filepath)
    audio.export(wav_filepath, format="wav")

def text_to_speech_with_eleven_labs(input_text, output_filepath, wav_filepath):
    """ Generate speech using Eleven Labs and play it """
    client = ElevenLabs(api_key=ELEVENLABS_API_KEY)
    audio = client.generate(
        text=input_text,
        voice="Aria",
        output_format="mp3_22050_32",
        model="eleven_turbo_v2"
    )
    elevenlabs.save(audio,output_filepath)

    # Convert MP3 to WAV
    convert_mp3_to_wav(output_filepath, wav_filepath)

    # Play audio based on OS
    os_name = platform.system()
    try:
        if os_name == "Windows":
            subprocess.run(['powershell', '-c', f'(New-Object Media.SoundPlayer "{wav_filepath}").PlaySync();'])
        elif os_name == "Darwin":  # macOS
            subprocess.run(['afplay', wav_filepath])
        elif os_name == "Linux":
            subprocess.run(['aplay', wav_filepath])
        else:
            raise OSError("Unsupported OS")
    except Exception as e:
        print(f"Error playing audio: {e}")

# Run the function
text_to_speech_with_eleven_labs(
    input_text,
    output_filepath="elevenlabs_autoplay_testing.mp3",
    wav_filepath="elevenlabs_autoplay_testing.wav"
)