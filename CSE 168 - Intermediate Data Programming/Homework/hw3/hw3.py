import cse163_utils  # noqa: F401


# This is a hacky workaround to an unfortunate bug on macs that causes an
# issue with seaborn, the graphing library we want you to use on this
# assignment.  You can just ignore the above line or delete it if you are
# not using a mac!
# Add your imports and code here!

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import mean_squared_error



    
def parse(file_name):
    """
    This functin converts CSV file, returning a Pandas dataframe.
    """
    
    return pd.read_csv(file_name, na_values = '---')

data = parse('hw3-nces-ed-attainment.csv')



def completions_between_years(data, yr1, yr2, sex):
    '''
    This function takes a data frame, two year arguments, and a sex,
    returning the percent of different degrees completed for the
    given year range and sex.
    '''
    d = data[(data['Year'] >= yr1) & (data['Year'] < yr2) 
    & (data['Sex'] == sex)]
    if len(d) == 0:
        return None
    return d

def compare_bachelors_1980(data):
    """
    Returns a tuple (% for men, % for women) having earned Bachelor's degree
    in 1980.
    """
    d = data[(data['Year'] == 1980) & (data['Min degree'] == 'bachelor\'s')]\
        .groupby(['Sex'])['Total'].sum().loc[['M', 'F']]
    return (d[0], d[1])



def top_2_2000s(data):
    '''
    This function finds the two most commonly awarded levels of educational 
    attainment awarded between 2000-2010 (inclusive), using the mean percent 
    to compare the education levels. 
    
    Returns a list of tuples as follows: 
    [(#1 level, mean % of #1 level), (#2 level, mean % of #2 level)].
    '''
    data = data[(data['Year'] >= 2000) & (data['Year'] <= 2010) &
    (data['Sex'] == 'A')].groupby(['Min degree'])['Total'].mean().nlargest(2)
    
    return [i for i in data.items()]

def percent_change_bachelors_2000s(data, sex='A'):
    '''
    This function finds the difference between total percent of bachelor's
    degrees received in 2000 compared to 2010 based on sex. If no sex is given
    then the percent change for all students (sex = ‘A’) is evaluated.
    
    Function returns the difference as a float.
    '''
    d = data[(data['Min degree'] == 'bachelor\'s') & (data['Sex'] == sex)]
    d2000 = d[d['Year'] == 2000]['Total'].sum()
    d2010 = d[d['Year'] == 2010]['Total'].sum()
    return d2010 - d2000


#def line_plot_bachelors(data):
#    '''
#    Plot the total percentage of all people of bachelor's degree as
#    minimal completion with a line chart over years.
#    '''
#    data = data[data['Min degree'] == 'bachelor\'s']\
#               .groupby(['Year'])['Total'].sum()
#    plt = sns.lineplot(data.keys(),data.values)
#    plt.savefig('line_plot_bachelors.png')
    
def line_plot_bachelors(data):
    """
    Plot the line chart of the total percentages of all people who have earned
    bachelor's degree as minimal completion over the years and save the plot.
    """
    d = data[(data['Min degree'] == 'bachelor\'s')]\
        .groupby(['Year'])['Total'].sum()
    sns.lineplot(d.keys(), d.values)
    plt.savefig('line_plot_bachelors.png')


def bar_chart_high_school(data):
    '''
    Plot the total percentages of women, men, and total people with a minimum 
    education of high school degrees in the year 2009. Save your generated 
    graph as bar_chart_high_school.png.
    '''
    d = data[(data['Year'] == 2009) & (data['Min degree'] == 'high school')]\
        .groupby(['Sex'])['Total'].sum()
    sns.barplot(d.keys(), d.values)
    plt.savefig('line_plot_bachelors.png')
    

def plot_hispanic_min_degree(data):
    '''
    Plot the results of how the percent of Hispanic individuals with degrees 
    has changed between 1990 and 2010 (inclusive) for high school and 
    bachelor's degrees with a chart of your choice.
    '''
    data = data[(data['Year'] >= 1990) & (data['Year'] <= 2010) &
                ((data['Min degree'] == 'high school')
                    | (data['Min degree'] == 'bachelor\'s'))]
    sns.catplot(x="Year", y="Hispanic", hue="Min degree", data=data)
    plt.savefig('plot_hispanic_min_degree.png')
    
def fit_and_predict_degrees(data):
    '''
    This function takes the data as a parameter and returns the
    test mean square error as a float.
    '''
    data = data[['Year', 'Min degree', 'Sex', 'Total']]
    data = data.dropna()
    data = pd.get_dummies(data)
    X = data.loc[:, data.columns != 'Total']
    y = data['Total']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
    model = DecisionTreeRegressor()
    model.fit(X_train, y_train)
    y_test_pred = model.predict(X_test)
    return mean_squared_error(y_test, y_test_pred)
    



def main():
    print ("--- Part 0 ---")
    data = parse('hw3-nces-ed-attainment.csv')
    completions_between_years(data, 2007, 2008, 'F')
    cse163_utils.assert_equals((24.0, 21.0), compare_bachelors_1980(data))
    cse163_utils.assert_equals([('high school', 87.55714285714285),
                                ("associate's", 38.75714285714286)],
                               top_2_2000s(data))
    cse163_utils.assert_equals(2.599999999999998,
                               percent_change_bachelors_2000s(data))

    
    print ("--- Part 1 ---")
#    line_plot_bachelors(data)
#    bar_chart_high_school(data)
#    plot_hispanic_min_degree(data)
   
    print ("--- Part 2 ---")
    print (fit_and_predict_degrees(data))



if __name__ == '__main__':
    main()
