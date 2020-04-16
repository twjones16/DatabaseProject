drop database if exists finalproject_tim_jack;
create database congress_db;

\c finalproject_tim_jack

drop table if exists state cascade;
create table state (
  name varchar not null,
  date_established varchar not null,
  primary key (name)
);

drop table if exists party cascade;
create table party (
    name varchar not null,
    date_established varchar not null,
    primary key (name)
);

drop table if exists chamber cascade;
create table chamber (
    name varchar not null,
    primary key (name)
);

drop table if exists district cascade;
create table district (
    name varchar not null,
    chamber varchar not null,
    state varchar not null,
    primary key (name),
    foreign key (chamber) references chamber(name),
    foreign key (state) references state(name)
);

drop table if exists payroll cascade;
create table payroll (
    congress_number integer not null,
    senate integer,
    house integer,
    speaker integer,
    puerto_rico integer,
    senate_majority_leader integer,
    senate_minority_leader integer,
    house_majority_leader integer,
    house_minority_leader integer,
    vice_president integer,
    primary key (congress_number)
);

drop table if exists representative cascade;
create table representative (
  district varchar not null,
  congress_number integer not null,
  first varchar not null,
  last varchar not null,
  prior_occupation varchar,
  party varchar not null,
  age integer,
  primary key (district, congress_number),
  foreign key (party) references party(name),
  foreign key (district) references district(name),
  foreign key (congress_number) references payroll(congress_number)
);

drop table if exists chamber_leader cascade;
create table chamber_leader (
    district varchar not null,
    congress_number integer not null,
    title varchar not null,
    primary key (district, congress_number),
    foreign key (district, congress_number) references representative(district, congress_number)
);

drop table if exists election cascade;
create table election (
  district varchar not null,
  congress_number integer not null,
  votes_for integer not null,
  total_votes integer not null,
  primary key (district, congress_number),
  foreign key (district, congress_number) references representative(district, congress_number)
);

drop table if exists committee cascade;
create table committee (
  name varchar not null,
  date_established varchar,
  primary key (name)
);

drop table if exists membership cascade;
create table membership (
  district varchar not null,
  congress_number integer not null,
  committee varchar not null,
  primary key (district, congress_number, committee),
  foreign key (district, congress_number) references representative(district, congress_number),
  foreign key (committee) references committee(name)
);

drop table if exists bill cascade;
create table bill (
  bill_number varchar not null,
  congress_number int not null,
  name varchar not null,
  date integer not null,
  primary key (bill_number, congress_number),
  foreign key (congress_number) references payroll(congress_number)
);

drop table if exists vote cascade;
create table vote (
    district varchar not null,
    congress_number integer not null,
    bill_number varchar not null,
    vote varchar not null,
    primary key (district, congress_number, bill_number),
    foreign key (district, congress_number) references representative(district, congress_number),
    foreign key (bill_number, congress_number) references bill(bill_number, congress_number)
);

drop table if exists party_leader cascade;
create table party_leader(
    district varchar not null,
    congress_number integer null,
    role varchar not null,
    primary key (district, congress_number),
    foreign key (district, congress_number) references representative(district, congress_number)
);

grant all privileges on all tables in schema public to twjone16;
