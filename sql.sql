/*
SQLyog Community Edition- MySQL GUI v8.03 
MySQL - 5.6.12-log : Database - 023_thief
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;

CREATE DATABASE /*!32312 IF NOT EXISTS*/`023_thief` /*!40100 DEFAULT CHARACTER SET latin1 */;

USE `023_thief`;

/*Table structure for table `auth_group` */

DROP TABLE IF EXISTS `auth_group`;

CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(150) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `auth_group` */

/*Table structure for table `auth_group_permissions` */

DROP TABLE IF EXISTS `auth_group_permissions`;

CREATE TABLE `auth_group_permissions` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `auth_group_permissions` */

/*Table structure for table `auth_permission` */

DROP TABLE IF EXISTS `auth_permission`;

CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=73 DEFAULT CHARSET=latin1;

/*Data for the table `auth_permission` */

insert  into `auth_permission`(`id`,`name`,`content_type_id`,`codename`) values (1,'Can add log entry',1,'add_logentry'),(2,'Can change log entry',1,'change_logentry'),(3,'Can delete log entry',1,'delete_logentry'),(4,'Can view log entry',1,'view_logentry'),(5,'Can add permission',2,'add_permission'),(6,'Can change permission',2,'change_permission'),(7,'Can delete permission',2,'delete_permission'),(8,'Can view permission',2,'view_permission'),(9,'Can add group',3,'add_group'),(10,'Can change group',3,'change_group'),(11,'Can delete group',3,'delete_group'),(12,'Can view group',3,'view_group'),(13,'Can add user',4,'add_user'),(14,'Can change user',4,'change_user'),(15,'Can delete user',4,'delete_user'),(16,'Can view user',4,'view_user'),(17,'Can add content type',5,'add_contenttype'),(18,'Can change content type',5,'change_contenttype'),(19,'Can delete content type',5,'delete_contenttype'),(20,'Can view content type',5,'view_contenttype'),(21,'Can add session',6,'add_session'),(22,'Can change session',6,'change_session'),(23,'Can delete session',6,'delete_session'),(24,'Can view session',6,'view_session'),(25,'Can add camera',7,'add_camera'),(26,'Can change camera',7,'change_camera'),(27,'Can delete camera',7,'delete_camera'),(28,'Can view camera',7,'view_camera'),(29,'Can add crime_category',8,'add_crime_category'),(30,'Can change crime_category',8,'change_crime_category'),(31,'Can delete crime_category',8,'delete_crime_category'),(32,'Can view crime_category',8,'view_crime_category'),(33,'Can add login',9,'add_login'),(34,'Can change login',9,'change_login'),(35,'Can delete login',9,'delete_login'),(36,'Can view login',9,'view_login'),(37,'Can add visitor_log',10,'add_visitor_log'),(38,'Can change visitor_log',10,'change_visitor_log'),(39,'Can delete visitor_log',10,'delete_visitor_log'),(40,'Can view visitor_log',10,'view_visitor_log'),(41,'Can add user',11,'add_user'),(42,'Can change user',11,'change_user'),(43,'Can delete user',11,'delete_user'),(44,'Can view user',11,'view_user'),(45,'Can add police_station',12,'add_police_station'),(46,'Can change police_station',12,'change_police_station'),(47,'Can delete police_station',12,'delete_police_station'),(48,'Can view police_station',12,'view_police_station'),(49,'Can add familiar_person',13,'add_familiar_person'),(50,'Can change familiar_person',13,'change_familiar_person'),(51,'Can delete familiar_person',13,'delete_familiar_person'),(52,'Can view familiar_person',13,'view_familiar_person'),(53,'Can add familiar_log',14,'add_familiar_log'),(54,'Can change familiar_log',14,'change_familiar_log'),(55,'Can delete familiar_log',14,'delete_familiar_log'),(56,'Can view familiar_log',14,'view_familiar_log'),(57,'Can add criminals',15,'add_criminals'),(58,'Can change criminals',15,'change_criminals'),(59,'Can delete criminals',15,'delete_criminals'),(60,'Can view criminals',15,'view_criminals'),(61,'Can add crimehistory',16,'add_crimehistory'),(62,'Can change crimehistory',16,'change_crimehistory'),(63,'Can delete crimehistory',16,'delete_crimehistory'),(64,'Can view crimehistory',16,'view_crimehistory'),(65,'Can add complaint',17,'add_complaint'),(66,'Can change complaint',17,'change_complaint'),(67,'Can delete complaint',17,'delete_complaint'),(68,'Can view complaint',17,'view_complaint'),(69,'Can add alert',18,'add_alert'),(70,'Can change alert',18,'change_alert'),(71,'Can delete alert',18,'delete_alert'),(72,'Can view alert',18,'view_alert');

