load(
    "//tensorflow:tensorflow.bzl",
    "tf_cc_binary",
)

# boost::thread is used since std::thread has small size (512kB) stack on macOS.
# So include path and lib path options and necessary linker options were added.

tf_cc_binary(
  name = "AQ",
  srcs = glob(["*.cpp", "*.h"]),
  deps = [
    "//tensorflow/core:tensorflow",
  ],
  copts = ["-I/usr/local/include", "-O3", "-msse4.2"],
  linkopts = ["-L/usr/local/lib", "-lboost_thread-mt", "-lboost_chrono"]
)

tf_cc_binary(
  name = "AQ_dbg",
  srcs = glob(["*.cpp", "*.h"]),
  deps = [
    "//tensorflow/core:tensorflow",
  ],
  copts = ["-I/usr/local/include", "-msse4.2", "-g", "-fsanitize=address", "-fno-omit-frame-pointer"],
  linkopts = ["-L/usr/local/lib", "-fsanitize=address", "-lboost_thread-mt", "-lboost_chrono"]
)
