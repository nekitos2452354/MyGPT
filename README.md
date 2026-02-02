# MyGPT2

Простое desktop-приложение на Python с графическим интерфейсом для работы с GPT.

Проект использует:
- Python
- customtkinter (GUI)
- revChatGPT
- pyttsx3 (озвучка)
- keyboard

Структура проекта
```bash
MYGPT2/
├─ src/
│  ├─ APIReg.py
│  ├─ GPTWindow.py
│  ├─ miniGPTWin.py
│  └─ Voice.py
├─ data/
│  └─ apiKey.example
├─ main.py
├─ requirements.txt
├─ .gitignore
└─ README.md

---

## Требования

- Python 3.10 или 3.11
- pip
- Git

---

## Установка

### 1. Клонировать репозиторий

```bash
git clone https://github.com/USERNAME/MyGPT2.git
cd MyGPT2

2. Создать виртуальное окружение
macOS / Linux
```bash
    python3 -m venv venv
    source venv/bin/activate
```bash
Windows
    python -m venv venv
    venv\Scripts\activate

3. Установить зависимости
```bash
    pip install -r requirements.txt

4. Запуск 
```bash
    python main.py

