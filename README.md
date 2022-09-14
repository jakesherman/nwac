# nwac

A python package for downloading historical NWAC telemetry and forecast data.

## Install

```bash
pip install nwac
```

## Usage

```
from nwac import download_historical_data, stations
nwac_stations = stations()
hurricane_ridge_data = download_historical_data(
    station_names=["Hurricane Ridge"],
    years=[2021, 2022]
)
hurricane_ridge_data.head()
```

![](backcountry.png)
