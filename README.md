# File-based key-value-datastore
Data are stored as key-value paies in JSON files

# Dependencies:
  - sys
  - argparse
  - threading
  - os
  - datetime

# Command line
```sh
$ python main.py [-p <path to store data>] -c <clientName> -o <Operation to be performed> -k <key> -v <value> [-t <time-to-live>]
```

> by default the data is stored at C:\data-store\

> "client.log" is used to log the file usage

#Example commands:
```sh
$ python main.py -h
```
```sh
$ python main.py -c Krishanth -o Create -k A56GH6 -v "RIP Maradonna"
```
```sh
$ python main.py -c Krishanth -o Read -k A56GH6
```
```sh
$ python main.py -c Krishanth -o Delete -k A56GH6
```
