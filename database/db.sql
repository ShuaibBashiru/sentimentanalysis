CREATE TABLE contents(
id int not null AUTO_INCREMENT,
    category_id int not null DEFAULT 0,
    title varchar(50) null DEFAULT '',
    faults text not null,
    solution_one text not null,
    solution_two text null,
    solution_three text null,
    image_name text null,
    uniqueCode varchar(50) not null,
    status_id INT NOT NULL DEFAULT 0,
    record_status INT NOT NULL DEFAULT 1,
    visibility INT NOT NULL DEFAULT 0,
    created_by int not null,
    modified_by int not null,
    date_created date not null,
    time_created time not null,
    date_modified date not null,
    time_modified time not null,
    PRIMARY KEY(id)
);

CREATE TABLE contents_category(
id int not null AUTO_INCREMENT,
    category_name varchar(80) null DEFAULT '',
    description text null,
    image_name text null,
    uniqueCode varchar(50) not null,
    status_id INT NOT NULL DEFAULT 0,
    record_status INT NOT NULL DEFAULT 1,
    visibility INT NOT NULL DEFAULT 0,
    created_by int not null,
    modified_by int not null,
    date_created date not null,
    time_created time not null,
    date_modified date not null,
    time_modified time not null,
    PRIMARY KEY(id)
);

CREATE TABLE items_category(
id int not null AUTO_INCREMENT,
    category_name varchar(80) null DEFAULT '',
    description text null,
    image_name text null,
    uniqueCode varchar(50) not null,
    status_id INT NOT NULL DEFAULT 0,
    record_status INT NOT NULL DEFAULT 1,
    visibility INT NOT NULL DEFAULT 0,
    created_by int not null,
    modified_by int not null,
    date_created date not null,
    time_created time not null,
    date_modified date not null,
    time_modified time not null,
    PRIMARY KEY(id)
);

CREATE TABLE items(
id int not null AUTO_INCREMENT,
    category_id int not null DEFAULT 0,
    title text null,
    slogan text null,
    header text null,
    contents text null,
    image_name text null,
    uniqueCode varchar(50) not null,
    status_id INT NOT NULL DEFAULT 0,
    record_status INT NOT NULL DEFAULT 1,
    visibility INT NOT NULL DEFAULT 0,
    created_by int not null,
    modified_by int not null,
    date_created date not null,
    time_created time not null,
    date_modified date not null,
    time_modified time not null,
    PRIMARY KEY(id)
);


CREATE TABLE feedback(
id int not null AUTO_INCREMENT,
    category_id int not null DEFAULT 0,
    username varchar(100) not null,
    title varchar(50) null DEFAULT '',
    comments text not null,
    uniqueCode varchar(50) not null,
    status_id INT NOT NULL DEFAULT 0,
    record_status INT NOT NULL DEFAULT 1,
    visibility INT NOT NULL DEFAULT 0,
    created_by int not null,
    modified_by int not null,
    year_date varchar(20) null DEFAULT '0',
    month_date varchar(20) null DEFAULT '0',
    day_date varchar(20) null DEFAULT '0',
    date_created date not null,
    time_created time not null,
    date_modified date not null,
    time_modified time not null,
    PRIMARY KEY(id)
);