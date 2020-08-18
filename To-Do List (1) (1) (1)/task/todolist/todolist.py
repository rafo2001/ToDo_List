# Write your code here
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Date
from datetime import datetime, timedelta
from sqlalchemy.orm import sessionmaker

Base = declarative_base()


class Table(Base):
    __tablename__ = 'task'
    id = Column(Integer, primary_key=True)
    task = Column(String, default='')
    deadline = Column(Date, default=datetime.today())

    def __repr__(self):
        return self.task


class ToDoList:
    def __init__(self, file_name):
        # self.session = None
        engine = create_engine(f'sqlite:///{file_name}?check_same_thread=False')
        Base.metadata.create_all(engine)
        session = sessionmaker(bind=engine)
        self.session = session()
        self.today = datetime.today()
        self.week_days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

    def query_today_tasks(self):
        rows = self.session.query(Table).filter(Table.deadline == self.today.date()).all()
        i = 0
        print()
        print(f"Today {self.today.day} {self.today.strftime('%b')}:")
        for row in rows:
            i += 1
            print(f"{str(i)}. {row}")
        if i == 0:
            print("Nothing to do!")

    def query_week_tasks(self):
        for day in range(7):
            target_date = self.today + timedelta(days=day)
            rows = self.session.query(Table).filter(Table.deadline == target_date.date()).all()
            i = 0
            print()
            print(f"{self.week_days[target_date.weekday()]} {target_date.day} {target_date.strftime('%b')}:")
            for row in rows:
                i += 1
                print(f"{str(i)}. {row}")
            if i == 0:
                print("Nothing to do!")

    def query_all_tasks(self, text):
        rows = self.session.query(Table).order_by(Table.deadline).all()
        i = 0
        print()
        print(text)
        for row in rows:
            i += 1
            due_date = row.deadline
            print(f"{str(i)}. {row}. {due_date.day} {due_date.strftime('%b')}")
        if i == 0:
            print("Nothing to do!")
            return False
        return True

    def query_missed_tasks(self):
        rows = self.session.query(Table).filter(Table.deadline < self.today.date()).order_by(Table.deadline).all()
        i = 0
        print()
        print("Missed tasks:")
        for row in rows:
            i += 1
            due_date = row.deadline
            print(f"{str(i)}. {row}. {due_date.day} {due_date.strftime('%b')}")
        if i == 0:
            print("Nothing is missed!")

    def delete_tasks(self):
        if self.query_all_tasks("Choose the number of the task you want to delete:"):
            row_number = int(input())
            self.delete_row(row_number - 1)

    def delete_row(self, row_number):
        rows = self.session.query(Table).order_by(Table.deadline).all()
        row_to_delete = rows[row_number]
        self.session.delete(row_to_delete)
        self.session.commit()
        print("The task has been deleted!")

    def insert_task(self, task, deadline):
        new_row = Table(task=task, deadline=datetime.strptime(deadline, '%Y-%m-%d').date())
        self.session.add(new_row)
        self.session.commit()
        print("The task has been added!")

    def get_task(self):
        print()
        new_task = input("Enter task\n")
        new_date = input("Enter deadline\n")
        self.insert_task(new_task, new_date)


filename = "todo.db"
mi_tabla = ToDoList(filename)
while True:
    print()
    print("1) Today's tasks\n2) Week's tasks\n3) All tasks\n4) Missed tasks\n"
          "5) Add task\n6) Delete task\n0) Exit")
    opcion = int(input())
    if opcion == 1:
        mi_tabla.query_today_tasks()
    elif opcion == 2:
        mi_tabla.query_week_tasks()
    elif opcion == 3:
        mi_tabla.query_all_tasks("All tasks:")
    elif opcion == 4:
        mi_tabla.query_missed_tasks()
    elif opcion == 5:
        mi_tabla.get_task()
    elif opcion == 6:
        mi_tabla.delete_tasks()
    elif opcion == 0:
        print()
        print("Bye!")
        break
