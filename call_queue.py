from gtts import gTTS as tts
import os
from io import BytesIO


def call_patient(name,  room, queue_number):
    call = tts("Nomor antrian"+ queue_number + ", atas nama " + name + "," + "Silahkan menuju" + room, lang='id')
    audio_buffer = BytesIO()
    tts.write_to_fp(audio_buffer)
    audio_buffer.seek(0)
    return audio_buffer