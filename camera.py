from picamera import PiCamera


camera = PiCamera()
camera.resolution = (1280, 720)

image_counter = 0
video_counter = 0


def take_caption():

    file_name = "images/img_" + str(image_counter) + ".jpg"

    camera.capture(file_name)

    image_counter += 1


def take_video(duration: float):

    file_name = "videos/video_" + str(video_counter) + ".h264"

    camera.start_recording(file_name)
    camera.wait_recording(duration)
    camera.stop_recording()

    video_counter += 1