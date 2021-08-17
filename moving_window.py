import numpy as np
import glob
from pydub import AudioSegment
import matplotlib.pyplot as plt
import pygal

#
mysp=__import__("my-voice-analysis")

label_list = []
silence_duration_list = []
sound_duration_list = []

tlt_syllables =0
tlt_duration = 0

s_t_list = []
e_t_list = []


## Prceprocess all the audio segs by adding 3 sec pause to each segment
file_count = 0
for fname in glob.glob("audio segs" + '/*.wav'):
    # print(fname.split('\\')[1])
    audio_in_file = fname
    audio_out_file = "audio segs extended/" + fname.split('\\')[1]
    one_sec_segment = AudioSegment.silent(duration=3000)  # duration in milliseconds
    # read wav file to an audio segment
    song = AudioSegment.from_wav(audio_in_file)
    # Add above two audio segments
    final_song = one_sec_segment + song
    final_song.export(audio_out_file, format="wav")
    file_count += 1

###### Calculate the number of syllables  for each audio segments
sylb_list = []
last_sylb_rate = 0

tlt_sylb = 0

print(file_count)
for i in range(file_count):
    p = str(i+1)+"Label"  # Audio File title
    c = r"C:\Users\Owner\Desktop\Online video player\video player design\pause_insertion\audio segs extended"  # Path to the Audio_File directory (Python 3.7)
    num_sylb = mysp.myspsyl(p, c)
    audio_dur = mysp.myspst(p, c)
    if audio_dur!=0:
        # sylb_rate = num_sylb / audio_dur
        sylb_list.append(num_sylb)
        print(str(i + 1) + ".wav : " + str(num_sylb) + " sylbs")
        tlt_sylb+=num_sylb
    else:
        # sylb_rate_list.append(last_sylb_rate)
        num_sylb=0
        sylb_list.append(0)
        print(str(i+1)+".wav" + "file not clear. Set syllable to 0")


print("total sylb: ",tlt_sylb)
print("sylb list: ",sylb_list)


##### Visualize the sylb rate
avg_sylb_rate = np.average(sylb_list)
vid_length = 120+30
plt.xlim(0, vid_length)
plt.ylim(0, 8)


plt.plot(np.linspace(0,120,len(sylb_list)),sylb_list,color = 'blue',linewidth = 1)

plt.plot([0,vid_length],[avg_sylb_rate,avg_sylb_rate],'--',color = 'red',linewidth = 1,label = 'Average syllable rate')
plt.xlabel('Video time (sec)', fontsize=18)
plt.ylabel('Syllable (# of syllables)', fontsize=16)
plt.savefig("syllable vs time.svg", dpi=200)
plt.legend()
plt.show()
