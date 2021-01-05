-- MySQL dump 10.13  Distrib 8.0.22, for Win64 (x86_64)
--
-- Host: localhost    Database: db_Biblioteca
-- ------------------------------------------------------
-- Server version	8.0.22

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `tbl_autores`
--

DROP TABLE IF EXISTS `tbl_autores`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tbl_autores` (
  `ID_Autor` smallint NOT NULL,
  `Nome_Autor` varchar(50) DEFAULT NULL,
  `Sobrenome_Autor` varchar(60) DEFAULT NULL,
  PRIMARY KEY (`ID_Autor`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tbl_autores`
--

LOCK TABLES `tbl_autores` WRITE;
/*!40000 ALTER TABLE `tbl_autores` DISABLE KEYS */;
INSERT INTO `tbl_autores` VALUES (1,'Daniel','Barret'),(2,'Gerald','Carter'),(3,'Mark','Sobel'),(4,'William','Stanek'),(5,'Richard','Blum'),(6,'João',NULL),(7,'João','da Silva'),(8,'Rita','de Souza'),(9,'Ana',NULL);
/*!40000 ALTER TABLE `tbl_autores` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tbl_editoras`
--

DROP TABLE IF EXISTS `tbl_editoras`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tbl_editoras` (
  `ID_Editora` smallint NOT NULL AUTO_INCREMENT,
  `Nome_Editora` varchar(50) NOT NULL,
  PRIMARY KEY (`ID_Editora`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tbl_editoras`
--

LOCK TABLES `tbl_editoras` WRITE;
/*!40000 ALTER TABLE `tbl_editoras` DISABLE KEYS */;
INSERT INTO `tbl_editoras` VALUES (1,'Prentice Hall'),(2,'O´Reilly'),(3,'Microsoft Press'),(4,'Willey');
/*!40000 ALTER TABLE `tbl_editoras` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tbl_livro`
--

DROP TABLE IF EXISTS `tbl_livro`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tbl_livro` (
  `ID_Livro` smallint NOT NULL AUTO_INCREMENT,
  `Nome_Livro` varchar(50) NOT NULL,
  `ISBN` varchar(30) NOT NULL,
  `Data_Pub` date NOT NULL,
  `Preco_Livro` decimal(10,0) NOT NULL,
  `ID_Autor` smallint NOT NULL,
  `ID_editora` smallint NOT NULL,
  PRIMARY KEY (`ID_Livro`),
  KEY `fk_ID_Autor` (`ID_Autor`),
  KEY `fk_ID_editora` (`ID_editora`),
  CONSTRAINT `fk_ID_Autor` FOREIGN KEY (`ID_Autor`) REFERENCES `tbl_autores` (`ID_Autor`),
  CONSTRAINT `fk_ID_editora` FOREIGN KEY (`ID_editora`) REFERENCES `tbl_editoras` (`ID_Editora`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tbl_livro`
--

LOCK TABLES `tbl_livro` WRITE;
/*!40000 ALTER TABLE `tbl_livro` DISABLE KEYS */;
INSERT INTO `tbl_livro` VALUES (1,'Linux Command Line and Shell Scripting','143856969','2009-12-21',68,5,4),(2,'SSH, o Shell Seguro','127658789','2009-12-21',58,1,2),(3,'Using Samba','123856789','2000-12-21',61,2,2),(4,'Fedora and Red Hat Linux','123456789','2010-11-01',62,3,1),(5,'Windows Server 2012 Inside Out','123356789','2004-05-17',67,4,3),(6,'Microsoft Exchange Server 2010','123366789','2000-12-21',45,4,3);
/*!40000 ALTER TABLE `tbl_livro` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tbl_teste_incremento`
--

DROP TABLE IF EXISTS `tbl_teste_incremento`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tbl_teste_incremento` (
  `Codigo` smallint NOT NULL AUTO_INCREMENT,
  `Nome` varchar(20) NOT NULL,
  PRIMARY KEY (`Codigo`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tbl_teste_incremento`
--

LOCK TABLES `tbl_teste_incremento` WRITE;
/*!40000 ALTER TABLE `tbl_teste_incremento` DISABLE KEYS */;
/*!40000 ALTER TABLE `tbl_teste_incremento` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2021-01-02 11:53:42
