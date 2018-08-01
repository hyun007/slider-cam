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
        self.set_capture_target(1)

    def set_capture_target(self, value):
        config = gp.check_result(gp.gp_camera_get_config(self.camera))
        capture_target = gp.check_result(
                        gp.gp_widget_get_child_by_name(config, 'capturetarget'))
        count = gp.check_result(gp.gp_widget_count_choices(capture_target))
        if value < 0 or value >= count:
            print('Parameter out of range')
            value = 1
        value = gp.check_result(gp.gp_widget_get_choice(capture_target, value))
        gp.check_result(gp.gp_widget_set_value(capture_target, value))
        gp.check_result(gp.gp_camera_set_config(self.camera, config))
        gp.check_result(gp.gp_camera_exit(self.camera))
    
    def info(self):
        text = self.camera.get_summary(self.context)
        print('Summary')
        print('=======')
        print(str(text))
        self.camera.exit(self.context)

    def capture(self):
        #logging.basicConfig(format='%(levelname)s: %(name)s: %(message)s', level=logging.WARNING)
        #gp.check_result(gp.use_python_logging())

        print('Capturing image')
        self.camera.trigger_capture(self.context)
        #file_path = gp.check_result(self.camera.capture(gp.GP_CAPTURE_IMAGE))

        #print('Camera file path: {0}/{1}'.format(file_path.folder, file_path.name))
        #target = os.path.join('/tmp', file_path.name)
        #print('Copying image to', target)
        #camera_file = self.camera.file_get(self.context, file_path.folder, file_path.name, gp.GP_FILE_TYPE_NORMAL)
        self.camera.exit(self.context)

