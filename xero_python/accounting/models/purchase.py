# coding: utf-8

"""
    Accounting API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    OpenAPI spec version: 2.3.0
    Contact: api@xero.com
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401

from xero_python.models import BaseModel


class Purchase(BaseModel):
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
        "unit_price": "float",
        "account_code": "str",
        "cogs_account_code": "str",
        "tax_type": "str",
    }

    attribute_map = {
        "unit_price": "UnitPrice",
        "account_code": "AccountCode",
        "cogs_account_code": "COGSAccountCode",
        "tax_type": "TaxType",
    }

    def __init__(
        self, unit_price=None, account_code=None, cogs_account_code=None, tax_type=None
    ):  # noqa: E501
        """Purchase - a model defined in OpenAPI"""  # noqa: E501

        self._unit_price = None
        self._account_code = None
        self._cogs_account_code = None
        self._tax_type = None
        self.discriminator = None

        if unit_price is not None:
            self.unit_price = unit_price
        if account_code is not None:
            self.account_code = account_code
        if cogs_account_code is not None:
            self.cogs_account_code = cogs_account_code
        if tax_type is not None:
            self.tax_type = tax_type

    @property
    def unit_price(self):
        """Gets the unit_price of this Purchase.  # noqa: E501

        Unit Price of the item. By default UnitPrice is rounded to two decimal places. You can use 4 decimal places by adding the unitdp=4 querystring parameter to your request.  # noqa: E501

        :return: The unit_price of this Purchase.  # noqa: E501
        :rtype: float
        """
        return self._unit_price

    @unit_price.setter
    def unit_price(self, unit_price):
        """Sets the unit_price of this Purchase.

        Unit Price of the item. By default UnitPrice is rounded to two decimal places. You can use 4 decimal places by adding the unitdp=4 querystring parameter to your request.  # noqa: E501

        :param unit_price: The unit_price of this Purchase.  # noqa: E501
        :type: float
        """

        self._unit_price = unit_price

    @property
    def account_code(self):
        """Gets the account_code of this Purchase.  # noqa: E501

        Default account code to be used for purchased/sale. Not applicable to the purchase details of tracked items  # noqa: E501

        :return: The account_code of this Purchase.  # noqa: E501
        :rtype: str
        """
        return self._account_code

    @account_code.setter
    def account_code(self, account_code):
        """Sets the account_code of this Purchase.

        Default account code to be used for purchased/sale. Not applicable to the purchase details of tracked items  # noqa: E501

        :param account_code: The account_code of this Purchase.  # noqa: E501
        :type: str
        """

        self._account_code = account_code

    @property
    def cogs_account_code(self):
        """Gets the cogs_account_code of this Purchase.  # noqa: E501

        Cost of goods sold account. Only applicable to the purchase details of tracked items.  # noqa: E501

        :return: The cogs_account_code of this Purchase.  # noqa: E501
        :rtype: str
        """
        return self._cogs_account_code

    @cogs_account_code.setter
    def cogs_account_code(self, cogs_account_code):
        """Sets the cogs_account_code of this Purchase.

        Cost of goods sold account. Only applicable to the purchase details of tracked items.  # noqa: E501

        :param cogs_account_code: The cogs_account_code of this Purchase.  # noqa: E501
        :type: str
        """

        self._cogs_account_code = cogs_account_code

    @property
    def tax_type(self):
        """Gets the tax_type of this Purchase.  # noqa: E501

        The tax type from TaxRates  # noqa: E501

        :return: The tax_type of this Purchase.  # noqa: E501
        :rtype: str
        """
        return self._tax_type

    @tax_type.setter
    def tax_type(self, tax_type):
        """Sets the tax_type of this Purchase.

        The tax type from TaxRates  # noqa: E501

        :param tax_type: The tax_type of this Purchase.  # noqa: E501
        :type: str
        """

        self._tax_type = tax_type
