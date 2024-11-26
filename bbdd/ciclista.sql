CREATE TABLE equipo (
    nomeq VARCHAR(25) NOT NULL, 
    director VARCHAR(100) NOT NULL, -- Nombre del director del equipo no puede ser nulo.
    telefono VARCHAR(16) UNIQUE, -- Teléfono del director del equipo, único. Puede no existir, pero si existe no se puede repetir.
    CONSTRAINT PK_equi PRIMARY KEY (nomeq));

CREATE TABLE ciclista (
    dorsal SMALLINT NOT NULL, 
    nombre VARCHAR(30) NOT NULL , -- Nombre del ciclista no puede ser nulo.   
    edad SMALLINT, 
    nomeq VARCHAR(25),
    salario REAL,
    CONSTRAINT PK_ciclista PRIMARY KEY (dorsal), -- Clave primaria del ciclista es el dorsal, identificador único.
    CONSTRAINT FK_ciclista_equipo FOREIGN KEY (nomeq) REFERENCES equipo(nomeq) -- Referencia a la tabla equipo al que pertenece el ciclista.
    );

CREATE TABLE etapa (
    netapa SMALLINT NOT NULL, 
    km SMALLINT,
    salida VARCHAR(35),
    llegada VARCHAR(35),
    dorsal SMALLINT,
    CONSTRAINT PK_etapa PRIMARY KEY (netapa), -- Clave primaria de la etapa es el número de etapa, identificador único.
    CONSTRAINT FK_etapa_ciclista FOREIGN KEY (dorsal) REFERENCES ciclista(dorsal) -- Referencia a la tabla ciclista que ha ganado la etapa.
);

CREATE TABLE puerto (
    nompuerto VARCHAR(35) NOT NULL, 
    altura SMALLINT,
    categoria CHAR,
    pendiente REAL,
    netapa SMALLINT,
    dorsal SMALLINT,
    CONSTRAINT PK_puerto PRIMARY KEY (nompuerto), -- Clave primaria del puerto es el nombre del puerto, identificador único.
    CONSTRAINT FK_puerto_etapa FOREIGN KEY (netapa) REFERENCES etapa(netapa), -- Referencia a la tabla etapa en la que se encuentra el puerto.
    CONSTRAINT FK_puerto_ciclista FOREIGN KEY (dorsal) REFERENCES ciclista(dorsal) -- Referencia a la tabla ciclista que ha ganado el puerto.
);


-- Nueva tabla que almacena los resultados de los ciclistas en cada una de las etapas.
CREATE TABLE resultados (
    id_resultado INT AUTO_INCREMENT NOT NULL, 
    dorsal SMALLINT NOT NULL, 
    netapa SMALLINT NOT NULL, 
    tiempo TIME NOT NULL,
    CONSTRAINT PK_resultados PRIMARY KEY (id_resultado),
    CONSTRAINT FK_resultados_ciclista FOREIGN KEY (dorsal) REFERENCES ciclista(dorsal),
    CONSTRAINT FK_resultados_etapa FOREIGN KEY (netapa) REFERENCES etapa(netapa)
);

-- PERMISOS

-- Crear roles
CREATE ROLE director;
CREATE ROLE operador;
CREATE ROLE periodista;
CREATE ROLE publico;

-- Permisos para el director (total control)
GRANT ALL PRIVILEGES ON ALL TABLES IN SCHEMA ciclismo TO director;

-- Permisos para el operador
GRANT SELECT, INSERT, UPDATE, DELETE ON TABLE etapa, puerto, resultados TO operador; -- El operador debe poder insertar los resultados también.
GRANT SELECT ON TABLE equipo, ciclista TO operador;

-- Permisos para el periodista
GRANT SELECT ON ALL TABLES IN SCHEMA ciclismo TO periodista;

-- Crear una vista para el público
CREATE VIEW publico_ciclista AS
SELECT dorsal, nombre, nomeq
FROM ciclista;

