from gtts import gTTS as tts

def call_patient(first_name, second_name,  room, queue_number):
    call = tts("Nomor antrian"+ queue_number + ", atas nama " + first_name + second_name + "," + "Silahkan menuju" + room, lang='id')
    return call.save('patient_call-' + first_name + "-" + second_name + '-.mp3')