CREATE FUNCTION rls.fn_securitypredicate(@SalesRep AS VARCHAR(60)) 
    RETURNS TABLE  
WITH SCHEMABINDING  
AS  
    RETURN SELECT 1 AS fn_securitypredicate_result   
WHERE @SalesRep = USER_NAME();