/*Table structure for table `auth_user` */

DROP TABLE IF EXISTS `auth_user`;

CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(150) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `auth_user` */

/*Table structure for table `auth_user_groups` */

DROP TABLE IF EXISTS `auth_user_groups`;

CREATE TABLE `auth_user_groups` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`),
  CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `auth_user_groups` */

/*Table structure for table `auth_user_user_permissions` */

DROP TABLE IF EXISTS `auth_user_user_permissions`;

CREATE TABLE `auth_user_user_permissions` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `auth_user_user_permissions` */

/*Table structure for table `django_admin_log` */

DROP TABLE IF EXISTS `django_admin_log`;

CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`),
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `django_admin_log` */

/*Table structure for table `django_content_type` */

DROP TABLE IF EXISTS `django_content_type`;

CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=19 DEFAULT CHARSET=latin1;

/*Data for the table `django_content_type` */

insert  into `django_content_type`(`id`,`app_label`,`model`) values (1,'admin','logentry'),(3,'auth','group'),(2,'auth','permission'),(4,'auth','user'),(5,'contenttypes','contenttype'),(6,'sessions','session'),(18,'Thief','alert'),(7,'Thief','camera'),(17,'Thief','complaint'),(16,'Thief','crimehistory'),(8,'Thief','crime_category'),(15,'Thief','criminals'),(14,'Thief','familiar_log'),(13,'Thief','familiar_person'),(9,'Thief','login'),(12,'Thief','police_station'),(11,'Thief','user'),(10,'Thief','visitor_log');

/*Table structure for table `django_migrations` */

DROP TABLE IF EXISTS `django_migrations`;

CREATE TABLE `django_migrations` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=20 DEFAULT CHARSET=latin1;

/*Data for the table `django_migrations` */

insert  into `django_migrations`(`id`,`app`,`name`,`applied`) values (1,'Thief','0001_initial','2024-02-09 07:32:29.354883'),(2,'contenttypes','0001_initial','2024-02-09 07:32:29.409149'),(3,'auth','0001_initial','2024-02-09 07:32:29.644662'),(4,'admin','0001_initial','2024-02-09 07:32:29.698300'),(5,'admin','0002_logentry_remove_auto_add','2024-02-09 07:32:29.706321'),(6,'admin','0003_logentry_add_action_flag_choices','2024-02-09 07:32:29.714342'),(7,'contenttypes','0002_remove_content_type_name','2024-02-09 07:32:29.763467'),(8,'auth','0002_alter_permission_name_max_length','2024-02-09 07:32:29.788031'),(9,'auth','0003_alter_user_email_max_length','2024-02-09 07:32:29.810089'),(10,'auth','0004_alter_user_username_opts','2024-02-09 07:32:29.818110'),(11,'auth','0005_alter_user_last_login_null','2024-02-09 07:32:29.844178'),(12,'auth','0006_require_contenttypes_0002','2024-02-09 07:32:29.848188'),(13,'auth','0007_alter_validators_add_error_messages','2024-02-09 07:32:29.856210'),(14,'auth','0008_alter_user_username_max_length','2024-02-09 07:32:29.879773'),(15,'auth','0009_alter_user_last_name_max_length','2024-02-09 07:32:29.904839'),(16,'auth','0010_alter_group_name_max_length','2024-02-09 07:32:29.930907'),(17,'auth','0011_update_proxy_permissions','2024-02-09 07:32:29.941936'),(18,'auth','0012_alter_user_first_name_max_length','2024-02-09 07:32:29.966999'),(19,'sessions','0001_initial','2024-02-09 07:32:29.994574');

/*Table structure for table `django_session` */

DROP TABLE IF EXISTS `django_session`;

CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `django_session` */

insert  into `django_session`(`session_key`,`session_data`,`expire_date`) values ('l8tfdxr39guhlnlkd5qec8tr04sidwbn','eyJsaWQiOjEsImxnIjoibGluIn0:1rYM43:wy82iMQ-i8DiYOQ235iWoLFytdJgkjaVhtdFVvr4VGA','2024-02-23 08:16:51.628619');

/*Table structure for table `thief_alert` */

DROP TABLE IF EXISTS `thief_alert`;

CREATE TABLE `thief_alert` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `date` varchar(100) NOT NULL,
  `CAMERA_id` bigint(20) NOT NULL,
  `CRIMINALS_id` bigint(20) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `Thief_alert_CAMERA_id_40917fa4_fk_Thief_camera_id` (`CAMERA_id`),
  KEY `Thief_alert_CRIMINALS_id_27bda68f_fk_Thief_criminals_id` (`CRIMINALS_id`),
  CONSTRAINT `Thief_alert_CRIMINALS_id_27bda68f_fk_Thief_criminals_id` FOREIGN KEY (`CRIMINALS_id`) REFERENCES `thief_criminals` (`id`),
  CONSTRAINT `Thief_alert_CAMERA_id_40917fa4_fk_Thief_camera_id` FOREIGN KEY (`CAMERA_id`) REFERENCES `thief_camera` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `thief_alert` */

