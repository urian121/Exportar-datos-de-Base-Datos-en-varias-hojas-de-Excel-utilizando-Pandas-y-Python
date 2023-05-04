-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 04-05-2023 a las 16:09:07
-- Versión del servidor: 10.4.27-MariaDB
-- Versión de PHP: 8.2.0

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `demo`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `registros`
--

CREATE TABLE `registros` (
  `id` int(10) NOT NULL,
  `nombre` varchar(30) DEFAULT NULL,
  `profesion` varchar(30) DEFAULT NULL,
  `status` int(1) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `registros`
--

INSERT INTO `registros` (`id`, `nombre`, `profesion`, `status`) VALUES
(1, 'Urian Viera', 'Ingeniero de Sistemas', 0),
(2, 'Abelardo Perez', 'Ingeniero de Sistemas', 0),
(3, 'Braudin Laya', 'Ingeniero de Sistemas', 0),
(4, 'Dayana Ramirez', 'Web Developer', 0),
(5, 'Any Somosa', 'Licenciada en Enfermera', 0),
(6, 'Jennifer Lopez', 'Agente Comercial', 0),
(7, 'Alberto Fodol', 'Desarrollador', 0),
(8, 'Jose Gregorio', 'full-stack', 0),
(9, 'Luisa Mora', 'Diseñadora UI/UX', 0),
(10, 'Dary Perez', 'Analista de Sistemas', 0),
(11, 'Ryan Gosling', 'Diseñador Grafico', 0),
(12, 'Chris Hemsworth', 'Analista de Sistemas', 0);

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `registros`
--
ALTER TABLE `registros`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `registros`
--
ALTER TABLE `registros`
  MODIFY `id` int(10) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=13;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
