import psycopg2
import toml


def json_parser(data, header) -> str:
    return data.dict().get(
        header
    )


def charge_toml(header: str, name_variable: str):
    conf = toml.load(f'/mnt/napster_disk/Neural coders/software/fast_api_test/configurations.toml')
    return conf.get(f'{header}').get(f'{name_variable}')


def connection_database(hostname: str, username: str, password: str, database: str, port: str):
    return psycopg2.connect(host=hostname, user=username, password=password, dbname=database, port=port,
                            sslmode='require', sslrootcert='ca-certificate.crt')


def send_data_to_db(email: str, usr: str):
    host = charge_toml("connect_postgres", "host")
    database = charge_toml("connect_postgres", "database")
    user = charge_toml("connect_postgres", "user")
    password = charge_toml("connect_postgres", "password")
    port = charge_toml("connect_postgres", "port")
    conn = connection_database(hostname=host, username=user, password=password, database=database, port=port)
    conn.execute(f"insert into data_api (email, user) values ('{email}', '{usr}')")
    conn.commit()
    conn.close()
