from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from sqlalchemy import select
from sqlalchemy import exc
import json
from dotenv import load_dotenv
import os
load_dotenv()
app = Flask(__name__)
CORS(app, supports_credentials=True)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('SQLALCHEMY_DATABASE_URI')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = os.environ.get('SQLALCHEMY_TRACK_MODIFICATIONS')
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')
db = SQLAlchemy(app)

class Store(db.Model):
    sto_id = db.Column(db.Integer, primary_key=True)
    sto_location = db.Column(db.String(64))
    sto_phone = db.Column(db.String(64))
    sto_hours = db.Column(db.Integer)
    m_id = db.Column(db.Integer, db.ForeignKey('staff.sta_id', ondelete='CASCADE'), nullable=True)
    def __init__(self, sto_id, sto_location, sto_phone, sto_hours, m_id):
        self.sto_id = sto_id
        self.sto_location = sto_location
        self.sto_phone = sto_phone
        self.sto_hours = sto_hours
        self.m_id = m_id

class Staff(db.Model):
    sta_id = db.Column(db.Integer, primary_key=True)
    sta_name =  db.Column(db.String(64))
    sta_email = db.Column(db.String(128))
    sta_job_title = db.Column(db.String(64))
    sto_id = db.Column(db.Integer, db.ForeignKey('store.sto_id', ondelete='CASCADE'), nullable=False)
    def __init__(self, sta_id, sta_name, sta_email, sta_job_title, sto_id):
        self.sta_id = sta_id
        self.sta_name = sta_name
        self.sta_email = sta_email
        self.sta_job_title = sta_job_title
        self.sto_id = sto_id

class Customer(db.Model):
    c_id = db.Column(db.Integer, primary_key=True)
    c_name = db.Column(db.String(64))
    c_email = db.Column(db.String(128))
    c_birthday = db.Column(db.Date)
    c_payment_info = db.Column(db.String(64))
    def __init__(self, c_id, c_name, c_email, c_birthday, c_payment_info):
        self.c_id = c_id
        self.c_name = c_name
        self.c_email = c_email
        self.c_birthday = c_birthday
        self.c_payment_info = c_payment_info

class Furniture(db.Model):
    f_id = db.Column(db.Integer, primary_key=True)
    f_name =  db.Column(db.String(64))
    f_type = db.Column(db.String(64))
    f_color = db.Column(db.String(64))
    f_manufacturer = db.Column(db.String(64))
    f_cost = db.Column(db.Float)
    def __init__(self, f_id, f_name, f_type, f_color, f_manufacturer, f_cost):
        self.f_id = f_id
        self.f_name = f_name
        self.f_type = f_type
        self.f_color = f_color
        self.f_manufacturer = f_manufacturer
        self.f_cost = f_cost

class Order(db.Model):
    o_id = db.Column(db.Integer, primary_key=True)
    c_id = db.Column(db.Integer, db.ForeignKey('customer.c_id', ondelete='CASCADE'), nullable=False)
    o_date = db.Column(db.Date)
    sto_id = db.Column(db.Integer, db.ForeignKey('store.sto_id', ondelete='CASCADE'), nullable=False)
    def __init__(self, o_id, c_id, o_date, sto_id):
        self.o_id = o_id
        self.c_id = c_id
        self.o_date = o_date
        self.sto_id = sto_id

class OrderFurniture(db.Model):
    o_id = db.Column(db.Integer, db.ForeignKey('order.o_id', ondelete='CASCADE'), nullable=False, primary_key=True)
    f_id = db.Column(db.Integer, db.ForeignKey('furniture.f_id', ondelete='CASCADE'), nullable=False, primary_key=True)
    of_quantity = db.Column(db.Integer)
    of_cost = db.Column(db.Float)
    def __init__(self, o_id, f_id, of_quantity, of_cost):
        self.o_id = o_id
        self.f_id = f_id
        self.of_quantity = of_quantity
        self.of_cost = of_cost
    
 
