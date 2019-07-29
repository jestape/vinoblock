
DELIMITER $$

CREATE EVENT `migrate sensor_data` 
	ON SCHEDULE EVERY 1 DAY STARTS '2019-07-27 00:00:01'
	DO BEGIN
    
		INSERT INTO db.sensor_data_daily(_day, _sensor, temperature, humidity)
            SELECT DATE(_timestamp), _sensor, AVG(temperature), AVG(humidity) FROM sensor_data GROUP BY DAY(_timestamp), _sensor;
	    
        DELETE FROM db.sensor_data;


	END $$

DELIMITER ;