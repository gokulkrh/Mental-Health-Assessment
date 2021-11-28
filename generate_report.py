def generate_report(arr):
    happiness_per, sad_per, severe_per = arr[0], arr[1], arr[2]
    happiness_report = ""
    sadness_report = ""
    severe_report = ""

    if happiness_per >= 70:
        happiness_report += "This person is quite happy content with thier life."
    elif 70 > happiness_per >= 50:
        happiness_report += "This person is quite normal, there is some positivity in their life as well as some bad things just like everyone else."
    elif 50 > happiness_per >= 30:
        happiness_report += "Although there is good things in their mind. This person could be under a lot stress."
    elif 30 > happiness_per >= 15:
        happiness_report += "There seems to be no positive things happening for this person, could be under a lot of stress"

    if sad_per >= 70:
        sadness_report += "This person is extremely unhappy and is susceptible to having mental breakdowns and suicidal thoughts.\nIt is best to suspend this person and give them proper medical attention"
    elif 70 > sad_per >= 50:
        sadness_report += "There is a lot of despair in their responses, this person is vulnerable to having stress related mental disorders.\nTherapy/councelling necessary"
    elif 50 > sad_per >= 30:
        sadness_report += "There is some despair and sadness in the responses,\nthere could be hope but still therapy/councelling is recommended"
    elif 30 > sad_per >= 15:
        sadness_report += "There are hints of sadness in some of the responses, this person could be vulnerable"

    if severe_per >= 70:
        severe_report += "Mental health is extremely poor, very high risk of suicide or mental disorders,\nneeds to be removed from service and given medical attention and therapy."
    elif 70 > severe_per >= 50:
        severe_report += "Mental health is poor, risk of mental disorders, could be having suicidal thoughts,\nremoving from service and therapy recommended."
    elif 50 > severe_per >= 30:
        severe_report += "Mental health is bad, therapy/counselling recommended, seems to be having suicidal thoughts."
    elif 30 > severe_per >= 15:
        severe_report += "Mental health maybe ok but is still vulnerable, there could be unresolved issues that could later affect this person."

    report = happiness_report + "\n" + sadness_report + "\n" + severe_report
    return report
