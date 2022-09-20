### python 기본 command

---

<conda 설정> activate <conda 이름>  
  
내 가상환경  
    - base  
    - python_api  

default는 base  
  
conda deactivate (deactivate_가상환경 비활성화)  
  
conda activate python_api (python_api 가상환경 활성화)  

---

### 실행 명령어
  
FLASK_APP=app.py FLASK_DEBUG=1 flask run

- httpie로 GET 요청 보내기  
  -  http -v GET http://localhost:5000/ping  
    -  그냥 postman으로 보내는게 더 좋을것같다