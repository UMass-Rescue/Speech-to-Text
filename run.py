import sys, os, time, logging, json
from pydub import AudioSegment

def mp3_to_wav(source):
	destination = "tmp.wav"
	# convert mp3 to wav
	sound = AudioSegment.from_mp3(source)
	sound.export(destination, format="wav")
	return destination

logging.basicConfig(filename='stt.log', level=logging.INFO)
program_name = sys.argv[0]
arguments = sys.argv[1:]
file_path = ""
file_name = ""

for i in range(len(arguments)):
	start_time = time.time()
	file_path = arguments[i]
	file_name = os.path.basename(file_path)
	name_ext = os.path.splitext(file_name)
	transcript = "{}_transcript".format(name_ext[0])
	if name_ext[1] == ".mp3":
		wav_tmp = mp3_to_wav(file_path)
	txt = "deepspeech --model deepspeech-0.6.1-models/output_graph.pbmm --lm deepspeech-0.6.1-models/lm.binary --trie deepspeech-0.6.1-models/trie --audio {} > {}.txt".format(wav_tmp, transcript)
	js = "deepspeech --json --model deepspeech-0.6.1-models/output_graph.pbmm --lm deepspeech-0.6.1-models/lm.binary --trie deepspeech-0.6.1-models/trie --audio {} > {}.json".format(wav_tmp, transcript)
	#print(os.system(json))
	os.system(js)

	with open('ninja_transcript.json', 'r') as f:
		trans = json.load(f)

	script = ""
	for word in trans["words"]:
		script = script + word["word"] + " "

	with open('ninja_transcript.txt', 'w') as f:
		f.write(script)

	elapsed_time = time.time() - start_time
	logging.info('Confidence: {}'.format(trans["confidence"]))
	logging.info('Elapsed Time: {:0.2f} seconds'.format(elapsed_time))
	

