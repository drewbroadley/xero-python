# coding: utf-8

"""
    Xero Payroll AU API

    This is the Xero Payroll API for orgs in Australia region.  # noqa: E501

    Contact: api@xero.com
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401

from xero_python.models import BaseModel


class PayrollCalendar(BaseModel):
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
        "name": "str",
        "calendar_type": "CalendarType",
        "start_date": "date[ms-format]",
        "payment_date": "date[ms-format]",
        "payroll_calendar_id": "str",
        "updated_date_utc": "datetime[ms-format]",
        "validation_errors": "list[ValidationError]",
    }

    attribute_map = {
        "name": "Name",
        "calendar_type": "CalendarType",
        "start_date": "StartDate",
        "payment_date": "PaymentDate",
        "payroll_calendar_id": "PayrollCalendarID",
        "updated_date_utc": "UpdatedDateUTC",
        "validation_errors": "ValidationErrors",
    }

    def __init__(
        self,
        name=None,
        calendar_type=None,
        start_date=None,
        payment_date=None,
        payroll_calendar_id=None,
        updated_date_utc=None,
        validation_errors=None,
    ):  # noqa: E501
        """PayrollCalendar - a model defined in OpenAPI"""  # noqa: E501

        self._name = None
        self._calendar_type = None
        self._start_date = None
        self._payment_date = None
        self._payroll_calendar_id = None
        self._updated_date_utc = None
        self._validation_errors = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if calendar_type is not None:
            self.calendar_type = calendar_type
        if start_date is not None:
            self.start_date = start_date
        if payment_date is not None:
            self.payment_date = payment_date
        if payroll_calendar_id is not None:
            self.payroll_calendar_id = payroll_calendar_id
        if updated_date_utc is not None:
            self.updated_date_utc = updated_date_utc
        if validation_errors is not None:
            self.validation_errors = validation_errors

    @property
    def name(self):
        """Gets the name of this PayrollCalendar.  # noqa: E501

        Name of the Payroll Calendar  # noqa: E501

        :return: The name of this PayrollCalendar.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this PayrollCalendar.

        Name of the Payroll Calendar  # noqa: E501

        :param name: The name of this PayrollCalendar.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def calendar_type(self):
        """Gets the calendar_type of this PayrollCalendar.  # noqa: E501


        :return: The calendar_type of this PayrollCalendar.  # noqa: E501
        :rtype: CalendarType
        """
        return self._calendar_type

    @calendar_type.setter
    def calendar_type(self, calendar_type):
        """Sets the calendar_type of this PayrollCalendar.


        :param calendar_type: The calendar_type of this PayrollCalendar.  # noqa: E501
        :type: CalendarType
        """

        self._calendar_type = calendar_type

    @property
    def start_date(self):
        """Gets the start_date of this PayrollCalendar.  # noqa: E501

        The start date of the upcoming pay period. The end date will be calculated based upon this date, and the calendar type selected (YYYY-MM-DD)  # noqa: E501

        :return: The start_date of this PayrollCalendar.  # noqa: E501
        :rtype: date
        """
        return self._start_date

    @start_date.setter
    def start_date(self, start_date):
        """Sets the start_date of this PayrollCalendar.

        The start date of the upcoming pay period. The end date will be calculated based upon this date, and the calendar type selected (YYYY-MM-DD)  # noqa: E501

        :param start_date: The start_date of this PayrollCalendar.  # noqa: E501
        :type: date
        """

        self._start_date = start_date

    @property
    def payment_date(self):
        """Gets the payment_date of this PayrollCalendar.  # noqa: E501

        The date on which employees will be paid for the upcoming pay period (YYYY-MM-DD)  # noqa: E501

        :return: The payment_date of this PayrollCalendar.  # noqa: E501
        :rtype: date
        """
        return self._payment_date

    @payment_date.setter
    def payment_date(self, payment_date):
        """Sets the payment_date of this PayrollCalendar.

        The date on which employees will be paid for the upcoming pay period (YYYY-MM-DD)  # noqa: E501

        :param payment_date: The payment_date of this PayrollCalendar.  # noqa: E501
        :type: date
        """

        self._payment_date = payment_date

    @property
    def payroll_calendar_id(self):
        """Gets the payroll_calendar_id of this PayrollCalendar.  # noqa: E501

        Xero identifier  # noqa: E501

        :return: The payroll_calendar_id of this PayrollCalendar.  # noqa: E501
        :rtype: str
        """
        return self._payroll_calendar_id

    @payroll_calendar_id.setter
    def payroll_calendar_id(self, payroll_calendar_id):
        """Sets the payroll_calendar_id of this PayrollCalendar.

        Xero identifier  # noqa: E501

        :param payroll_calendar_id: The payroll_calendar_id of this PayrollCalendar.  # noqa: E501
        :type: str
        """

        self._payroll_calendar_id = payroll_calendar_id

    @property
    def updated_date_utc(self):
        """Gets the updated_date_utc of this PayrollCalendar.  # noqa: E501

        Last modified timestamp  # noqa: E501

        :return: The updated_date_utc of this PayrollCalendar.  # noqa: E501
        :rtype: datetime
        """
        return self._updated_date_utc

    @updated_date_utc.setter
    def updated_date_utc(self, updated_date_utc):
        """Sets the updated_date_utc of this PayrollCalendar.

        Last modified timestamp  # noqa: E501

        :param updated_date_utc: The updated_date_utc of this PayrollCalendar.  # noqa: E501
        :type: datetime
        """

        self._updated_date_utc = updated_date_utc

    @property
    def validation_errors(self):
        """Gets the validation_errors of this PayrollCalendar.  # noqa: E501

        Displays array of validation error messages from the API  # noqa: E501

        :return: The validation_errors of this PayrollCalendar.  # noqa: E501
        :rtype: list[ValidationError]
        """
        return self._validation_errors

    @validation_errors.setter
    def validation_errors(self, validation_errors):
        """Sets the validation_errors of this PayrollCalendar.

        Displays array of validation error messages from the API  # noqa: E501

        :param validation_errors: The validation_errors of this PayrollCalendar.  # noqa: E501
        :type: list[ValidationError]
        """

        self._validation_errors = validation_errors
