import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
import logging
import warnings
warnings.filterwarnings('ignore')
import tensorflow as tf
# tf.compat.v1.logging.set_verbosity(tf.compat.v1.logging.ERROR) # TF1
# tf.get_logger().setLevel(logging.ERROR) # TF2