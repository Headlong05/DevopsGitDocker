from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
import psycopg2

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


def create_table():
    conn = psycopg2.connect(
        host='db',
        user='artem',
        password='123',
        database='postgres'
    )
    cur = conn.cursor()

    cur.execute("""DROP TABLE IF EXISTS students;""")

    cur.execute("""CREATE TABLE IF NOT EXISTS students 
        (id SERIAL PRIMARY KEY,
        name VARCHAR(100), 
        age INTEGER, 
        major VARCHAR(50))
    """)

    cur.execute("""INSERT INTO students (name, age, major) VALUES
        ('Алиса', 20, 'Computer Science'),
        ('Александр', 22, 'Mathematics'),
        ('Виктория', 21, 'Physics'),
        ('Диана', 23, 'Chemistry'),
        ('Даша', 20, 'Biology');
    """)

    conn.commit()
    cur.close()
    conn.close()

    print('Таблица создана')


@app.on_event("startup")
def startup():
    create_table()


@app.get("/search")
async def search(query: str = None):
    conn = psycopg2.connect(
        host='db',
        user='artem',
        password='123',
        database='postgres'
    )
    cur = conn.cursor()

    if query:
        cur.execute("SELECT * FROM students WHERE name LIKE %s", (f"%{query.capitalize()}%",))
    else:
        cur.execute("SELECT * FROM students")

    data = cur.fetchall()

    cur.close()
    conn.close()

    return [{"id": item[0], "name": item[1], "age": item[2], "major": item[3]} for item in data]