-- Otorgar permisos al rol público
GRANT SELECT ON publico_ciclista TO publico;
GRANT SELECT ON TABLE equipo, etapa, puerto,resultados TO publico; -- Publico tiene visibilidad sobre los resultados de las etapas también.


-- Crear usuarios y asignar roles
CREATE USER director_vuelta WITH PASSWORD 'director123';
GRANT director TO director_vuelta;

CREATE USER operador1 WITH PASSWORD 'operador123';
GRANT operador TO operador1;

CREATE USER periodista1 WITH PASSWORD 'periodista123';
GRANT periodista TO periodista1;

CREATE USER periodista2 WITH PASSWORD 'periodista321';
GRANT periodista TO periodista2;

CREATE USER app_publico WITH PASSWORD 'apppublico123';
GRANT publico TO app_publico;


INSERT INTO EQUIPO VALUES
('Astana','Jose Perez', 111111111),
('Santander','Miguel Echevarria', 222222222),
('Carrera','Luigi Petroni', 3333333333),
('Castorama','Jean Philip', 444444444),
('Gatorade','Gian Luca Pacceli', 5555555555),
('Kelme','Alvaro Pino', 666666666),
('ONCE','Manuel Sainz', 777777777),
('PDM','Piet Van Der Kruis', 888888888),
('Euskadi','Minguez', 999999999),
('TVM','Steveens Henk', 123456789);

