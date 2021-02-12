# coding: utf-8

"""
    Xero Payroll AU API

    This is the Xero Payroll API for orgs in Australia region.  # noqa: E501

    Contact: api@xero.com
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401

from xero_python.models import BaseModel


class PayTemplate(BaseModel):
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
        "earnings_lines": "list[EarningsLine]",
        "deduction_lines": "list[DeductionLine]",
        "super_lines": "list[SuperLine]",
        "reimbursement_lines": "list[ReimbursementLine]",
        "leave_lines": "list[LeaveLine]",
    }

    attribute_map = {
        "earnings_lines": "EarningsLines",
        "deduction_lines": "DeductionLines",
        "super_lines": "SuperLines",
        "reimbursement_lines": "ReimbursementLines",
        "leave_lines": "LeaveLines",
    }

    def __init__(
        self,
        earnings_lines=None,
        deduction_lines=None,
        super_lines=None,
        reimbursement_lines=None,
        leave_lines=None,
    ):  # noqa: E501
        """PayTemplate - a model defined in OpenAPI"""  # noqa: E501

        self._earnings_lines = None
        self._deduction_lines = None
        self._super_lines = None
        self._reimbursement_lines = None
        self._leave_lines = None
        self.discriminator = None

        if earnings_lines is not None:
            self.earnings_lines = earnings_lines
        if deduction_lines is not None:
            self.deduction_lines = deduction_lines
        if super_lines is not None:
            self.super_lines = super_lines
        if reimbursement_lines is not None:
            self.reimbursement_lines = reimbursement_lines
        if leave_lines is not None:
            self.leave_lines = leave_lines

    @property
    def earnings_lines(self):
        """Gets the earnings_lines of this PayTemplate.  # noqa: E501


        :return: The earnings_lines of this PayTemplate.  # noqa: E501
        :rtype: list[EarningsLine]
        """
        return self._earnings_lines

    @earnings_lines.setter
    def earnings_lines(self, earnings_lines):
        """Sets the earnings_lines of this PayTemplate.


        :param earnings_lines: The earnings_lines of this PayTemplate.  # noqa: E501
        :type: list[EarningsLine]
        """

        self._earnings_lines = earnings_lines

    @property
    def deduction_lines(self):
        """Gets the deduction_lines of this PayTemplate.  # noqa: E501


        :return: The deduction_lines of this PayTemplate.  # noqa: E501
        :rtype: list[DeductionLine]
        """
        return self._deduction_lines

    @deduction_lines.setter
    def deduction_lines(self, deduction_lines):
        """Sets the deduction_lines of this PayTemplate.


        :param deduction_lines: The deduction_lines of this PayTemplate.  # noqa: E501
        :type: list[DeductionLine]
        """

        self._deduction_lines = deduction_lines

    @property
    def super_lines(self):
        """Gets the super_lines of this PayTemplate.  # noqa: E501


        :return: The super_lines of this PayTemplate.  # noqa: E501
        :rtype: list[SuperLine]
        """
        return self._super_lines

    @super_lines.setter
    def super_lines(self, super_lines):
        """Sets the super_lines of this PayTemplate.


        :param super_lines: The super_lines of this PayTemplate.  # noqa: E501
        :type: list[SuperLine]
        """

        self._super_lines = super_lines

    @property
    def reimbursement_lines(self):
        """Gets the reimbursement_lines of this PayTemplate.  # noqa: E501


        :return: The reimbursement_lines of this PayTemplate.  # noqa: E501
        :rtype: list[ReimbursementLine]
        """
        return self._reimbursement_lines

    @reimbursement_lines.setter
    def reimbursement_lines(self, reimbursement_lines):
        """Sets the reimbursement_lines of this PayTemplate.


        :param reimbursement_lines: The reimbursement_lines of this PayTemplate.  # noqa: E501
        :type: list[ReimbursementLine]
        """

        self._reimbursement_lines = reimbursement_lines

    @property
    def leave_lines(self):
        """Gets the leave_lines of this PayTemplate.  # noqa: E501


        :return: The leave_lines of this PayTemplate.  # noqa: E501
        :rtype: list[LeaveLine]
        """
        return self._leave_lines

    @leave_lines.setter
    def leave_lines(self, leave_lines):
        """Sets the leave_lines of this PayTemplate.


        :param leave_lines: The leave_lines of this PayTemplate.  # noqa: E501
        :type: list[LeaveLine]
        """

        self._leave_lines = leave_lines
