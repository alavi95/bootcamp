import psycopg2


def sql_connection():
	conn = psycopg2.connect(
		dbname = sql_db,
		host = sql_endpoint,
		port = '8192',
		user = sql_user,
		password = sql_pw)
	return conn