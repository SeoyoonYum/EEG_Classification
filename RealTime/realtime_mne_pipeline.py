import mne
from mne_realtime import LSLClient

host = 'EmotivDataStream-EEG'
wait_max = 10

ch_names = ['AF3', 'F7', 'F3', 'FC5', 'T7', 'P7', 'O1','O2', 'P8', 'T8', 'FC6', 'F4', 'F8', 'AF4']
sfreq = 128  # Hz

# Create the MNE Info object
info = mne.create_info(ch_names=ch_names, sfreq=sfreq)

if __name__ == '__main__':
    
    with LSLClient(info=info, host=host, wait_max=wait_max, tmax = 0.5) as client:
        client_info = client.get_measurement_info()
        sfreq = int(client_info['sfreq'])

        # let's observe ten seconds of data
        i = 1
        while True:
            print(f'Got epoch {i}')
            plt.cla()
            epoch = client.get_data_as_epoch(n_samples=sfreq)
            epoch.average().plot(axes=ax)
            plt.pause(1.)
            i += 1
            if i == 10:
                break
        plt.draw()