#!/usr/bin/env python
# encoding: utf=8

"""
reverse.py

Reverse the beats, segments, tatums, bars, and sections of a track. 

Originally created by Robert Ochshorn on 2008-06-11.  Refactored by
Joshua Lifton 2008-09-07.

Modified by Joe Paxton
16 Feb 2015
"""

import echonest.remix.audio as audio

usage = """
Usage: 
    python reverse.py <beats|segments|tatums|bars|sections> <inputFilename> <outputFilename.mp3>

Example:
    python reverse.py beats YouCanCallMeAl.mp3 AlMeCallCanYou.mp3
"""

def main(toReverse, inputFilename, outputFilename):
    audioFile = audio.LocalAudioFile(inputFilename)
    if toReverse == 'beats' :
        chunks = audioFile.analysis.beats
    elif toReverse == 'segments':
        chunks = audioFile.analysis.segments
    elif toReverse == 'tatums':
		chunks = audioFile.analysis.tatums
    elif toReverse == 'bars'    :
		chunks = audioFile.analysis.bars
    elif toReverse == 'sections' :
		chunks = audioFile.analysis.sections
    else :
        print usage
        return
    chunks.reverse()
    reversedAudio = audio.getpieces(audioFile, chunks)
    reversedAudio.encode(outputFilename)

if __name__ == '__main__':
    import sys
    try :
        toReverse = sys.argv[1]
        inputFilename = sys.argv[2]
        outputFilename = sys.argv[3]
    except :
        print usage
        sys.exit(-1)
    if not toReverse in ["beats", "segments", "tatums", "bars", "sections"]:
        print usage
        sys.exit(-1)
    main(toReverse, inputFilename, outputFilename)
