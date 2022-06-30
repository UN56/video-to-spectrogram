this is a modified project from the original [ARSS](https://github.com/derselbst/ARSS).
# Video To Spectrogram     
printing frame by frame image on Spectrogram  

some result:  

https://user-images.githubusercontent.com/73573076/176667342-3c2de0ac-8cbf-40aa-a87c-87b0bcb04f54.mp4

To:

https://user-images.githubusercontent.com/73573076/176666302-4c8bac08-e515-4c77-849c-fb95c3ba1bc4.mp4

And The [unedited ver](https://youtu.be/17uUXlxOa-M)

## Usage

Copy Repo  
`git clone https://github.com/UN56/video-to-spectrogram.git`  

install library  
`pip install -r requirements.txt`

run  
`python videoToFrames.py` (make sure the video name is `sample.mp4`)

make sure to change the `frames` variable in `bmpToAudio.py` to how many frames you have in the `/frames` folder

run  
`python bmpToAudio.py`

note down the sound duration for the part 2

![sample](https://user-images.githubusercontent.com/73573076/176692580-71576d61-da1d-442e-ad34-f693fb6c5c91.jpg)

change the `audioNum` variable in `joinAudio.py` to how many audio files you have and add 1 (example 10 files, put 11)  

run  
`python joinAudio.py`

And you have the audio file in the `audioOutput` folder, yayy

## Usage Part 2 (optional)

use WSL

for the live spectrogram, I'm recommend using [friture](https://friture.org/)  

now record [friture](https://friture.org/) with your favorite recorder, and cut the video in the first frame

(example)
<img width="487" alt="firstFrame" src="https://user-images.githubusercontent.com/73573076/176692659-d3dae3b7-b1d2-4faf-9692-029aec5bd43b.png">

add 0.4843310657596372 to the sound duration 

and run  
(check `bash.txt`)

change `num_frames` variable in the `merge.py` to the frame you have in the `videoFrames` folder and add 1

run  
`python merge.py`

and the result is the `output.mp4` file.
