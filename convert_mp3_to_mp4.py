from moviepy.editor import *
import uuid


def mp4_to_mp3(mp4_filename, mp3_filename):
    file_to_convert = AudioFileClip(mp4_filename)
    file_to_convert.write_audiofile(mp3_filename)
    file_to_convert.close()


if __name__ == "__main__":
    mp4_filename = "./entrevista.mp4"
    mp3_filename = '{filename}.mp3'.format(filename=uuid.uuid4().hex)
    mp4_to_mp3(mp4_filename, mp3_filename)
