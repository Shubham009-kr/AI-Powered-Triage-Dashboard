class AIProviderError(Exception):
    """Raised when the AI provider cannot complete a request."""


class AIResponseParseError(Exception):
    """Raised when the AI response cannot be parsed."""