import subprocess, signal, time, os, re
from multiprocessing import Process
from threading import Timer

def download_livestream(url, duration):
    # use yt-dlp to download video 
    # use whereis ffmpeg/yt-dlp to find ffmpeg/yt-dlp path
    subproc = subprocess.Popen(["/home/yash/miniconda3/envs/pedestrian-detection/bin/yt-dlp",'--no-part','-q','--progress','--ffmpeg-location','/home/yash/miniconda3/envs/pedestrian-detection/bin/ffmpeg',"-o","./data/video/raw-mp4/QuadCam.%(ext)s", url])
    print("Process started!")

    # Download for 10 seconds
    time.sleep(duration)
    # Stop downloading
    subproc.terminate()
    print("We are waiting!\n")
    subproc.wait()

def extract_number(f):
    s = re.findall("(\d+).png", f)
    return (int(s[0]) if s else -1, f)

def extract_frames_from_video(video_path, output_dir):
    if len(os.listdir(output_dir)) == 0:
        print("empty!")
        start_number = 1
    else:
        print("Not empty!")
        # Getting the last number in the directory so that ffmpeg doesn't restart at 1
        files = [os.path.join(output_dir, f) for f in os.listdir(output_dir)]
        start_number = int(max(files, key=extract_number)[20:-4]) + 1
    # Adding the .png file-extension
    output_dir += "%04d.png"
    subprocess.run(['/home/yash/miniconda3/envs/pedestrian-detection/bin/ffmpeg', '-i', video_path, '-start_number', str(start_number),'-vf','fps=1/60',output_dir])

def delete_video(video_path):
    # Delete the downloaded video file
    os.remove(video_path)


# Example usage
youtube_url = 'https://www.youtube.com/watch?v=DbH7LGdUxJI'  # Replace with the actual YouTube livestream URL
duration = 20  # 10 seconds

# Now, we are downloading the livestream for 20 seconds, stopping, extracting the frames as images, deleting the original video, and then restrating the whole process again 
while True:
    download_livestream(youtube_url, duration)
    extract_frames_from_video('./data/video/raw-mp4/QuadCam.mp4', './data/video/frames/')
    delete_video('./data/video/raw-mp4/QuadCam.mp4')
