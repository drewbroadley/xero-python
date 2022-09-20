# coding: utf-8

"""
    Xero Payroll AU API

    This is the Xero Payroll API for orgs in Australia region.  # noqa: E501

    Contact: api@xero.com
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401

from xero_python.models import BaseModel


class Settings(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        "accounts": "list[Account]",
        "tracking_categories": "SettingsTrackingCategories",
        "days_in_payroll_year": "int",
        "employees_are_stp2": "bool",
    }

    attribute_map = {
        "accounts": "Accounts",
        "tracking_categories": "TrackingCategories",
        "days_in_payroll_year": "DaysInPayrollYear",
        "employees_are_stp2": "EmployeesAreSTP2",
    }

    def __init__(
        self,
        accounts=None,
        tracking_categories=None,
        days_in_payroll_year=None,
        employees_are_stp2=None,
    ):  # noqa: E501
        """Settings - a model defined in OpenAPI"""  # noqa: E501

        self._accounts = None
        self._tracking_categories = None
        self._days_in_payroll_year = None
        self._employees_are_stp2 = None
        self.discriminator = None

        if accounts is not None:
            self.accounts = accounts
        if tracking_categories is not None:
            self.tracking_categories = tracking_categories
        if days_in_payroll_year is not None:
            self.days_in_payroll_year = days_in_payroll_year
        if employees_are_stp2 is not None:
            self.employees_are_stp2 = employees_are_stp2

    @property
    def accounts(self):
        """Gets the accounts of this Settings.  # noqa: E501

        Payroll Account details for SuperExpense, SuperLiabilty, WagesExpense, PAYGLiability & WagesPayable.  # noqa: E501

        :return: The accounts of this Settings.  # noqa: E501
        :rtype: list[Account]
        """
        return self._accounts

    @accounts.setter
    def accounts(self, accounts):
        """Sets the accounts of this Settings.

        Payroll Account details for SuperExpense, SuperLiabilty, WagesExpense, PAYGLiability & WagesPayable.  # noqa: E501

        :param accounts: The accounts of this Settings.  # noqa: E501
        :type: list[Account]
        """

        self._accounts = accounts

    @property
    def tracking_categories(self):
        """Gets the tracking_categories of this Settings.  # noqa: E501


        :return: The tracking_categories of this Settings.  # noqa: E501
        :rtype: SettingsTrackingCategories
        """
        return self._tracking_categories

    @tracking_categories.setter
    def tracking_categories(self, tracking_categories):
        """Sets the tracking_categories of this Settings.


        :param tracking_categories: The tracking_categories of this Settings.  # noqa: E501
        :type: SettingsTrackingCategories
        """

        self._tracking_categories = tracking_categories

    @property
    def days_in_payroll_year(self):
        """Gets the days_in_payroll_year of this Settings.  # noqa: E501

        Number of days in the Payroll year  # noqa: E501

        :return: The days_in_payroll_year of this Settings.  # noqa: E501
        :rtype: int
        """
        return self._days_in_payroll_year

    @days_in_payroll_year.setter
    def days_in_payroll_year(self, days_in_payroll_year):
        """Sets the days_in_payroll_year of this Settings.

        Number of days in the Payroll year  # noqa: E501

        :param days_in_payroll_year: The days_in_payroll_year of this Settings.  # noqa: E501
        :type: int
        """

        self._days_in_payroll_year = days_in_payroll_year

    @property
    def employees_are_stp2(self):
        """Gets the employees_are_stp2 of this Settings.  # noqa: E501

        Indicates if the organisation has been enabled for STP Phase 2 editing of employees.  # noqa: E501

        :return: The employees_are_stp2 of this Settings.  # noqa: E501
        :rtype: bool
        """
        return self._employees_are_stp2

    @employees_are_stp2.setter
    def employees_are_stp2(self, employees_are_stp2):
        """Sets the employees_are_stp2 of this Settings.

        Indicates if the organisation has been enabled for STP Phase 2 editing of employees.  # noqa: E501

        :param employees_are_stp2: The employees_are_stp2 of this Settings.  # noqa: E501
        :type: bool
        """

        self._employees_are_stp2 = employees_are_stp2
