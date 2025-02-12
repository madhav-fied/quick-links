from pydantic import BaseModel


class URLShorthand(BaseModel):
    shorthand: str
    url: str
    owner: str | None = None
    