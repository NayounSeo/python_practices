import tensorflow as tf
# to turn down 'for unknown op' log
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'

def main():
  hello = tf.constant("HELLO, TensorFlow! I did really want to meet you")
  sess = tf.Session()
  print(sess.run(hello))


if __name__ == "__main__":
  main()
