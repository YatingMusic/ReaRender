import os
import sys
import glob
import time
import threading
import pretty_midi
import beyond.Reaper
from copy import deepcopy
from rearender.autogui import click_window


def traverse_dir(
        root_dir,
        extension=('mid', 'MID', 'midi'),
        amount=None,
        str_=None,
        is_pure=False,
        verbose=False,
        is_sort=False,
        is_ext=True):

    if verbose:
        print('[*] Scanning...')
    file_list = []
    cnt = 0
    for root, _, files in os.walk(root_dir):
        for file in files:
            if file.endswith(extension):
                if (amount is not None) and (cnt == amount):
                    break
                if str_ is not None:
                    if str_ not in file:
                        continue
                mix_path = os.path.join(root, file)
                pure_path = mix_path[len(root_dir)+1:] if is_pure else mix_path
                if not is_ext:
                    ext = pure_path.split('.')[-1]
                    pure_path = pure_path[:-(len(ext)+1)]
                if verbose:
                    print(pure_path)
                file_list.append(pure_path)
                cnt += 1
    if verbose:
        print('Total: %d files' % len(file_list))
        print('Done!!!')
    if is_sort:
        file_list.sort()
    return file_list


def set_gobal_bpm(bpm):
    retval, proj, ptidx, timeposOut, measureposOut, beatposOut, bpmOut, timesig_numOut, timesig_denomOut, lineartempoOut = Reaper.RPR_GetTempoTimeSigMarker(0, -1, 0, 0, 0, 0, 0, 0, 0)
    Reaper.SetTempoTimeSigMarker(0, ptidx, timeposOut, measureposOut, beatposOut, bpm, timesig_numOut, timesig_denomOut, lineartempoOut)
    Reaper.UpdateArrange()
    Reaper.UpdateTimeline()


def clear_all():
    # delet items
    Reaper.Main_OnCommand(40035, 0)
    Reaper.Main_OnCommand(40006, 0)
    
    # got to start
    Reaper.CSurf_GoStart()


def move_cursor_start():
    Reaper.CSurf_GoStart()


def set_current_track(tidx):
    #Reaper.Main_OnCommand(40297, 0)     # unselected all track
    #Reaper.SetTrackSelected(Reaper.GetTrack(0, tidx), True)             # set selected track
    trackId = Reaper.GetTrack(0, tidx)
    Reaper.SetOnlyTrackSelected(trackId)


def set_track_media(path_track, tidx, is_press=False):
    Reaper.CSurf_GoStart()
    set_current_track(tidx)
    if is_press:
        t = threading.Thread(target=click_window)
        t.start()
    Reaper.InsertMedia(path_track, 0)

def select_all_region():
    start,end=0,0#self.get_region()
    Reaper.Main_OnCommand(40035, 0) #select all items
    itemsNum = Reaper.CountSelectedMediaItems(0)
    out=[]
    for i in range(itemsNum):
        item=Reaper.GetSelectedMediaItem(0, i)
        #rpr.RPR_IsMediaItemSelected(item)
        itemStart=Reaper.GetMediaItemInfo_Value(item,"D_POSITION")
        itemEnd=itemStart+Reaper.GetMediaItemInfo_Value(item,"D_LENGTH")
        if itemStart <start:
            start=max(0,itemStart)
        if itemEnd > end:
            end = itemEnd
    Reaper.GetSet_LoopTimeRange(True, 0, start, end, 0) #設定範圍
    #Reaper.Main_OnCommand(40289,0)
    #for item in out:
    #    Reaper.SetMediaItemSelected(item,True)
        
    return out

def render_media(
        path_media, 
        path_audio, 
        bpm=None, 
        is_press=False, 
        track_idx=0):
    '''
    function for rendering single track midi file or audio file
    the media will be inserted in the 1st track
    '''

    clear_all()
    move_cursor_start()

    # set bpm
    if bpm:
        set_gobal_bpm(int(bpm))
   
    # set media
    set_track_media(path_media, track_idx, is_press=is_press)
    
    # set audio filename
    filename = os.path.basename(path_audio)
    outdir = path_audio[:-len(filename)]
    print('filename:', filename)
    print('outdir:', outdir)
    Reaper.GetSetProjectInfo_String(0, "RENDER_FILE", outdir, True)
    Reaper.GetSetProjectInfo_String(0, "RENDER_PATTERN", filename, True)

    # save
    Reaper.Main_OnCommand(40296, 0) # select all
    Reaper.Main_OnCommand(41824, 0) # render project


def render_multi_media(
        mapping_dict, 
        path_audio,
        bpm=None, 
        is_press=None, 
        ):

    clear_all()
    move_cursor_start()

    # set bpm
    if bpm:
        set_gobal_bpm(int(bpm))

    # set media
    for idx, (track_idx, path_media) in enumerate(mapping_dict.items()):
        if isinstance(is_press, list):
            isp = is_press[idx]
        else:
            isp = is_press
        set_track_media(path_media, track_idx, is_press=is_press)

    # set audio filename
    filename = os.path.basename(path_audio)
    outdir = path_audio[:-len(filename)]
    print('filename:', filename)
    print('outdir:', outdir)
    Reaper.GetSetProjectInfo_String(0, "RENDER_FILE", outdir, True)
    Reaper.GetSetProjectInfo_String(0, "RENDER_PATTERN", filename, True)

    # save
    Reaper.Main_OnCommand(40296, 0) # select all
    select_all_region()
    Reaper.Main_OnCommand(41824, 0) # render project


if __name__ == '__main__':
    # test functions here
    pass
