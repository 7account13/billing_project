from flask import Flask, render_template, request, redirect, url_for,jsonify
import sqlite3

app = Flask(__name__)

# Route for the dashboard
@app.route('/')
def dashboard():
    return render_template('dashboard.html')

# Route for customers page
@app.route('/customers')
def customers():
    conn = sqlite3.connect('km.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM customers')
    customers = cursor.fetchall()
    conn.close()

    return render_template('customers.html', customers=customers)

# Route to add a new customer
@app.route('/add_customer', methods=['GET', 'POST'])
def add_customer():
    if request.method == 'POST':
        name = request.form['name']
        gst = request.form['gst']
        email = request.form.get('email')
        phone = request.form.get('phone')
        billing_address = request.form.get('billing_address')
        shipping_address = request.form.get('shipping_address')

        conn = sqlite3.connect('km.db')
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO customers (name, gst, email, phone, billing_address, shipping_address)
            VALUES (?, ?, ?, ?, ?, ?)
        ''', (name, gst, email, phone, billing_address, shipping_address))
        conn.commit()
        conn.close()

        return redirect(url_for('customers'))

    return render_template('add_customer.html')

# Route to edit an existing customer
@app.route('/edit_customer/<int:id>', methods=['GET', 'POST'])
def edit_customer(id):
    conn = sqlite3.connect('km.db')
    cursor = conn.cursor()

    if request.method == 'POST':
        name = request.form['name']
        gst = request.form['gst']
        email = request.form.get('email')
        phone = request.form.get('phone')
        billing_address = request.form.get('billing_address')
        shipping_address = request.form.get('shipping_address')

        cursor.execute('''
            UPDATE customers
            SET name = ?, gst = ?, email = ?, phone = ?, billing_address = ?, shipping_address = ?
            WHERE id = ?
        ''', (name, gst, email, phone, billing_address, shipping_address, id))
        conn.commit()
        conn.close()

        return redirect(url_for('customers'))

    cursor.execute('SELECT * FROM customers WHERE id = ?', (id,))
    customer = cursor.fetchone()
    conn.close()

    return render_template('edit_customer.html', customer=customer)

# Route for products page
@app.route('/products')
def products():
    conn = sqlite3.connect('km.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM products')
    products = cursor.fetchall()
    conn.close()

    return render_template('products.html', products=products)

# Route to add a new product
@app.route('/add_product', methods=['GET', 'POST'])
def add_product():
    if request.method == 'POST':
        name = request.form['name']
        unit = request.form['unit']
        hsn_code = request.form['hsn_code']
        selling_price = request.form['selling_price']
        intra_state_tax_rate = request.form['intra_state_tax_rate']
        inter_state_tax_rate = request.form['inter_state_tax_rate']

        conn = sqlite3.connect('km.db')
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO products (name, unit, hsn_code, selling_price, intra_state_tax_rate, inter_state_tax_rate)
            VALUES (?, ?, ?, ?, ?, ?)
        ''', (name, unit, hsn_code, selling_price, intra_state_tax_rate, inter_state_tax_rate))
        conn.commit()
        conn.close()

        return redirect(url_for('products'))

    return render_template('add_product.html')

# Route to edit an existing product
@app.route('/edit_product/<int:id>', methods=['GET', 'POST'])
def edit_product(id):
    conn = sqlite3.connect('km.db')
    cursor = conn.cursor()

    if request.method == 'POST':
        name = request.form['name']
        unit = request.form['unit']
        hsn_code = request.form['hsn_code']
        selling_price = request.form['selling_price']
        intra_state_tax_rate = request.form['intra_state_tax_rate']
        inter_state_tax_rate = request.form['inter_state_tax_rate']

        cursor.execute('''
            UPDATE products
            SET name = ?, unit = ?, hsn_code = ?, selling_price = ?, intra_state_tax_rate = ?, inter_state_tax_rate = ?
            WHERE id = ?
        ''', (name, unit, hsn_code, selling_price, intra_state_tax_rate, inter_state_tax_rate, id))
        conn.commit()
        conn.close()

        return redirect(url_for('products'))

    cursor.execute('SELECT * FROM products WHERE id = ?', (id,))
    product = cursor.fetchone()
    conn.close()

    return render_template('edit_product.html', product=product)

# Other routes
@app.route('/quotes')
def quotes():
    return render_template('quotes.html')

@app.route('/invoice')
def invoice():
    
    conn = sqlite3.connect('km.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM invoices')
    invoices = cursor.fetchall()
    conn.close()
    return render_template('invoices.html')

# Route to add a new invoice
@app.route('/add_invoice', methods=['GET', 'POST'])
def add_invoice():
    if request.method == 'POST':
        # Logic to save the new invoice
        return redirect(url_for('invoices'))
    def get_db_connection():
        conn = sqlite3.connect('km.db')
        conn.row_factory = sqlite3.Row
        return conn


    

    return render_template('add_invoice.html')
    def get_db_connection():
        conn = sqlite3.connect('km.db')
        conn.row_factory = sqlite3.Row
        return conn

    def create_invoice():
        customer_id = request.form['customer']
        product_id = request.form['product']
        quantity = request.form['quantity']

        conn = get_db_connection()
        product = conn.execute('SELECT selling_price FROM products WHERE id = ?', (product_id,)).fetchone()
        rate = product['selling_price']
        total = int(quantity) * rate
        conn.execute(
        'INSERT INTO invoices (customer_id, product_id, quantity, rate, total) VALUES (?, ?, ?, ?, ?)',
        (customer_id, product_id, quantity, rate, total)
    )
        conn.commit()
        conn.close()
    return jsonify({'success': True})




@app.route('/purchase-orders')
def purchase_orders():
    return render_template('purchase_orders.html')

@app.route('/payments-received')
def payments_received():
    return render_template('payments_received.html')

@app.route('/expenses')
def expenses():
    return render_template('expenses.html')

@app.route('/gst-filings')
def gst_filings():
    return render_template('gst_filings.html')

@app.route('/reports')
def reports():
    return render_template('reports.html')

if __name__ == '__main__':
    app.run(debug=True)
