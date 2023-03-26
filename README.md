# 단어 외우기
study_english은 한국어-영어 단어 쌍 데이터 세트를 사용하여 영어 단어를 학습하는 간단한 데스크톱 애플리케이션입니다. 이 애플리케이션은 파이썬을 기반으로 하며, 그래픽 사용자 인터페이스(GUI)를 위해 tkinter 라이브러리와 데이터 세트 처리를 위해 pandas 라이브러리를 사용합니다.

### Table of Contents
- Features
- Prerequisites
- Installation
- Usage
- Contributing
- License

### Features
- 입력한 영어 단어 확인
- 현재 단어에 대한 힌트 표시
- 진행상활 추적
- 단어 섞기

### Prerequisites
- Python 3.7 or higher
- pandas library
- openpyxl library
- tkinter library

### Installation
1. 파이썬이 설치되어 있지 않다면 Python 3.7 이상을 설치하세요. 공식 웹사이트에서 다운로드 받을 수 있습니다: https://www.python.org/downloads/
2. 터미널이나 명령 프롬프트를 열고 pip를 사용하여 필요한 라이브러리를 설치하세요:

```bash
pip install pandas openpyxl
```
3. 애플리케이션의 소스 코드를 다운로드하세요.
4. Prepare an Excel file named "words.xlsx" containing the following columns:
- korean: 한국 단어
- english: 영어 단어
- hint: A hint for the English word (optional)
소스 코드와 같은 디렉터리에 파일을 저장하세요.

### Usage
터미널이나 명령 프롬프트를 사용하여 소스 코드를 다운로드한 디렉터리로 이동하세요.

다음 명령을 실행하여 애플리케이션을 실행하세요:

```bash
python3 study_english.py
```
GUI 창이 애플리케이션과 함께 열립니다. 애플리케이션을 사용하려면 다음 단계를 따르세요:

1. 표시된 한국어 단어를 읽으세요.
2. 입력 필드에 영어 단어를 추측하여 입력하고 Enter 키를 누르거나 "확인" 버튼을 클릭하세요.
3. 단어가 정확하면 애플리케이션은 다음 단어를 표시합니다. 그렇지 않으면 오류 메시지가 표시되고 힌트가 나타납니다.
4. "힌트 표시" 버튼을 클릭하여 현재 단어에 대한 힌트를 확인하세요.
5. 진행률 막대는 데이터셋의 총 단어 수 중 정확하게 추측한 단어 수를 보여줍니다.
6. "중지" 버튼을 클릭하여 프로그램을 종료하고 최종 점수를 확인하세요.

### Contributing
If you would like to contribute to the project, please follow these steps:

1. Fork the repository
2. Create a new branch with a descriptive name
3. Make your changes and commit them to your branch
4. Create a pull request to merge your changes into the main branch
5. Wait for your pull request to be reviewed and merged

Actually, I created this for the purpose of studying, so there may be some shortcomings. Please understand and if there are any issues, please send me an email. It would be great if you could contribute a lot to my areas of weakness. Let's all study hard and let's upgrade this program in a cool way.

### License
This project is licensed under the MIT License.