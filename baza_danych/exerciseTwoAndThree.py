from sqlalchemy import create_engine, Column, Integer, String, Float, text
from sqlalchemy.orm import declarative_base, Session

engine = create_engine('sqlite+pysqlite:///:memory:', echo=True, future=True)
Base = declarative_base()


class Student(Base):
    __tablename__ = 'students'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Integer)
    grade = Column(Float)


Base.metadata.create_all(engine)

with Session(engine) as _session:
    _students = [Student(name="Jan Kowalski", age=10, grade=4.1), Student(name="Jan Kowalski 2", age=20, grade=4.2),
                 Student(name="Jan Kowalski 3", age=30, grade=4.3)]
    _session.add_all(_students)
    _session.commit()


def print_all_students():
    with Session(engine) as session:
        students = session.execute(text("SELECT * FROM students")).all()
        for student in students:
            print(f'{student}')


def add_student(student: Student):
    with Session(engine) as session:
        student = Student(name=student.name, age=student.age, grade=student.grade)
        session.add(student)
        session.commit()


def get_student_by_id(student_id):
    with Session(engine) as session:
        student = session.execute(text(f"SELECT * FROM students WHERE id={student_id}")).all()
    return student


def update_student_by_id(student_id, student: Student):
    with Session(engine) as session:
        student_to_update = session.get(Student, student_id)
        if student_to_update:
            student_to_update.name = student.name
            student_to_update.age = student.age
            student_to_update.grade = student.grade
            session.commit()


def delete_student_by_id(student_id):
    with Session(engine) as session:
        student_to_delete = session.get(Student, student_id)
        if student_to_delete:
            session.delete(student_to_delete)
            session.commit()

# print_all_students()
# add_student(Student(name="Jan Kowalski 5", age=15, grade=3.1))
# print(get_student_by_id(2))
# update_student_by_id(2, Student(name="Jan Nowak", age=15, grade=3.1))
# delete_student_by_id(2)
# print_all_students()
