#Created 18:07 26/02/19
#Description: A text to speech engine that synthesizes speech
#by combining recordings of me saying single phonemes from the
#ARPABET phonetic transcription codes
import re, pyaudio, time, wave, contextlib

class tts:
    def __init__(self):
        self.p = pyaudio.PyAudio()
        filename = 'cmudict-0.7b.txt'
        self.loadDict(filename)

    def loadDict(self, filename):
        self.dict = {}
        with open(filename, 'r') as file:
            for line in file:
                if not line.startswith(';;;'):
                    key, val = line.split('  ',2)
                    self.dict[key] = re.findall(r"[A-Z]+",val)

    def getPhonemes(self, word):
        phonemes = []
        print(word)
        if word in self.dict:
            phonemes += self.dict[word]
        #print(phonemes)
        return phonemes

    def say(self, word):
        chunk = 1024
        p = pyaudio.PyAudio()
        for phoneme in word:
            wf = wave.open("phonemes/"+phoneme.upper()+".wav", 'rb')
            stream = self.p.open(format=p.get_format_from_width(wf.getsampwidth()),
                        channels=wf.getnchannels(),
                        rate=wf.getframerate(),
                        output=True)
            data = wf.readframes(chunk)
            while data:
                stream.write(data)
                data = wf.readframes(chunk)
            stream.stop_stream()
            stream.close()
        return
#Doing this is quite complicated; You'll want to think this over
#    def numToWords(self, passage):
#        numbers = ['ONE', 'TWO', 'THREE', 'FOUR', 'FIVE', 'SIX', 'SEVEN', 'EIGHT', 'NINE', 'TEN']
#        result = re.sub(r'[1]', "ONE", passage)

    def textToSpeech(self, passage):
        regex = re.compile('[^a-zA-Z\. ]')
        passage = regex.sub('', passage)
        passage =  passage.upper()
        print(passage)
        #passage = self.numToWords(passage)
        sentences = passage.split('.')
        #print(sentences)
        for i, sentence in enumerate(sentences):
            sentences[i] = sentence.split(" ")
            #print(sentences[i])
            for j, word in enumerate(sentences[i]):
                sentences[i][j] = self.getPhonemes(word)#[::-1]#.reverse()
        print(sentences)
        #Could do this all in one big loop but will break it into 2 for logical reasons
        for sentence in sentences:
            for word in sentence:
                self.say(word)
                time.sleep(0.05)
            time.sleep(0.15)
