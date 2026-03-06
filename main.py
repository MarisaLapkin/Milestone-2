from Class_Setup import Housing_Data

#Functions

#Given a list of type Housing Data and a year between 2021 and 2023 returns the integer total population
def student_population_total(schools:list[Housing_Data], year:int)-> int:
    total = 0
    for s in schools:
        if year == 2021:
            total += s.students['Student Population 2021']
        elif year == 2022:
            total += s.students['Student Population 2022']
        elif year == 2023:
            total += s.students['Student Population 2023']
        else:
            print('Year Must Be Between 2021 and 2023')
            return -1
    return total

# Given a list of type Housing Data returns a dictionary of the average rent and square footage across all list items
def housing_averages_total(schools:list[Housing_Data])->dict:
    averages = {'Average Rent':0.0, 'Average Size':0.0}
    average_rent = 0
    average_size = 0
    for s in schools:
        average_rent += s.averages['Average Rent']
        average_size += s.averages['Average Size']
    averages['Average Rent'] = average_rent/len(schools)
    averages['Average Size'] = average_size/len(schools)
    return averages

#Given a list of type Housing Data and a school name an integer represents the price per square foot of housing in that area
def price_per_square_foot(schools:list[Housing_Data], name:str)->float:
    for s in schools:
        if s.school == name:
            price = s.averages['Average Rent']/s.averages['Average Size']
        else:
            print('School Name Not Found')
            return -1
    return price


# Given a list of type Housing Data and a threshold of price per square foot, returns the name of the schools above/below
def price_per_foot_lt(schools:list[Housing_Data], max:float)->list[str]:
    schools_list = []
    for s in schools:
        if price_per_square_foot(schools,s) < max and price_per_square_foot(schools,s) != -1:
            schools_list.append(s.school)
        if price_per_square_foot(schools,s) == -1:
            pass
    return schools_list

def price_per_foot_gt(schools:list[Housing_Data], min:float)->list[str]:
    schools_list = []
    for s in schools:
        if price_per_square_foot(schools,s) > min:
            schools_list.append(s.school)
    return schools_list


# Given a list of type Housing Data, a string representation of a school name, and an integer representation of a year,
#returns the float representation of the percent of current students that can live in on-campus housing
def percent_students_oncampus(schools:list[Housing_Data], name:str, year:int)->float:
    for school in schools:
        if school.school == name:
            beds = school.student_housing['On Campus Housing']
            if year == 2021:
                people = school.students['Student Population 2021']
            elif year == 2022:
                people = school.students['Student Population 2022']
            elif year == 2023:
                people = school.students['Student Population 2023']
            else:
                print ('Year Must Be Between 2021 and 2023')
                return -1
        else:
            print('School Name Not Found')
            return -1
    return beds/people


#write yours here




