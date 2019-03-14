# Custom-Text-To-Speech

For instructions on how to use this text to speech engine have a look at examples.py

Adding your own voice:

This program is based on a phonetic alphabet called the ARPABET which was developed by the Advanced Research Projects Agency as a part of their Speech Understanding Research project in the 1970s. (https://en.wikipedia.org/wiki/ARPABET)
The program works by looking up to words passed to it as input in a dictionary that pairs words to their ARPABET representations (contained in cmudict-0.7b.txt which is sourced from http://www.speech.cs.cmu.edu/cgi-bin/cmudict) and then playing back each of the phonemes in the ARPABET "spelling" of the word.
To add a different voice to the program all you need to do is to record yourself saying all the phonemes of the ARPABET (in a program such as audacity) and overwrite the pre-existing ones in the phonemes folder.
Do bear in mind that the ARPABET code of the phoneme doesn't necessarily match up to how you say it out loud so I would recommend using the table on wikipedia page to guide you on pronunciation.

Best of Luck! :)
