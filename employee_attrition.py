"""
this file contains data analysis of the emplyee data for a company
trying to control employee attrition.
we will answer the following questions;
1. what type of employees are leaving?
2. which employees are likely to leave in the future?
"""


import pandas as pd
from scipy.stats import ttest_ind


# run an independent t-test on employee variables.
# this should reveal the type of employees that are leaving


def employees_leaving():
    """this will run t-tests and return the variable(s)
    where the differenc in mean is signicant at p=0.05
    """

    df_existing_employees = pd.read_excel(
        "Hash-Analytic-Python-Analytics-Problem-case-study-1.xlsx",
        sheet_name="Existing employees",
    )
    df_former_employees = pd.read_excel(
        "Hash-Analytic-Python-Analytics-Problem-case-study-1.xlsx",
        sheet_name="Employees who have left",
    )

    # calculate t-test for satisfation_level
    satisfaction_ttest = ttest_ind(
        df_existing_employees["satisfaction_level"],
        df_former_employees["satisfaction_level"]
    )

    # calculate t-test for last_evaluation
    evaluation_ttest = ttest_ind(
        df_existing_employees["last_evaluation"], 
        df_former_employees["last_evaluation"]
    )

    # calculate t-test for number_project
    project_ttest = ttest_ind(
        df_existing_employees["number_project"], 
        df_former_employees["number_project"]
    )

    # calculate t-test for average_montly_hours
    hours_ttest = ttest_ind(
        df_existing_employees["average_montly_hours"],
        df_former_employees["average_montly_hours"]
    )

    # calculate t-test for time_spend_company
    company_time_ttest = ttest_ind(
        df_existing_employees["time_spend_company"],
        df_former_employees["time_spend_company"]
    )

    # calculate t-test for work_accident
    accident_ttest = ttest_ind(
        df_existing_employees["Work_accident"], 
        df_former_employees["Work_accident"]
    )

    # calculate t-test for promotion
    promotion_ttest = ttest_ind(
        df_existing_employees["promotion_last_5years"],
        df_former_employees["promotion_last_5years"]
    )

    # get t-test values greater less than p=0.05. return a list of column names that determine if an employee leaves
    ttests = {
        "satisfaction_level": satisfaction_ttest,
        "last_evaluation": evaluation_ttest,
        "number_pproject": project_ttest,
        "avaerage_montly_hours": hours_ttest,
        "time_spend_company": company_time_ttest,
        "Work_accident": accident_ttest,
        "promotion_last_5years": promotion_ttest,
    }
    result = []
    for column, test in ttests.items():
        if test[1] < 0.05:
            result.append(column)
    print(result)
    return result


if __name__ == "__main__":
    employees_leaving()
