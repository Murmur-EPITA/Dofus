python3 -m venv venv
.\venv\Scripts\activate.ps1
foreach($line in "requirements.txt")
{
    python -m pip install $line
}
