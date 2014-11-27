create database flypress;
use flypress;


create table user_master
(
    userid Varchar(5) Primary Key, 
    doctorname Varchar(15) Not Null, 
    password varchar(255) not null
); 

create table post_master
(
    post_id integer primary key, 
    post_title varchar(100) not null, 
    post_content text not null,
    timestamp varchar(50) not null
);

create table likes(
	post_id integer not null, 
    constraint user_master_post_fk foreign key(post_id) references post_master(post_id);
    post_likes integer not null
);