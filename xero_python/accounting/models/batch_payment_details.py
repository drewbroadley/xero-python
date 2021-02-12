# coding: utf-8

"""
    Xero Accounting API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    Contact: api@xero.com
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401

from xero_python.models import BaseModel


class BatchPaymentDetails(BaseModel):
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
        "bank_account_number": "str",
        "bank_account_name": "str",
        "details": "str",
        "code": "str",
        "reference": "str",
    }

    attribute_map = {
        "bank_account_number": "BankAccountNumber",
        "bank_account_name": "BankAccountName",
        "details": "Details",
        "code": "Code",
        "reference": "Reference",
    }

    def __init__(
        self,
        bank_account_number=None,
        bank_account_name=None,
        details=None,
        code=None,
        reference=None,
    ):  # noqa: E501
        """BatchPaymentDetails - a model defined in OpenAPI"""  # noqa: E501

        self._bank_account_number = None
        self._bank_account_name = None
        self._details = None
        self._code = None
        self._reference = None
        self.discriminator = None

        if bank_account_number is not None:
            self.bank_account_number = bank_account_number
        if bank_account_name is not None:
            self.bank_account_name = bank_account_name
        if details is not None:
            self.details = details
        if code is not None:
            self.code = code
        if reference is not None:
            self.reference = reference

    @property
    def bank_account_number(self):
        """Gets the bank_account_number of this BatchPaymentDetails.  # noqa: E501

        Bank account number for use with Batch Payments  # noqa: E501

        :return: The bank_account_number of this BatchPaymentDetails.  # noqa: E501
        :rtype: str
        """
        return self._bank_account_number

    @bank_account_number.setter
    def bank_account_number(self, bank_account_number):
        """Sets the bank_account_number of this BatchPaymentDetails.

        Bank account number for use with Batch Payments  # noqa: E501

        :param bank_account_number: The bank_account_number of this BatchPaymentDetails.  # noqa: E501
        :type: str
        """

        self._bank_account_number = bank_account_number

    @property
    def bank_account_name(self):
        """Gets the bank_account_name of this BatchPaymentDetails.  # noqa: E501

        Name of bank for use with Batch Payments  # noqa: E501

        :return: The bank_account_name of this BatchPaymentDetails.  # noqa: E501
        :rtype: str
        """
        return self._bank_account_name

    @bank_account_name.setter
    def bank_account_name(self, bank_account_name):
        """Sets the bank_account_name of this BatchPaymentDetails.

        Name of bank for use with Batch Payments  # noqa: E501

        :param bank_account_name: The bank_account_name of this BatchPaymentDetails.  # noqa: E501
        :type: str
        """

        self._bank_account_name = bank_account_name

    @property
    def details(self):
        """Gets the details of this BatchPaymentDetails.  # noqa: E501

        (Non-NZ Only) These details are sent to the org’s bank as a reference for the batch payment transaction. They will also show with the batch payment transaction in the bank reconciliation Find & Match screen. Depending on your individual bank, the detail may also show on the bank statement imported into Xero. Maximum field length = 18  # noqa: E501

        :return: The details of this BatchPaymentDetails.  # noqa: E501
        :rtype: str
        """
        return self._details

    @details.setter
    def details(self, details):
        """Sets the details of this BatchPaymentDetails.

        (Non-NZ Only) These details are sent to the org’s bank as a reference for the batch payment transaction. They will also show with the batch payment transaction in the bank reconciliation Find & Match screen. Depending on your individual bank, the detail may also show on the bank statement imported into Xero. Maximum field length = 18  # noqa: E501

        :param details: The details of this BatchPaymentDetails.  # noqa: E501
        :type: str
        """

        self._details = details

    @property
    def code(self):
        """Gets the code of this BatchPaymentDetails.  # noqa: E501

        (NZ Only) Optional references for the batch payment transaction. It will also show with the batch payment transaction in the bank reconciliation Find & Match screen. Depending on your individual bank, the detail may also show on the bank statement you import into Xero.  # noqa: E501

        :return: The code of this BatchPaymentDetails.  # noqa: E501
        :rtype: str
        """
        return self._code

    @code.setter
    def code(self, code):
        """Sets the code of this BatchPaymentDetails.

        (NZ Only) Optional references for the batch payment transaction. It will also show with the batch payment transaction in the bank reconciliation Find & Match screen. Depending on your individual bank, the detail may also show on the bank statement you import into Xero.  # noqa: E501

        :param code: The code of this BatchPaymentDetails.  # noqa: E501
        :type: str
        """
        if code is not None and len(code) > 12:
            raise ValueError(
                "Invalid value for `code`, " "length must be less than or equal to `12`"
            )  # noqa: E501

        self._code = code

    @property
    def reference(self):
        """Gets the reference of this BatchPaymentDetails.  # noqa: E501

        (NZ Only) Optional references for the batch payment transaction. It will also show with the batch payment transaction in the bank reconciliation Find & Match screen. Depending on your individual bank, the detail may also show on the bank statement you import into Xero.  # noqa: E501

        :return: The reference of this BatchPaymentDetails.  # noqa: E501
        :rtype: str
        """
        return self._reference

    @reference.setter
    def reference(self, reference):
        """Sets the reference of this BatchPaymentDetails.

        (NZ Only) Optional references for the batch payment transaction. It will also show with the batch payment transaction in the bank reconciliation Find & Match screen. Depending on your individual bank, the detail may also show on the bank statement you import into Xero.  # noqa: E501

        :param reference: The reference of this BatchPaymentDetails.  # noqa: E501
        :type: str
        """
        if reference is not None and len(reference) > 12:
            raise ValueError(
                "Invalid value for `reference`, "
                "length must be less than or equal to `12`"
            )  # noqa: E501

        self._reference = reference
