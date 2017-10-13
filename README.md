# CPU version of AQ on macOS

AQ is a program of Go game with level of expert players.  
[CGOS](http://www.yss-aya.com/cgos/19x19/standings.html) rating: 3674 (standings)  

This is a porting version of AQ for macOS without NVIDIA GPU.

## Requirement
- OS: macOS  
- CPU: CPU with SSE 4.2  
- Library: boost

## Usage

### AQ configuration
Set hardware and time control etc. in 'aq_config.txt.'  

## Build from source code.
```shell
brew install boost
git clone https://github.com/yich/AQ.git
# Below <AQ> means the directory of the local AQ repository
git clone --recursive https://github.com/tensorflow/tensorflow.git
# Below <tensorflow> means the directory of the local tensorflow repository
cd <tensorflow>
ln -s <AQ>/src tensorflow/cc/AQ
bazel build -c opt --copt=-mavx //tensorflow/cc/AQ:AQ
```

## How to run
```
cd <AQ>
mkdir bin
cd bin
mkdir log
ln -s <tensorflow>/bazel-bin/tensorflow/cc/AQ/AQ .
cp ../aq_config.txt .
cp ../prob/*.txt .
ln -s ../pb .
./AQ
```

## License
[MIT](https://github.com/ymgaq/AQ/blob/master/LICENSE.txt)

## Author
[Yu Yamaguchi](https://twitter.com/ymg_aq)

## Porting Information
ported for macOS by [ICHIKAWA, Yuji](https://twitter.com/y_ich).

* sl_0.pb and vl_0.pb was changed for CPU by no_device.py.
* The stack size of std::thread on macOS was too small for AQ, so I replaced std::thread with boost::thread.
