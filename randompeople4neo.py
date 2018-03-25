""" Creates, in a pseudo-random way, people and relationships among them. Outputs two CSV files. """


import random


USERS_NUM = 50
RELS_NUM = 1000


USER_NAMES = ['Alice', 'Bob', 'Zach', 'Lisa', 'Sara', 'Jack', 'John', 'Brian', 'Peter', 'Alan', 'Rob',
              'James', 'Oliver', 'Charlie', 'George', 'Thomas', 'Oscar', 'William', 'Emily', 'Jessica',
              'Sophie', 'Michael', 'Eric', 'Matthew', 'Amber']

USER_SURNAMES = ['Parker', 'Campbell', 'Smith', 'Brown', 'Johnson', 'Jones', 'Miller', 'Davis', 'Moore',
                 'Walker', 'Martin', 'Jackson', 'White', 'Robinson', 'Clark', 'Wright', 'Adams', 'Baker',
                 'Philips', 'Peterson', 'Watson', 'Price', 'Sullivan']

JOBS = ['Software Developer', 'UX Designer', 'UI Designer', 'System Administrator']


print(str(len(USER_NAMES)) + " Names")
print(str(len(USER_SURNAMES)) + " Surnames")
print("\n")


### OPENING THE USERS DATASET FILE

USERS_FILE = open('users.csv', 'w')


### WRITING THE HEADER IN THE FILE

USERS_FILE.write(':ID,name,surname,birthdate,job,:LABEL\n')


# CREATING THE USERS

for i in range(1, USERS_NUM + 1):
    name_idx = random.randint(0, len(USER_NAMES) - 1)
    surname_idx = random.randint(0, len(USER_SURNAMES) - 1)

    day_birth = random.randint(1, 28)
    month_birth = random.randint(1, 12)
    year_birth = random.randint(1970, 1992)
    birth = str(day_birth) + "-" + str(month_birth) + "-" + str(year_birth)

    name = USER_NAMES[name_idx]
    surname = USER_SURNAMES[surname_idx]

    job_idx = random.randint(0, len(JOBS) - 1)

    job = JOBS[job_idx]

    print(name + " " + surname)

    USERS_FILE.write('"' + str(i) + '","' + name +'","'+ surname + '","' + birth + '","' + job + '"')
    USERS_FILE.write(',Person;' + job +'')
    USERS_FILE.write('\n')



### OPENING THE RELATIONSHIPS DATASET FILE

RELS_FILE = open('rels.csv', 'w')


### WRITING THE HEADER IN THE FILE

RELS_FILE.write(":START_ID,:END_ID,:TYPE\n")


### CREATING THE RELATIONSHIPS

RELATIONSHIPS = []

for i in range(0, RELS_NUM):
    while True:
        start_id = random.randint(1, USERS_NUM)
        end_id = 0

        while True:
            end_id = random.randint(1, USERS_NUM)

            if end_id != start_id:
                break


        RELATIONSHIP_TYPE = "FRIEND_OF"

        RELATIONSHIP_TYPE_bit = random.randint(0, 1)
        if RELATIONSHIP_TYPE_bit == 0:
            RELATIONSHIP_TYPE = "COLLEAGUE_OF"

        rel = str(start_id) + "-" + str(end_id) + "-" + RELATIONSHIP_TYPE
        rel_rec = str(end_id) + "-" + str(start_id) + "-" + RELATIONSHIP_TYPE

        if ((RELATIONSHIP_TYPE_bit == 1 and not rel in RELATIONSHIPS)
                or (RELATIONSHIP_TYPE_bit == 0 and not rel in RELATIONSHIPS and not rel_rec in RELATIONSHIPS)):
            RELATIONSHIPS.append(rel)

            RELS_FILE.write(str(start_id) + "," + str(end_id) + "," + RELATIONSHIP_TYPE + "\n")

            print("### CREATED REL " + str(i))
            break

#~ print(RELATIONSHIPS)


###

USERS_FILE.close()
RELS_FILE.close()
