# srl-ootr-h2h-calculator
Scripts to read OoTR head to head info for S3 top 32


- Install bs4 and selenium
- You need to have chrome installed
- Download the webdriver and add it to the project folder
- To load races from SRL run `python load.py`
  - It will generate a file `standings.txt` and `standingsWithFF.txt`
  - If you don't want to load the data just use the files that are already included
- To process those files run `python process.py`
  - It will generate a file named `results.csv`
