# pylint:disable=C0111,C0103, line-too-long

def detailed_orders(db):
    '''return a list of all orders (order_id, customer.contact_name,
    employee.firstname) ordered by order_id'''
    query="""
    SELECT o.OrderID, c.ContactName , e.FirstName
    FROM Orders o
    INNER JOIN
	    Customers c ON c.CustomerID = o.CustomerID
    INNER JOIN
	    Employees e ON e.EmployeeID = o.EmployeeID
    ORDER BY o.OrderID
    """
    db.execute(query)
    c=db.fetchall()
    return c

def spent_per_customer(db):
    '''return the total amount spent per customer ordered by ascending total
    amount (to 2 decimal places)
    Exemple :
        Jean   |   100
        Marc   |   110
        Simon  |   432
        ...
    '''
    query="""
    SELECT c.ContactName,sum(od.UnitPrice * od.Quantity) AS TOTAL
    FROM
        OrderDetails od
    INNER JOIN
        Orders o ON o.OrderID = od.OrderID
    INNER JOIN Customers c ON c.CustomerID = o.CustomerID
    GROUP BY o.CustomerID
    ORDER BY TOTAL
    """
    db.execute(query)
    c=db.fetchall()
    return c
def best_employee(db):
    '''Implement the best_employee method to determine who’s the best employee! By “best employee”, we mean the one who sells the most.
    We expect the function to return a tuple like: ('FirstName', 'LastName', 6000 (the sum of all purchase)). The order of the information is irrelevant'''
    query="""
    SELECT e.FirstName ,e.LastName ,sum(od.UnitPrice * od.Quantity) AS TOTAL
    FROM
        OrderDetails od
    INNER JOIN
        Orders o ON o.OrderID = od.OrderID
    INNER JOIN Employees e ON e.EmployeeID = o.EmployeeID
    GROUP BY o.EmployeeID
    ORDER BY TOTAL DESC
    """
    db.execute(query)
    c=db.fetchone()
    return c

def orders_per_customer(db):
    '''Return a list of tuples where each tuple contains the contactName
    of the customer and the number of orders they made (contactName,
    number_of_orders). Order the list by ascending number of orders'''
    query="""
    SELECT c.ContactName , COUNT(o.OrderID) AS TOTAL
    FROM Customers c
    LEFT JOIN Orders o  ON c.CustomerID = o.CustomerID
    GROUP BY o.CustomerID
    ORDER BY TOTAL
    """
    db.execute(query)
    c=db.fetchall()
    return c
