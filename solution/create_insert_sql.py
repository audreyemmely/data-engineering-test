import psycopg2 
import csv
import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())   

def createInsertTable(csv_name):
    conn = psycopg2.connect(host= os.getenv('DB_HOST'),
                            dbname= os.getenv('DB_NAME'),
                            user= os.getenv('DB_USER'),
                            password= os.getenv('DB_PASSWORD'),
                            port= os.getenv('DB_PORT'))  

    cur = conn.cursor()

    print(f'Creating table dim_anp_{csv_name}...')
    cur.execute(f"""
        CREATE TABLE IF NOT EXISTS anp.dim_anp_{csv_name}
        (
        id              SERIAL NOT NULL PRIMARY KEY,
        year_month      DATE,
        uf              VARCHAR(2),
        product         VARCHAR(21),
        unit            VARCHAR(2),
        volume          DOUBLE PRECISION,
        created_at      TIMESTAMPTZ NOT NULL DEFAULT NOW()    
        );
        
        comment on column anp.dim_anp_{csv_name}.id is 'Chave primária da dimensão';
        comment on column anp.dim_anp_{csv_name}.year_month is 'Data referente às vendas';
        comment on column anp.dim_anp_{csv_name}.uf is 'Sigla das unidades federativas do Brasil';
        comment on column anp.dim_anp_{csv_name}.unit is 'Unidade de medida';
        comment on column anp.dim_anp_{csv_name}.volume is 'Volume vendido';
        comment on column anp.dim_anp_{csv_name}.created_at is 'Data da última carga do registro';""")

    conn.commit()
    print('Table created successfully.')

    print(f'Importing data from csv {csv_name} to database...')
    with open(f'../assets/csv/{csv_name}.csv', 'r') as f:
        reader = csv.reader(f)
        next(reader) # skip the header row
        for row in reader:
            cur.execute(
            f"""INSERT INTO anp.dim_anp_{csv_name} (year_month, uf, product, unit, volume) 
                VALUES (%s, %s, %s, %s, %s);""",
            row
        )
    conn.commit()
    conn.close()
    print('Import completed successfully.\n')