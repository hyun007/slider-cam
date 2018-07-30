import logging
import os
import subprocess
import sys

import gphoto2 as gp

class CameraControl:
    def __init__(self):
        self.context = gp.Context()
        self.camera = gp.Camera()
        self.camera.init(self.context)
    
    def info(self):
        text = self.camera.get_summary(self.context)
        print('Summary')
        print('=======')
        print(str(text))
        self.camera.exit(self.context)

    def capture(self):
        print('Capturing image')
        file_path = self.camera.trigger_capture(self.context)
        print('Camera file path: {0}/{1}'.format(file_path.folder, file_path.name))
        target = os.path.join('/tmp', file_path.name)
        print('Copying image to', target)
        camera_file = self.camera.file_get(self.context, file_path.folder, file_path.name, gp.GP_FILE_TYPE_NORMAL)
        self.camera.exit(self.context)

