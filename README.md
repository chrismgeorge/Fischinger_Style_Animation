# Audio Visual

### YouTube to MP3
#### Use any YouTube to MP3 or WAV converter on the internet, such as `https://ytmp3.cc/` to convert the youtube audio file you want to use to a MP3 or WAV file. If you already have the audio file, you can skip this step.
#### Additionally, export the combination of all of the songs into another wav or mp3 file.

### Audacity
#### Remix your audio tracks together however you want.
#### Fill any blank space with silence by highlighting the area and then going to `Generate->Silence`.
#### Every track needs to be the exact same length. (This is necessary for the animation)
#### Export each track individually into the `songs` folder in this directory as .wav files.
#### Optional: Rename the files to something you can recognize.

### Main
#### Run main.py by typing `python3 main.py` into terminal from the correct directory.
#### If your songs are not of the exact same length, this will exit prematurely, but might still save a few of the song files.
#### Once main.py is complete, the audio files will now be represented as lists, chunked together and will run at 21fps.
#### These files are automatically saved into `./visuals/data/`

### Visuals
#### Within `./visuals/` you will need to open and run `visuals.pyde` this will create all of the frames for the video and will exit when complete.
#### The frames will be stored in `./visuals/frames/`

### MP4
#### Now you can run `pngs_to_video.py` from terminal with `python3 pngs_to_video.py` from the correct directory.
#### Be careful, this will delete all of the frames automatically while making the video.
#### The video will be saved in `./visuals/video/`
#### I'd then recommend moving the video file to the `./movie_storage/` directory, making a new folder with the name of the movie or song, and then storing all of the files for the file video in there. Such as the remixed MP3/WAV perhaps.

### Movie
#### Now using, iMovie, Adobe Premiere, or some other video editing software, line up the remixed audio file and the video file. The video file will be on average 1 second shorter than the video file, but they will line up perfectly if they start at the same time.
#### That's It!

##### To clean up you may want to delete/move files out of import folders. Such as clearing the `./songs/` directory, the `./visuals/data/` directory and the `./visuals/video/` directory, if you haven't already done so.
