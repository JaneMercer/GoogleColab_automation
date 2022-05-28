import imageio
from os import listdir, path
import ffmpy

images = []
DATA_PATH = r"D:\To_laptop\DATASET IMAGES\Graber"   #path to folders with data
DIRS = ["to_gif_temp"]

for dir in DIRS:
    w = imageio.get_writer('nsf.mp4', format='FFMPEG', mode='I', fps=1)
                       # output_params=['-vaapi_device',
                       #                '/dev/dri/renderD128',
                       #                '-vf',
                       #                'format=gray|nv12,hwupload'],
                       # pixelformat='vaapi_vld')

    DATA_PATH_FULL = DATA_PATH +'\\'+dir
    for filename in listdir(DATA_PATH_FULL):
        file_path = path.join(DATA_PATH_FULL, filename)
        if path.isdir(file_path):
            # skip directories
            continue
        else:
            # images.append(imageio.imread(DATA_PATH_FULL+"\\"+filename))
            w.append_data(imageio.imread(DATA_PATH_FULL+"\\"+filename))


w.close()
# gif_name = 'FPS1.gif'
# imageio.mimsave(gif_name, images, fps=1)
#
# ff = ffmpy.FFmpeg(
#     inputs={gif_name: None},
#     outputs={'output.mp4': None})
# ff.run()