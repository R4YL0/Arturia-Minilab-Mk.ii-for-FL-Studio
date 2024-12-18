# Arturia-Minilab-Mk.ii-for-FL-Studio
This is a Python script I wrote in 2020 to simplify my interaction with FL Studio by using the Arturia Minilab Mk.ii Midi-Keyboard. This was before the official script was released, which you could also find [here](https://forum.image-line.com/viewtopic.php?t=262947). However, its workflow isn't like mine, so you might still want to try this script :)

It supports: Volume and Panning Faders (Mixer/Instrument), Interaction with the UI (Browser, Mixer, Playlist, Channels)
## Setup
For this script to work within FL Studio, you need to put the *MinilabMkII* folder into your **\Documents\Image-Line\FL Studio\Settings\Hardware** directory (not sure about MacOS). Furthermore, you have to go into the MIDI Control Center, select your **Minilab MkII** and import the *MCC-Script.minilabmk2* file. After that, you can store it onto any of the Memory slots and access it from the keyboard by holding shift and press the apropriately numbered pad. You'll notice that it worked if the Pads now have different colors instead of only Red.
On FL Studio, go to the MIDI Settings, choose your Minilab Mk.ii as an input device, and set the controller type to *Minilab MK2*.
## How it works
- Mixer Knobs (1-4, 9-12)
  - 1: Vol & 9: Pan for selected Channel
  - 2: Vol & 10: Pan for Channel one to the right
  - 3: Vol & 11: Pan for Channel two to the right
  - 4: Vol & 12: Pan for Channel three to the right
- Channel Knobs (13, 14)
  - 13: Pan & 14: Vol for selected Channel
- Navigation Knobs (Shift 1, Shift 9, 15, 16)
