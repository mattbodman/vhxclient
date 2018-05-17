#!/usr/bin/env python2


class UnauthorizedError(Exception):
    pass


class BadRequestError(Exception):
    pass


class PaymentRequiredError(Exception):
    pass


class NotFoundError(Exception):
    pass


class NotAcceptableError(Exception):
    pass


class InternalServerError(Exception):
    pass


class NoIdError(Exception):
    pass


class InvalidReportTypeError(Exception):
    pass
