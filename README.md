# REPOST-DL
캡스톤디자인 - Data/DL

## Install

```bash
git clone https://github.com/jeongseok5/REPOST-DL
cd REPOST-DL
pip install -r requirements.txt
```

## Example

```
python inference.py 
    -m BSRGANx2                # model
    -dir dir/for/inference     # directory for inference
    --disable_cuda             # Disable CUDA
```

You can change the ```-m``` to BSRGAN w/ scale factor==4. 


## Training Environment
|||
|:---|:---|
|GPU|Nvidia RTX 3080 12GB| 
|CUDA Version|11.4|
|cuDNN|8.7.0|
|Nvidia Driver Version|470.182.03|
|OS|ubuntu 20.04 LTS|
|torch|1.12.1+cu113|


## Model Pipeline
<img width="1080" alt="model_pipeline" src="https://github.com/MJU-Capstone-Album2Me/REPOST-DL/assets/91061904/37bc6cbb-af7a-4c18-b2ea-7abe931e24bd">

## Service Architecture
<img width="1080" alt="service_architecture" src="https://github.com/MJU-Capstone-Album2Me/REPOST-DL/assets/91061904/8b9bf49a-58cd-4625-9503-09f8d277533a">
