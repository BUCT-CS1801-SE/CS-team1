-- the sql sentence of the dataBase

-- create museum table

CREATE TABLE `museumapp`.`museum` (
  `museumID` INT(11) UNSIGNED NOT NULL,
  `museumName` VARCHAR(45) NOT NULL,
  `introduction` TEXT NULL,
  `opentime` VARCHAR(45) NULL,
  `Link` TEXT NULL,
  `location` VARCHAR(45) NULL,
  `label` TEXT NULL,
  `museum_introduction` TEXT NULL,
  `grade` DOUBLE NULL,
  `annual_visits` INT(11) NULL,
  `area` DOUBLE NULL,
  `telephone` VARCHAR(45) NULL,
  `admission _fee` TEXT NULL,
  `open _time` TEXT NULL,
  `building_time` VARCHAR(45) NULL,
  `collection_number` INT(11) NULL,
  `city` TEXT NULL,
  `status` INT(11) NULL,
  PRIMARY KEY (`museumID`),
  UNIQUE INDEX `museumID_UNIQUE` (`museumID` ASC) VISIBLE)
COMMENT = '博物馆表';


-- create exhibition table


CREATE TABLE `museumapp`.`exihibition` (
  `exhibitionID` INT(10) UNSIGNED NOT NULL AUTO_INCREMENT,
  `museumID` INT(11) UNSIGNED NOT NULL,
  `exhibitionTime` VARCHAR(128) NULL,
  `exhibitionTheme` VARCHAR(128) NOT NULL,
  `exhibitionIntroduction` TEXT NULL,
  `exhibitionLocation` TEXT NULL,
  `exhibitionThingList` TEXT NULL,
  `exhibition _picture` TEXT NULL,
  `status` INT(11) UNSIGNED NOT NULL,
  PRIMARY KEY (`exhibitionID`),
  UNIQUE INDEX `exhibitionID_UNIQUE` (`exhibitionID` ASC) VISIBLE,
  UNIQUE INDEX `exhibitionTheme_UNIQUE` (`exhibitionTheme` ASC) VISIBLE)
COMMENT = '展览表';


-- create collect table

CREATE TABLE `museumapp`.`collection` (
  `CollectionID` INT(10) UNSIGNED NOT NULL AUTO_INCREMENT,
  `museumID` INT(11) UNSIGNED NOT NULL,
  `collectionName` VARCHAR(45) NOT NULL,
  `collectionIntroduction` TEXT NULL,
  `collection _age` VARCHAR(45) NULL,
  `collectionImage` VARCHAR(45) NULL,
  `status` INT(11) UNSIGNED NOT NULL,
  PRIMARY KEY (`CollectionID`),
  UNIQUE INDEX `CollectionID_UNIQUE` (`CollectionID` ASC) VISIBLE,
  UNIQUE INDEX `collectionName_UNIQUE` (`collectionName` ASC) VISIBLE)
COMMENT = '藏品表\n';
