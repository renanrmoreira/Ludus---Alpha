CREATE TABLE identificacao_aluno (
    id SERIAL PRIMARY KEY,
    NIS INT,
    nome_aluno VARCHAR(100),
    sexo CHAR(1),
    UF VARCHAR(2),
    local_nascimento_municipio VARCHAR(100),
    uf_cartorio VARCHAR(2),
    municipio_cartório VARCHAR(100),
    nome_cartorio VARCHAR(100),
    identidade_docEstrangeiro_passaporte VARCHAR(100),
    data_expedicao_identidade DATE,
    orgao_emissor VARCHAR(2),
    uf_identidade VARCHAR(2),
    cpf VARCHAR(11)
);
ALTER TABLE identificacao_aluno ADD COLUMN aluno_raca varchar(50);

CREATE TABLE certidao (
	id_certidao SERIAL PRIMARY KEY,
    id_aluno INT,
    num_matricula_registro_civil VARCHAR(100), -- certidão nova
    num_termo VARCHAR(50), -- certidão antiga
    livro VARCHAR(10), -- certidão antiga
    folha VARCHAR(10), -- certidão antiga
    data_expedicao_certidao DATE,
    FOREIGN KEY (id_aluno) REFERENCES identificacao_aluno(id)
);

CREATE TABLE saude (
    id_saude SERIAL PRIMARY KEY,
    id_aluno INT,
    autismo BOOLEAN DEFAULT FALSE,
    rett BOOLEAN DEFAULT FALSE,
    asperger BOOLEAN DEFAULT FALSE,
    transtorno_desintegrativo BOOLEAN DEFAULT FALSE,
    baixa_visao BOOLEAN DEFAULT FALSE,
    cegueira BOOLEAN DEFAULT FALSE,
    auditiva BOOLEAN DEFAULT FALSE,
    intelectual BOOLEAN DEFAULT FALSE,
    fisica BOOLEAN DEFAULT FALSE,
    multipla BOOLEAN DEFAULT FALSE,
    sindrome_down BOOLEAN DEFAULT FALSE,
    surdez BOOLEAN DEFAULT FALSE,
    surdocegueira BOOLEAN DEFAULT FALSE,
    altas_habilidades BOOLEAN DEFAULT FALSE,
    superdotacao BOOLEAN DEFAULT FALSE,
    FOREIGN KEY (id_aluno) REFERENCES identificacao_aluno(id)
);

CREATE TABLE endereco (
	id_endereco SERIAL PRIMARY KEY,
    id_aluno INT,
    endereco VARCHAR(255),
    complemento VARCHAR(200),
    numero_endereco INT,
    municipio VARCHAR(100),
    bairro VARCHAR(100),
    cep INT,
    zona VARCHAR(3),
    telefone BIGINT,
    email VARCHAR(255),
    FOREIGN KEY (id_aluno) REFERENCES identificacao_aluno(id)
);

ALTER TABLE endereco ADD COLUMN uf varchar(2);

CREATE TABLE dados_pais_responsavel (
	id_dados_pais_responsavel SERIAL PRIMARY KEY,
    id_aluno INT,
    nome_mae VARCHAR(200),
    nome_pai VARCHAR(200),
    FOREIGN KEY (id_aluno) REFERENCES identificacao_aluno(id)
);

CREATE TABLE informacoes_matricula (
	id_informacoes_matricula SERIAL PRIMARY KEY,
    id_aluno INT,
    nome_escola VARCHAR(255),
    cod_censo_inep INT,
    data_ingresso_escola DATE,
    matricula INT,
    data_matricula DATE,
    codigo_turma INT,
    turno CHAR(1),
    codigo_serie INT,
    ano_letivo INT,
    codigo_procedencia INT,
    participa_programa BOOLEAN,
    transporte_escolar BOOLEAN,
    num_docs_apresentados INT,
    FOREIGN KEY (id_aluno) REFERENCES identificacao_aluno(id)
);
ALTER TABLE informacoes_matricula DROP COLUMN num_docs_apresentados;
ALTER TABLE informacoes_matricula DROP COLUMN ano_letivo;


CREATE TABLE solicitacao_matricula (
    id_aluno INT,
    nome_aluno VARCHAR(200),
    matricula INT,
    codigo_turma INT,
    turno CHAR(1),
    codigo_serie INT,
    ano_letivo INT,
    documentos_pendentes BOOLEAN,
    FOREIGN KEY (id_aluno) REFERENCES identificacao_aluno(id)
);

CREATE TABLE usuarios (
    id_usuario SERIAL PRIMARY KEY,
    login VARCHAR(255) UNIQUE,
    senha VARCHAR(255),
    nome_professor VARCHAR(255)
);

