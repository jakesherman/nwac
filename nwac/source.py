from datetime import date
import pandas as pd
import time


def stations():
    """Create a Dataframe of NWAC telemetry stations metadata"""
    data = [
        [1, 'Alpental Base', 3100, 'Snoqualmie Pass', '2014-10-11'],
        [2, 'Alpental Mid-Mountain', 4350, 'Snoqualmie Pass', '2014-12-04'],
        [3, 'Alpental Summit', 5470, 'Snoqualmie Pass', '2014-01-03'],
        [4, 'Hurricane Ridge', 5250, 'Olympics', '2014-09-23'],
        [5, 'Mt Baker - Heather Meadows', 4210, 'Mt Baker', '2014-09-23'],
        [6, 'Mt Baker - Pan Dome', 5020, 'Mt Baker', '2014-09-23'],
        [7, 'Mazama', 2170, 'Washington Pass', '2014-01-01'],
        [8, 'Washington Pass Base', 5450, 'Washington Pass', '2014-09-23'],
        [9, 'Washington Pass Upper', 6680, 'Washington Pass', '2014-09-23'],
        [10,
        'Dirty Face Summit',
        5980,
        'Lake Wenatchee - Mission Ridge',
        '2014-09-23'],
        [11, 'Lake Wenatchee', 1930, 'Lake Wenatchee - Mission Ridge', '2014-09-23'],
        [12, 'Berne Snow Camp', 2700, 'Mt Baker', '2014-09-23'],
        [13, 'Stevens Pass - Schmidt Haus', 3950, 'Stevens Pass', '2014-09-23'],
        [14, 'Stevens Pass - Grace Lakes', 4800, 'Stevens Pass', '2014-11-28'],
        [17, 'Stevens Pass - Skyline', 5250, 'Stevens Pass', '2014-12-23'],
        [18, 'Stevens Pass - Skyline', 5250, 'Stevens Pass', '2014-12-17'],
        [19,
        'Tumwater Mountain',
        4180,
        'Lake Wenatchee - Mission Ridge',
        '2014-09-23'],
        [20, 'Mt Washington', 4340, 'Snoqualmie Pass', '2014-08-01'],
        [21, 'Snoqualmie Pass', 3010, 'Snoqualmie Pass', '2014-08-01'],
        [22, 'Snoqualmie Pass - Dodge Ridge', 3760, 'Snoqualmie Pass', '2014-08-01'],
        [23, 'Snoqualmie Pass - East Shed', 3770, 'Snoqualmie Pass', '2014-08-01'],
        [24,
        'Mission Ridge Base',
        4610,
        'Lake Wenatchee - Mission Ridge',
        '2014-01-01'],
        [25,
        'Mission Ridge Summit',
        6730,
        'Lake Wenatchee - Mission Ridge',
        '2014-09-23'],
        [26,
        'Mission Ridge Mid-Mountain',
        5160,
        'Lake Wenatchee - Mission Ridge',
        '2014-09-23'],
        [27, 'Crystal Green Valley', 6230, 'Mt Rainier', '2015-01-12'],
        [28, 'Crystal Base', 4570, 'Mt Rainier', '2014-09-23'],
        [29, 'Crystal Summit', 6830, 'Mt Rainier', '2014-02-02'],
        [30, 'Sunrise Upper', 6880, 'Mt Rainier', '2014-09-23'],
        [31, 'Sunrise Base', 6410, 'Mt Rainier', '2014-04-05'],
        [32, 'Chinook Pass Summit', 6240, 'Mt Rainier', '2014-09-23'],
        [33, 'Chinook Pass Base', 5500, 'Mt Rainier', '2014-09-23'],
        [34, 'Camp Muir', 10110, 'Mt Rainier', '2014-09-23'],
        [35, 'Paradise', 5400, 'Mt Rainier', '2014-09-23'],
        [36, 'Paradise Wind', 5380, 'Mt Rainier', '2014-09-23'],
        [37, 'White Pass Base', 4470, 'White Pass', '2020-10-14'],
        [39, 'White Pass Upper', 5800, 'White Pass', '2014-09-23'],
        [40, 'Mt St Helens - Coldwater ', 3260, 'Mt St Helens', '2014-09-23'],
        [41, 'Mt Hood Meadows Cascade Express', 7300, 'Mt Hood', '2014-01-03'],
        [42, 'Mt Hood Meadows Blue', 6540, 'Mt Hood', '2014-09-23'],
        [43, 'Mt Hood Meadows Base', 5380, 'Mt Hood', '2014-09-23'],
        [44, 'Timberline Lodge', 5880, 'Mt Hood', '2014-09-23'],
        [45, 'Timberline Magic Mile', 6990, 'Mt Hood', '2014-09-23'],
        [46, 'Ski Bowl Base', 3660, 'Mt Hood', '2014-10-30'],
        [47, 'Ski Bowl Summit', 5010, 'Mt Hood', '2015-01-08'],
        [48, 'Blewett Pass', 4100, 'Lake Wenatchee - Mission Ridge', '2014-10-22'],
        [49, 'White Pass Pigtail Peak', 5970, 'White Pass', '2014-09-23'],
        [50, 'Stevens Pass - Brooks', 4800, 'Stevens Pass', '2015-11-26']
    ]
    return pd.DataFrame(data, columns=["Station_Id", "Name", "Elevation", "Location", "Start_Date"])