class StoreInventory(db.Model):
    sto_id = db.Column(db.Integer, db.ForeignKey('store.sto_id', ondelete='CASCADE'), nullable=False, primary_key=True)
    f_id = db.Column(db.Integer, db.ForeignKey('furniture.f_id', ondelete='CASCADE'), nullable=False, primary_key=True)
    si_quantity = db.Column(db.Integer)
    si_sell_price = db.Column(db.Float)
    def __init__(self, sto_id, f_id, si_quantity, si_sell_price):
        self.sto_id = sto_id
        self.f_id = f_id
        self.si_quantity = si_quantity
        self.si_sell_price = si_sell_price

#GETTERS : Currently these function only return everything in the table
def getStore():
    query = select(Store)
    result = db.session.execute(query)

    store_list = []
    for store in result.scalars():
        store_list.append((store.sto_id, store.sto_location, store.sto_phone, store.sto_hours, store.m_id))
    return store_list


def getStaffbyID(id):
    query = select(Staff).where(Staff.sta_id == id)
    result = db.session.execute(query)

    json_output = json.dumps(result)
    
    return json_output


def getStaff():
    query = select(Staff)
    result = db.session.execute(query)

    staff_list = []
    for staff in result.scalars():
        staff_list.append((staff.sta_id, staff.sta_name, staff.sta_email, staff.sta_job_title, staff.sto_id))
    return staff_list

def getCustomer():
    query = select(Customer)
    result = db.session.execute(query)

    customer_list = []
    for customer in result.scalars():
        customer_list.append((customer.c_id, customer.c_name, customer.c_email, customer.c_birthday, customer.c_payment_info))
    return customer_list

def getFurniture():
    query = select(Furniture)
    result = db.session.execute(query)

    furniture_list = []
    for furniture in result.scalars():
        furniture_list.append((furniture.f_id, furniture.f_name, furniture.f_type, furniture.f_color, furniture.f_manufacturer, furniture.f_cost))
    return furniture_list

def getOrder():
    query = select(Order)
    result = db.session.execute(query)

    order_list = []
    for order in result.scalars():
        order_list.append((order.o_id, order.c_id, order.o_date, order.sto_id))
    return order_list

def getOrderFurniture():
    query = select(OrderFurniture)
    result = db.session.execute(query)

    OrderFurniture_list = []
    for OrderFurniture in result.scalars():
        OrderFurniture_list.append((OrderFurniture.o_id, OrderFurniture.f_id, OrderFurniture.of_quantity, OrderFurniture.of_cost))
    return OrderFurniture_list

def getStoreInventory():
    query = select(StoreInventory)
    result = db.session.execute(query)

    StoreInventory_list = []
    for StoreInventory in result.scalars():
        StoreInventory_list.append((StoreInventory.sto_id, StoreInventory.f_id, StoreInventory.si_quantity, StoreInventory.si_sell_price))
    return StoreInventory_list


##### CREATE 

@app.route("/createStore", methods=['POST'])
def createStore():

    sto_id = request.form.get("sto_id")
    sto_location = request.form.get("sto_location")
    sto_phone = request.form.get("sto_phone")
    sto_hours = request.form.get("sto_hours")
    m_id = request.form.get("m_id")

    required_attributes = [sto_id,sto_location,sto_phone,sto_hours]
    for attribute in required_attributes:
        if attribute == None:
            return json.dumps("1 or more required attributes were left empty")
    try:
        entry = Store(sto_id=sto_id, sto_location=sto_location, sto_phone=sto_phone, sto_hours=sto_hours, m_id=m_id)
        db.session.add(entry)
        db.session.commit()
    except exc.IntegrityError as err:
        db.session.rollback()
        json_return = json.dumps("The store with id, " + sto_id + ", already exists")
        return json_return
    except Exception as err:
        db.session.rollback()
        json_return = json.dumps("Database error: " + err)
        return json_return
            
    json_return = json.dumps("Successfully added store:" + sto_id)
    return json_return

