-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Tempo de geração: 06-Nov-2023 às 19:28
-- Versão do servidor: 10.4.25-MariaDB
-- versão do PHP: 8.1.10

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Banco de dados: `entrevistas`
--

-- --------------------------------------------------------

--
-- Estrutura da tabela `entrevistados`
--

CREATE TABLE `entrevistados` (
  `Id` int(11) NOT NULL,
  `Nome` varchar(50) NOT NULL,
  `Telefone` varchar(15) NOT NULL,
  `email` varchar(50) NOT NULL,
  `Minibio` varchar(255) NOT NULL,
  `Entrevista` int(11) NOT NULL,
  `Pratico` int(11) NOT NULL,
  `Teorico` int(11) NOT NULL,
  `Soft_Skills` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Índices para tabelas despejadas
--

--
-- Índices para tabela `entrevistados`
--
ALTER TABLE `entrevistados`
  ADD PRIMARY KEY (`Id`);

--
-- AUTO_INCREMENT de tabelas despejadas
--

--
-- AUTO_INCREMENT de tabela `entrevistados`
--
ALTER TABLE `entrevistados`
  MODIFY `Id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=14;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
