
import cv2
import easyocr

reader = None

def get_reader():
    global reader

    if reader is None:
        reader = easyocr.Reader(['en'])

    return reader


def extract_text_from_video(video_path):

    ocr_reader = get_reader()

    cap = cv2.VideoCapture(video_path)

    extracted_text = ""

    frame_count = 0

    while cap.isOpened():

        success, frame = cap.read()

        if not success:
            break

        # Process every 60th frame
        if frame_count % 60 == 0:

            results = ocr_reader.readtext(frame)

            for result in results:

                extracted_text += result[1] + " "

        frame_count += 1

    cap.release()

    return extracted_text
