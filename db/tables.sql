CREATE TABLE sensor_data(

    _timestamp DATETIME,
    _sensor CHAR(16),
    temperature FLOAT(4,2),
    humidity FLOAT(4,2),

    CONSTRAINT sensor_data_PK 
        PRIMARY KEY (_timestamp, _sensor)

);

CREATE TABLE sensor_data_daily(
    _day DATE,
    _sensor CHAR(16),
    temperature FLOAT(4,2),
    humidity FLOAT(4,2),

    CONSTRAINT sensor_data_PK 
        PRIMARY KEY (_day, _sensor)

);