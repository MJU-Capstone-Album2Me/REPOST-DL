<h1><img width="35" src="https://github.com/MJU-Capstone-Album2Me/REPOST-Backend/assets/64758861/61a29d49-3c83-4a95-a929-86ede76598fd"/>&nbsp;&nbsp;RE:POST</h1>

## 서비스 소개
```
📷 이미지 고해상도 복원을 통한 추억 사진 공유 플랫폼
```
## 기획 배경 및 목표
과거에는 아날로그 사진이 주로 사용되었으며, 이러한 사진들은 시간의 흐름에 따라 훼손되거나 품질이 저하된다. 또한, 초기 디지털카메라 기술의 한계 때문에 이때 찍은 사진들의 화질도 좋지 않았다.
이러한 저해상도 사진의 품질 저하 문제는 디지털 형식으로 보존하거나 온라인에서 공유하려는 경우 큰 제약 요인이 된다.
<p></p>
따라서 본 서비스는 과거 아날로그 사진을 디지털 형식으로 변환하고 저화질의 디지털 이미지를 고해상도 복원 기술을 이용하여 이미지의 해상도를 높인다.
또한 이미지 복원을 용이하게 하고 복원된 이미지를 쉽게 공유할 수 있도록 사용자 친화적인 서비스를 구현하는 것을 목표로 한다.

<br><br>

## 기술 스택
<p align="center">
<img src="https://img.shields.io/badge/Java 17-008FC7?style=for-the-badge&logo=Java&logoColor=white"/>
<img src="https://img.shields.io/badge/spring 3.0.6-%236DB33F.svg?style=for-the-badge&logo=spring&logoColor=white"/>
<img src="https://img.shields.io/badge/Spring Security-6DB33F?style=for-the-badge&logo=Spring Security&logoColor=white"/>
<img src="https://img.shields.io/badge/Spring Data JPA-6DB33F?style=for-the-badge&logo=JPA&logoColor=white"/>
<img src="https://img.shields.io/badge/-QueryDSL-blue?style=for-the-badge"/>
<img src="https://img.shields.io/badge/mysql-%2300f.svg?style=for-the-badge&logo=mysql&logoColor=white"/>
<img src="https://img.shields.io/badge/-FastAPI-0C9B8C?style=for-the-badge&logo=fastAPI&logoColor=white"/>
<img src="https://img.shields.io/badge/-pytorch-F17259?style=for-the-badge&logo=pytorch&logoColor=white"/>
<img src="https://img.shields.io/badge/GitHub Actions-2088FF?style=for-the-badge&logo=GitHub Actions&logoColor=white"/>
<img src="https://img.shields.io/badge/Amazon EC2-FF9900?style=for-the-badge&logo=Amazon EC2&logoColor=white"/>
<img src="https://img.shields.io/badge/Amazon RDS-527FFF?style=for-the-badge&logo=Amazon RDS&logoColor=white"/>
<img src="https://img.shields.io/badge/Amazon S3-E15343?style=for-the-badge&logo=Amazon S3&logoColor=white"/>
<img src="https://img.shields.io/badge/Amazon CodeDeploy-82A450?style=for-the-badge&logo=Amazon CodeDeploy&logoColor=white"/>
</p>
<br><br>

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
