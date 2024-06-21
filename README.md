# gaussian-splatting-pro

Bug-free 3DGS implementation with latest Pytorch2.5 dev feature enabled!.

## Install deps

```bash
conda create -n dev python=3.12 pytorch torchvision scipy numpy rich ninja pytorch-cuda cuda -c pytorch-nightly -c nvidia -y

pip install third_party/raster
pip install third_party/knn
```