@app.route("/createStaff", methods=['POST'])
def createStaff():
    sta_id = request.form.get("sta_id")
    sta_name = request.form.get("sta_name")
    sta_email = request.form.get("sta_email")
    sta_job_title = request.form.get("sta_job_title")
    sto_id = request.form.get("sto_id")
    required_attributes = [sto_id,sta_name,sta_email,sta_job_title, sto_id]
    for attribute in required_attributes:
        if attribute == None:
            return json.dumps("1 or more required attributes were left empty")
    try:
        entry = Staff(sta_id=sta_id, sta_name=sta_name, sta_email=sta_email, sta_job_title=sta_job_title, sto_id=sto_id)
        db.session.add(entry)
        db.session.commit()
    except exc.IntegrityError as err:
        db.session.rollback()
        json_return = json.dumps("The staff with id, " + sta_id + ", already exists")
        return json_return
    except Exception as err:
        db.session.rollback()
        json_return = json.dumps("Database error: " + err)
        return json_return
            
    json_return = json.dumps("Successfully added staff: " + sta_id)
    return json_return

@app.route("/createCustomer", methods=['POST'])
def createCustomer():

    c_id = request.form.get("c_id")
    c_name = request.form.get("c_name")
    c_email = request.form.get("c_email")
    c_birthday = request.form.get("c_birthday")
    c_payment_info = request.form.get("c_payment_info")
    required_attributes = [c_id,c_name,c_email,c_birthday, c_payment_info]
    for attribute in required_attributes:
        if attribute == None:
            return json.dumps("1 or more required attributes were left empty")
    try:
        entry = Customer(c_id=c_id, c_name=c_name, c_email=c_email, c_birthday=c_birthday, c_payment_info=c_payment_info)
        db.session.add(entry)
        db.session.commit()
    except exc.IntegrityError as err:
        db.session.rollback()
        json_return = json.dumps("The customer with id, " + c_id + ", already exists")
        return json_return
    except Exception as err:
        db.session.rollback()
        json_return = json.dumps("Database error: " + err)
        return json_return
            
    json_return = json.dumps("Successfully added customer: " + c_id)
    return json_return

@app.route("/createFurniture", methods=['POST'])
def createFurniture():

    f_id = request.form.get("f_id")
    f_name = request.form.get("f_name")
    f_type = request.form.get("f_type")
    f_color = request.form.get("f_color")
    f_manufacturer = request.form.get("f_manufacturer")
    f_cost = request.form.get("f_cost")
    required_attributes = [f_id,f_name,f_type,f_color,f_manufacturer,f_cost]
    for attribute in required_attributes:
        if attribute == None:
            return json.dumps("1 or more required attributes were left empty")
    try:
        entry = Furniture(f_id=f_id, f_name=f_name, f_type=f_type, f_color=f_color, f_manufacturer=f_manufacturer, f_cost=f_cost)
        db.session.add(entry)
        db.session.commit()
    except exc.IntegrityError as err:
        db.session.rollback()
        json_return = json.dumps("The furniture with id, " + f_id + ", already exists")
        return json_return
    except Exception as err:
        db.session.rollback()
        json_return = json.dumps("Database error: " + err)
        return json_return
            
    json_return = json.dumps("Successfully added furniture: " + f_id)
    return json_return


@app.route("/createOrder", methods=['POST'])
def createOrder():

    o_id = request.form.get("o_id")
    c_id = request.form.get("c_id")
    o_date = request.form.get("o_date")
    sto_id = request.form.get("sto_id")
    required_attributes = [o_id,c_id,o_date,sto_id]
    for attribute in required_attributes:
        if attribute == None:
            return json.dumps("1 or more required attributes were left empty")
    try:
        entry = Order(o_id=o_id, c_id=c_id, o_date=o_date, sto_id=sto_id)
        db.session.add(entry)
        db.session.commit()
    except exc.IntegrityError as err:
        db.session.rollback()
        json_return = json.dumps("The order with id, " + o_id + ", already exists")
        return json_return
    except Exception as err:
        db.session.rollback()
        json_return = json.dumps("Database error: " + err)
        return json_return
            
    json_return = json.dumps("Successfully added order: " + o_id)
    return json_return

