python3 -m venv venv
.\venv\Scripts\activate.ps1
python -m pip install --upgrade pip
ForEach($line in (Get-Content -Path .\requirements.txt)){python -m pip install $line}
