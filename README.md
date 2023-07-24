
# EEG classification

Our first goal is to classify eeg of anomaly state and that of normal state, which is used when detecting motion from real-time raw eeg data.

After accomplishing the goal, we'll struggle to classify several finger motions such as pinch.


## Requirements

- Anaconda 23.5.2
- Tensorflow 2.13.0

## How to run

- Preprocess file preprocesses raw eeg file of edf format and saves as epoch file in fif format.
- Classify file imports the epoch fif file, fits ml model, and predicts.
- EEGModels python file is providing module of CNN based DL model.
- Dl_EEGnet file is dealing with EEGnet model included in EEGModels module.

## Acknowledgements

 - [EEGnet](https://github.com/vlawhern/arl-eegmodels)
 - [Papers](https://drive.google.com/drive/folders/1RE3_frkz09Xc-2zQDOZU8EFi6Sy5XsV4?usp=sharing)


## Contributing

 - Please add a new branch named the contributor's name. (e.g. minjoo)

 - Please add a new file containing all of your contributions in order to avoid confusion.

  - Feel free to contribute. We are waiting for your efforts.


## Authors

- [@dreamingpens](https://www.github.com/dreamingpens)



- [@Minjoo Kim](https://github.com/minjoo0729)
