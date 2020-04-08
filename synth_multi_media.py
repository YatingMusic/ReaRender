import os
import glob
import time
import datetime
import threading
from rearender.utils import render_multi_media


# start
program_start_time = time.time()

# config
tolerance_sec = 20

# IO folders
path_midi = '/Users/wayne391/Documents/Projects/midi_rendering/git/audio-autorender-reaper/src/multi_media/m.midi'
path_audio = '/Users/wayne391/Documents/Projects/midi_rendering/git/audio-autorender-reaper/src/multi_media/a.mp3'
path_outfile = '/Users/wayne391/Documents/Projects/midi_rendering/git/audio-autorender-reaper/src/multi_media/synth_out'

# mapping dict: (track_idx, path_media)
mapping_dict = {
    0: path_midi,
    1: path_audio,
}
is_press = [
    True,
    False
]
# render
render_multi_media(
    mapping_dict, 
    path_outfile,
    bpm=None, 
    is_press=is_press)

# finished
print('\n===== Finished =====')
runtime = time.time() - program_start_time
print('Elapsed time:', str(datetime.timedelta(seconds=runtime)))
