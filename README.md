# Speech-to-Text
Using the DeepSpeech library by Mozilla, this is a speech-to-text engine. Provided with an audio file as input this will output a transcript in the form of a text file and a json file which includes the words, the time in seconds at which each word was detected in the audio file, and a confidence metric. This program will also output a log which contains only the time it took to run each audio file and the confidence metric.

## Dependencies
`requirements.txt` contains all Python modules that this depends on, however, a models folder is still required containing pretrained model files that this engine will use.

Here are explicit instructions for installing a Python environment with the required dependencies in the `requirements.txt` folder. After cloning the repository, execute the following commands inside the project folder:

```shell
# Create and activate a virtualenv
virtualenv -p python3 deepspeech-venv
source deepspeech-venv/bin/activate

# Install requirements
pip install -r requirements.txt
```

Here is an example of the directory and file structure after the dependencies are installed and the models folder is downloaded and placed in the root directory of the project folder:
```
Speech-to-Text
│   README.md
│   requirements.txt
│   run.py
│
└───deepspeech-venv
│   │   bin
│   │   include
│   │   lib
│   
└───deepspeech-0.6.1-models
│   │   lm.binary
│   │   output_graph.pb
│   │   output_graph.pbmm
│   │   output_graph.tflite
│   │   trie
```
### Model Folder
I have compressed and uploaded a pretrained model to Google Drive, which should be extracted to the project folder. Below is the link:

https://drive.google.com/file/d/1R7uvOnLpESrep807VAilQ-ix5QTjOMjq/view?usp=sharing

## Usage
A simple interface was created with run.py. Run this script with all file locations as arguments following `run.py`. Any audio files of type mp3 or wav are supported and any number of audio files may be included as arguments.

### Example
```shell
python run.py audio.mp3 audio2.mp3 audio3.mp3
```

## Benchmarks
I have found a benchmark that many of the state-of-the-art automatic speech recognition engines were tested on. This was created by Picovoice (http://picovoice.ai). This benchmark considers three metrics: word error rate, real-time factor, and model size. The dataset used is the LibriSpeech ASR corpus (https://www.openslr.org/12/).

Several models were tested that are considered to be some of the highest performing ASR engines: Amazon Transcribe, CMU PocketSphinx, Google Speech-to-Text, our Mozilla DeepSpeech, Picovoice Cheetah, Picovoice Cheetah LibriSpeech LM, Picovoice Leopard, Picovoice Leopard LibriSpeech LM.

The results were promising. The engine we are using performed better than all other speech-to-text engines except for Picovoice Leopard LibriSpeech LM, whch had a slightly lower word error rate (6.58%), faster runtime, and much smaller model size. However, like all of these other engines, Picovoice's speech-to-text software is proprietary, while DeepSpeech is open source. I have included a table below that compares all of these engines using data from Picovoice's speech-to-text benchmark.

| Engine | WER | RTF (Desktop) | RTF (Raspberry Pi 3) | RTF (Raspberry Pi Zero) | Model Size (Acoustic and Language) |
:---:|:---:|:---:|:---:|:---:|:---:
Amazon Transcribe | 8.21% | N/A | N/A | N/A | N/A |
CMU PocketSphinx (0.1.15) | 31.82% | 0.32 | 1.87 | 2.04 | 97.8 MB |
Google Speech-to-Text | 12.23% | N/A | N/A | N/A | N/A |
**Mozilla DeepSpeech (0.6.1)** | 7.55% | 0.46  | N/A | N/A | 1146.8 MB |
Picovoice Cheetah (v1.2.0) | 10.49% | 0.04 | 0.62 | 3.11 | 47.9 MB |
Picovoice Cheetah LibriSpeech LM (v1.2.0) | 8.25% | 0.04 | 0.62 | 3.11 | 45.0 MB |
Picovoice Leopard (v1.0.0) | 8.34% | 0.02 | 0.55 | 2.55 | 47.9 MB |
Picovoice Leopard LibriSpeech LM (v1.0.0) | 6.58% | 0.02 | 0.55 | 2.55 | 45.0 MB |


## Feedback
Let me know if this is working well and anything suggestions if you think some functionality should be added and I will look into it. After testing out the engine, the `stt.log` file will have aggregated some log data based on your interactions with it. It will only contain the time it took to run, a confidence metric, and possible debug/error messages. I can take that log file and observe that to ensure that it is running smoothly.
