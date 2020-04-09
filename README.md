# ReaRender

A python toolkit for automatic audio/MIDI rendering using REAPER

## Introduction
For musicians/audio programmers, using DAW (digital audio workstation) for music/audio processing is common nowadays. They can utilize abundant sound effects/plugins and customized settings to achieve their desired sound. 

For AI/ML researchers, especially in MIR/audio fields, they need programmable libraries to process data. However, the quality of accessible ones are usually far from satisfied, comparing to commerical plugins. For example: instrument synthesis (soundfont/fluidsynth v.s. professional-grade virtual instruments, VSTi), sound effects (Sox v.s. VST).

This toolkit brings an alternative solution: musician/audio engineers can customize their setting in DAW as usual, while AI/ML researchers can automate the rendering process to get their desired data. **The toolkit is based on [REAPER](https://www.reaper.fm/) - a DAW providing APIs in pyhton/lua/C++.**

We hope this toolkit can boost the development in related fields. For example, it can synthesize huge amount of data with high quality, which is beneficial for *transcription, source separation, automatic music composition, and etc.


## Requirements
* Python 3
* REAPER 5.X

## Usage
#### 1. Install *beyond_reaper*

To controll REAPER in python, you need to install **beyond_reaper**.
Please check out [here](beyond_reaper) for the instructions.

#### 2. Create Projects
The instructions [here](docs/project_setting.md) will show musicians and engineers how to setup their REAPER project.

#### 3. RUN!
We have two templates:
* single media - [synth_single_media.py](synth_single_media.py)
* multi media - [synth_multi_media.py](synth_multi_media.py)

Following the structure of the repo and place the media files into these corresponding folders. You can run the programs directly.


## License
TBD

---
## References
* [ReaScript API](https://www.reaper.fm/sdk/reascript/reascripthelp.html)

* [Reascript API Doc](https://www.extremraym.com/cloud/reascript-doc/#MIDI_GetNote)