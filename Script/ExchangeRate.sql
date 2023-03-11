

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--

--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `ExchangeRate`
--

CREATE TABLE `ExchangeRate` (
  `ID` int(11) NOT NULL,
  `MONEDA` char(3) NOT NULL,
  `COMPRA` decimal(6,3) NOT NULL,
  `VENTA` decimal(6,3) NOT NULL,
  `FECHA` date NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Volcado de datos para la tabla `ExchangeRate`
--

INSERT INTO `ExchangeRate` (`ID`, `MONEDA`, `COMPRA`, `VENTA`, `FECHA`) VALUES
(11, 'DOL', '3.810', '3.860', '2023-02-13'),
(15, 'SOL', '3.880', '3.990', '2023-02-15');

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `ExchangeRate`
--
ALTER TABLE `ExchangeRate`
  ADD PRIMARY KEY (`ID`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `ExchangeRate`
--
ALTER TABLE `ExchangeRate`
  MODIFY `ID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=16;COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
