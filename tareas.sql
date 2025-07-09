CREATE TABLE tareas (
    id INT AUTO_INCREMENT PRIMARY KEY,
    email VARCHAR(100) NOT NULL,
    tarea TEXT,
    subtarea TEXT,
    hora_inicio DATETIME,
    hora_final DATETIME,
    comentarios TEXT,
    completado BOOLEAN
);
