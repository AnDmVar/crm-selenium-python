CREATE DATABASE IF NOT EXISTS salesforce;
USE salesforce;

DROP TABLE IF EXISTS opportunity;
CREATE TABLE opportunity (id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(120) NOT NULL,
    account_name VARCHAR(500) NOT NULL,
    close_date DATE NOT NULL,
    type VARCHAR(20) NOT NULL DEFAULT "--None--",
    stage VARCHAR(20) NOT NULL,
    primary_campaign_source VARCHAR(80),
    probability INT(3) UNSIGNED,
    budget_confirmed BOOLEAN NOT NULL DEFAULT 0,
    amount DECIMAL(16,2) UNSIGNED DEFAULT NULL,
    discovery_completed BOOLEAN NOT NULL DEFAULT 0,
    roi_analysis_completed BOOLEAN NOT NULL DEFAULT 0,
    loss_reason VARCHAR(50) NOT NULL DEFAULT "--None--",
    nextstep VARCHAR(255),
    lead_source VARCHAR(50) NOT NULL DEFAULT "--None--",
    description TEXT(32000)) ENGINE=InnoDB;
ALTER TABLE opportunity AUTO_INCREMENT = 1000;

INSERT INTO opportunity (name, account_name, close_date, type, stage, primary_campaign_source,
    probability, budget_confirmed, amount, discovery_completed, roi_analysis_completed,
    loss_reason, nextstep, lead_source, description)
VALUES ('Acme - Product', 'Acme (Sample)', '2021-05-22', '--None--', 'Negotiation', NULL, 65, True, 35000, True,
    True, '--None--', NULL, 'Website', NULL),
    ('Global Media - Resources', 'Global Media (Sample)', '2020-03-15', 'New Business', 'Closed Lost', NULL, 50,
    True, 8000, True, True, 'Price', NULL, 'Advertisement', NULL),
    ('Salesforce - Services', 'salesforce.com (Sample)', '2021-07-11', 'Existing Business', 'Qualification', NULL,
    25, False, NULL, False, False, '--None--', NULL, 'Partner', NULL)