import pyaudio
import numpy as np
import wave
import math
import matplotlib.pyplot as plt
import sys, os

# "CHUNK" is the number of frames in the buffer.
CHUNK = 2100
FORMAT = pyaudio.paInt16
CHANNELS = 1
# "RATE" is the number of samples collected per second.
RATE = 44100


# rms algorithm from internet
def rms(data):
    count = len(data)
    sum_squares = 0.0
    for sample in data:
        n = sample * (1.0/32768)
        sum_squares += n*n
    return math.sqrt( sum_squares / count )


# get list of rms by chunk
def getRMSByChunk(wf, RECORD_SECONDS):
    rmsList = []

    for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
      data = wf.readframes(CHUNK)
      data_int = np.fromstring(data, dtype=np.int16)
      x_hold = rms(data_int)*500
      rmsList.append(int(x_hold))

    # normalize between 0 - 255
    min_subed_off = np.array(rmsList) -  min(rmsList)
    normalized = list(np.floor(255*(min_subed_off / np.amax(min_subed_off))))

    return normalized


def main():
    # gives a list of all songs in Songs folder
    songs = os.listdir('./songs/')
    sizes_seen = []
    for song in songs:

      # only do wav files
      if ('.wav' not in song):
        continue

      # get entire pathname to song
      song_path = './songs/'+song

      # set up audio
      wf = wave.open(song_path, 'rb')
      p = pyaudio.PyAudio()
      frames = wf.getnframes()
      rate = wf.getframerate()
      duration = int(frames / float(rate))

      stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
                      channels=wf.getnchannels(),
                      rate=wf.getframerate(),
                      output=True)

      # get list of rms by chunk
      rmsList = getRMSByChunk(wf, duration)

      save_name = song.replace('.wav', '.txt')
      data_file_path = './visuals/data/' + save_name

      if (len(sizes_seen) > 0):
        if (len(rmsList) not in sizes_seen):
          print('Need to have equally sized files')
          exit(0)
      else:
        sizes_seen.append(len(rmsList))

      with open(data_file_path, 'w') as file:
          file.write(str(rmsList))


if __name__ == "__main__":
    try:
        main()
    except(IndexError):
        print('An error occurred.')
        exit(0)
