import psycopg
from psycopg.rows import dict_row

db_connection=psycopg.connect(host='localhost' ,dbname='Learning',user='postgres',password='password',row_factory=dict_row)

def fn_saveoperation(json_data):
    try:
        with db_connection.cursor() as db_operation:
            db_operation.execute('INSERT INTO weatherreport(city_name,received_time,timezone,temperature,humidity,wind_speed,is_hot,is_rainy)'
                                 'VALUES (%s,%s,%s,%s,%s,%s,%s,%s)',(json_data['city'],json_data['time'],json_data['timezone'],json_data['temperature'],json_data['humidity'],json_data['wind speed'],json_data['is_hot'],json_data['is_rainy']))
            insert_count=db_operation.rowcount
            if insert_count==1:
                db_connection.commit()
                return 'Insert Successfully happen'
            else:
                return 'Insert not happen'
    except psycopg.Error as e:
        db_connection.rollback()
        print(f'Database error: {e}')
        return 'Insert failed'


