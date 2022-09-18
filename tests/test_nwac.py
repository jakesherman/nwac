
import nwac
import pytest


def test_stations():
    """Test that the stations function returns the correct results"""
    nwac_stations = nwac.stations()
    assert nwac_stations.iloc[0]["Name"] == "Alpental Base"
    assert len(nwac_stations.index) == 47
    
    
def test_telemetry_downloader():
    """Test downloading historical telemetry data"""
    hurricane_ridge_data = nwac.download_historical_data(
        station_names=["Hurricane Ridge"],
        years=[2021]
    )
    assert len(hurricane_ridge_data.index) == 8758
    assert hurricane_ridge_data.iloc[0]["Temp"] == 7.331
