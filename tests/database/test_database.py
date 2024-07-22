# all tests for database

import pytest


@pytest.mark.database
def test_database_connection(database_test):
    database_test.test_connection()

@pytest.mark.database
def test_check_all_users(database_test):
    users = database_test.get_all_users()
    print(users)

@pytest.mark.database
def test_check_user_sergii(database_test):
    user = database_test.get_user_address_by_name('Sergii')

    assert user[0][0] == 'Maydan Nezalezhnosti 1'
    assert user[0][1] == 'Kyiv'
    assert user[0][2] == '3127'
    assert user[0][3] == 'Ukraine'

@pytest.mark.database
def test_product_qnt_update(database_test):
    database_test.update_product_qnt_by_id(1,25)
    water_qnt = database_test.select_product_qnt_by_id(1)

    assert water_qnt[0][0] == 25

@pytest.mark.database
def test_product_insert(database_test):
    database_test.insert_product(4, 'печиво', 'солодке', 30)
    water_qnt = database_test.select_product_qnt_by_id(4)

    assert water_qnt[0][0] == 30

@pytest.mark.database
def test_product_delete(database_test):
    database_test.insert_product(99, 'тестові', 'дані', 999)
    database_test.delete_product_by_id(99)
    qnt = database_test.select_product_qnt_by_id(99)
    assert len(qnt) == 0 #array is empty

@pytest.mark.database
def test_detailed_orders(database_test):
    orders = database_test.get_detailed_orders()
    print("Замовлення", orders)
    assert len(orders) == 1


    assert orders[0][0] == 1
    assert orders[0][1] == 'Sergii'
    assert orders[0][2] == 'солодка вода'
    assert orders[0][3] == 'з цукром'

