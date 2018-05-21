import sys

from .config import ALIBABA_API_ERROR_CODES, ALIBABA_API_CALLS

__all__ = ['AliExpressAPICallError', 'NetworkError', '_e']


class AliExpressAPICallError(Exception):
    def __init__(self, *args, **kwargs):
        Exception.__init__(self)
        self.args = args
        self.call = ALIBABA_API_CALLS[kwargs.pop('call', None)]
        self.code = kwargs.pop('code', None)
        self.msg = ALIBABA_API_ERROR_CODES[self.code]

    def __str__(self):  # pragma: no cover
        if self.code is not None:
            return '%(code)s: %(msg)s. Call: %(call)s' % self.__dict__
        return Exception.__str__(self)


class NetworkError(Exception):
    def __init__(self, *args, **kwargs):
        Exception.__init__(self)
        self.args = args
        self.call = ALIBABA_API_CALLS[kwargs.pop('call', None)]
        self.code = kwargs.pop('code', None)
        self.msg = kwargs.pop('msg', None)

    def __str__(self):  # pragma: no cover
        if self.code is not None:
            return '%(code)s: %(msg)s in %(call)s' % self.__dict__
        return Exception.__str__(self)


def _e(*args, **kwargs):
    """
    Returns an exception of type ``error_class`` based on an instance of
    :class:`AWSError`  all relevant information appended.
    """
    exc = sys.exc_info()[1]
    error = AliExpressAPICallError(*args)
    error.call = exc.call
    error.code = exc.code
    error.msg = exc.msg if exc.msg else None
    return error
