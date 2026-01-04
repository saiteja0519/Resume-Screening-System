from db_connection import get_connection

def save_candidate(name, score):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO candidates (name, score) VALUES (%s, %s)",
        (name, score)
    )
    conn.commit()
    conn.close()

def display_ranking():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "SELECT name, score FROM candidates ORDER BY score DESC"
    )
    results = cursor.fetchall()

    print("\n--- Candidate Ranking ---")
    for r in results:
        print(f"Name: {r[0]}, Score: {r[1]}")
    conn.close()
