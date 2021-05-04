# Every Street Durham

This repository is to download and visualize GPS traces from Garmin Connect.

See the map: https://davidbradway.github.io/everystreetdurham

## Usage

For Windows Anaconda Prompt. Similar for other platforms.
```
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python -m pip install --upgrade pip
cd data
garmin-backup --backup-dir=garminactivities USERNAME --password PASSWORD -f gpx
cd ..
python process.py
python gpx_reduce_all.py
python everysinglestreet.py
deactivate
```

To use the included `update.bat` Windows CMD batch script, add GARMINUSER and GARMINKEY to your Windows User Environment Variables. Then you should just be able to run the script by double-clicking it or from the Command Prompt.

