# Speech-to-Text
Using the DeepSpeech library by Mozilla, this is a speech-to-text engine. Provided with an audio file as input this will output a transcript in the form of a text file and a json file which includes the words, the time in seconds at which the word was detected in the audio file, and a confidence metric. This program will also output a log which contains only the time it took to run each audio file and the confidence metric.

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

## Feedback
Let me know if this is working well and anything suggestions if you think some functionality should be added and I will look into it. After testing out the engine, the `stt.log` file will have aggregated some log data based on your interactions with it. It will only contain the time it took to run, a confidence metric, and possible debug/error messages. I can take that log file and observe that to ensure that it is running smoothly.
