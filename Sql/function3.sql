CREATE OR REPLACE FUNCTION get_user_is_admin(user_id INT)
RETURNS BOOLEAN AS $$
BEGIN
    RETURN (SELECT is_admin FROM Client WHERE id = user_id);
END;
$$ LANGUAGE plpgsql;
