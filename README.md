# 단어 외우기
## main.py
이 프로젝트는 영어 학습을 돕는 간단한 프로그램 입니다. 사용자는 다양한 학습 방법을 통해 영어 단어와 문장을 익힐 수 있습니다.

### 주요 기능
1. 영어 단어 맞추기: 영어 단어 학습을 돕는 프로그램으로, 단어와 그 의미를 맞추는 게임입니다.
2. 영어 카드 맞추기: 영어 단어와 문장을 사용한 플래시카드 학습 게임입니다.
3. 랜덤 실행: 위의 두 가지 학습 방법 중 하나를 무작위로 선택해 실행합니다.

### 설치 및 실행 방법
1. 이 프로젝트를 로컬 저장소에 복제합니다.
2. 프로젝트 폴더로 이동합니다.
3. 의존성이 필요한 경우, 필요한 라이브러리를 설치합니다.
4. python main.py 명령어를 통해 애플리케이션을 실행합니다.

### 사용 방법
1. 메인 메뉴에서 원하는 학습 방법을 선택합니다.
2. 선택한 학습 방법에 따라 영어 단어 또는 문장을 맞추는 게임을 진행합니다.
3. 필요한 경우, 랜덤 실행 버튼을 눌러 무작위로 선택된 학습 방법을 진행합니다.
4. 학습을 종료하려면 종료 버튼을 누릅니다.

### 기타 정보
- 애플리케이션은 Python과 Tkinter로 작성되었습니다.
- 프로젝트는 오픈 소스로 제공되며, 누구나 자유롭게 사용, 수정 및 배포할 수 있습니다.

## english_card_game.py
이 프로그램은 사용자가 CSV 파일에 저장된 영어 단어와 그에 해당하는 한국어 뜻을 학습할 수 있도록 도와주는 프로그램입니다. 사용자는 주어진 5개의 옵션 중에서 올바른 영어 단어를 선택하여 정답 여부를 확인할 수 있습니다.

### 설치 및 실행 방법
1. 프로젝트를 다운로드 받아 압축을 해제합니다.
2. 작업 환경에 Python3이 설치되어 있는지 확인하세요.
3. words.csv 파일에 학습하고 싶은 단어를 추가하거나 수정하세요. 각 행에는 한국어 단어와 영어 단어를 쉼표로 구분하여 입력합니다.
4. 프로그램을 실행하기 위해 터미널에서 python main.py 명령을 실행하세요.

### 사용 방법
1. 프로그램을 실행하면 주어진 한국어 단어에 해당하는 영어 단어를 선택해야 합니다.
2. 정답이라고 생각하는 옵션을 클릭하세요. 정답일 경우 정답임을 알리는 메시지가 표시되며, 오답일 경우 정답을 알려주는 메시지가 표시됩니다.
3. 모든 단어를 맞출 경우 프로그램은 자동으로 종료됩니다. 진행 중에 프로그램을 종료하려면 '종료' 버튼을 클릭하세요.

### 주의사항
- `words.csv` 파일의 내용을 수정하려면 텍스트 편집기 또는 CSV 에디터를 사용하시면 됩니다. 단, 한글을 사용할 경우 인코딩이 `UTF-8`로 저장되어야 합니다.

## study_english.py
study_english은 한국어-영어 단어 쌍 데이터 세트를 사용하여 영어 단어를 학습하는 간단한 데스크톱 애플리케이션입니다. 이 애플리케이션은 파이썬을 기반으로 하며, 그래픽 사용자 인터페이스(GUI)를 위해 tkinter 라이브러리와 데이터 세트 처리를 위해 pandas 라이브러리를 사용합니다.

### Table of Contents
- Features
- Prerequisites
- Installation
- Usage
- Contributing
- Inquiry
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

### Inquiry
문제가 발생하거나 도움이 필요한 경우 이슈를 작성해 주세요.

### License
This project is licensed under the MIT License.