-- Drop de superdotacao que não estava sendo utilizado

ALTER TABLE saude DROP COLUMN superdotacao;

--Trocando zona de 2 digitos para 6

ALTER TABLE endereco ADD COLUMN zn varchar(6);

UPDATE endereco SET zn = zona;

ALTER TABLE endereco DROP COLUMN zona;

ALTER TABLE endereco RENAME COLUMN zn TO zona;

--Alterando turno de 1 para 13 digitos

ALTER TABLE informacoes_matricula ADD COLUMN tr varchar(13);

UPDATE informacoes_matricula SET tr = turno;

ALTER TABLE informacoes_matricula DROP COLUMN turno;

ALTER TABLE informacoes_matricula RENAME COLUMN tr TO turno;

--Alterando serio e cod procedencia para varchar

ALTER TABLE informacoes_matricula ADD COLUMN cd varchar(255);

UPDATE informacoes_matricula SET cd = codigo_serie;

ALTER TABLE informacoes_matricula DROP COLUMN codigo_serie;

ALTER TABLE informacoes_matricula RENAME COLUMN cd TO codigo_serie;



ALTER TABLE informacoes_matricula ADD COLUMN cd varchar(255);

UPDATE informacoes_matricula SET cd = codigo_procedencia;

ALTER TABLE informacoes_matricula DROP COLUMN codigo_procedencia;

ALTER TABLE informacoes_matricula RENAME COLUMN cd TO codigo_procedencia;

CREATE FUNCTION inserir_certidao_automaticamente()
RETURNS TRIGGER AS $$
BEGIN
  INSERT INTO certidao (id_aluno, num_matricula_registro_civil, num_termo, livro, folha, data_expedicao_certidao)
  VALUES (NEW.id, 'default_value', 'default_value', 'default_value', 'default_value', 'default_value');
  RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER trigger_inserir_certidao AFTER INSERT ON identificacao_aluno
FOR EACH ROW EXECUTE FUNCTION inserir_certidao_automaticamente();

CREATE OR REPLACE FUNCTION inserir_saude_automaticamente()
RETURNS TRIGGER AS $$
BEGIN
  INSERT INTO saude (id_aluno, autismo, rett, asperger, transtorno_desintegrativo, baixa_visao, cegueira, auditiva, intelectual, fisica, multipla, sindrome_down, surdez, surdocegueira, altas_habilidades)
  VALUES (NEW.id, FALSE, FALSE, FALSE, FALSE, FALSE, FALSE, FALSE, FALSE, FALSE, FALSE, FALSE, FALSE, FALSE, FALSE);
  RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER trigger_inserir_saude
AFTER INSERT ON identificacao_aluno
FOR EACH ROW
EXECUTE FUNCTION inserir_saude_automaticamente();


CREATE OR REPLACE FUNCTION inserir_endereco_automaticamente()
RETURNS TRIGGER AS $$
BEGIN
  INSERT INTO endereco (id_aluno, endereco, complemento, numero_endereco, municipio, bairro, cep, zona, telefone, email, uf)
  VALUES (NEW.id, '', '', 0, '', '', 0, '', 0, '', '');
  RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER trigger_inserir_endereco
AFTER INSERT ON identificacao_aluno
FOR EACH ROW
EXECUTE FUNCTION inserir_endereco_automaticamente();

CREATE OR REPLACE FUNCTION inserir_dados_pais_responsavel_automaticamente()
RETURNS TRIGGER AS $$
BEGIN
  INSERT INTO dados_pais_responsavel (id_aluno, nome_mae, nome_pai)
  VALUES (NEW.id, '', '');
  RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER trigger_inserir_dados_pais_responsavel
AFTER INSERT ON identificacao_aluno
FOR EACH ROW
EXECUTE FUNCTION inserir_dados_pais_responsavel_automaticamente();

CREATE OR REPLACE FUNCTION inserir_informacoes_matricula_automaticamente()
RETURNS TRIGGER AS $$
BEGIN
  INSERT INTO informacoes_matricula (id_aluno, nome_escola, cod_censo_inep, data_ingresso_escola, matricula, data_matricula, codigo_turma, turno, codigo_serie, codigo_procedencia, participa_programa, transporte_escolar)
  VALUES (NEW.id, '', 0, CURRENT_DATE, 0, CURRENT_DATE, 0, '', '', '', FALSE, FALSE);
  RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER trigger_inserir_informacoes_matricula
AFTER INSERT ON identificacao_aluno
FOR EACH ROW
EXECUTE FUNCTION inserir_informacoes_matricula_automaticamente();







