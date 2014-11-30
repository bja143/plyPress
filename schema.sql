create database plypress;
use plypress;

--create table user_master
--(
--    email_id varchar(40) not null primary key,
--    fullname Varchar(15) not null, 
--    password char(255) not null,
--    full_name varchar(100) not null
--); 


create table post_master
(
    post_id integer primary key, 
    post_title varchar(100) not null, 
    post_content text not null,
    posted_on datetime  not null
);

--create table comments(
--  post_id integer not null,
--  comment_id integer not null,
--  comment_content text not null,
--  email_id varchar(30) not null,
--  comment_author varchar(50) not null
--);

-- create table likes(
-- 	post_id integer not null, 
--     constraint user_master_post_fk foreign key(post_id) references post_master(post_id),
--     post_likes integer not null
-- );
