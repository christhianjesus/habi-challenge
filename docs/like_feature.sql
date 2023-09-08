DROP TABLE IF EXISTS like_history;
CREATE TABLE like_history (
  id int(11) NOT NULL,
  user_id int(11) NOT NULL,
  property_id int(11) NOT NULL,
  enabled bool NOT NULL DEFAULT TRUE,
  create_date datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  FOREIGN KEY (user_id) REFERENCES user(id),
  FOREIGN KEY (property_id) REFERENCES property(id)
);
