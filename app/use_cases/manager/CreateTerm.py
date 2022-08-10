from ...model.College import College
from ...model.Term import Term
from ..Base import Base


class CreateTerm(Base):

    def __init__(self, college: College) -> None:
        super().__init__()
        self.college = college

    def execute(self) -> Term:
        pass