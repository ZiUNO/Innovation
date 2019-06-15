# Innovation 创新项目
## 基于CPM的FPS手势控制引擎系统
基于TensorFlow深度学习框架开发，基于CPM（Convolutional Pose Machines）的FPS手势控制引擎系统，旨在将手势识别和控制系统用于FPS游戏，供玩家操控角色的各种操作。通过手势识别的方式来操控游戏角色，例如前进、更换装备、射击等操作。

### 运行
执行脚本run_demo_hand_with_tracker.py。

### 配置要求
> 显卡 GTX960M及以上

### Version
| env  | version |
|:---|:---:|
| python | 3.6.5 |
| tensorflow-gpu | 1.4.0 |
| opencv | 3.2.0.8 |
| numpy | 1.16.4 |
| matplotlib | 3.1.0 |

### 参考文献
>Convolutional Pose Machines: A Deep Architecture for Estimating Articulated Poses \
SE Wei  - 2016 - 被引量: 1 \
Pose Machines provide a sequential prediction framework for learning rich implicit spatial models. In this work we show a systematic design for how convolutional networks can be incorporated into the pose machine framework for learning image features and image-dependent spatial models for the task of pose estimation. The contribution of this paper is to implicitly model long-range dependencies between variables in structured prediction tasks such as articulated pose estimation. We achieve this by designing a sequential architecture composed of convolutional networks that directly operate on belief maps from previous stages, producing increasingly refined estimates for part locations, without the need for explicit graphical model-style inference. Our approach addresses the characteristic difficulty of vanishing gradients during training by providing a natural learning objective function that enforces intermediate supervision, thereby replenishing back-propagated gradients and conditioning the learning procedure. We demonstrate state-of-the-art performance and outperform competing methods on standard benchmarks including the MPII, LSP, and FLIC datasets.
