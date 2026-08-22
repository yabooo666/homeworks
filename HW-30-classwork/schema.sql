-- ==============================================================
-- 1. ცხრილის შექმნა (ჯერ არ ვავსებთ)
-- ==============================================================
DROP TABLE IF EXISTS products;

CREATE TABLE products (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR(100) NOT NULL,
    price DECIMAL(10, 2) NOT NULL,
    quantity INTEGER NOT NULL DEFAULT 0,
    status VARCHAR(50)
);

-- ==============================================================
-- 2. ტრიგერები (INSERT და UPDATE დროს ავტომატური სტატუსის მინიჭება)
-- ==============================================================

-- ტრიგერი INSERT-ის დროს
CREATE TRIGGER set_status_on_insert AFTER INSERT ON products
BEGIN
    UPDATE products
    SET status = CASE
        WHEN NEW.quantity <= 0 THEN 'out of stock'
        WHEN NEW.quantity BETWEEN 1 AND 10 THEN 'low stock'
        ELSE 'in stock'
    END
    WHERE id = NEW.id;
END;

-- ტრიგერი UPDATE-ის დროს (რაოდენობის ცვლილებისას)
CREATE TRIGGER set_status_on_update AFTER UPDATE OF quantity ON products
BEGIN
    UPDATE products
    SET status = CASE
        WHEN NEW.quantity <= 0 THEN 'out of stock'
        WHEN NEW.quantity BETWEEN 1 AND 10 THEN 'low stock'
        ELSE 'in stock'
    END
    WHERE id = NEW.id;
END;

-- ==============================================================
-- 3. PostgreSQL / MySQL სტილის პროცედურის სინტაქსი (საცნობაროდ):
-- ==============================================================
-- CREATE OR REPLACE PROCEDURE reduce_stock(p_product_id INT, p_quantity INT)
-- LANGUAGE plpgsql
-- AS $$
-- BEGIN
--     UPDATE products 
--     SET quantity = quantity - p_quantity 
--     WHERE id = p_product_id;
-- END;
-- $$;
