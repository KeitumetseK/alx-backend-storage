-- 101-average_weighted_score.sql
DELIMITER //

CREATE PROCEDURE ComputeAverageWeightedScoreForUsers()
BEGIN
    DECLARE done INT DEFAULT 0;
    DECLARE userId INT;
    DECLARE cur CURSOR FOR SELECT id FROM users;
    DECLARE CONTINUE HANDLER FOR NOT FOUND SET done = 1;

    OPEN cur;

    read_loop: LOOP
        FETCH cur INTO userId;
        IF done THEN
            LEAVE read_loop;
        END IF;
        
        -- Call the procedure to update the average score for the current user
        CALL ComputeAverageWeightedScoreForUser(userId);
    END LOOP;

    CLOSE cur;
END //

DELIMITER ;

