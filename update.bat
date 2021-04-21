echo To use this BATCH script add GARMINUSER and GARMINKEY to your Windows environment variables

echo Change Directory
cd C:\Users\dpb6\Downloads\repos\everystreetdurham

echo Activate Python Virtual Environment
call C:\Users\dpb6\Downloads\repos\everystreetdurham\venv\Scripts\activate.bat

echo Run garmin backup command
garmin-backup --backup-dir="data\garminactivities" %GARMINUSER% --password %GARMINKEY% -f gpx

echo Filter: make a copy of runs and walks in Durham
python process.py

echo Subsample GPS tracks intelligently
python gpx_reduce_all.py

echo Create Leaflet map of City border and GPS tracks
python everysinglestreet.py

echo Open HTML file in default browser
start "" "docs\index.html"

cmd /k

rem cmd /c C:\ProgramData\Anaconda3\condabin\conda.bat run "C:\ProgramData\Anaconda3\python.exe" "C:\Users\User Name\Path to your Python File\Python File.py"
