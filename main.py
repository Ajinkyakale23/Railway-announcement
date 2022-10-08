
import pandas as pd
from pydub import AudioSegment
from gtts import gTTS


def textToSpeech(text, filname):
    mytext = str(text)
    language = "hi"
    myobj = gTTS(text=mytext, lang=language, slow=False)
    myobj.save(filname)


def mergeAudios(audios):
    combined = AudioSegment.empty()
    for audio in audios:
        combined += AudioSegment.from_mp3(audio)
    return combined


def generateSkeleton():
    audio = AudioSegment.from_mp3('Railway Announcement.mp3')
    # 1- Generate kripya dheyan dijiye
    start = 0000
    finish = 3000
    audioProcessed = audio[start:finish]
    audioProcessed.export("1_hindi.mp3", format='mp3')

    start = 7000
    finish = 11000
    audioProcessed = audio[start:finish]
    audioProcessed.export("3_hindi.mp3", format='mp3')

    start = 10500
    finish = 16000
    audioProcessed = audio[start:finish]
    audioProcessed.export("5_hindi.mp3", format='mp3')

    start = 3000
    finish = 7500
    audioProcessed = audio[start:finish]
    audioProcessed.export("7_hindi.mp3", format='mp3')

    start = 23000
    finish = 32000
    audioProcessed = audio[start:finish]
    audioProcessed.export("8_English.mp3", format='mp3')

    start = 16000
    finish = 23000
    audioProcessed = audio[start:finish]
    audioProcessed.export("9_hindi.mp3", format='mp3')


def generateAnnouncement(filename):
    df = pd.read_excel(filename)
    print(df)
    for (index, item) in df.iterrows():

        # 2 - is from - city
        textToSpeech(item['From'], '2_hindi.mp3')

        # 4 -is via - city
        textToSpeech(item['Via'], '4_hindi.mp3')

        # 6 -is to-city
        textToSpeech(item['To'], '6_hindi.mp3')

        # 8 -is train no and name
        textToSpeech(str(item['Train_no']) + " " +
                     item['Train_name'], '8_hindi.mp3')

        # 10 - Generate platform number
        textToSpeech(item['platform'], '10_hindi.mp3')

        audio = [f"{i}_hindi.mp3" for i in range(1, 11)]
        announcement = mergeAudios(audio)
        announcement.export(f"Announcement_{index+1}.mp3", format="mp3")


if __name__ == "__main__":
    print("Generating Skeleton...")
    generateSkeleton()

    print("Now generating Announcement...")
    generateAnnouncement("announce_hindi.xlsx")
