#CSE 163 HW6
#Mike Kmiec



import cse163_utils 
import geopandas
import pandas as pd
import matplotlib.pyplot as plt


def load_in_data(fname1, fname2):
    """
    Returns a GeoDataFrame that has merged given two datasets

    Takes the file name of Census Tract shape file and the file name of food
    access CSV file
    """
    data1 = geopandas.read_file(fname1)
    data2 = geopandas.GeoDataFrame(pd.read_csv(fname2))
    return data1.merge(data2, left_on='CTIDFP00', right_on='CensusTract',
                       how='left')


def percentage_food_data(data):
    """
    Returns the percentage of census tracts in Wasington state that is
    provided in food access data
    """
    d = data[data['State'] == 'WA']
    return len(d)/len(data)*100


def plot_map(data):
    """
    Plots a map of Washington and saves it in 'washington_map.png' file
    """
    data.plot()
    plt.savefig('washington_map.png')


def plot_population_map(data):
    """
    Plots a map of Washington with each census tract colored by its population
    and saves it in 'washington_population_map.png' file
    """
    ct = data.dissolve(by='CensusTract', aggfunc='sum')
    ct.plot(column='POP2010', legend=True)
    plt.savefig('washington_population_map.png')


def plot_population_county_map(data):
    """
    Plots a map of Washington with each county colored by its population
    and saves it in 'washington_county_population_map.png'
    """
    popluation_county = data.dissolve(by='County', aggfunc='sum')
    popluation_county.plot(column='POP2010', legend=True)
    plt.title('Population_county_map')
    plt.savefig('washington_county_population_map.png')


def plot_food_access_by_county(data):
    """
    Plots several maps of Washington depending on low access and low income
    and saves it in 'washington_county_food_access.png' file
    """
    data2 = data[['County', 'geometry', 'POP2010', 'lapophalf', 'lapop10',
                 'lalowihalf', 'lalowi10']]
    d = data2.dissolve(by='County', aggfunc='sum')
    d['lapophalf_ratio'] = d['lapophalf']/d['POP2010']
    d['lapop10_ratio'] = d['lapop10']/d['POP2010']
    d['lalowihalf_ratio'] = d['lalowihalf']/d['POP2010']
    d['lalowi10_ratio'] = d['lalowi10']/d['POP2010']
    fig, [[ax1, ax2], [ax3, ax4]] = plt.subplots(2, figsize=(20, 10), ncols=2)
    d.plot(ax=ax1, column='lapophalf_ratio', legend=True, vmin=0, vmax=1)
    d.plot(ax=ax3, column='lapop10_ratio', legend=True, vmin=0, vmax=1)
    d.plot(ax=ax2, column='lalowihalf_ratio', legend=True, vmin=0, vmax=1)
    d.plot(ax=ax4, column='lalowi10_ratio', legend=True, vmin=0, vmax=1)
    ax1.set_title('Low Access: Half')
    ax2.set_title('Low Access + Low Income: Half')
    ax3.set_title('Low Access: 10')
    ax4.set_title('Low Access + Low Income: 10')
    fig.savefig('washington_county_food_access.png')


def plot_low_access_tracts(data):
    """
    Plots all the census tracts that are considered low access
    and saves it in 'washington_low_access.png' file
    """
    fig, ax = plt.subplots(1)
    urban = (data['Urban'] == 1) & (data['lapophalf'] >= 500)
    rural = (data['Rural'] == 1) & (data['lapop10'] >= 500)
    data.plot(ax=ax, color='#EEEEEE')
    data[data['State'] == 'WA'].plot(ax=ax, color='#AAAAAA')
    data[urban | rural].plot(ax=ax)
    fig.savefig('washington_low_access.png')


def main():
    data = load_in_data('tl_2010_53_tract00/tl_2010_53_tract00.shp',
                        'food_access.csv')
    print(percentage_food_data(data))
    plot_map(data)
    plot_population_map(data)
    plot_population_county_map(data)
    plot_food_access_by_county(data)
    plot_low_access_tracts(data)


if __name__ == '__main__':
    main()











