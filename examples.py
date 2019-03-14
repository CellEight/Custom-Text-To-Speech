import time
#1. First import the ttsEngine file. It'll need to be in the same folder that your
#code is running from as will cmudict-0.7b.txt and the phonemes folder
import ttsEngine
#2. Create an instance of the tts class
tts = ttsEngine.tts()
#3. Call the tts.textToSpeech() method with the text you would like to be read
tts.textToSpeech("the sky over the port was the colour of television")
time.sleep(1)
tts.textToSpeech("The Vampire Who Keeps Us In Line Decrees We Must Amuse Ourselves With What She Leaves")
time.sleep(1)
tts.textToSpeech("Everything under heaven is utter chaos; the situation is excellent")
#4. Listen to a freakish simulacrum of my voice (or your's if you make the neessary changes!)
# wax lyrical on a subject of your choosing!
