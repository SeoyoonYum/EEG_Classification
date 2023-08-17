"""Example program to show how to read a multi-channel time series from LSL."""

from pylsl import StreamInlet, resolve_stream

# first resolve an EEG stream on the lab network
print("looking for an EEG stream...")
streams = resolve_stream('type', 'EEG')

# create a new inlet to read from the stream
inlet = StreamInlet(streams[0])


list = []
while True:
    for i in range(16):
        # get a new sample (you can also omit the timestamp part if you're not
        # interested in it)
        #for i in range(64)
        sample, timestamp = inlet.pull_sample()
        list.append(sample)
        #chunk += sample
        #print(chunk)
        #chunk = []
    print(len(list))
    list = []