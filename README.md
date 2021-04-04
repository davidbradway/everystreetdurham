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
python src\everysinglestreet.py
deactivate
```
