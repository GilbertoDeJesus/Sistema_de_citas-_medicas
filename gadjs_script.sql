CREATE DATABASE IF NOT EXISTS gadjs_citas;
use gadjs_citas; 

create table usuario (
	id int not null auto_increment,
	nombre varchar(50),
	apellido varchar(50),
	email varchar(255),
	password varchar(255),
	fecha date not null,
	CONSTRAINT pk_usuario PRIMARY KEY(id),
	CONSTRAINT uq_email UNIQUE(email)
)ENGINE=InnoDb;

create table paciente (
	id int not null auto_increment,
	nombre varchar(50),
	apellido varchar(50),
	genero varchar(20),
	edad int,
	email varchar(255),
	direccion varchar(255),
	telefono varchar(255),
	is_active boolean not null default 1,
	sintomas varchar(500),
	fecha date not null,
	CONSTRAINT pk_paciente PRIMARY KEY(id)
)ENGINE=InnoDb;

create table consultorio (
	id int not null auto_increment,
	nombre varchar(200),
	fecha date not null,
	CONSTRAINT pk_consultorio PRIMARY KEY(id)
)ENGINE=InnoDb;

create table medico (
	id int not null auto_increment,
	nombre varchar(50),
	apellido varchar(50),
	genero varchar(20),
	email varchar(255),
	direccion varchar(255),
	telefono varchar(255),
	is_active boolean not null default 1,
	fecha date not null,
	consultorio_id int,
	CONSTRAINT pk_medico PRIMARY KEY(id),
    CONSTRAINT fk_medico_consultorio FOREIGN KEY(consultorio_id) REFERENCES consultorio(id)
)ENGINE=InnoDb;

create table cita(
	id int not null auto_increment,
	titulo varchar(100),
	nota text,
	paciente_id int,
	sintomas text,
	usuario_id int,
	medico_id int,
	fecha date not null,
	reservacion date not null,
	CONSTRAINT pk_cita PRIMARY KEY(id),
    CONSTRAINT fk_cita_usuario FOREIGN KEY(usuario_id) REFERENCES usuario(id),
    CONSTRAINT fk_cita_paciente FOREIGN KEY(paciente_id) REFERENCES paciente(id),
    CONSTRAINT fk_cita_medico FOREIGN KEY(medico_id) REFERENCES medico(id)
)ENGINE=InnoDb;