CREATE TABLE IF NOT EXISTS qliq_qoil (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    company_name VARCHAR(255),
    'date' DATE,
    calc_type VARCHAR(255),
    qliq INTEGER,
    qoil INTEGER
    )