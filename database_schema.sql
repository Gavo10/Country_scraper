-- Create table 
CREATE TABLE IF NOT EXISTS paises (
    id BIGSERIAL PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    capital VARCHAR(100) NOT NULL,
    poblacion BIGINT NOT NULL,
    area DOUBLE PRECISION NOT NULL,
    is_deleted BOOLEAN NOT NULL DEFAULT FALSE,
    deleted_at TIMESTAMP WITH TIME ZONE NULL
);

-- Sample data
INSERT INTO paises (nombre, capital, poblacion, area, is_deleted, deleted_at) VALUES
('Argentina', 'Buenos Aires', 45195777, 2780400, FALSE, NULL),
('Brasil', 'Brasília', 212559417, 8515767, FALSE, NULL),
('Chile', 'Santiago', 19116209, 756102, FALSE, NULL),
('Uruguay', 'Montevideo', 3473727, 176215, FALSE, NULL),
('Paraguay', 'Asunción', 7132530, 406752, FALSE, NULL),
('Perú', 'Lima', 32971846, 1285216, FALSE, NULL)
ON CONFLICT DO NOTHING;


-- SELECT * FROM paises;
