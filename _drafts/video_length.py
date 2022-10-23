import glob
import subprocess
from datetime import timedelta, datetime

lengths = []
LOCATION = "/Users/seungwonjeong/Desktop/sparta/Week1"  # '영상이 들어있는 폴더 경로'
EXTENSION = "mp4"  # 확장자

def get_length(filename):
    ffmpeg = subprocess.Popen(
        ['ffmpeg', '-i', filename],
        stderr=subprocess.PIPE
    )
    grep = subprocess.Popen(
        ['grep', 'Duration'],
        stdin=ffmpeg.stderr,
        stdout=subprocess.PIPE
    )
    awk = subprocess.Popen(
        ['awk', "{print $2}"],
        stdin=grep.stdout,
        stdout=subprocess.PIPE
    )
    trim = subprocess.Popen(
        ['tr', '-d', ','],
        stdin=awk.stdout,
        stdout=subprocess.PIPE
    )
    for line in trim.stdout:
        # 딱 첫 번째 줄만 출력.
        return line.decode('utf-8')

# root_dir needs a trailing slash (i.e. /root/dir/)
for filename in glob.iglob(LOCATION + f'**/*.{EXTENSION}', recursive=True):
     lengths.append(get_length(filename))


# 시간 parse
deltas = []
for elem in lengths:
    datetime = datetime.strptime(elem[:-4], '%H:%M:%S')
    delta = timedelta(hours=datetime.hour, minutes=datetime.minute, seconds=datetime.second)
    deltas.append(delta)

# sum
print(sum(deltas, timedelta(0)))