@app.route("/createOrderFurniture", methods=['POST'])
def createOrderFurniture():
    #TO DO
    o_id = request.form.get("o_id")
    f_id = request.form.get("f_id")
    of_quantity = request.form.get("of_quantity")
    of_cost = request.form.get("of_cost")
    required_attributes = [o_id,f_id,of_quantity,of_cost]
    for attribute in required_attributes:
        if attribute == None:
            return json.dumps("1 or more required attributes were left empty")
    try:
        entry = OrderFurniture(o_id=o_id, f_id=f_id, of_quantity=of_quantity, of_cost=of_cost)
        db.session.add(entry)
        db.session.commit()
    except exc.IntegrityError as err:
        db.session.rollback()
        json_return = json.dumps("The order with id, " + o_id + "," + f_id + " already exists")
        return json_return
    except Exception as err:
        db.session.rollback()
        json_return = json.dumps("Database error: " + err)
        return json_return
            
    json_return = json.dumps("Successfully added order: " + o_id + ", " + f_id)
    return json_return

@app.route("/createStoreInventory", methods=['POST'])
def createStoreInventory():

    sto_id = request.form.get("sto_id")
    f_id = request.form.get("f_id")
    si_quantity = request.form.get("si_quantity")
    si_sell_price = request.form.get("si_sell_price")
    required_attributes = [sto_id,f_id,si_quantity,si_sell_price]
    for attribute in required_attributes:
        if attribute == None:
            return json.dumps("1 or more required attributes were left empty")
    try:
        entry = StoreInventory(sto_id=sto_id, f_id=f_id, si_quantity=si_quantity, si_sell_price=si_sell_price)
        db.session.add(entry)
        db.session.commit()
    except exc.IntegrityError as err:
        db.session.rollback()
        json_return = json.dumps("The StoreInventory with id, " + sto_id + "," + f_id + " already exists")
        return json_return
    except Exception as err:
        db.session.rollback()
        json_return = json.dumps("Database error: " + err)
        return json_return
            
    json_return = json.dumps("Successfully added StoreInventory: " + sto_id + ", " + f_id)
    return json_return


##### READ : Currently read just calls the function to get everything in the table
#Eventually it will need to query

@app.route("/getStore", methods=['POST'])
def getStores():
    #TO DO
    return json.dumps(getStore())

@app.route("/getStaff", methods=['POST'])
def getStaffs():
    #TO DO
    return json.dumps(getStaff())

@app.route("/getCustomer", methods=['POST'])
def getCustomers():
    #TO DO
    return json.dumps(getCustomer())

@app.route("/readStaffbyID", methods=['POST'])
def readStaff():
    #sta_id = request.form.get("sta_id")
    #json_staff = getStaffbyID(sta_id)
    return 'Staff'

@app.route("/getFurniture", methods=['POST'])
def getFurnitures():
    #TO DO
    return json.dumps(getFurniture())

@app.route("/getOrder", methods=['POST'])
def getOrders():
    #TO DO
    return json.dumps(getOrder())

@app.route("/getOrderFurniture", methods=['POST'])
def getOrderFurnitures():
    #TO DO
    return json.dumps(getOrderFurniture())

@app.route("/getStoreInventory", methods=['POST'])
def getStoreInventorys():
    #TO DO
    return json.dumps(getStoreInventory())


##### UPDATE 

@app.route("/updateStore", methods=['POST'])
def updateStore():

    sto_id = request.form.get("sto_id")
    sto_location = request.form.get("sto_location")
    sto_phone = request.form.get("sto_phone")
    sto_hours = request.form.get("sto_hours")
    m_id = request.form.get("m_id")
    if sto_id == None:
        return json.dumps("Store ID required for update")
    try:
        obj = db.session.query(Store).filter(
            Store.sto_id==sto_id).first()
        
        if obj == None:
            return json.dumps("Store " + sto_id + " not found")

        if sto_location != None:
            obj.sto_location = sto_location
        if sto_phone != None:
            obj.sto_phone = sto_phone
        if sto_hours != None:
            obj.sto_hours = sto_hours
        if m_id != None:
            obj.m_id = m_id
        
        db.session.commit()
    except Exception as err:
        db.session.rollback()
        return json.dumps("Database error: " + err)
    return json.dumps("Store id," + sto_id + ", successfully updated")

