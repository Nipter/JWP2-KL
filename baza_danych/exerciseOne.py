from sqlalchemy import create_engine, text
from sqlalchemy.orm import declarative_base, Session

engine = create_engine('sqlite:///census.sqlite', echo=True, future=True)
Base = declarative_base()


def print_unique_state_names():
    with Session(engine) as session:
        names = session.execute(text("SELECT DISTINCT name FROM state_fact")).all()
        print(f'Number of states {names.__len__()}')
        for name in names:
            print(f'{name}')


def print_population_of_alaska_and_new_york_in_2000_and_2008():
    with Session(engine) as session:
        population_2000_alaska = session.execute(text("SELECT SUM(pop2000) FROM census WHERE state='Alaska'")).all()
        population_2000_new_york = session.execute(text("SELECT SUM(pop2000) FROM census WHERE state='New York'")).all()

        population_2008_alaska = session.execute(text("SELECT SUM(pop2008) FROM census WHERE state='Alaska'")).all()
        population_2008_new_york = session.execute(text("SELECT SUM(pop2008) FROM census WHERE state='New York'")).all()
        print(f'Population of Alaska in 2000: {population_2000_alaska}')
        print(f'Population of Alaska in 2008: {population_2000_new_york}')
        print(f'Population of New York in 2000: {population_2008_alaska}')
        print(f'Population of New York in 2008: {population_2008_new_york}')


def print_sum_of_male_and_femail_in_new_york_in_2008():
    with Session(engine) as session:
        population_2008_new_york_male = session.execute(
            text("SELECT SUM(pop2008) FROM census WHERE state='New York' AND sex='M'")).all()
        population_2008_new_york_femail = session.execute(
            text("SELECT SUM(pop2008) FROM census WHERE state='New York' AND sex='F'")).all()

        print(f'Population of male in New York in 2008: {population_2008_new_york_male}')
        print(f'Population of female in New York in 2008: {population_2008_new_york_femail}')

# print_unique_state_names()
# print_population_of_alaska_and_new_york_in_2000_and_2008()
# print_sum_of_male_and_femail_in_new_york_in_2008()
