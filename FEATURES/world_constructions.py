import chromadb

from langchain.vectorstores import Chroma
from langchain_community.embeddings.sentence_transformer import (
    SentenceTransformerEmbeddings,
)

from sentence_transformers import CrossEncoder

import os, sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'DB_and_Azure'))
from sql_db_functions import sql_db_functions as SQLf


import pandas as pd



class world_construction:

    def __init__(self):
        pass

    
    def init_luxury_gallery():
        #try:

        conn, cursor = SQLf.connect_sql()

        query = """
            SELECT product_characteristics.id, Brand_id , Detail, Summary, Brand, Price 
            FROM product_characteristics INNER JOIN Products ON product_characteristics.Brand_id = Products.Brand_Prod_id
            WHERE Brand = 'Gucci' or Brand = 'Prada'
            ;
        """
        cursor.execute(query)
        rows = cursor.fetchall()

        SQLf.close_connection_db(conn=conn,cursor=cursor)

        df = pd.DataFrame(rows, columns=['id', 'prod_id' , 'Detail', 'Summary', 'Brand', 'Price'])

        df['Detail'] = df['Detail'] = df['Detail'].str.replace('\n', ' / ').str.replace(r'\s+', ' ').str.replace('*', ' ')

        df.prod_id = df.prod_id.astype(int)
        df.prod_id.to_numpy

        prod_ids = ",".join(df.prod_id.astype('string').tolist())

        conn, cursor = SQLf.connect_sql()
        query = f"SELECT Brand_id, base64 FROM product_img WHERE Brand_id in ({prod_ids}) ;"
        cursor.execute(query)
        rows_img = cursor.fetchall()

        SQLf.close_connection_db(conn=conn,cursor=cursor)

        
        df_image = pd.DataFrame(rows_img, columns=['prod_id', 'base64']).dropna()

        df_image = df_image.groupby('prod_id')['base64'].apply(list).reset_index()
        
        df = pd.merge(df,df_image, on='prod_id')

    

        return df

        #except:
        #    print('error in luxury gallery SQL pull')


    def init_retail_gallery():
        try:

            conn, cursor = SQLf.connect_sql()

            query = """
                SELECT product_characteristics.id, Brand_id , Detail, Summary, Brand, Price 
                FROM product_characteristics INNER JOIN Products ON product_characteristics.Brand_id = Products.Brand_Prod_id
                WHERE Brand = 'Mango' or Brand = 'HM' or Brand = 'GAP'
                ;
            """
            cursor.execute(query)
            rows = cursor.fetchall()

            SQLf.close_connection_db(conn=conn,cursor=cursor)

            df = pd.DataFrame(rows, columns=['id', 'prod_id' , 'Detail', 'Summary', 'Brand', 'Price'])

            df['Detail'] = df['Detail'] = df['Detail'].str.replace('\n', ' / ').str.replace(r'\s+', ' ').str.replace('*', ' ')

            df.prod_id = df.prod_id.astype(int)
            df.prod_id.to_numpy

            prod_ids = ",".join(df.prod_id.astype('string').tolist())

            conn, cursor = SQLf.connect_sql()
            query = f"SELECT Brand_id, base64 FROM product_img WHERE Brand_id in ({prod_ids}) ;"
            cursor.execute(query)
            rows_img = cursor.fetchall()

            SQLf.close_connection_db(conn=conn,cursor=cursor)

            
            df_image = pd.DataFrame(rows_img, columns=['prod_id', 'base64']).dropna()

            df_image = df_image.groupby('prod_id')['base64'].apply(list).reset_index()
            
            df = pd.merge(df,df_image, on='prod_id')

        

            return df

        except:
            print('error in luxury gallery SQL pull')



    def init_chroma_db():


        client = chromadb.HttpClient(host='localhost',port=8000)
        #collection = client.get_collection(name="multi_modal_rag")

        embedding = Cf.get_embeddings() 

        vectorstore = Chroma(
            client=client,
            collection_name="RAG-Child",
            embedding_function=embedding,
        )    
        
        return vectorstore
    
    def init_model_crossencoder():

        model_crossencoder = CrossEncoder('cross-encoder/ms-marco-MiniLM-L-6-v2', max_length=512)

        return model_crossencoder
    
    
    
