CREATE TABLE IF NOT EXISTS dim_products (
    sku VARCHAR(50) PRIMARY KEY,
    product_type VARCHAR(100),
    price DECIMAL(10, 4)

);

    DELETE FROM dim_products;

    INSERT INTO dim_products (sku, product_type, price)
    SELECT DISTINCT
    sku,
    product_type,
    price

    FROM supply_chain_data;

CREATE TABLE IF NOT EXISTS dim_logistics (
    logistic_key INTEGER PRIMARY KEY AUTOINCREMENT,
    transportation_modes VARCHAR(50),
    shipping_carriers VARCHAR(100),
    supplier_name VARCHAR(100),
    routes VARCHAR(100),
    location VARCHAR(100)
);

    DELETE FROM dim_logistics;

    INSERT INTO dim_logistics (transportation_modes, shipping_carriers, supplier_name, routes, location)
    SELECT DISTINCT
    transportation_modes,
    shipping_carriers,
    supplier_name,
    routes,
    location

    FROM supply_chain_data;

CREATE TABLE IF NOT EXISTS fact_shipments (
    shipment_id INTEGER PRIMARY KEY AUTOINCREMENT,
    sku VARCHAR(50),
    logistic_key INTEGER,
    availability INTEGER,
    number_of_products_sold INTEGER,
    revenue_generated DECIMAL(10, 4),
    stock_levels INTEGER,
    total_lead_time INTEGER,
    gross_margin_rate DECIMAL(5, 4),
    costs DECIMAL(10, 4),
    defect_rates DECIMAL(5, 4),
    FOREIGN KEY (sku) REFERENCES dim_products(sku),
    FOREIGN KEY (logistic_key) REFERENCES dim_logistics(logistic_key)
);

    DELETE FROM fact_shipments;

    INSERT INTO fact_shipments (sku, logistic_key, availability, number_of_products_sold, revenue_generated, stock_levels, total_lead_time, gross_margin_rate, costs, defect_rates)
    SELECT
    c.sku,
    d.logistic_key,
    c.availability,
    c.number_of_products_sold,
    c.revenue_generated,
    c.stock_levels,
    c.total_lead_time,       
    c.gross_margin_rate,    
    c.costs,               
    c.defect_rates
    FROM supply_chain_data c
    JOIN dim_logistics d ON
    c.shipping_carriers = d.shipping_carriers AND
    c.transportation_modes = d.transportation_modes AND
    c.routes = d.routes AND
    c.location = d.location AND
    c.supplier_name = d.supplier_name;
    