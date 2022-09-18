# nwac

A python package for downloading historical Northwest Avalanche Center (NWAC) telemetry data. Currently, the package supports downloading historical telemetry data by year and weather station. 

This project is not affiliated with NWAC in any way. Please go to https://nwac.us/ to visit NWAC's website, and if you find their telemetry or forecasts useful please consider donating to them to help their nonprofit mission of providing avalanche information to help keep PNW backcountry users safe.

![Backcountry skiers traversing to Illumination Saddle](hood.jpg)


## Install

```bash
pip install nwac
```

## Usage

To see all of the available weather stations, use the `stations` function:

```python
import nwac
nwac_stations = nwac.stations()
```

To download telemetry data, use the `download_historical_data` function. You can specify station names or ids along with years, or if you leave all function arguments blank it will download data from every NWAC station from 2014 to present. The downloading process will take ~ 10 minutes, so please consider only downloading data from the stations and timeframes that you require for your analysis. 

```python
hurricane_ridge_data = nwac.download_historical_data(
    station_names=["Hurricane Ridge"],
    years=[2021, 2022]
)
hurricane_ridge_data.head()
```
