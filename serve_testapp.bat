cd C:\Users\vcm\PycharmProjects\testapp
git pull https://%TESTAPP_GIT_PAT%@github.com/zeshengli98/testapp.git
venv\Scripts\python.exe -m pip install -r requirements.txt
venv\Scripts\python.exe server.py
