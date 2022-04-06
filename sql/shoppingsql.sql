CREATE DATABASE  IF NOT EXISTS `shopping` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `shopping`;
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
-- Dumping data for table `accessories`
--

LOCK TABLES `accessories` WRITE;
/*!40000 ALTER TABLE `accessories` DISABLE KEYS */;
INSERT INTO `accessories` VALUES (1,'Everstyle','Black and Gold Jhumka',100,10,_binary ':/newPrefix/pics/WhatsApp Image 2020-12-05 at 10.39.33 AM.jpeg'),(2,'Everstyle','Ear cuffs',120,12,_binary ':/newPrefix/pics/WhatsApp Image 2020-12-05 at 10.39.33 AM (1).jpeg);'),(3,'Everstyle','Dainty stone neckpiece',250,0,_binary ':/newPrefix/pics/WhatsApp-Image-2020-12-04-at-6.27.08-PM.png'),(4,'Everstyle','Black Hangings',200,0,_binary ':/newPrefix/pics/WhatsApp Image 2020-12-05 at 10.39.32 AM.jpeg);');
/*!40000 ALTER TABLE `accessories` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `bottoms`
--

LOCK TABLES `bottoms` WRITE;
/*!40000 ALTER TABLE `bottoms` DISABLE KEYS */;
INSERT INTO `bottoms` VALUES (6,'Myntra','Black and white Striped shorts',400,_binary ':/pics/WhatsApp-Image-2020-12-03-at-9.51.43-PM-_1_.png',5,4,100),(7,'DreamDay','Torn Blue Denim',500,_binary ':/pics/WhatsApp-Image-2020-12-03-at-9.51.43-PM.png',100,100,98),(8,'Ajio','Maroon Skirt',600,_binary ':/pics/WhatsApp-Image-2020-12-03-at-9.51.44-PM.png',99,100,97),(9,'Meesho','Floral Pencil Skirt',400,_binary ':/pics/WhatsApp-Image-2020-12-03-at-9.51.43-PM-_2_.png',100,98,100),(10,'DreamDay','Blue Denim Dungaree',500,_binary ':/newPrefix/pics/_Image_2020-12-03_at_10.09.27_PM_1_.png',99,100,100);
/*!40000 ALTER TABLE `bottoms` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `cart`
--

LOCK TABLES `cart` WRITE;
/*!40000 ALTER TABLE `cart` DISABLE KEYS */;
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

--
-- Dumping data for table `dresses`
--

