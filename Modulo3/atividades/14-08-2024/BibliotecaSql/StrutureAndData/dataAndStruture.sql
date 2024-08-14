CREATE DATABASE  IF NOT EXISTS `biblioteca` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `biblioteca`;
-- MySQL dump 10.13  Distrib 8.0.38, for Win64 (x86_64)
--
-- Host: 127.0.0.1    Database: biblioteca
-- ------------------------------------------------------
-- Server version	8.0.39

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `autores`
--

DROP TABLE IF EXISTS `autores`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `autores` (
  `id` int NOT NULL AUTO_INCREMENT,
  `nome` varchar(255) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=47 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `autores`
--

LOCK TABLES `autores` WRITE;
/*!40000 ALTER TABLE `autores` DISABLE KEYS */;
INSERT INTO `autores` VALUES (1,'Sun Tzu'),(2,'Robert Silverberg'),(3,'Best American Series Editor'),(4,'Stephen Greenblatt'),(5,'Joyce Carol Oates'),(6,'Xiaomei Chen'),(7,'Christopher Dolley'),(8,'Tobias Wolff'),(9,'Melvyn P. Leffler'),(10,'Sukrita Paul Kumar'),(11,'Ralph Waldo Emerson'),(12,'Susan Belasco'),(13,'Rita Dove'),(14,'William Shakespeare'),(15,'Raza Mir'),(16,'Frank Moulaert'),(17,'Bob Hale'),(18,'Mark Richardson'),(19,'Martin Puchner'),(20,'Michael Cox'),(21,'Leah A. Lievrouw'),(22,'Dinah Birch'),(23,'Ellen Rooney'),(24,'Patricia Genoe McLaren'),(25,'Gordon L. Clark'),(26,'Núria Homedes'),(27,'Alisa Gaunder'),(28,'David Armitage'),(29,'David O. Sears'),(30,'John F. A. Sawyer'),(31,'Alfred Bendixen'),(32,'Roger Mac Ginty'),(33,'Murray Longmore'),(34,'Leslie Bethell'),(35,'Laura Marcus'),(36,'Jack Sidnell'),(37,'Chris Scarre'),(38,'M. H. Abrams'),(39,'James D. Hart'),(40,'Robert Von Hallberg'),(41,'Jean-Michel Rabaté'),(42,'Helga Nowotny'),(43,'Warren Breckman'),(44,'James Duncan'),(45,'David Schalkwyk'),(46,'Peter Lamarque');
/*!40000 ALTER TABLE `autores` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `editoras`
--

DROP TABLE IF EXISTS `editoras`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `editoras` (
  `id` int NOT NULL AUTO_INCREMENT,
  `nome` varchar(100) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `editoras`
--

LOCK TABLES `editoras` WRITE;
/*!40000 ALTER TABLE `editoras` DISABLE KEYS */;
INSERT INTO `editoras` VALUES (1,'Penguin Random House'),(2,'HarperCollins'),(3,'Simon & Schuster'),(4,'Hachette Livre'),(5,'Macmillan Publishers'),(6,'Scholastic'),(7,'Bloomsbury'),(8,'Oxford University Press'),(9,'Wiley'),(10,'Pearson');
/*!40000 ALTER TABLE `editoras` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `livros`
--

DROP TABLE IF EXISTS `livros`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `livros` (
  `id` int NOT NULL AUTO_INCREMENT,
  `titulo` varchar(255) NOT NULL,
  `estado_do_livro` enum('Disponível','Emprestado','Em Reparo') NOT NULL,
  `ano` int DEFAULT NULL,
  `data_aquisicao` date DEFAULT NULL,
  `observacao` text,
  `lido` tinyint(1) DEFAULT NULL,
  `editora_id` int DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=57 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `livros`
--

LOCK TABLES `livros` WRITE;
/*!40000 ALTER TABLE `livros` DISABLE KEYS */;
INSERT INTO `livros` VALUES (1,'The Art of War','Disponível',500,'2023-01-01','Disponível para empréstimo',0,1),(2,'The Science Fiction Hall of Fame','Emprestado',1965,'2023-01-02','Disponível para empréstimo',1,2),(3,'The Best American Series','Disponível',2000,'2023-01-03','Disponível para empréstimo',0,3),(4,'The Norton Anthology of English Literature','Emprestado',1962,'2023-02-07','Disponível para empréstimo',1,4),(5,'The Oxford Book of American Short Stories','Disponível',1992,'2023-01-05','Disponível para empréstimo',0,5),(6,'The Columbia Anthology of Modern Chinese Drama','Emprestado',2008,'2023-01-06','Disponível para empréstimo',1,6),(7,'The Penguin Book of English Short Stories','Disponível',2007,'2023-01-07','Disponível para empréstimo',0,7),(8,'The Vintage Book of Contemporary American Short Stories','Emprestado',1994,'2023-01-08','Disponível para empréstimo',1,8),(9,'The Cambridge History of the Cold War','Disponível',2010,'2023-01-09','Disponível para empréstimo',0,9),(10,'The HarperCollins Book of English Poetry','Emprestado',2004,'2023-01-10','Disponível para empréstimo',1,10),(11,'The Essential Writings of Ralph Waldo Emerson','Disponível',2000,'2023-01-11','Disponível para empréstimo',0,1),(12,'The Bedford Anthology of American Literature','Emprestado',2008,'2023-01-12','Disponível para empréstimo',1,2),(13,'The Penguin Anthology of 20th Century American Poetry','Disponível',2011,'2023-01-13','Disponível para empréstimo',0,3),(14,'The Complete Works of William Shakespeare','Emprestado',2003,'2023-01-14','Disponível para empréstimo',1,4),(15,'The Routledge Companion to Philosophy in Organization Studies','Disponível',2013,'2023-01-15','Disponível para empréstimo',0,5),(16,'The International Handbook of Social Innovation','Emprestado',2014,'2023-01-16','Disponível para empréstimo',1,6),(17,'The Blackwell Companion to Philosophy of Language','Disponível',2012,'2023-02-14','Disponível para empréstimo',0,7),(18,'The Cambridge Companion to American Poets','Emprestado',2008,'2023-02-09','Disponível para empréstimo',1,8),(19,'The Norton Anthology of World Literature','Disponível',2012,'2023-01-19','Disponível para empréstimo',0,9),(20,'The Oxford Handbook of Global Policy','Emprestado',2018,'2023-02-11','Disponível para empréstimo',1,10),(21,'The Handbook of New Media','Disponível',2006,'2023-02-15','Disponível para empréstimo',1,1),(22,'The Oxford Companion to English Literature','Emprestado',2000,'2023-01-22','Disponível para empréstimo',1,2),(23,'The Cambridge Companion to Feminist Literary Theory','Disponível',2004,'2023-02-21','Disponível para empréstimo',1,3),(24,'The Routledge Companion to Management and Organizational History','Emprestado',2016,'2023-01-24','Disponível para empréstimo',1,4),(25,'The Oxford Handbook of Economic Geography','Disponível',2000,'2023-02-16','Disponível para empréstimo',0,5),(26,'The Palgrave Handbook of Global Health Data','Emprestado',2018,'2023-01-26','Disponível para empréstimo',1,6),(27,'The Routledge Handbook of Japanese Politics','Disponível',2016,'2023-01-27','Disponível para empréstimo',0,7),(28,'The Cambridge History of the Modern World','Emprestado',2008,'2023-01-28','Disponível para empréstimo',1,8),(29,'The Oxford Handbook of Political Psychology','Disponível',2011,'2023-02-20','Disponível para empréstimo',0,9),(30,'The Blackwell Companion to the Bible and Culture','Emprestado',2006,'2023-01-30','Disponível para empréstimo',1,10),(31,'The Cambridge Companion to American Travel Writing','Disponível',2008,'2023-02-13','Disponível para empréstimo',1,1),(32,'The Routledge Handbook of Peacebuilding','Emprestado',2013,'2023-02-24','Disponível para empréstimo',0,2),(33,'The Oxford Handbook of Clinical Medicine','Disponível',2014,'2023-02-02','Disponível para empréstimo',0,3),(34,'The Cambridge History of Latin America','Emprestado',2006,'2023-02-03','Disponível para empréstimo',1,4),(35,'The Routledge Companion to Literature and Psychoanalysis','Disponível',2017,'2023-02-10','Disponível para empréstimo',0,5),(36,'The Cambridge Handbook of Language and Social Interaction','Emprestado',2011,'2023-02-23','Disponível para empréstimo',1,6),(37,'The Penguin Historical Atlas of Ancient Rome','Disponível',1998,'2023-02-06','Disponível para empréstimo',0,7),(38,'The Norton Anthology of English Literature','Emprestado',1962,'2023-02-07','Disponível para empréstimo',1,8),(39,'The Oxford Companion to American Literature','Disponível',2001,'2023-02-08','Disponível para empréstimo',0,9),(40,'The Cambridge Companion to American Poets','Emprestado',2008,'2023-02-09','Disponível para empréstimo',1,10),(41,'The Routledge Companion to Literature and Psychoanalysis','Disponível',2017,'2023-02-10','Disponível para empréstimo',0,1),(42,'The Oxford Handbook of Global Policy','Emprestado',2018,'2023-02-11','Disponível para empréstimo',1,2),(43,'The Cambridge History of Modern European Thought','Disponível',2011,'2023-02-12','Disponível para empréstimo',0,3),(44,'The Cambridge Companion to American Travel Writing','Emprestado',2008,'2023-02-13','Disponível para empréstimo',1,4),(45,'The Blackwell Companion to Philosophy of Language','Disponível',2012,'2023-02-14','Disponível para empréstimo',0,5),(46,'The Handbook of New Media','Emprestado',2006,'2023-02-15','Disponível para empréstimo',1,6),(47,'The Oxford Handbook of Economic Geography','Disponível',2000,'2023-02-16','Disponível para empréstimo',0,7),(48,'The Cambridge Companion to the History of the Book','Emprestado',2015,'2023-02-17','Disponível para empréstimo',1,8),(49,'The Routledge Companion to American Literature','Disponível',2020,'2023-02-18','Disponível para empréstimo',0,9),(50,'The Cambridge Companion to the Philosophy of Language','Emprestado',2004,'2023-02-19','Disponível para empréstimo',1,10),(51,'The Oxford Handbook of Political Psychology','Disponível',2011,'2023-02-20','Disponível para empréstimo',0,1),(52,'The Cambridge Companion to Feminist Literary Theory','Emprestado',2004,'2023-02-21','Disponível para empréstimo',1,2),(53,'The Routledge Handbook of Peacebuilding','Disponível',2013,'2023-02-24','Disponível para empréstimo',0,3),(54,'The Cambridge Handbook of Language and Social Interaction','Emprestado',2011,'2023-02-23','Disponível para empréstimo',1,4),(55,'The Routledge Handbook of Peacebuilding','Disponível',2013,'2023-02-24','Disponível para empréstimo',0,5),(56,'The Oxford Handbook of Social and Political Trust','Emprestado',2016,'2023-02-25','Disponível para empréstimo',1,6);
/*!40000 ALTER TABLE `livros` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `livros_autores`
--

DROP TABLE IF EXISTS `livros_autores`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `livros_autores` (
  `livro_id` int NOT NULL,
  `autor_id` int NOT NULL,
  PRIMARY KEY (`livro_id`,`autor_id`),
  KEY `autor_id` (`autor_id`),
  CONSTRAINT `livros_autores_ibfk_1` FOREIGN KEY (`livro_id`) REFERENCES `livros` (`id`),
  CONSTRAINT `livros_autores_ibfk_2` FOREIGN KEY (`autor_id`) REFERENCES `autores` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `livros_autores`
--

LOCK TABLES `livros_autores` WRITE;
/*!40000 ALTER TABLE `livros_autores` DISABLE KEYS */;
INSERT INTO `livros_autores` VALUES (1,1),(47,1),(53,1),(2,2),(47,2),(54,2),(3,3),(48,3),(55,3),(4,4),(48,4),(56,4),(5,5),(49,5),(6,6),(49,6),(7,7),(50,7),(8,8),(50,8),(9,9),(51,9),(10,10),(51,10),(11,11),(52,11),(12,12),(52,12),(13,13),(53,13),(14,14),(53,14),(15,15),(54,15),(16,16),(54,16),(17,17),(55,17),(18,18),(55,18),(19,19),(56,19),(20,20),(56,20),(21,21),(47,21),(22,22),(48,22),(23,23),(49,23),(24,24),(50,24),(25,25),(51,25),(26,26),(52,26),(27,27),(53,27),(28,28),(54,28),(29,29),(55,29),(30,30),(56,30),(31,31),(47,31),(32,32),(48,32),(33,33),(49,33),(34,34),(50,34),(35,35),(51,35),(36,36),(52,36),(37,37),(53,37),(38,38),(54,38),(39,39),(55,39),(40,40),(56,40),(41,41),(47,41),(42,42),(48,42),(43,43),(49,43),(44,44),(50,44),(45,45),(51,45),(46,46),(52,46);
/*!40000 ALTER TABLE `livros_autores` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-08-14  9:22:58