@app.route("/updateStaff", methods=['POST'])
def updateStaff():

    sta_id = request.form.get("sto_id")
    sta_name = request.form.get("sta_name")
    sta_email = request.form.get("sta_email")
    sta_job_title = request.form.get("sta_job_title")
    sto_id = request.form.get("sto_id")
    if sta_id == None:
        return json.dumps("Staff ID required for update")
    try:
        obj = db.session.query(Staff).filter(
            Staff.sta_id==sta_id).first()
        
        if obj == None:
            return json.dumps("Staff " + sta_id + " not found")

        if sta_name != None:
            obj.sta_name = sta_name
        if sta_email != None:
            obj.sta_email = sta_email
        if sta_job_title != None:
            obj.sta_job_title = sta_job_title
        if sto_id != None:
            obj.sto_id = sto_id
        
        db.session.commit()
    except Exception as err:
        db.session.rollback()
        return json.dumps("Database error: " + err)
    return json.dumps("Staff id," + sta_id + ", successfully updated")

@app.route("/updateCustomer", methods=['POST'])
def updateCustomer():

    c_id = request.form.get("c_id")
    c_name = request.form.get("c_name")
    c_email = request.form.get("c_email")
    c_birthday = request.form.get("c_birthday")
    c_payment_info = request.form.get("c_payment_info")
    if c_id == None:
        return json.dumps("Customer ID required for update")
    try:
        obj = db.session.query(Customer).filter(
            Customer.c_id==c_id).first()
        
        if obj == None:
            return json.dumps("Customer " + c_id + " not found")

        if c_name != None:
            obj.c_name = c_name
        if c_email != None:
            obj.c_email = c_email
        if c_birthday != None:
            obj.c_birthday = c_birthday
        if c_payment_info != None:
            obj.sto_id = c_payment_info
        
        db.session.commit()
    except Exception as err:
        db.session.rollback()
        return json.dumps("Database error: " + err)
    return json.dumps("Customer id," + c_id + ", successfully updated")

@app.route("/updateFurniture", methods=['POST'])
def updateFurniture():

    f_id = request.form.get("f_id")
    f_name = request.form.get("f_name")
    f_type = request.form.get("f_type")
    f_color = request.form.get("f_color")
    f_manufacturer = request.form.get("f_manufacturer")
    f_cost = request.form.get("f_cost")
    if f_id == None:
        return json.dumps("Furniture ID required for update")
    try:
        obj = db.session.query(Furniture).filter(
            Furniture.f_id==f_id).first()
        
        if obj == None:
            return json.dumps("Furniture " + f_id + " not found")

        if f_name != None:
            obj.f_name = f_name
        if f_type != None:
            obj.f_type = f_type
        if f_color != None:
            obj.f_color = f_color
        if f_manufacturer != None:
            obj.sto_id = f_manufacturer
        if f_cost != None:
            obj.f_cost = f_cost
        
        db.session.commit()
    except Exception as err:
        db.session.rollback()
        return json.dumps("Database error: " + err)
    return json.dumps("Furniture id," + f_id + ", successfully updated")

@app.route("/updateOrder", methods=['POST'])
def updateOrder():

    o_id = request.form.get("o_id")
    c_id = request.form.get("c_id")
    o_date = request.form.get("o_date")
    sto_id = request.form.get("sto_id")
    if o_id == None:
        return json.dumps("Order ID required for update")
    try:
        obj = db.session.query(Order).filter(
            Order.o_id==o_id).first()
        
        if obj == None:
            return json.dumps("Order " + o_id + " not found")

        if c_id != None:
            obj.c_id = c_id
        if o_date != None:
            obj.o_date = o_date
        if sto_id != None:
            obj.sto_id = sto_id
        
        db.session.commit()
    except Exception as err:
        db.session.rollback()
        return json.dumps("Database error: " + err)
    return json.dumps("Order id," + o_id + ", successfully updated")