INSERT INTO CICLISTA VALUES
(1,'Miguel Indurain',32,'Santander', 120000),
(2,'Pedro Delgado',35,'Santander', 100000),
(3,'Alex Zulle',27,'ONCE', 60000),
(4,'Tony Rominger',30,'ONCE', 60000),
(5,'Gert-Jan Theunisse',32,'TVM', 55000),
(6,'Adriano Baffi',33,'Euskadi', 55000),
(7,'Massimiliano Lelli',30,'Euskadi', 55000),
(8,'Jean Van Poppel',33,'Euskadi', 30000),
(9,'Massimo Podenzana',34,'Castorama', 60000),
(10,'Mario Cipollini',28,'Euskadi', 10000),
(11,'Flavio Giupponi',31,'Kelme', 30000),
(12,'Alessio Di Basco',31,'Carrera', 60000),
(13,'Lale Cubino',28,'Euskadi', 60000),
(14,'Roberto Pagnin',33,'Castorama', 60000),
(15,'Jesper Skibby',31,'TVM', 55000),
(16,'Dimitri Konishev',29,'ONCE', 55000),
(17,'Bruno Leali',37,'Kelme', 30000),
(18,'Robert Millar',37,'TVM', 30000),
(19,'Julian Gorospe',34,'Santander', 10000),
(20,'Alfonso Gutierrez',29,'Astana', 55000),
(21,'Erwin Nijboer',31,'Astana', 10000),
(22,'Giorgio Furlan',32,'Kelme', 30000),
(23,'Lance Armstrong',27,'Carrera', 60000),
(24,'Claudio Chiappucci',29,'Carrera', 60000),
(25,'Gianni Bugno',32,'Gatorade', 60000),
(26,'Mikel Zarrabeitia',27,'Santander', 60000),
(27,'Laurent Jalabert',28,'ONCE', 60000),
(28,'Jesus Montoya',33,'Santander', 30000),
(29,'Angel Edo',28,'Kelme', 55000),
(30,'Melchor Mauri',28,'Santander', 5000),
(31,'Vicente Aparicio',30,'Santander', 60000),
(32,'Laurent Dufaux',28,'ONCE', 60000),
(33,'Stefano della Santa',29,'ONCE', 30000),
(34,'Angel Yesid Camargo',30,'Kelme', 10000),
(35,'Erik Dekker',28,'Astana', 55000),
(36,'Gian Matteo Fagnini',32,'Euskadi', 55000),
(37,'Scott Sunderland',29,'TVM', 55000),
(38,'Javier Palacin',25,'Euskadi', 30000),
(39,'Rudy Verdonck',30,'Euskadi', 10000),
(40,'Viatceslav Ekimov',32,'Astana', 60000),
(41,'Rolf Aldag',25,'Santander', 10000),
(42,'Davide Cassani',29,'TVM', 55000),
(43,'Francesco Casagrande',28,'Euskadi', 30000),
(44,'Luca Gelfi',27,'Gatorade', 10000),
(45,'Alberto Elli',26,'Astana', 30000),
(46,'Agustin Sagasti',24,'Euskadi', 60000),
(47,'Laurent Pillon',32,'Kelme', 60000),
(48,'Marco Saligari',29,'Kelme', 55000),
(49,'Eugeni Berzin',23,'Kelme', 30000),
(50,'Fernando Escartin',27,'ONCE', 10000),
(51,'Udo Bolts',30,'Santander', 10000),
(52,'Vladislav Bobrik',26,'Kelme', 60000),
(53,'Michele Bartoli',28,'Euskadi', 60000),
(54,'Steffen Wesemann',30,'Santander', 10000),
(55,'Nicola Minali',28,'Kelme', 55000),
(56,'Andrew Hampsten',29,'Santander', 30000),
(57,'Stefano Zanini',28,'Castorama', 30000),
(58,'Gerd Audehm',34,'Santander', 60000),
(59,'Mariano Picolli',28,'Euskadi', 60000),
(60,'Giovanni Lombardi',28,'Kelme', 60000),
(61,'Walte Castignola',26,'Castorama', 60000),
(62,'Raul Alcala',30,'Carrera', 30000),
(63,'Alvaro Mejia',32,'Carrera', 30000),
(64,'Giuseppe Petito',28,'Euskadi', 55000),
(65,'Pascal Lino',29,'Carrera', 10000),
(66,'Enrico Zaina',24,'Kelme', 60000),
(67,'Armand de las Cuevas',28,'Castorama', 60000),
(68,'Angel Citracca',28,'Castorama', 10000),
(69,'Eddy Seigneur',27,'Castorama', 55000),
(70,'Sandro Heulot',29,'Santander', 30000),
(71,'Prudencio Indurain',27,'Santander', 30000),
(72,'Stefano Colage',28,'Kelme', 10000),
(73,'Laurent Fignon',35,'Gatorade', 5000),
(74,'Claudio Chioccioli',36,'Carrera', 30000),
(75,'Juan Romero',32,'Euskadi', 60000),
(76,'Marco Giovannetti',34,'Gatorade', 60000),
(77,'Javier Mauleon',33,'ONCE', 10000),
(78,'Antonio Esparza',35,'Kelme', 55000),
(79,'Johan Bruyneel',33,'ONCE', 55000),
(80,'Federico Echave',37,'ONCE', 10000),
(81,'Piotr Ugrumov',33,'Kelme', 30000),
(82,'Edgar Corredor',30,'Kelme', 30000),
(83,'Hernan Buenahora',32,'Kelme', 60000),
(84,'Jon Unzaga',31,'ONCE', 60000),
(85,'Dimitri Abdoujaparov',30,'Carrera', 60000),
(86,'Juan Martinez Oliver',32,'Kelme', 55000),
(87,'Fernando Mota',32,'Astana', 30000),
(88,'Angel Camarillo',28,'ONCE', 55000),
(89,'Stefan Roche',36,'Carrera', 30000),
(90,'Ivan Ivanov',27,'Astana', 10000),
(91,'Nestor Mora',28,'Kelme', 60000),
(92,'Federico Garcia',27,'Astana', 60000),
(93,'Bo Hamburger',29,'TVM', 60000),
(94,'Marino Alonso',30,'Santander', 5000),
(95,'Manuel Guijarro',31,'Euskadi', 55000),
(96,'Tom Cordes',29,'Astana', 10000),
(97,'Casimiro Moreda',28,'ONCE', 60000),
(98,'Eleuterio Anguita',25,'Astana', 60000),
(99,'Per Pedersen',29,'Euskadi', 60000),
(100,'William Palacios',30,'ONCE', 10000) ;

