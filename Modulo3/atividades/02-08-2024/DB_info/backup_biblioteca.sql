-- phpMyAdmin SQL Dump
-- version 5.2.1deb1
-- https://www.phpmyadmin.net/
--
-- Host: localhost:3306
-- Tempo de geração: 03-Ago-2024 às 17:26
-- Versão do servidor: 10.11.6-MariaDB-0+deb12u1
-- versão do PHP: 8.2.20

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Banco de dados: `biblioteca`
--

-- --------------------------------------------------------

--
-- Estrutura da tabela `autores`
--

CREATE TABLE `autores` (
  `id` int(11) NOT NULL,
  `nome` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Extraindo dados da tabela `autores`
--

INSERT INTO `autores` (`id`, `nome`) VALUES
(1, 'Sun Tzu'),
(2, 'Robert Silverberg'),
(3, 'Best American Series Editor'),
(4, 'Stephen Greenblatt'),
(5, 'Joyce Carol Oates'),
(6, 'Xiaomei Chen'),
(7, 'Christopher Dolley'),
(8, 'Tobias Wolff'),
(9, 'Melvyn P. Leffler'),
(10, 'Sukrita Paul Kumar'),
(11, 'Ralph Waldo Emerson'),
(12, 'Susan Belasco'),
(13, 'Rita Dove'),
(14, 'William Shakespeare'),
(15, 'Raza Mir'),
(16, 'Frank Moulaert'),
(17, 'Bob Hale'),
(18, 'Mark Richardson'),
(19, 'Martin Puchner'),
(20, 'Michael Cox'),
(21, 'Leah A. Lievrouw'),
(22, 'Dinah Birch'),
(23, 'Ellen Rooney'),
(24, 'Patricia Genoe McLaren'),
(25, 'Gordon L. Clark'),
(26, 'Núria Homedes'),
(27, 'Alisa Gaunder'),
(28, 'David Armitage'),
(29, 'David O. Sears'),
(30, 'John F. A. Sawyer'),
(31, 'Alfred Bendixen'),
(32, 'Roger Mac Ginty'),
(33, 'Murray Longmore'),
(34, 'Leslie Bethell'),
(35, 'Laura Marcus'),
(36, 'Jack Sidnell'),
(37, 'Chris Scarre'),
(38, 'M. H. Abrams'),
(39, 'James D. Hart'),
(40, 'Robert Von Hallberg'),
(41, 'Jean-Michel Rabaté'),
(42, 'Helga Nowotny'),
(43, 'Warren Breckman'),
(44, 'James Duncan'),
(45, 'David Schalkwyk'),
(46, 'Peter Lamarque');

-- --------------------------------------------------------

--
-- Estrutura da tabela `livros`
--

CREATE TABLE `livros` (
  `id` int(11) NOT NULL,
  `titulo` varchar(255) NOT NULL,
  `estado_do_livro` enum('Disponível','Emprestado','Em Reparo') NOT NULL,
  `ano` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Extraindo dados da tabela `livros`
--

INSERT INTO `livros` (`id`, `titulo`, `estado_do_livro`, `ano`) VALUES
(101, 'The Art of War', 'Disponível', 500),
(102, 'The Science Fiction Hall of Fame', 'Emprestado', 1965),
(103, 'The Best American Series', 'Disponível', 2000),
(104, 'The Norton Anthology of English Literature', 'Emprestado', 1962),
(105, 'The Oxford Book of American Short Stories', 'Disponível', 1992),
(106, 'The Columbia Anthology of Modern Chinese Drama', 'Emprestado', 2008),
(107, 'The Penguin Book of English Short Stories', 'Disponível', 2007),
(108, 'The Vintage Book of Contemporary American Short Stories', 'Emprestado', 1994),
(109, 'The Cambridge History of the Cold War', 'Disponível', 2010),
(110, 'The HarperCollins Book of English Poetry', 'Emprestado', 2004),
(111, 'The Essential Writings of Ralph Waldo Emerson', 'Disponível', 2000),
(112, 'The Bedford Anthology of American Literature', 'Emprestado', 2008),
(113, 'The Penguin Anthology of 20th Century American Poetry', 'Disponível', 2011),
(114, 'The Complete Works of William Shakespeare', 'Emprestado', 2003),
(115, 'The Routledge Companion to Philosophy in Organization Studies', 'Disponível', 2013),
(116, 'The International Handbook of Social Innovation', 'Emprestado', 2014),
(117, 'The Blackwell Companion to Philosophy of Language', 'Disponível', 2012),
(118, 'The Cambridge Companion to American Poets', 'Emprestado', 2008),
(119, 'The Norton Anthology of World Literature', 'Disponível', 2012),
(120, 'The Oxford Handbook of Global Policy', 'Emprestado', 2018),
(121, 'The Handbook of New Media', 'Disponível', 2006),
(122, 'The Oxford Companion to English Literature', 'Emprestado', 2000),
(123, 'The Cambridge Companion to Feminist Literary Theory', 'Disponível', 2004),
(124, 'The Routledge Companion to Management and Organizational History', 'Emprestado', 2016),
(125, 'The Oxford Handbook of Economic Geography', 'Disponível', 2000),
(126, 'The Palgrave Handbook of Global Health Data', 'Emprestado', 2018),
(127, 'The Routledge Handbook of Japanese Politics', 'Disponível', 2016),
(128, 'The Cambridge History of the Modern World', 'Emprestado', 2008),
(129, 'The Oxford Handbook of Political Psychology', 'Disponível', 2011),
(130, 'The Blackwell Companion to the Bible and Culture', 'Emprestado', 2006),
(131, 'The Cambridge Companion to American Travel Writing', 'Disponível', 2008),
(132, 'The Routledge Handbook of Peacebuilding', 'Emprestado', 2013),
(133, 'The Oxford Handbook of Clinical Medicine', 'Disponível', 2014),
(134, 'The Cambridge History of Latin America', 'Emprestado', 2006),
(135, 'The Routledge Companion to Literature and Psychoanalysis', 'Disponível', 2017),
(136, 'The Cambridge Handbook of Language and Social Interaction', 'Emprestado', 2011),
(137, 'The Penguin Historical Atlas of Ancient Rome', 'Disponível', 1998),
(138, 'The Norton Anthology of English Literature', 'Emprestado', 1962),
(139, 'The Oxford Companion to American Literature', 'Disponível', 2001),
(140, 'The Cambridge Companion to American Poets', 'Emprestado', 2008),
(141, 'The Routledge Companion to Literature and Psychoanalysis', 'Disponível', 2017),
(142, 'The Oxford Handbook of Global Policy', 'Emprestado', 2018),
(143, 'The Cambridge History of Modern European Thought', 'Disponível', 2011),
(144, 'The Cambridge Companion to American Travel Writing', 'Emprestado', 2008),
(145, 'The Blackwell Companion to Philosophy of Language', 'Disponível', 2012),
(146, 'The Handbook of New Media', 'Emprestado', 2006),
(147, 'The Oxford Handbook of Economic Geography', 'Disponível', 2000),
(148, 'The Cambridge Companion to the History of the Book', 'Emprestado', 2015),
(149, 'The Routledge Companion to American Literature', 'Disponível', 2020),
(150, 'The Cambridge Companion to the Philosophy of Language', 'Emprestado', 2004),
(151, 'The Oxford Handbook of Political Psychology', 'Disponível', 2011),
(152, 'The Cambridge Companion to Feminist Literary Theory', 'Emprestado', 2004),
(153, 'The Routledge Handbook of Peacebuilding', 'Disponível', 2013),
(154, 'The Cambridge Handbook of Language and Social Interaction', 'Emprestado', 2011),
(155, 'The Routledge Handbook of Peacebuilding', 'Disponível', 2013),
(156, 'The Oxford Handbook of Social and Political Trust', 'Emprestado', 2016);

-- --------------------------------------------------------

--
-- Estrutura da tabela `livros_autores`
--

CREATE TABLE `livros_autores` (
  `livro_id` int(11) NOT NULL,
  `autor_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Extraindo dados da tabela `livros_autores`
--

INSERT INTO `livros_autores` (`livro_id`, `autor_id`) VALUES
(101, 1),
(101, 2),
(101, 27),
(102, 2),
(102, 3),
(102, 28),
(103, 3),
(103, 4),
(103, 29),
(104, 4),
(104, 5),
(104, 30),
(105, 5),
(105, 6),
(105, 31),
(106, 6),
(106, 7),
(106, 32),
(107, 7),
(107, 8),
(107, 33),
(108, 8),
(108, 9),
(108, 34),
(109, 9),
(109, 10),
(109, 35),
(110, 10),
(110, 11),
(110, 36),
(111, 11),
(111, 12),
(111, 37),
(112, 12),
(112, 13),
(112, 38),
(113, 13),
(113, 14),
(113, 39),
(114, 14),
(114, 15),
(114, 40),
(115, 15),
(115, 16),
(115, 41),
(116, 16),
(116, 17),
(116, 42),
(117, 17),
(117, 18),
(117, 43),
(118, 18),
(118, 19),
(118, 44),
(119, 19),
(119, 20),
(119, 45),
(120, 20),
(120, 21),
(120, 46),
(121, 21),
(121, 22),
(122, 22),
(122, 23),
(123, 23),
(123, 24),
(124, 24),
(124, 25),
(125, 25),
(125, 26);

--
-- Índices para tabelas despejadas
--

--
-- Índices para tabela `autores`
--
ALTER TABLE `autores`
  ADD PRIMARY KEY (`id`);

--
-- Índices para tabela `livros`
--
ALTER TABLE `livros`
  ADD PRIMARY KEY (`id`);

--
-- Índices para tabela `livros_autores`
--
ALTER TABLE `livros_autores`
  ADD PRIMARY KEY (`livro_id`,`autor_id`),
  ADD KEY `autor_id` (`autor_id`);

--
-- AUTO_INCREMENT de tabelas despejadas
--

--
-- AUTO_INCREMENT de tabela `autores`
--
ALTER TABLE `autores`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=47;

--
-- AUTO_INCREMENT de tabela `livros`
--
ALTER TABLE `livros`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=157;

--
-- Restrições para despejos de tabelas
--

--
-- Limitadores para a tabela `livros_autores`
--
ALTER TABLE `livros_autores`
  ADD CONSTRAINT `livros_autores_ibfk_1` FOREIGN KEY (`livro_id`) REFERENCES `livros` (`id`),
  ADD CONSTRAINT `livros_autores_ibfk_2` FOREIGN KEY (`autor_id`) REFERENCES `autores` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
