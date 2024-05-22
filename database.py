from dotenv import load_dotenv
import psycopg2
import os

load_dotenv()

def connect_db():
    try:
        conn = psycopg2.connect(
            host=os.getenv('DB_HOST'),
            dbname=os.getenv('DB_NAME'),
            user=os.getenv('DB_USER'),
            password=os.getenv('DB_PASS'),
            port=os.getenv('DB_PORT')
        )
        return conn
    except psycopg2.OperationalError as e:
        print(f"Falha ao conectar ao banco de dados: {e}")
    except Exception as e:
        print(f"Um erro inesperado ocorreu: {e}")
    
def executar_query(query, parametros):
    conn = connect_db()
    if conn is not None:
        try:
            with conn.cursor() as cur:
                cur.execute(query, parametros)
                conn.commit()
                return "Dados inseridos com sucesso"
        except psycopg2.Error as e:
            conn.rollback()
            return f"Falha ao inserir dados: {str(e)}"
        finally:
            conn.close()
    else:
        return "Conexão com o banco de dados não foi estabelecida."
    
def insert_cadastro_sistema(login,nome_prof,senha):
    query = """INSERT INTO usuarios (login, nome_professor, senha) VALUES (%s, %s, %s)"""

    parametros = (login, nome_prof, senha)
    return executar_query(query, parametros)

def insert_identificacao_aluno(nis, nome_aluno, sexo_aluno, nascimento_uf, nascimento_municipio,
                               cartorio_uf, nome_cartorio, cartorio_municipio, data_exp_identidade,
                               orgao_emissor, uf_identidade, cpf, raca_aluno):

    query = """
        INSERT INTO identificacao_aluno 
        (NIS, nome_aluno, sexo, UF, local_nascimento_municipio,
         uf_cartorio, nome_cartorio, data_expedicao_identidade,
         orgao_emissor, uf_identidade, cpf, aluno_raca, municipio_cartorio)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """
    parametros = (nis, nome_aluno, sexo_aluno, nascimento_uf, nascimento_municipio,
              cartorio_uf, nome_cartorio, data_exp_identidade,
              orgao_emissor, uf_identidade, cpf, raca_aluno, cartorio_municipio)
    return executar_query(query, parametros)


def insert_certidao(num_matricula_registro_civil, num_termo, livro, folha, data_expedicao_certidao):

    query = """
        INSERT INTO certidao 
        (num_matricula_registro_civil, num_termo, livro, folha, data_expedicao_certidao)
        VALUES ( %s, %s, %s, %s,%s)
    """
    parametros = (num_matricula_registro_civil, num_termo, livro, folha, data_expedicao_certidao)
    return executar_query(query, parametros)


def insert_saude(autismo, rett, asperger, transtorno_desintegrativo,
                 baixa_visao, cegueira, auditiva, intelectual, fisica,
                 multipla, sindrome_down, surdez, surdocegueira, altas_habilidades):
    query = """
        INSERT INTO saude (autismo, rett, asperger, transtorno_desintegrativo,
                                       baixa_visao, cegueira, auditiva, intelectual, fisica,
                                       multipla, sindrome_down, surdez, surdocegueira, altas_habilidades)
                    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """
    parametros = (autismo, rett, asperger, transtorno_desintegrativo,
                      baixa_visao, cegueira, auditiva, intelectual, fisica,
                      multipla, sindrome_down, surdez, surdocegueira, altas_habilidades)
    return executar_query(query, parametros)


def insert_endereco(endereco, complemento, numero_endereco, municipio, bairro, cep, zona, telefone, email, uf):

    query = """
        INSERT INTO endereco (endereco, complemento, numero_endereco, municipio, bairro, cep, telefone, email, uf, zona)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """
    parametros = (endereco, complemento, numero_endereco, municipio, bairro, cep, telefone, email, uf, zona)
    return executar_query(query, parametros)


def insert_dados_pais_responsavel(nome_mae, nome_pai):
    query = """
        INSERT INTO dados_pais_responsavel 
        (nome_mae, nome_pai)
        VALUES (%s, %s)
    """
    parametros = (nome_mae, nome_pai)
    return executar_query(query, parametros)


def insert_informacoes_matricula(nome_escola, cod_censo, data_ingresso_escola, matricula, data_matricula,
                                 codigo_turma, participa_programa, transporte_escolar, turno, codigo_serie, codigo_procedencia):

    query = """
        INSERT INTO informacoes_matricula
        (nome_escola, cod_censo, data_ingresso_escola, matricula, data_matricula, codigo_turma, participa_programa, transporte_escolar, turno, codigo_serie, codigo_procedencia)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """
    parametros = (nome_escola, cod_censo, data_ingresso_escola, matricula, data_matricula,
                                 codigo_turma, participa_programa, transporte_escolar, turno, codigo_serie, codigo_procedencia)
    
    return executar_query(query, parametros)

def insert_solicitacao_matricula(nome_aluno, matricula, codigo_turma, turno, codigo_serie, ano_letivo, documentos_pendentes):
    query = """
        INSERT INTO solicitacao_matricula
        (nome_aluno, matricula, codigo_turma, turno, codigo_serie, ano_letivo, documentos_pendentes)
        VALUES (%s, %s, %s, %s, %s, %s, %s)
    """
    parametros = (nome_aluno, matricula, codigo_turma, turno, codigo_serie, ano_letivo, documentos_pendentes)
    return executar_query(query, parametros)

def verifica_login(login):
    conn = connect_db()

    if conn is not None:
        try:
            with conn.cursor() as cur:
                query = "SELECT * FROM usuarios WHERE login = %s"
                cur.execute(query, (login,))
                dados = cur.fetchall()
                return len(dados) > 0
            
        except psycopg2.Error as e:
             print(f"Database error: {str(e)}")
             return False
        finally:
            conn.close()
    else:
        print("Conexão com o banco de dados não foi estabelecida.")
        return False

def realiza_login(login, senha):
    conn = connect_db()

    if conn is not None:
        try:
            with conn.cursor() as cur:
                query = "SELECT * FROM usuarios WHERE login = %s AND senha = %s"
                cur.execute(query, (login, senha))
                dados = cur.fetchall()

                return bool(dados)
            
        except psycopg2.Error as e:
             print(f"Database error: {str(e)}")
             return False
        finally:
            conn.close()
    else:
        print("Conexão com o banco de dados não foi estabelecida.")
        return False