/*Table structure for table `thief_camera` */

DROP TABLE IF EXISTS `thief_camera`;

CREATE TABLE `thief_camera` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `camera_number` varchar(20) NOT NULL,
  `USER_id` bigint(20) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `Thief_camera_USER_id_003bc5ad_fk_Thief_user_id` (`USER_id`),
  CONSTRAINT `Thief_camera_USER_id_003bc5ad_fk_Thief_user_id` FOREIGN KEY (`USER_id`) REFERENCES `thief_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `thief_camera` */

/*Table structure for table `thief_complaint` */

DROP TABLE IF EXISTS `thief_complaint`;

CREATE TABLE `thief_complaint` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `complaint` varchar(500) NOT NULL,
  `cdate` varchar(20) NOT NULL,
  `reply` varchar(500) NOT NULL,
  `rdate` varchar(20) NOT NULL,
  `USER_id` bigint(20) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `Thief_complaint_USER_id_908edddf_fk_Thief_user_id` (`USER_id`),
  CONSTRAINT `Thief_complaint_USER_id_908edddf_fk_Thief_user_id` FOREIGN KEY (`USER_id`) REFERENCES `thief_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `thief_complaint` */

/*Table structure for table `thief_crime_category` */

DROP TABLE IF EXISTS `thief_crime_category`;

CREATE TABLE `thief_crime_category` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `category_name` varchar(100) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

/*Data for the table `thief_crime_category` */

insert  into `thief_crime_category`(`id`,`category_name`) values (1,'IPC 308');

/*Table structure for table `thief_crimehistory` */

DROP TABLE IF EXISTS `thief_crimehistory`;

CREATE TABLE `thief_crimehistory` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `date` varchar(30) NOT NULL,
  `history` varchar(300) NOT NULL,
  `CATEGORY_id` bigint(20) NOT NULL,
  `CRIMINAL_id` bigint(20) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `Thief_crimehistory_CATEGORY_id_f5bf3ad3_fk_Thief_cri` (`CATEGORY_id`),
  KEY `Thief_crimehistory_CRIMINAL_id_be4f7092_fk_Thief_criminals_id` (`CRIMINAL_id`),
  CONSTRAINT `Thief_crimehistory_CRIMINAL_id_be4f7092_fk_Thief_criminals_id` FOREIGN KEY (`CRIMINAL_id`) REFERENCES `thief_criminals` (`id`),
  CONSTRAINT `Thief_crimehistory_CATEGORY_id_f5bf3ad3_fk_Thief_cri` FOREIGN KEY (`CATEGORY_id`) REFERENCES `thief_crime_category` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `thief_crimehistory` */

/*Table structure for table `thief_criminals` */

DROP TABLE IF EXISTS `thief_criminals`;

CREATE TABLE `thief_criminals` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL,
  `gender` varchar(100) NOT NULL,
  `age` varchar(100) NOT NULL,
  `place` varchar(100) NOT NULL,
  `post` varchar(100) NOT NULL,
  `pin` varchar(100) NOT NULL,
  `contact` varchar(100) NOT NULL,
  `photo` varchar(100) NOT NULL,
  `POLICE_id` bigint(20) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `Thief_criminals_POLICE_id_eb42b81b_fk_Thief_police_station_id` (`POLICE_id`),
  CONSTRAINT `Thief_criminals_POLICE_id_eb42b81b_fk_Thief_police_station_id` FOREIGN KEY (`POLICE_id`) REFERENCES `thief_police_station` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `thief_criminals` */

/*Table structure for table `thief_familiar_log` */

DROP TABLE IF EXISTS `thief_familiar_log`;

CREATE TABLE `thief_familiar_log` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `date` varchar(100) NOT NULL,
  `time` varchar(100) NOT NULL,
  `CAMERA_id` bigint(20) NOT NULL,
  `FAMILIAR_PERSON_id` bigint(20) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `Thief_familiar_log_CAMERA_id_e7882c05_fk_Thief_camera_id` (`CAMERA_id`),
  KEY `Thief_familiar_log_FAMILIAR_PERSON_id_e6960a4d_fk_Thief_fam` (`FAMILIAR_PERSON_id`),
  CONSTRAINT `Thief_familiar_log_FAMILIAR_PERSON_id_e6960a4d_fk_Thief_fam` FOREIGN KEY (`FAMILIAR_PERSON_id`) REFERENCES `thief_familiar_person` (`id`),
  CONSTRAINT `Thief_familiar_log_CAMERA_id_e7882c05_fk_Thief_camera_id` FOREIGN KEY (`CAMERA_id`) REFERENCES `thief_camera` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `thief_familiar_log` */

