import tensorflow as tf
from packaging import version


def importantText(text, color='red', underline=True):
    """ Function used to make print statements more legible """
    if color == 'green':
        colorANSI = 92
    if color == 'red':
        colorANSI = 91

    if underline:
        effectsANSI = '1;4;'
    else:
        effectsANSI = '1;'

    return f"\033[{effectsANSI}{colorANSI}m{text}\033[0m"


def checkTensorflowSetup(verbose):
    # Check to make sure you're running TensorFlow 2.0+
    assert version.parse(tf.__version__).release[0] >= 2, \
        "This notebook requires TensorFlow 2.0 or above."

    if verbose == 1:
        print(f'Tensorflow Version: {importantText(tf.__version__)}')
        print(f'Tensorflow Build: {importantText("GPU" if tf.test.is_built_with_cuda() else "CPU")}')

    if verbose == 2:
        # Use this to check if your GPU is actually utilized
        tf.debugging.set_log_device_placement(True)

    # To check if it can see and possibly utilize your gpu(s)
    gpu_lst = tf.config.experimental.list_physical_devices('GPU')

    print(importantText(
        "If you have nvidia gpu'(s) and CUDA configured you'll see them below:"))
    for gpu in gpu_lst:
        # Allocate memory on the fly instead of preallocating all your VRAM
        tf.config.experimental.set_memory_growth(gpu, True)
        print(f'GPU: {gpu.name}')
