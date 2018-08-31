# Kmeans
Experimenting with Kmeans using IntelPython3

## Usage

You must run this script with [IntelPython3](https://software.seek.intel.com/python-distribution).

It takes a csv file with data as input and outputs another csv file with your clusters information, the output csv file can be imported in Google Sheets for easiar visualization.

Ex:
``` 
kmeans.py -f animals.csv -d Animal -c "Small,Medium,Big,Two Legs,Four Legs,Hair,Hooves,Mane,Feathers,Hunt,Run,Fly,Swim" -k 2 -o k2.csv
```
