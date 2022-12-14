from typing import  List
from .Manager import Manager
from .Program import Program
from .Student import Student
from ..dtos.Status import Status


class College:

    def __init__(self, name: str) -> None:
        self.name = name
        self.managers: List[Manager] = []
        self.programs: List[Program] = []
        self.students: List[Student] = []

    def add_manager(self, new_manager: Manager) -> Status:
        if new_manager.college != None:
            return Status(False, "The manager already exists")
        new_manager.college = self
        self.managers.append(new_manager)
        return Status(True, "Successfully added manager")

    def add_student(self, new_student: Student) -> Status:
        if new_student.college != None:
            return Status(False, "The student already exists")
        new_student.college = self
        self.students.append(new_student)
        return Status(True, "Successfully added student")

    def add_program(self, new_program: Program) -> Status:
        if new_program.college != None:
            return Status(False, "The program already exists")
        new_program.college = self
        self.programs.append(new_program)
        return Status(True, "Successfully added program")

    def get_manager_by_username(self, username: str) -> Manager:
        for manager in self.managers:
            if manager.username == username:
                return manager
        return None

    def get_student_by_id(self, id: str) -> Student:
        for student in self.students:
            if student.student_id == id:
                return student
        return None