@app.route("/updateOrderFurniture", methods=['POST'])
def updateOrderFurniture():

    o_id = request.form.get("o_id")
    f_id = request.form.get("f_id")
    of_quantity = request.form.get("of_quantity")
    of_cost = request.form.get("of_cost")
    if o_id == None:
        return json.dumps("Order ID required for update")
    if f_id == None:
        return json.dumps("Furniture ID required for update")
    try:
        obj = db.session.query(OrderFurniture).filter(
            OrderFurniture.o_id==o_id, Order.f_id==f_id).first()
        
        if obj == None:
            return json.dumps("OrderFurniture " + o_id + ", " + f_id + " not found")

        if of_quantity != None:
            obj.of_quantity = of_quantity
        if of_cost != None:
            obj.of_cost = of_cost
        
        db.session.commit()
    except Exception as err:
        db.session.rollback()
        return json.dumps("Database error: " + err)
    return json.dumps("OrderFurniture id," + o_id + ", " + f_id + " successfully updated")

@app.route("/updateStoreInventory", methods=['POST'])
def updateStoreInventory():

    sto_id = request.form.get("sto_id")
    f_id = request.form.get("f_id")
    si_quantity = request.form.get("si_quantity")
    si_sell_price = request.form.get("si_sell_price")
    if sto_id == None:
        return json.dumps("Store ID required for update")
    if f_id == None:
        return json.dumps("Furniture ID required for update")
    try:
        obj = db.session.query(StoreInventory).filter(
            StoreInventory.sto_id==sto_id, StoreInventory.f_id==f_id).first()
        
        if obj == None:
            return json.dumps("StoreInventory " + sto_id + ", " + f_id + " not found")

        if si_quantity != None:
            obj.si_quantity = si_quantity
        if si_sell_price != None:
            obj.si_sell_price = si_sell_price
        
        db.session.commit()
    except Exception as err:
        db.session.rollback()
        return json.dumps("Database error: " + err)
    return json.dumps("StoreInventory id," + sto_id + ", " + f_id + ", successfully updated")

#### DELETE

@app.route("/deleteStore", methods=['POST'])
def deleteStore():
    sto_id = request.form.get('sto_id')
    if sto_id == None:
        return json.dumps("Need store ID to delete store")

    try:
        obj = db.session.query(Store).filter(
            Store.sto_id==sto_id).first()
        
        if obj == None:
            return json.dumps("Store ID, " + sto_id + ", not found")
        
        db.session.delete(obj)
        db.session.commit()
    except Exception as err:
        db.session.rollback()
        return json.dumps("Database error:" + err)

    return json.dumps("Successfully deleted storeID:" + sto_id)

@app.route("/deleteStaff", methods=['POST'])
def deleteStaff():

    sta_id = request.form.get('sta_id')
    if sta_id == None:
        return json.dumps("Need staff ID to delete staff")

    try:
        obj = db.session.query(Staff).filter(
            Staff.sta_id==sta_id).first()
        
        if obj == None:
            return json.dumps("Staff ID, " + sta_id + ", not found")
        
        db.session.delete(obj)
        db.session.commit()
    except Exception as err:
        db.session.rollback()
        return json.dumps("Database error:" + err)

    return json.dumps("Successfully deleted staffID:" + sta_id)

@app.route("/deleteCustomer", methods=['POST'])
def deleteCustomer():

    c_id = request.form.get('c_id')
    if c_id == None:
        return json.dumps("Need customer ID to delete store")

    try:
        obj = db.session.query(Customer).filter(
            Customer.c_id==c_id).first()
        
        if obj == None:
            return json.dumps("Customer ID, " + c_id + ", not found")
        
        db.session.delete(obj)
        db.session.commit()
    except Exception as err:
        db.session.rollback()
        return json.dumps("Database error:" + err)

    return json.dumps("Successfully deleted customerID:" + c_id)

@app.route("/deleteFurniture", methods=['POST'])
def deleteFurniture():

    f_id = request.form.get('f_id')
    if f_id == None:
        return json.dumps("Need furniture ID to delete store")

    try:
        obj = db.session.query(Furniture).filter(
            Furniture.f_id==f_id).first()
        
        if obj == None:
            return json.dumps("Furniture ID, " + f_id + ", not found")
        
        db.session.delete(obj)
        db.session.commit()
    except Exception as err:
        db.session.rollback()
        return json.dumps("Database error:" + err)

    return json.dumps("Successfully deleted furnitureID:" + f_id)

