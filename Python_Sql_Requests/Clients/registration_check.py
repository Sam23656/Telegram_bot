from Python_Sql_Requests.connect_database import run_connection


def registration_check(client_id: str):
    connect, cursor = run_connection()
    cursor.execute(f"SELECT * FROM check_client_contact_info('{client_id}')")
    connect.commit()
    result = cursor.fetchone()
    result = result[0]
    return result
