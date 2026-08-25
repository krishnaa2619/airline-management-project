-- MySQL dump 10.13  Distrib 8.0.40, for Win64 (x86_64)
--
-- Host: localhost    Database: airway
-- ------------------------------------------------------
-- Server version	8.0.40

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
-- Table structure for table `admin`
--

DROP TABLE IF EXISTS `admin`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `admin` (
  `Admin_Name` varchar(50) DEFAULT NULL,
  `Admin_Password` varchar(50) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `admin`
--

LOCK TABLES `admin` WRITE;
/*!40000 ALTER TABLE `admin` DISABLE KEYS */;
INSERT INTO `admin` VALUES ('jay','1807'),('krishna','1603'),('admin','admin');
/*!40000 ALTER TABLE `admin` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `booking`
--

DROP TABLE IF EXISTS `booking`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `booking` (
  `Cust_id` int DEFAULT NULL,
  `Ticket_No` bigint NOT NULL,
  `class` varchar(30) DEFAULT NULL,
  `row_no` int DEFAULT NULL,
  `column_letter` char(1) DEFAULT NULL,
  `Flight_no` int DEFAULT NULL,
  PRIMARY KEY (`Ticket_No`),
  KEY `Cust_id` (`Cust_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `booking`
--

LOCK TABLES `booking` WRITE;
/*!40000 ALTER TABLE `booking` DISABLE KEYS */;
INSERT INTO `booking` VALUES (13,15582269,'Premium Economy class',3,'A',98765),(13,16672604,'Economy class',9,'i',12345),(12,16850866,'Business class',3,'D',99887),(22,20167011,'First class',1,'c',98765),(21,25064165,'Business class',8,'D',66554),(11,31542063,'Economy class',1,'I',88776),(18,46763581,'Premium Economy class',3,'D',88776),(12,51317852,'Economy class',4,'A',10987),(18,52058594,'Premium Economy class',3,'C',88776),(23,52455727,'Business class',8,'a',12345),(17,55703191,'First class',2,'B',22110),(17,56076669,'Economy class',9,'I',55443),(13,68053998,'First class',1,'A',12345),(19,69414198,'Economy class',2,'H',66554),(15,72462460,'First class',2,'c',77889),(14,72820490,'Economy class',1,'I',22110),(11,83146174,'First class',2,'C',98765),(14,84002296,'Business class',5,'B',11223),(16,86585377,'Economy class',3,'I',66554),(14,89112807,'Economy class',9,'I',12345),(22,91565775,'Premium Economy class',3,'e',44556),(14,92017639,'Premium Economy class',3,'f',11223);
/*!40000 ALTER TABLE `booking` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `customer`
--

DROP TABLE IF EXISTS `customer`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `customer` (
  `Cust_id` int NOT NULL AUTO_INCREMENT,
  `Cust_Name` varchar(50) DEFAULT NULL,
  `Cust_Email` varchar(50) DEFAULT NULL,
  `Cust_PhoneNo` varchar(10) DEFAULT NULL,
  `Cust_Password` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`Cust_id`),
  UNIQUE KEY `Cust_PhoneNo` (`Cust_PhoneNo`)
) ENGINE=InnoDB AUTO_INCREMENT=27 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `customer`
--

LOCK TABLES `customer` WRITE;
/*!40000 ALTER TABLE `customer` DISABLE KEYS */;
INSERT INTO `customer` VALUES (11,'Akash Gupta ','akash121@gmail.com','9501291345','ak@gu'),(12,'Kevin Johnson','johnson.k@hotmail.com','9875672376','ke@jo'),(13,'Ajay Rathi','ajrat@hotmail.com','9999999999','aj@ra'),(14,'Yash Hemnani','yash@gmail.com','9712233166','ya@he'),(15,'Ishan Sharma','pedoishan@gmail.com','7328743676','is@sh'),(16,'Thejas A.S.','annabella@gmail.com','9876543210','th@as'),(17,'krishna agarwal','krishna@gmail.com','6354507058','krishna@1603'),(18,'jay P','jay@gmail.com','8160769857','jay@1807'),(19,'Ajit Gandhi','ajit.g911@gmail.com','9289748932','aj@ga'),(20,'Ankur Mishra','m.ankur@gmail.com','8374829034','an@mi'),(21,'krishna','krishna.a@gmail.com','9327337331','1603'),(23,'moksh jain','moksh@gmail.com','7990679633','1201'),(24,'naman jain','naman@gmail.com','3693693693','6666'),(25,'mate matlock','matlock@gmail.com','8546321456','ma22'),(26,'kirtan b','kiran@gmail.com','7532698456','kri@123');
/*!40000 ALTER TABLE `customer` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `flight`
--

DROP TABLE IF EXISTS `flight`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `flight` (
  `Flight_Number` int NOT NULL,
  `Flight_Name` varchar(50) DEFAULT NULL,
  `Departure` varchar(50) DEFAULT NULL,
  `Arrival` varchar(50) DEFAULT NULL,
  `Price` int DEFAULT NULL,
  PRIMARY KEY (`Flight_Number`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `flight`
--

LOCK TABLES `flight` WRITE;
/*!40000 ALTER TABLE `flight` DISABLE KEYS */;
INSERT INTO `flight` VALUES (10987,'Air India','Bangalore','Delhi',7100),(11223,'IndiGo','Mumbai','Kolkata',7500),(12345,'IndiGo','Delhi','Mumbai',5800),(19489,'Vistara','Surat','Hyderabad',50003),(22110,'IndiGo','Surat','Delhi',6150),(25678,'Air India','Kolkata','Surat',5300),(33221,'Vistara','Mumbai','Surat',8500),(44556,'IndiGo','Hyderabad','Surat',4200),(54321,'Air India','Chennai','Hyderabad',3850),(55443,'Vistara','Bangalore','Mumbai',7900),(66554,'Vistara','Goa','Bangalore',5500),(67890,'IndiGo','Delhi','Goa',6200),(77889,'IndiGo','Ahmedabad','Mumbai',4650),(88776,'Vistara','Delhi','Chennai',6950),(95802,'Air India ','Bangalore','Kolkata',6500),(98765,'Air India','Surat','Goa',4500),(99887,'Vistara','Chennai','Kolkata',7350);
/*!40000 ALTER TABLE `flight` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2025-10-22  3:42:12
