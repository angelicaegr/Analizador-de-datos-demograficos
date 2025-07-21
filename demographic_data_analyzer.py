import pandas as pd


def calculate_demographic_data(print_data=True):
    # Read data from file
    path = 'adult.data.csv'
    df = pd.read_csv(path)

    # How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
    race_count = df['race'].value_counts()

    # What is the average age of men?
    condition = df['sex'] == 'Male'
    average_age_men = df.loc[condition, 'age'].mean()

    # What is the percentage of people who have a Bachelor's degree?
    condition = df['education'] == 'Bachelors'
    percentage_bachelors = (len(df[condition]) / len(df)) * 100

    # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
    # What percentage of people without advanced education make more than 50K?

    # with and without `Bachelors`, `Masters`, or `Doctorate`
    condition = (df['education'] == 'Bachelors') | (df['education'] == 'Masters') | (df['education'] == 'Doctorate')
    df_advanced_education = df[condition]
    people_advance_education = len(df_advanced_education)

    df_no_advanced_education = df[~condition]
    people_no_advance_education = len(df_no_advanced_education)

    higher_education = people_advance_education
    lower_education = people_no_advance_education

    # percentage with salary >50K
    df_high_income_advanced_education = df_advanced_education[df_advanced_education['salary'] == '>50K']
    people_advance_education_50k = len(df_high_income_advanced_education)
    percentage_high_income_advanced_education = (people_advance_education_50k / people_advance_education) * 100

    higher_education_rich = percentage_high_income_advanced_education

    df_high_income_no_advanced_education = df_no_advanced_education[df_no_advanced_education['salary'] == '>50K']
    high_income_no_advanced_education = len(df_high_income_no_advanced_education)
    percentage_high_income_no_advanced_education = (high_income_no_advanced_education / people_no_advance_education) * 100

    lower_education_rich = percentage_high_income_no_advanced_education

    # What is the minimum number of hours a person works per week (hours-per-week feature)?
    min_work_hours = df['hours-per-week'].min()

    # What percentage of the people who work the minimum number of hours per week have a salary of >50K?
    
    df_min_hours = df[df['hours-per-week'] <= 20] #Considering a Part time job, 20 hours per week
    people_part_time = len(df_min_hours)

    df_high_income_part_time = df_min_hours[df_min_hours['salary'] == '>50K']
    percentage_high_income_part_time = (len(df_high_income_part_time) / people_part_time) * 100
    
    num_min_workers = people_part_time

    rich_percentage = percentage_high_income_part_time

    # What country has the highest percentage of people that earn >50K?
    condition = (df['salary'] == '>50K')
    count_values_for_country_high_income = df.loc[condition, 'native-country'].value_counts() / df['native-country'].value_counts() * 100

    country_high_percentage = count_values_for_country_high_income.idxmax()
    country_high_percentage_value = count_values_for_country_high_income.max()

    highest_earning_country = country_high_percentage
    highest_earning_country_percentage = country_high_percentage_value

    # Identify the most popular occupation for those who earn >50K in India.
    condition = (df['native-country'] == 'India') & (df['salary'] == '>50K')
    popular_occupation = df.loc[condition, 'occupation'].value_counts().idxmax()

    top_IN_occupation = popular_occupation

    # DO NOT MODIFY BELOW THIS LINE

    if print_data:
        print("Number of each race:\n", race_count) 
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(f"Percentage with higher education that earn >50K: {higher_education_rich}%")
        print(f"Percentage without higher education that earn >50K: {lower_education_rich}%")
        print(f"Min work time: {min_work_hours} hours/week")
        print(f"Percentage of rich among those who work fewest hours: {rich_percentage}%")
        print("Country with highest percentage of rich:", highest_earning_country)
        print(f"Highest percentage of rich people in country: {highest_earning_country_percentage}%")
        print("Top occupations in India:", top_IN_occupation)

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage':
        highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }
