USE mysql;

DROP DATABASE IF EXISTS JKStatusSystem;

CREATE DATABASE JKStatusSystem;

USE JKStatusSystem;

    
CREATE TABLE `Role`
(
    `id`   INT UNSIGNED NOT NULL PRIMARY KEY,
    `name` VARCHAR(100) NOT NULL
);

CREATE TABLE `User`
(
    `id`            BIGINT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `first_name`    VARCHAR(100),
    `last_name`     VARCHAR(100),
    `status`        INT UNSIGNED NOT NULL DEFAULT 1 CHECK (status IN (1, 2)),
    `email`         VARCHAR(256) NOT NULL UNIQUE,
    `password`      VARCHAR(512),
    `password_salt` VARCHAR(32),
    `role_id`       INT UNSIGNED NOT NULL,

    FOREIGN KEY (role_id) REFERENCES Role (id)
);

CREATE TABLE `Permission`
(
    `id`   BIGINT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `name` VARCHAR(100) NOT NULL
);

CREATE TABLE `PermissionToRole`
(
    `id`            BIGINT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `permission_id` BIGINT UNSIGNED NOT NULL,
    `role_id`       INT UNSIGNED NOT NULL,

    FOREIGN KEY (permission_id) REFERENCES Permission (id),
    FOREIGN KEY (role_id) REFERENCES Role (id)
);

CREATE TABLE `UserSession`
(
    `id`              BIGINT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `user_id`         BIGINT UNSIGNED NOT NULL,
    `token`           VARCHAR(300) UNIQUE NOT NULL,
    `token_hindrance` VARCHAR(32)         NOT NULL,
    `date_start`      DATETIME            NOT NULL,
    `date_end`        DATETIME            NOT NULL,
    `ip`              VARCHAR(39)         NOT NULL,

    FOREIGN KEY (user_id) REFERENCES User (id)
);


-- Insert Required data
INSERT INTO Role (id, name) VALUES
(1 ,'Super Admin'),
(2 ,'Admin'),
(3 ,'Operator'),
(4 ,'Watcher');

-- END Insert Required data


-- Insert Permissions

-- END Insert Permissions









-- Insert Dev Data
INSERT INTO User (first_name, last_name, status, email, password, password_salt, role_id) VALUES
('Julian', 'Korgol', 1, 'julian.korgol@core2goal.com', 'daef4953b9783365cad6615223720506cc46c5167cd16ab500fa597aa08ff964eb24fb19687f34d7665f778fcb6c5358fc0a5b81e1662cf90f73a2671c53f991', 'fukaqMxwvjpSj9WkH4WFu4YAvRNjThuv', 1),
('Jan', 'Kowalski', 1, 'example@example.com', 'daef4953b9783365cad6615223720506cc46c5167cd16ab500fa597aa08ff964eb24fb19687f34d7665f778fcb6c5358fc0a5b81e1662cf90f73a2671c53f991', 'N7VYjzzPsXXdujxMWRJjZ5LrUFoVYoZC', 4),
('Anna', 'Kowalska', 2, 'notactive@example.com', 'daef4953b9783365cad6615223720506cc46c5167cd16ab500fa597aa08ff964eb24fb19687f34d7665f778fcb6c5358fc0a5b81e1662cf90f73a2671c53f991', 'n3UPoTnEYYCXpPvoy2fo4rED55tQALJX', 2);
-- END Insert Dev Data
