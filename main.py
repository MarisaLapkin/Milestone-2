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

#Given a csu and a year, returns the percentage of total local population that are students
def student_percentage(school: list[Housing_Data], campus: str, year:int)-> float:
    for idx in school:
        if idx.school == campus:
            if year == 2021:
                student_population = idx.students['Student Population 2021']
            elif year == 2022:
                student_population = idx.students['Student Population 2022']
            elif year == 2023:
                student_population = idx.students['Student Population 2023']
            else:
                return "Year Must Be Between 2021 and 2023"

            total_population = idx.population['City Population']
            return (round(student_population / total_population, 4)) * 100, "%"

    return "School Name Not Found"

def homeless_percentage(school: list[Housing_Data], campus:str):
    for idx in school:
        if idx.school == campus:
            total_population = idx.population['City Population']
            homeless_population = idx.homeless["Homeless Population"]
            return round(homeless_population / total_population, 4) * 100

def csu_homelessness(school: list[Housing_Data], percentage: float)->str:
    new_list = []
    for idx in school:
        percent = homeless_percentage(school, idx.school)
        if percent >= percentage:
            new_list.append(idx.school)

    return f"The universities that have a higher percentage of homeless than {percentage}% include {new_list}"


def csu_lowest_housing_price(school: list[Housing_Data])->str:
    if not school:
        raise ValueError("School list is empty")

    lowest_school = school[0].school
    lowest_price = school[0].averages['Average Rent Per Month']

    for idx in school:
        price = idx.averages['Average Rent Per Month']
        if price < lowest_price:
            lowest_price = price
            lowest_school = idx.school

    return f"The school with the lowest average rent is {lowest_school} at ${lowest_price} per month"