/*Table structure for table `thief_familiar_person` */

DROP TABLE IF EXISTS `thief_familiar_person`;

CREATE TABLE `thief_familiar_person` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `F_name` varchar(100) NOT NULL,
  `F_place` varchar(100) NOT NULL,
  `F_contact` varchar(100) NOT NULL,
  `F_image` varchar(100) NOT NULL,
  `USER_id` bigint(20) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `Thief_familiar_person_USER_id_e9d34c8e_fk_Thief_user_id` (`USER_id`),
  CONSTRAINT `Thief_familiar_person_USER_id_e9d34c8e_fk_Thief_user_id` FOREIGN KEY (`USER_id`) REFERENCES `thief_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

/*Data for the table `thief_familiar_person` */

insert  into `thief_familiar_person`(`id`,`F_name`,`F_place`,`F_contact`,`F_image`,`USER_id`) values (1,'nefih kader','pazhayangadi','9874563214','/static/photo/20240209_133510.jpg',1);

/*Table structure for table `thief_login` */

DROP TABLE IF EXISTS `thief_login`;

CREATE TABLE `thief_login` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `username` varchar(100) NOT NULL,
  `password` varchar(100) NOT NULL,
  `type` varchar(50) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;

/*Data for the table `thief_login` */

insert  into `thief_login`(`id`,`username`,`password`,`type`) values (1,'admin@gmail.com','admin','admin'),(2,'nafihkader2820@gmail.com','Kedar@2024','user'),(3,'ksdpolice@gmail.com','6497','policestation');

/*Table structure for table `thief_police_station` */

DROP TABLE IF EXISTS `thief_police_station`;

CREATE TABLE `thief_police_station` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL,
  `place` varchar(100) NOT NULL,
  `post` varchar(100) NOT NULL,
  `pin` varchar(100) NOT NULL,
  `email` varchar(100) NOT NULL,
  `contact` varchar(100) NOT NULL,
  `LOGIN_id` bigint(20) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `Thief_police_station_LOGIN_id_6bd97055_fk_Thief_login_id` (`LOGIN_id`),
  CONSTRAINT `Thief_police_station_LOGIN_id_6bd97055_fk_Thief_login_id` FOREIGN KEY (`LOGIN_id`) REFERENCES `thief_login` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

/*Data for the table `thief_police_station` */

insert  into `thief_police_station`(`id`,`name`,`place`,`post`,`pin`,`email`,`contact`,`LOGIN_id`) values (1,'Kasargod Police Station','Kasargod','Kasargod','679087','ksdpolice@gmail.com','9638527412',3);

/*Table structure for table `thief_user` */

DROP TABLE IF EXISTS `thief_user`;

CREATE TABLE `thief_user` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL,
  `place` varchar(100) NOT NULL,
  `post` varchar(100) NOT NULL,
  `pin` varchar(100) NOT NULL,
  `email` varchar(100) NOT NULL,
  `contact` varchar(100) NOT NULL,
  `photo` varchar(100) NOT NULL,
  `LOGIN_id` bigint(20) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `Thief_user_LOGIN_id_ee1ae123_fk_Thief_login_id` (`LOGIN_id`),
  CONSTRAINT `Thief_user_LOGIN_id_ee1ae123_fk_Thief_login_id` FOREIGN KEY (`LOGIN_id`) REFERENCES `thief_login` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

/*Data for the table `thief_user` */

insert  into `thief_user`(`id`,`name`,`place`,`post`,`pin`,`email`,`contact`,`photo`,`LOGIN_id`) values (1,'justin@baby','kannur','Angadikadavu','670706','nafihkader2820@gmail.com','8590632966','/static/photo/20240209_132923.jpg',2);

/*Table structure for table `thief_visitor_log` */

DROP TABLE IF EXISTS `thief_visitor_log`;

CREATE TABLE `thief_visitor_log` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `image` varchar(200) NOT NULL,
  `date` varchar(100) NOT NULL,
  `time` varchar(100) NOT NULL,
  `CAMERA_id` bigint(20) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `Thief_visitor_log_CAMERA_id_ba1771d6_fk_Thief_camera_id` (`CAMERA_id`),
  CONSTRAINT `Thief_visitor_log_CAMERA_id_ba1771d6_fk_Thief_camera_id` FOREIGN KEY (`CAMERA_id`) REFERENCES `thief_camera` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `thief_visitor_log` */

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
