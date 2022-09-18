# nwac

A python package for downloading historical NWAC telemetry and forecast data.

<img src="https://57hours.com/wp-content/uploads/2021/10/Heather-Canyon-Double-Black-Diamond-1776x1197.jpg" alt="Perch in a fishtank" width="400"/>


## Install

```bash
pip install nwac
```

## Usage

```python
from nwac import download_historical_data, stations
nwac_stations = stations()
hurricane_ridge_data = download_historical_data(
    station_names=["Hurricane Ridge"],
    years=[2021, 2022]
)
hurricane_ridge_data.head()
```