LOCK TABLES `dresses` WRITE;
/*!40000 ALTER TABLE `dresses` DISABLE KEYS */;
INSERT INTO `dresses` VALUES (11,'DreamDay','RedGown',800,_binary ':/newPrefix/pics/App_Image_2020-12-03_at_10.09.27_PM.png',99,100,97),(12,'Ali Express','Yellow Romper Dress',400,_binary ':/newPrefix/pics/App_Image_2020-12-03_at_10.09.26_PM.png',100,97,0),(13,'Myntra','Grey Casual Dress',500,_binary ':/newPrefix/pics/App_Image_2020-12-03_at_10.09.28_PM.png',0,99,100),(14,'Ajio','Red Skirt and Crop Top',700,_binary ':/newPrefix/pics/WhatsApp Image 2020-12-05 at 10.53.28 AM.jpeg',100,0,8),(15,'Myntra','Black Skirt and Crop Top',500,_binary ':/newPrefix/pics/WhatsApp Image 2020-12-05 at 10.53.28 AM (1).jpeg',99,5,96);
/*!40000 ALTER TABLE `dresses` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `orders`
--

LOCK TABLES `orders` WRITE;
/*!40000 ALTER TABLE `orders` DISABLE KEYS */;
INSERT INTO `orders` VALUES (1,'vysh','1390','OrangeCropTop','Aliexpress',400,5,'M',_binary ':/newPrefix/pics/Orange Crop Top.png','paris',2000),(2,'vysh','1391','OrangeCropTop','Aliexpress',400,1,'L',_binary ':/newPrefix/pics/Orange Crop Top.png','paris',400),(3,'swathi','1394','Black Hangings ','Everstyle',200,6,'-',_binary ':/newPrefix/pics/WhatsApp Image 2020-12-05 at 10.39.32 AM.jpeg','france',1200),(4,'shirin','1395','Dainty stone neckpiece ','Everstyle',250,5,'-',_binary ':/newPrefix/pics/WhatsApp-Image-2020-12-04-at-6.27.08-PM.png','UK',1250),(5,'shirin','1396','Black Hangings ','Everstyle',200,5,'-',_binary ':/newPrefix/pics/WhatsApp Image 2020-12-05 at 10.39.32 AM.jpeg','UK',1000),(6,'vysh','1397','Black and Gold Jhumka','Everstyle',100,5,'-',_binary ':/newPrefix/pics/WhatsApp Image 2020-12-05 at 10.39.33 AM.jpeg','delhi',500),(7,'vysh','1398','Dainty stone neckpiece ','Everstyle',250,5,'-',_binary ':/newPrefix/pics/WhatsApp-Image-2020-12-04-at-6.27.08-PM.png','delhi',1250),(8,'vysh','1399','Yellow Romper Dress','Ali Express',400,1,'M',_binary ':/newPrefix/pics/App_Image_2020-12-03_at_10.09.26_PM.png','delhi',400),(9,'sam','1400','Ear cuffs','Everstyle',120,3,'-',_binary ':/newPrefix/pics/WhatsApp Image 2020-12-05 at 10.39.33 AM (1).jpeg','NYC',360),(10,'sam','1401','Dainty stone neckpiece ','Everstyle',250,5,'-',_binary ':/newPrefix/pics/WhatsApp-Image-2020-12-04-at-6.27.08-PM.png','NYC',1250),(11,'sam','1402','Black Hangings ','Everstyle',200,5,'-',_binary ':/newPrefix/pics/WhatsApp Image 2020-12-05 at 10.39.32 AM.jpeg','NYC',1000),(12,'sush','1403','Dainty stone neckpiece ','Everstyle',250,5,'-',_binary ':/newPrefix/pics/WhatsApp-Image-2020-12-04-at-6.27.08-PM.png','goa',1250),(13,'sush','1404','Ear cuffs','Everstyle',120,5,'-',_binary ':/newPrefix/pics/WhatsApp Image 2020-12-05 at 10.39.33 AM (1).jpeg','goa',600),(14,'sush','1405','Black Hangings ','Everstyle',200,5,'-',_binary ':/newPrefix/pics/WhatsApp Image 2020-12-05 at 10.39.32 AM.jpeg','goa',1000);
/*!40000 ALTER TABLE `orders` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `tops_tunics_and_dresses`
--

LOCK TABLES `tops_tunics_and_dresses` WRITE;
/*!40000 ALTER TABLE `tops_tunics_and_dresses` DISABLE KEYS */;
INSERT INTO `tops_tunics_and_dresses` VALUES (1,'Aliexpress','OrangeCropTop',400,_binary ':/newPrefix/pics/Orange Crop Top.png',0,0,9),(2,'Ajio','BlackTunicTop',500,_binary ':/newPrefix/pics/BlackTunicTop.png',5,10,0),(3,'Ajio','PinkFloralTop',300,_binary ':/newPrefix/pics/PinkFloralTop.png',97,100,97),(4,'DreamDay','BlackMeshTop',350,_binary ':/newPrefix/pics/BlackMeshTop.png',3,3,10),(5,'Meesho','PinkTunicTop',400,_binary ':/newPrefix/pics/PinkTunicTop.png',100,100,97);
/*!40000 ALTER TABLE `tops_tunics_and_dresses` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `users`
--

LOCK TABLES `users` WRITE;
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
INSERT INTO `users` VALUES (2,'vysh','987654321','vysh12'),(3,'ram','897456123','ram123'),(5,'gabriel','8970654787','inparis'),(6,'vishwa','123456789','123'),(8,'varun','7760539180','12varun'),(14,'sam','978546231','samjam'),(15,'arjun','987456321','arjun34'),(16,'rani','12345','1212'),(17,'chai','978461332','chaisam'),(19,'swathi','1234567789','swa123'),(20,'sfsd','7760539180','7777777'),(24,'shirin','9874563','we'),(26,'sush','9897456321','sush');
/*!40000 ALTER TABLE `users` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping events for database 'shopping'
--

--
-- Dumping routines for database 'shopping'
--
/*!50003 DROP PROCEDURE IF EXISTS `increaseQuantityAccessories` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'STRICT_TRANS_TABLES,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
CREATE DEFINER=`root`@`localhost` PROCEDURE `increaseQuantityAccessories`(

	in newQuantity int,
    proName varchar(20)
)
BEGIN
	update accessories set a_quantity = a_quantity + newQuantity where a_name=proName;
END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `reduceQuantityAccessories` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'STRICT_TRANS_TABLES,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
CREATE DEFINER=`root`@`localhost` PROCEDURE `reduceQuantityAccessories`(

	in newQuantity int,
    proName varchar(30)
)
BEGIN
	update accessories set a_quantity = a_quantity - newQuantity where a_name = proName;
END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `reduceQuantityAccessory` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'STRICT_TRANS_TABLES,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
CREATE DEFINER=`root`@`localhost` PROCEDURE `reduceQuantityAccessory`(

	in newQuantity int,
    proName varchar(20)
)
BEGIN
	update accessories set a_quantity = a_quantity + newQuantity where a_name = proName;
END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `reduceQuantityBottom` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'STRICT_TRANS_TABLES,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
CREATE DEFINER=`root`@`localhost` PROCEDURE `reduceQuantityBottom`(

	in newQuantity int,
    proName varchar(30)
)
BEGIN
	update bottoms set quantity = quantity - newQuantity where bottom_name = proName; 
END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `reduceQuantityBottomL` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'STRICT_TRANS_TABLES,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
CREATE DEFINER=`root`@`localhost` PROCEDURE `reduceQuantityBottomL`(

	in newQuantity int,
    proName varchar(30),
	size varchar(5)
)
BEGIN
	update bottoms set l = l - newQuantity where bottom_name = proName and size=size; 
END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `reduceQuantityBottomM` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'STRICT_TRANS_TABLES,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
CREATE DEFINER=`root`@`localhost` PROCEDURE `reduceQuantityBottomM`(

	in newQuantity int,
    proName varchar(30),
	size varchar(5)
)
BEGIN
	update bottoms set m = m - newQuantity where bottom_name = proName and size=size; 
END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `reduceQuantityBottomS` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'STRICT_TRANS_TABLES,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
CREATE DEFINER=`root`@`localhost` PROCEDURE `reduceQuantityBottomS`(

	in newQuantity int,
    proName varchar(30),
	size varchar(5)
)
BEGIN
	update bottoms set s = s - newQuantity where bottom_name = proName and size=size; 
END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `reduceQuantityDresses` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'STRICT_TRANS_TABLES,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
CREATE DEFINER=`root`@`localhost` PROCEDURE `reduceQuantityDresses`(

in newQuantity int,
proName varchar(30)
)
BEGIN
    update dresses set quantity = quantity - newQuantity where dresses_name = proName;
END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `reduceQuantityDressesL` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'STRICT_TRANS_TABLES,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
CREATE DEFINER=`root`@`localhost` PROCEDURE `reduceQuantityDressesL`(

in newQuantity int,
proName varchar(30),
size varchar(5)
)
BEGIN
    update dresses set l = l - newQuantity where dresses_name = proName and size=size;
END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `reduceQuantityDressesM` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'STRICT_TRANS_TABLES,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
CREATE DEFINER=`root`@`localhost` PROCEDURE `reduceQuantityDressesM`(

in newQuantity int,
proName varchar(30),
size varchar(5)
)
BEGIN
    update dresses set m = m - newQuantity where dresses_name = proName and size=size;
END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `reduceQuantityDressesS` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'STRICT_TRANS_TABLES,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
CREATE DEFINER=`root`@`localhost` PROCEDURE `reduceQuantityDressesS`(

in newQuantity int,
proName varchar(30),
size varchar(5)
)
BEGIN
    update dresses set s = s - newQuantity where dresses_name = proName and size=size;
END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `reduceQuantityTops` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'STRICT_TRANS_TABLES,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
CREATE DEFINER=`root`@`localhost` PROCEDURE `reduceQuantityTops`(
	in newQuantity int,
    proName varchar(20),
    size varchar(5)
)
BEGIN
	update tops_tunics_and_dresses set s = s - newQuantity where top_name = proName and size=size; 
END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `reduceQuantityTopsL` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'STRICT_TRANS_TABLES,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
CREATE DEFINER=`root`@`localhost` PROCEDURE `reduceQuantityTopsL`(
	in newQuantity int,
    proName varchar(20),
    size varchar(5)
)
BEGIN
	update tops_tunics_and_dresses set l = l - newQuantity where top_name = proName and size=size; 
END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `reduceQuantityTopsM` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'STRICT_TRANS_TABLES,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
CREATE DEFINER=`root`@`localhost` PROCEDURE `reduceQuantityTopsM`(
	in newQuantity int,
    proName varchar(20),
    size varchar(5)
)
BEGIN
	update tops_tunics_and_dresses set m = m - newQuantity where top_name = proName and size=size; 
END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `reduceQuantityTopsS` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'STRICT_TRANS_TABLES,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
CREATE DEFINER=`root`@`localhost` PROCEDURE `reduceQuantityTopsS`(
	in newQuantity int,
    proName varchar(20),
    size varchar(5)
)
BEGIN
	update tops_tunics_and_dresses set s = s - newQuantity where top_name = proName and size=size; 
END ;;
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

-- Dump completed on 2021-01-18 15:48:04
