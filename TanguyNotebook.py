def process_meters(meter_df):
    meter_df = meter_df.drop(meter_df.loc[meter_df.meter == -1].index).sort_values(by=['timestamp', "building_id"])
    return meter_df
$

def remove_meters_outliers(meters):
    qt2 = meters.groupby('meter').quantile(q = 0.75)
    qt1 = meters.groupby('meter').quantile(q = 0.25) #this is a dataframe
    iqr = qt2.meter_reading - qt1.meter_reading #this is a dataframe
    print(iqr)
    print(iqr.loc[2])
    for k in range(0,4):
        print(qt1.loc[k, 'meter_reading'])
        print(f"clipping values lower than {qt1.loc[k, 'meter_reading'] - 2*iqr.loc[k]} and greater than {qt2.loc[k,'meter_reading'] + 2*iqr.loc[k]}")
        filter_meter_k = meters.loc[(meters.meter == k) & ((meters.meter_reading > qt2.loc[k, 'meter_reading'] + 2*iqr.loc[k] ) | (meters.meter_reading <qt1.loc[k, 'meter_reading'] - 2*iqr.loc[k]))]
        meters = meters.drop(filter_meter_k.index)
    return meters
