import tensorflow as tf

for basename in ['sl_0', 'vl_0']:
    with tf.Graph().as_default():
      with open(basename + '.pb', 'rb') as f:
        graph_def = tf.GraphDef()
        graph_def.ParseFromString(f.read())
        for node in graph_def.node:
            node.device = ""
        tf.import_graph_def(graph_def, name="")
        tf.train.write_graph(graph_def, './', basename + '_nodev.pb', as_text=False)
