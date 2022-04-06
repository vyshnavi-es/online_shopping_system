-- MySQL dump 10.13  Distrib 8.0.22, for Win64 (x86_64)
--
-- Host: 127.0.0.1    Database: shopping
-- ------------------------------------------------------
-- Server version	8.0.22

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
-- Dumping data for table `cart`
--

LOCK TABLES `cart` WRITE;
/*!40000 ALTER TABLE `cart` DISABLE KEYS */;
INSERT INTO `cart` VALUES (1340,'Aliexpress','OrangeCropTop',400,1,'M',':/newPrefix/pics/Orange Crop Top.png',400),(1341,'Ajio','BlackTunicTop',500,2,'L',':/newPrefix/pics/Black Tunic Top.png',1000),(1342,'Ajio','PinkFloralTop',300,3,'S',':/newPrefix/pics/Pink Floral Top.png',900),(1343,'Meesho','PinkTunicTop',400,3,'L',':/newPrefix/pics/Pink Tunic Top.png',1200),(1344,'DreamDay','BlackMeshTop',350,2,'M',':/newPrefix/pics/Black Mesh Top.png',700),(1345,'Myntra','Black and white Striped shorts',400,2,'M',':/pics/WhatsApp-Image-2020-12-03-at-9.51.43-PM-_1_.png',800),(1346,'DreamDay','Torn Blue Denim',500,2,'L',':/pics/WhatsApp-Image-2020-12-03-at-9.51.43-PM.png',1000),(1347,'Ajio','Maroon Skirt',600,3,'L',':/pics/WhatsApp-Image-2020-12-03-at-9.51.44-PM.png',1800),(1348,'Meesho','Floral Pencil Skirt',400,2,'M',':/pics/WhatsApp-Image-2020-12-03-at-9.51.43-PM-_2_.png',800),(1349,'DreamDay','Blue Denim Dungaree',500,1,'S',':/newPrefix/pics/_Image_2020-12-03_at_10.09.27_PM_1_.png',500),(1350,'DreamDay','RedGown',800,3,'L',':/newPrefix/pics/App_Image_2020-12-03_at_10.09.27_PM.png',2400),(1351,'Ali Express','Yellow Romper Dress',400,2,'M',':/newPrefix/pics/App_Image_2020-12-03_at_10.09.26_PM.png',800),(1352,'Myntra','Grey Casual Dress',500,1,'S',':/newPrefix/pics/App_Image_2020-12-03_at_10.09.28_PM.png',500),(1353,'Ajio','Red Skirt and Crop Top',700,2,'L',':/newPrefix/pics/WhatsApp Image 2020-12-05 at 10.53.28 AM.jpeg',1400),(1354,'Myntra','Black Skirt and Crop Top',500,4,'L',':/newPrefix/pics/WhatsApp Image 2020-12-05 at 10.53.28 AM (1).jpeg',2000),(1355,'Everstyle','Black and Gold Jhumka',100,2,'-',':/newPrefix/pics/WhatsApp Image 2020-12-05 at 10.39.33 AM.jpeg',200),(1356,'Everstyle','Ear cuffs',120,1,'-',':/newPrefix/pics/WhatsApp Image 2020-12-05 at 10.39.33 AM (1).jpeg',120),(1357,'Everstyle','Dainty stone neckpiece ',250,4,'-',':/newPrefix/pics/WhatsApp-Image-2020-12-04-at-6.27.08-PM.png',1000),(1358,'Everstyle','Black Hangings ',200,5,'-',':/newPrefix/pics/WhatsApp Image 2020-12-05 at 10.39.32 AM.jpeg',1000);
/*!40000 ALTER TABLE `cart` ENABLE KEYS */;
UNLOCK TABLES;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'STRICT_TRANS_TABLES,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
/*!50003 CREATE*/ /*!50017 DEFINER=`root`@`localhost`*/ /*!50003 TRIGGER `cart_BEFORE_INSERT` BEFORE INSERT ON `cart` FOR EACH ROW BEGIN
	set new.itemTotal = new.pro_price * new.quantity;
END */;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2021-01-17  0:45:56
