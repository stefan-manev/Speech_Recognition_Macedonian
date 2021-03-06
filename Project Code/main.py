"""
Main execution file

Copyright 2020 by Blagoj Hristov

See the LICENSE file for the licensing associated with this software.

Author:
  Blagoj Hristov, March 2020

"""

import os
import sys
import numpy as np
from matplotlib import pyplot as plt
import seaborn as sns
import h5py
import librosa as lb
from feature_extraction.spectral import generate_mfcc, generate_spectrogram
from refactoring.transcript import refactor_all, index_transcript, format_transcript
from refactoring.files import rename_files
from preprocessing.audio import resample_audio
from utils.utils import load_mfcc_batch, plot_mfcc, plot_spectrogram, load_spectrogram_batch, plot_all


if __name__ == '__main__':

    data_path = 'F:\\Speech_Recognition_Macedonian\\Database\\train'
    rate = 16000
    coeff = 13

    # rename_files(path=data_path, verbose=True)

    # resample_audio(path=data_path, sampling_rate=rate, verbose=True)

    # refactor_all(path=data_path)

    # generate_mfcc(path=data_path, sampling_rate=rate, num_coeff=coeff, verbose=True)

    # generate_spectrogram(path=data_path, sampling_rate=rate, verbose=True)

    audio, _ = lb.load(data_path + os.sep + '8' + os.sep + '000000' + os.sep + '8-000000-0000.wav', sr=rate)

    batch_mfcc = load_mfcc_batch(path=data_path + os.sep + '8' + os.sep + '000000')

    batch_spec = load_spectrogram_batch(path=data_path + os.sep + '8' + os.sep + '000000')

    mfcc_data = batch_mfcc[:, :, 0]
    spectrogram_data = batch_spec[:, :, 0]

    plot_all(audio_signal=audio, spectrogram_data=spectrogram_data, mfcc_data=mfcc_data, sampling_rate=rate)
