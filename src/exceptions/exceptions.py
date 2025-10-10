

class AppError(Exception):
    pass


class ValidationError(AppError):
    pass


class CommandParseError(AppError):
    pass


class UnknownCommandError(AppError):
    pass