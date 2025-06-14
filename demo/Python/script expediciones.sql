-- Tabla Host
CREATE TABLE Host (
    id_host INT IDENTITY(1,1) PRIMARY KEY,
    descripcion NVARCHAR(255)
);
go;
-- Tabla Localizacion
CREATE TABLE Localizacion (
    id_localizacion INT IDENTITY(1,1) PRIMARY KEY,
    descripcion NVARCHAR(255),
    id_host INT FOREIGN KEY REFERENCES Host(id_host)
);
go;
-- Tabla Pico
CREATE TABLE Pico (
    id_pico INT IDENTITY(1,1) PRIMARY KEY,
    id_localizacion INT FOREIGN KEY REFERENCES Localizacion(id_localizacion),
    nombrePico NVARCHAR(255),
    abierto BIT,
    altura FLOAT,
    cambio_trekking BIT,
    sin_aprobacion BIT,
    año_de_cambio INT,
    estado BIT,
    restricciones NVARCHAR(255)
);
go;
-- Tabla Nacionalidad
CREATE TABLE Nacionalidad (
    id_nacionalidad INT IDENTITY(1,1) PRIMARY KEY,
    descripcion NVARCHAR(100)
);
go;
-- Tabla Miembros
CREATE TABLE Miembros (
    id_miembro INT IDENTITY(1,1) PRIMARY KEY,
    id_nacionalidad INT FOREIGN KEY REFERENCES Nacionalidad(id_nacionalidad),
    nombre NVARCHAR(100),
    apellido NVARCHAR(100),
    sexo NVARCHAR(10),
    es_lider BIT,
    es_staff BIT,
    año_nacimiento INT,
    fallecido BIT,
);
go;
-- Tabla Fecha
CREATE TABLE Fecha (
    id_fecha INT IDENTITY(1,1) PRIMARY KEY,
    fecha DATE,
    año INT,
    temporada INT
);
go;
-- Tabla Accidente
CREATE TABLE Accidente (
    id_accidente INT IDENTITY(1,1) PRIMARY KEY,
    descripcion NVARCHAR(255)
);
go;
-- Tabla Motivo
CREATE TABLE Motivo (
    id_motivo INT IDENTITY(1,1) PRIMARY KEY,
    descripcion NVARCHAR(255)
);
go;
-- Tabla Resultado
CREATE TABLE Resultado (
    id_resultado INT IDENTITY(1,1) PRIMARY KEY,
    id_motivo INT FOREIGN KEY REFERENCES Motivo(id_motivo),
    descripcion NVARCHAR(255)
);
go;
-- Tabla Ruta
CREATE TABLE Ruta (
    id_ruta INT IDENTITY(1,1) PRIMARY KEY,
    descripcion NVARCHAR(255)
);
go;
-- Tabla Expediciones
CREATE TABLE Expediciones (
    id_expedicion INT IDENTITY(1,1) PRIMARY KEY,
    id_fecha INT FOREIGN KEY REFERENCES Fecha(id_fecha),
    id_accidente INT FOREIGN KEY REFERENCES Accidente(id_accidente),
    id_miembro INT FOREIGN KEY REFERENCES Miembros(id_miembro),
    id_pico INT FOREIGN KEY REFERENCES Pico(id_pico),
    id_resultado INT FOREIGN KEY REFERENCES Resultado(id_resultado),
    id_ruta INT FOREIGN KEY REFERENCES Ruta(id_ruta),
    altitud FLOAT,
    cupos INT,
    conteo_mortalidad INT
);
