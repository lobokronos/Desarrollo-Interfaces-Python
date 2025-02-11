import cx_Oracle

DB_USER= "SYS"
DB_PASSWORD = "1234"
DB_DSN="localhost/XEPDB1"

def conectar_bd():
    conexion=cx_Oracle.connect(DB_USER,DB_PASSWORD,DB_DSN)
    cursor=conexion.cursor()

    ##CREAR LA TABLA DE USUARIOS SI NO EXISTE

    cursor.execute("""
        BEGIN
            EXECUTE INMEDIATE 'CREATE TABLE usuarios_DI(
                id_usuario NUMBER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
                nombre_usuario VARCHAR(50) UNIQUE NOT NULL,
                password VARCHAR3(100) NOT NULL
                )';
            EXCEPTION
                WHEN OTHERS THEN
                    IF SQLCODE!=-955 THEN RAISE END IF;
                END;
        """)

    ##CREAR LA TABLA DE FAVORITOS

    cursor.execute("""
        BEGIN
            EXECUTE INMEDIATE 'CREATE TABLE favoritoss_DI(
                id_favorito NUMBER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
                id_usuario NUMBBER REFERENCES usuarios_DI(id_usuario),
                url_imagen VARCHAR(255) NOT NULL,
                )';
            EXCEPTION
                WHEN OTHERS THEN
                    IF SQLCODE!=-955 THEN RAISE END IF;
                END;
        """)

    conexion.commit()
    return conexion


if __name__ == '__main__':
    conexion = conectar_bd()
