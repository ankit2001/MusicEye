# File to play midi files

import pygame as pg
import optparse

# Function to play the files 
def play(file):
	time_in = pg.time.Clock()
  # Using pygame module to paly midi files using mixer and frequecy count
	pg.mixer.music.load(file)
	print(str(file) + ":  Music file is loaded")
	pg.mixer.music.play()
	while pg.mixer.music.get_busy():
		time_in.tick(35)

parser=optparse.OptionParser()
parser.add_option("-f","--file",dest="midi",help="midi file name")
(options,args)=parser.parse_args()
if __name__ == "__main__":

  midi_file = options.midi
  freq = 45000
  bitsize = -16
  # Assigning channels
  channels = 4
  buffer = 1024
  pg.mixer.init(freq, bitsize, channels, buffer)
  pg.mixer.music.set_volume(0.9)
  # Let's start
  try:
    play(midi_file)
  except KeyboardInterrupt:
    pg.mixer.music.fadeout(1000)
    pg.mixer.music.stop()
    raise SystemExit

