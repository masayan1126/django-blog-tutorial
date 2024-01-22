from dataclasses import dataclass


@dataclass
class TagDomain:
    def __init__(
        self,
        id,
        name: str,
    ):
        self.id = id
        self.name = name

    def __repr__(self):
        return f"TagDomain(id={self.id}, name={self.name})"
