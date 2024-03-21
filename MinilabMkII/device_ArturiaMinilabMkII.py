#name=Arturia Minilab Mk II ver.1
# Code written by: Khaled Kottmann

import playlist
import mixer
import midi
import ui
import device
import channels
import patterns
import transport
import general
import constants

class MidiControllerConfig():
    def OnMidiMsg(self, event):
        #p = channels.channelCount()
        #event
        #event.handled = True
        #if event.handled:
         #   print(event.handled, event.timestamp, event.status, event.data1, event.data2, event.port, event.sysex, event.midiChan, event.midiId)
    #Knobs
        if event.status == 185:
        #Mixer
            #Tracks werden markiert
            if mixer.isTrackSelected(constants.x) == 0:
                for i in range(0,122):
                    if mixer.isTrackSelected(i) != 0:
                        constants.x = i
                        break
            #Changing Tracks in Mixer
            #if event.data1 == 120:                
             #   ui.showWindow(midi.widMixer)
              #  if event.data2 < 64 and constants.x > 0:
               #     constants.x = constants.x - 1
                #if event.data2 > 64 and constants.x < 122:
                 #   constants.x = constants.x + 1
            #    mixer.selectTrack(constants.x)
             #   mixer.getTrackPluginId(constants.x,1)
              #  for i in range(0,126):
               #     if i != constants.x:
                #        if mixer.isTrackSelected(i) != 0:
                 #           mixer.selectTrack(i)
            if event.data1 == 120:                
                ui.setFocused(midi.widMixer)
                if event.data2 < 64 and constants.x > 0:
                    ui.previous()
                if event.data2 > 64 and constants.x < 122:
                    ui.next()

            #TrackVolume
            if event.data1 == 117:
                #ui.showWindow(midi.widMixer)
                #ui.setFocused(midi.widMixer)
                if event.data2 < 64:
                    mixer.setTrackVolume(constants.x,mixer.getTrackVolume(constants.x) - 0.01)
                if event.data2 > 64:
                    mixer.setTrackVolume(constants.x,mixer.getTrackVolume(constants.x) + 0.01)
            #TrackPanning
            if event.data1 == 106:
                #ui.showWindow(midi.widMixer)
                #ui.setFocused(midi.widMixer)
                if event.data2 < 64:
                    mixer.setTrackPan(constants.x, mixer.getTrackPan(constants.x) - 0.01)
                if event.data2 > 64:
                    mixer.setTrackPan(constants.x, mixer.getTrackPan(constants.x) + 0.01)
            
        #Chanell Rack
            #Channel wird markiert
            if channels.isChannelSelected(constants.s-1) == 0:
                for i in range(0,channels.channelCount()):
                    if channels.isChannelSelected(i) != 0:
                        constants.s = i + 1
                        break
            #Channel wird selected
            if event.data1 == 119:
                #ui.showWindow(midi.widChannelRack)
                ui.setFocused(midi.widChannelRack)
                for i in range(1, channels.selectedChannel()):
                    if channels.isChannelSelected(i) != 0:
                        constants.s = i
                if event.data2 < 64:
                    if constants.s > 1:
                        constants.s = constants.s - 1
                if event.data2 > 64:
                    if channels.channelCount() > constants.s:
                        constants.s = constants.s + 1
                channels.selectChannel(constants.s - 1)
                for i in range(0,channels.channelCount()):
                    if i != constants.s - 1:
                        if channels.isChannelSelected(i) != 0:
                            channels.selectChannel(i)
            if event.data1 == 89 & event.data2 > 0:
                channels.showEditor(constants.s - 1)
            
            #Grids in Channnel Rack
            if event.data1 == 87:
                k = channels.getChannelPan(constants.s - 1)
                if event.data2 < 64:
                    channels.setChannelPan(constants.s-1, k - 0.01)
                if event.data2 > 64:
                    channels.setChannelPan(constants.s-1, k + 0.01)
            if event.data1 == 88:
                j = channels.getChannelVolume(constants.s - 1)
                if event.data2 < 64:
                    channels.setChannelVolume(constants.s-1, j - 0.01)
                if event.data2 > 64:
                    channels.setChannelVolume(constants.s-1, j + 0.01)
        #Patterns
            #Channel wird markiert
            
            if patterns.isPatternSelected(constants.p) == 0:
                for i in range(0,patterns.patternCount()+1):
                    if patterns.isPatternSelected(i) != 0:
                        constants.p = i
                        break
            if event.data1 == 121:
                ui.setFocused(midi.widPlaylist)
                if event.data2 < 64:
                    if constants.p > 1:
                        patterns.jumpToPattern(constants.p-1)
                        constants.p = constants.p-1
                if event.data2 > 64:
                    if patterns.patternCount() > constants.p:
                        patterns.jumpToPattern(constants.p+1)
                        constants.p = constants.p+1
                        constants.a = patterns.patternCount()
                    if constants.a == constants.p:
                        patterns.findFirstNextEmptyPat(midi.FFNEP_DontPromptName)
                        constants.p = constants.p+1
            
        #Ui
            if event.data1 == 122:
                if event.data2 < 64 and event.data2 > 58:
                    ui.setFocused(midi.widBrowser)
                    ui.previous()
                elif event.data2 < 64:
                    ui.previous()
                if event.data2 > 64 and event.data2 < 70:
                    ui.setFocused(midi.widBrowser)
                    ui.next()
                elif event.data2 > 64:
                    ui.next()
            if event.data1 == 90 and event.data2 > 0:
                ui.enter()
                    
        #Metronom und andere buttons
            if event.data1 == 20 and event.data2 > 0:
                transport.globalTransport(midi.FPT_Metronome, 110)
            if event.data1 == 21 and event.data2 > 0:
                transport.globalTransport(midi.FPT_Overdub, 112)
            if event.data1 == 22 and event.data2 > 0:
                transport.globalTransport(midi.FPT_LoopRecord, 113)
    #Knob 15 % Knob 16
        #Channel Pan & Volume
            #if ui.getFocused(midi.widChannelRack) == 1:
            if event.data1 == 107:
                if event.data2 < 64:
                    channels.setChannelPan(constants.s-1, channels.getChannelPan(constants.s-1) - 0.01)
                if event.data2 > 64:
                    channels.setChannelPan(constants.s-1, channels.getChannelPan(constants.s-1) + 0.01)
            if event.data1 == 118:
                if event.data2 < 64:
                    channels.setChannelVolume(constants.s-1, channels.getChannelVolume(constants.s-1) - 0.01)
                if event.data2 > 64:
                    channels.setChannelVolume(constants.s-1, channels.getChannelVolume(constants.s-1) + 0.01)
        #Mixer
            #elif ui.getFocused(midi.widPlaylist) == 1:
             #   if event.data1 == 119:
              #      if event.data2 < 64:
               #         ui.jog(-1)
                #    if event.data2 > 64:
                 #       ui.jog(1)
                #if event.data1 == 120:
                 #   if event.data2 < 64:
                  #      ui.up()
                   # if event.data2 > 64:
                    #    ui.down()
                        
        #Piano Roll
            #elif ui.getFocused(midi.widMixer) == 1:
             #   if event.data1 == 120:
              #      if event.data2 < 64:
               #         transport.globalTransport(midi.FPT_MixerWindowJog,-1)
                #    if event.data2 > 64:
                 #       transport.globalTransport(midi.FPT_MixerWindowJog,1)
    #Mixer
        
            
    #Grids in Channnel Rack
        #if event.status == 153:
         #   channels.setGridBit(constants.s-1, event.data1, 1)
        #if event.status == 137:
         #   channels.setGridBit(constants.s-1, event.data1, 0)

# New Instance
Minilab = MidiControllerConfig()


def OnMidiMsg(event):
    Minilab.OnMidiMsg(event)