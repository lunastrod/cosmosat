from time import time, sleep

from picamera import PiCamera
from file_logger import log_flight_info, log_downlink_msg
from moteino import moteino_write

## time constants
time_counter_image = 0
TIME_STEP_IMAGE= 5

time_counter_video = 0
TIME_STEP_VIDEO = 5
VIDEO_DURATION = 0.1

## other constants
image_counter = 0
video_counter = 0

IMAGE_RESOLUTION_H = 1280
IMAGE_RESOLUTION_V = 720

IMAGE_LK = "imagen"
VIDEO_LK = "video"

DOWNLINK_SEPARATING_CHAR = '-'

## camera setup
camera = PiCamera()
camera.resolution = (IMAGE_RESOLUTION_H, IMAGE_RESOLUTION_V)


def take_caption(t0: float):

    
    global time_counter_image, TIME_STEP_IMAGE, image_counter

    file_name = "images/img_" + str(image_counter) + ".jpg"

    try:
        camera.capture(file_name)

        log_image(t0)

        time_counter_image += TIME_STEP_IMAGE

        image_counter += 1

    except:
        print("fail photo")
        return "$"


def take_video(t0: float):

    
    global time_counter_video, TIME_STEP_VIDEO, video_counter
    
    t = time() - t0

    if (t > time_counter_video):

        file_name = "videos/video_" + str(video_counter) + ".h264"

        try:
            camera.start_recording(file_name)
            camera.wait_recording(VIDEO_DURATION)
            camera.stop_recording()

            log_video(t0)

            time_counter_video+= TIME_STEP_VIDEO

            video_counter += 1

        except:
            print("fail video")
            return "$"

def log_image(t0: float):
    
    t = time() - t0
    
    if (t > time_counter_image):

        info_arr = [IMAGE_LK, "caption", t]

        log_flight_info(info_arr)
        log_downlink_msg(info_arr)

        comando = DOWNLINK_SEPARATING_CHAR.join([str(n) for n in info_arr])
        moteino_write(comando)
        print(comando)


def log_video(t0: float):
    
    info_arr = [VIDEO_LK, "video", t]

   # log_flight_info()
    #log_downlink_msg(info_arr)

    comando = DOWNLINK_SEPARATING_CHAR.join([str(n) for n in info_arr])
    moteino_write(comando)
    print(comando)