INSERT INTO ETAPA VALUES
(1,9,'Valladolid','Valladolid',1),
(2,180,'Valladolid','Salamanca',36),
(3,240,'Salamanca','Caceres',12),
(4,230,'Almendralejo','Cordoba',83),
(5,170,'Cordoba','Granada',27),
(6,150,'Granada','Sierra Nevada',52),
(7,250,'Baza','Alicante',22),
(8,40,'Benidorm','Benidorm',1),
(9,150,'Benidorm','Valencia',35),
(10,200,'Igualada','Andorra',2),
(11,195,'Andorra','Estacion de Cerler',65),
(12,220,'Benasque','Zaragoza',12),
(13,200,'Zaragoza','Pamplona',93),
(14,172,'Pamplona','Alto de la Cruz de la Demanda',86),
(15,207,'Santo Domingo de la Calzada','Santander',10),
(16,160,'Santander','Lagos de Covadonga',5),
(17,140,'Cangas de Onis','Alto del Naranco',4),
(18,195,'Avila','Avila',8),
(19,190,'Avila','Destilerias Dyc',2),
(20,52,'Segovia','Destilerias Dyc',2),
(21,170,'Destilerias Dyc','Madrid',27) ;

INSERT INTO PUERTO VALUES
('Alto del Naranco',565,'1',6.90,10,30),
('Arcalis',2230,'E',6.50,10,4),
('Cerler-Circo de Ampriu',2500,'E',5.87,11,9),
('Coll de la Comella',1362,'1',8.07,10,2),
('Coll de Ordino',1980,'E',5.30,10,7),
('Cruz de la Demanda',1850,'E',7.00,11,20),
('Lagos de Covadonga',1134,'E',6.86,16,42),
('Navacerrada',1860,'1',7.50,19,2),
('Puerto de Alisas',672,'1',5.80,15,1),
('Puerto de la Morcuera',1760,'2',6.50,19,2),
('Puerto de Mijares',1525,'1',4.90,18,24),
('Puerto de Navalmoral',1521,'2',4.30,18,2),
('Puerto de Pedro Bernardo',1250,'1',4.20,18,25),
('Sierra Nevada',2500,'E',6.00,2,26) ;

INSERT INTO RESULTADOS VALUES
(1,1,1,'02:30:00'),
(2,2,1,'02:40:00'),
(3,3,1,'04:30:00'),
(4,4,1,'04:30:00'),
(5,5,1,'04:30:00'),
(6,6,1,'04:30:00'),
(7,7,1,'04:30:00'),
(8,8,1,'04:30:00'),
(9,9,1,'04:30:00'),
(10,10,1,'04:30:00'),
(11,11,1,'04:30:00'),
(12,12,1,'04:30:00'),
(13,13,1,'04:30:00'),
(14,14,1,'04:30:00'),
(15,15,1,'04:30:00'),
(16,16,1,'04:30:00'),
(17,17,1,'04:30:00'),
(18,18,1,'04:30:00'),
(19,19,1,'04:30:00'),
(20,20,1,'04:30:00'),
(21,21,1,'04:30:00'),
(22,22,1,'04:30:00'),
(23,23,1,'04:30:00'),
(24,24,1,'04:30:00'),
(25,25,1,'04:30:00'),
(26,26,1,'04:30:00'),
(27,27,1,'04:30:00'),
(28,28,1,'04:30:00'),
(29,29,1,'04:30:00'),
(30,30,1,'04:30:00'),
(31,31,1,'04:30:00'),
(32,32,1,'04:30:00'),
(33,33,1,'04:30:00'),
(34,34,1,'04:30:00'),
(35,35,1,'04:30:00'),
(36,36,1,'04:30:00'),
(37,37,1,'04:30:00'),
(38,38,1,'04:30:00');

