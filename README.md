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


## Model Pipeline
![파이프라인](https://github.com/MJU-Capstone-Album2Me/REPOST-DL/assets/91061904/37bc6cbb-af7a-4c18-b2ea-7abe931e24bd)