@app.route("/deleteOrder", methods=['POST'])
def deleteOrder():

    o_id = request.form.get('o_id')
    if o_id == None:
        return json.dumps("Need order ID to delete order")

    try:
        obj = db.session.query(Order).filter(
            Order.o_id==o_id).first()
        
        if obj == None:
            return json.dumps("Order ID, " + o_id + ", not found")
        
        db.session.delete(obj)
        db.session.commit()
    except Exception as err:
        db.session.rollback()
        return json.dumps("Database error:" + err)

    return json.dumps("Successfully deleted orderID:" + o_id)

@app.route("/deleteOrderFurniture", methods=['POST'])
def deleteOrderFurniture():

    o_id = request.form.get('o_id')
    f_id = request.form.get('f_id')
    if o_id == None:
        return json.dumps("Need order ID to delete OrderFurniture")
    if f_id == None:
        return json.dumps("Need furniture ID to delete OrderFurniture")

    try:
        obj = db.session.query(OrderFurniture).filter(
            OrderFurniture.o_id==o_id, OrderFurniture.f_id==f_id).first()
        
        if obj == None:
            return json.dumps("OrderFurniture ID, " + o_id + ", " + f_id + " not found")
        
        db.session.delete(obj)
        db.session.commit()
    except Exception as err:
        db.session.rollback()
        return json.dumps("Database error:" + err)

    return json.dumps("Successfully deleted orderfurnitureID:" + o_id + "," + f_id)

@app.route("/deleteStoreInventory", methods=['POST'])
def deleteStoreInventory():

    sto_id = request.form.get('sto_id')
    f_id = request.form.get('f_id')
    if sto_id == None:
        return json.dumps("Need order ID to delete StoreInventory")
    if f_id == None:
        return json.dumps("Need furniture ID to delete StoreInventory")

    try:
        obj = db.session.query(StoreInventory).filter(
            StoreInventory.sto_id==sto_id, StoreInventory.f_id==f_id).first()
        
        if obj == None:
            return json.dumps("StoreInventory ID, " + sto_id + ", " + f_id + " not found")
        
        db.session.delete(obj)
        db.session.commit()
    except Exception as err:
        db.session.rollback()
        return json.dumps("Database error:" + err)

    return json.dumps("Successfully deleted StoreInventoryID:" + sto_id + "," + f_id)

def seedDatabase():
    sto_id = "1"
    sto_location = "123 Street Road"
    sto_phone = "832-348-2385"
    sto_hours = "10"
    try:
        entry = Store(sto_id=sto_id, sto_location=sto_location, sto_phone=sto_phone, sto_hours=sto_hours, m_id=None)
        db.session.add(entry)
        db.session.commit()
    except Exception as err:
        print(err)

def deleteAllStore():

    try:
        db.session.query(Store).delete()
        db.session.commit()
    except Exception as err:
        print("Exception: " + err)

def deleteAllStaff():

    try:
        db.session.query(Staff).delete()
        db.session.commit()
    except Exception as err:
        print("Exception: " + err)

def deleteAllCustomer():

    try:
        db.session.query(Customer).delete()
        db.session.commit()
    except Exception as err:
        print("Exception: " + err)

def deleteAllOrder():

    try:
        db.session.query(Order).delete()
        db.session.commit()
    except Exception as err:
        print("Exception: " + err)
    
def deleteAllFurniture():

    try:
        db.session.query(Furniture).delete()
        db.session.commit()
    except Exception as err:
        print("Exception: " + err)

def deleteAllOrderFurniture():

    try:
        db.session.query(OrderFurniture).delete()
        db.session.commit()
    except Exception as err:
        print("Exception: " + err)

def deleteAllStoreInventory():

    try:
        db.session.query(StoreInventory).delete()
        db.session.commit()
    except Exception as err:
        print("Exception: " + err)

def wipeDatabase():

    deleteAllStore()
    deleteAllStaff()
    deleteAllCustomer()
    deleteAllOrder()
    deleteAllFurniture()
    deleteAllOrderFurniture()
    deleteAllStoreInventory()
    

if __name__ == '__main__':

    db.create_all()
    wipeDatabase() #This line is used for testing, may need to comment out for production
    seedDatabase()
    app.run(port=8000)