def _download_station_data(station_id, year, simple_column_names=True):
    """Download one year's worth of station data"""
    nwac_telemetry_cols = {
        'id'                              : "Station_Id",
        'Relative Humidity  (%) '         : "Relative_Humidity",
        'Solar Radiation  (W/m2) '        : "Solar_Radiation",
        '24 Hour Snow  (") '              : "Snow_24_Hour",
        'Soil Moisture C  (VWC) '         : "Soil_Moisture_C",
        'Date/Time (PST)'                 : "Date_Time",
        'Wind Direction  (deg.) '         : "Wind_Direction",
        'Net Solar  (mJ/m2) '             : "Net_Solar",
        'Wind Speed Maximum  (mph) '      : "Wind_Speed_Max",
        'Wind Speed Minimum  (mph) '      : "Wind_Speed_Min",
        'Wind Speed Average  (mph) '      : "Wind_Speed_Avg",
        'Soil Temperature B  (deg F) '    : "Soil_Temp_B",
        'Barometric Pressure  (mb) '      : "Pressure",
        'Soil Temperature A  (deg F) '    : "Soil_Temp_A",
        'Soil Moisture B  (VWC) '         : "Soil_Moisture_B",
        'Battery Voltage  (v) '           : "Battery_Voltage",
        'Soil Moisture A  (VWC) '         : "Soil_Moisture_A",
        'Precipitation  (") '             : "Precipitation",
        'Equipment Temperature  (deg F) ' : "Equipment_Temperature",
        'Total Snow Depth  (") '          : "Total_Snow_Depth",
        'Intermittent/Shot Snow  (") '    : "Intermittent_Shot_Snow",
        'Soil Temperature C  (deg F) '    : "Soil_Temp_C",
        'Temperature  (deg F) '           : "Temp",  
    }
    url = f"http://www.nwac.us/data-portal/csv/q/?datalogger_id={station_id}&year={year}"
    data = pd.read_csv(url)
    if simple_column_names:
        data = data.rename(columns=nwac_telemetry_cols)
    return data


def download_historical_data(station_ids=None, station_names=None, years=None, 
                             simple_column_names=True, verbose=False):
    """Download historical NWAC station telemetry data for multiple stations/years
    
    Parameters
    ----------
    
    station_ids : list (optional) (default is all)
        A list of one or more NWAC station ids. Please only use one of station_ids
        or station_names but not both. If unspecified, the default will be
        all stations.
        
    station_names : list (optional) (default is all)
        A list of one or more NWAC station names. Please only use one of station_ids
        or station_names but not both. If unspecified, the default will be be all 
        stations. 
        
    years : list (optional)
        A list of one or more years to download data for. The first year of data
        availabilty, although 2015 data is more complete and reliable. 
        
    simple_column_names : bool (default is True)
        Transform the long column names into more readable ones. 
        
    verbose : bool (default is False)
        Show verbose download progress

    Returns
    -------
    nwac_data : pd.DataFrame
        A DataFrame of historical NWAC telemetry data
    
    """
    
    # Assertations
    all_stations = stations()
    assert ((station_ids is not None) + (station_names is not None)) < 2
    if station_ids is not None:
        assert isinstance(station_ids, list)
        assert all([station_id in all_stations["Station_Id"] for station_id in station_ids])
    elif station_names is not None:
        assert isinstance(station_names, list)
        assert all([station_name in list(all_stations["Name"]) for station_name in station_names])
    else:
        station_ids = list(all_stations["Station_Id"].unique())
    if years is not None:
        assert isinstance(years, list)
        years = [int(year) for year in years]
        assert min(years) >= 2014
    else:
        current_year = date.today().year
        years = list(range(2014, current_year + 1))
    
    # Transform station ids to names and vice versa
    station_id_to_name = dict(zip(all_stations["Station_Id"], all_stations["Name"]))
    station_name_to_id = dict(zip(all_stations["Name"], all_stations["Station_Id"]))
    if station_ids is None:
        station_ids = [station_name_to_id[station_name] for station_name in station_names]
    
    # Download the data
    station_years_data = []
    for year in years:
        if verbose:
            print("Downloading data for year:", year)
        for station_id in station_ids:
            if verbose:
                print("> Downloading data for station:", station_id_to_name[station_id])
            station_year_data = _download_station_data(
                station_id=station_id, 
                year=year, 
                simple_column_names=simple_column_names
            )
            existing_columns = list(station_year_data)
            station_year_data = (
                station_year_data
                .assign(Station_Id=station_id)
                .assign(Station_Name=station_id_to_name[station_id])
            )
            station_year_data = station_year_data[["Station_Id", "Station_Name"] + existing_columns]
            time.sleep(0.5)  # -- small gaps in pinging the server
            station_years_data.append(station_year_data)
    if verbose:
        print("Download completed!")
    return pd.concat(station_years_data)
