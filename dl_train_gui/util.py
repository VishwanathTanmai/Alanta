from enum import Enum
from dl_train_gui import __version__ as version
from dl_train_gui.demo import DemoProgram

def get_version():
    return version

def create_default_program():
    return DemoProgram()

class Mode(Enum):
    NONE = 'none'
    ORIGINAL = 'original'
    SCALE_BY_HEIGHT = 'height'
    SCALE_BY_WIDTH = 'width'
    RESIZE = 'resize'

def get_company_logo():
    name = 'Alanta'
    path = './web/img/logo.jpeg'
    copyright = '&#169; 2024-25 Alanta'
    display_mode = Mode.NONE.value
    height = 24
    width = 80
    return [name, path, display_mode, height, width, copyright]