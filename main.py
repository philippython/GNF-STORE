from flask import Flask, render_template, redirect, url_for, flash, request, abort
from forms import DeliveryForm
from flask_ckeditor import CKEditor
from flask_bootstrap import Bootstrap
import smtplib
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired, URL
from functools import wraps


app = Flask(__name__)
app.config['SECRET_KEY'] = 'jhvdbadhvsbdnfhJNDKAHFDNKJNS'
ckeditor = CKEditor(app)
Bootstrap(app)
my_email = "odulajaphilip@gmail.com"
password = "temitayo2004"


product_dictionary = {
    'name': ['Fresh Tomatoes', 'Fresh Pepper', 'Rice', 'Egg', 'Garri', 'Beans', 'Turkey', 'Sawa', 'Titus', 'Potato', 'Plantain', 'Yam', 'Palm oil', 'Groundnut Oil',
             'Spaghetti Slim/Fat', 'Spaghetti Slim', 'Big Sweet corn', 'Fried rice \nmixed ing.', 'Spicity jollof',
             'fried rice spice', 'Tomato paste','Curry and thyme', 'Maggi Cubes', 'And a lot more'],
    'price': ['#100 upwards', '#100 upwards', '#1,200(per congo)', '3 for #200', '#400(per congo)', '#1000(per congo)', '#2,400 per kg', '#300 upwards',
              '#600 upwards', '#200 upwards', '#200 upwards',
              '#700 upwards', '#800(per bottle)', '#1,000(per bottle)', '#350 each', '#6,800 per pack', '#500 each',
              '#500 each', '#50 each', '#50 each', '#100 each', 'a pair for #50', '#200 per sachet'],
    'image': ['tom', 'pep', 'rice', 'egg', 'garri', 'beans', 'turkey', 'sawa', 'titus', 'potato', 'plantain', 'yam', 'palmoil',
              'groundnut', 'spag', 'spagpack', 'corn', 'mix', 'jol', 'fri', 'gino', 'thy', 'mag', 'store']
}
drink_dictionary = {
    'name': ['Jameson', 'Black bullet', 'Can orijin', 'Smirnoff Ice', 'Guinness', 'Trophy', '8pm', 'Magic Moment',
             'Four cousins', 'Big Lord Gin', 'Mini Lord', 'Big Best Whiskey', 'Mini Best Whiskey', 'Chelsea Gin',
             'Smirnoff Vodka', 'Action Bitter', 'Andre', 'Best Cream', 'Skirt', 'Captain Jack', 'Orijin pet', 'Kolaq',
             'Soft Drinks', 'Small Bigi', 'Active', 'Can Active', 'Exotic', 'Can exotic', 'Fearless', 'Predator',
             'Viju Milk', 'Nutri milk', 'Fresh yo', 'Bag of Water', 'Pulpy 5 Alive'],
    'price': ['#11,000', '#600', '#350', '#400', '#300', '#300', '#3,000', '#2,500', '#5,000', '#1,500', '#500',
              '#2,000', '#600', '#500', '#2,500', '#1,500', '#5,000', '#3,000', '#1,500', '#1,500', '#500', '#500',
              '#150', '#100', '#700', '#250', '#700', '#250', '#250', '#250', '#250', '#250', '#300', '#300',
              '#600'],
    'image': ['jameson', 'bullet', 'canori', 'smir', 'cangun', 'trop', '8pm', 'mm', '4c', 'lord', 'losm', 'whiz', 'wiz',
              'che', 'off', 'act', 'and', 'cre', 'ski', 'jack', 'pet', 'ala', 'drink', 'bigi', 'tive', 'ctive', 'exo',
              'cexo', 'fear', 'pre', 'vij', 'nut', 'yo', 'wat', 'pulp']
}
provision_dictionary = {
    'name': ['Noodles pcs', 'Noodles Pack', 'chocolates', 'Jam Bread', 'Checkers Custard', 'Bama', 'Titus Sardine',
             'Estus Sardine', 'Butter', 'Peanut butter', 'Condoms',
             'Sanitary Pad', 'Sanitary Pad', 'Milo Tin', 'Peak Milk Tin', 'Milo Refill', 'Peak Milk Refill', 'Goldenmorn'
             'sachet', 'Goldenmorn Refill', 'Dano Refill', 'Biscuits'],
    'price': ['#70 upwards', '#2,600 upwards', '#50-#100 up', '#100', '#600', '#650', '#650', '#500', '#450 up',
              '#500', '#150 upwards', '#100-150(sachet)', '#400 upwards', '#2,600', '#2,600', '#1,300', '#1,800',
              '#120', '#1,800', '#600', '#50 upwards'],
    'image': ['in', 'inp', 'cho', 'jam', 'cus', 'bam', 'sar', 'est', 'download', 'pea', 'cond', 'diva', 'ld', 'milo',
              'mil', 'milr', 'milkr', 'gms', 'gml', 'dano', 'biscuit']
}


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/products')
def product():
    return render_template('products.html', diction=drink_dictionary)


@app.route('/contact')
def contact():
    return render_template('contact.html')


@app.route('/foodstuffs')
def foodstuffs():
    return render_template('foodsutuff.html', diction=product_dictionary)


@app.route('/provision')
def provision():
    return render_template('provision.html', diction=provision_dictionary)


@app.route('/delivery', methods=['GET', 'POST'])
def delivery():
    form = DeliveryForm()
    if form.validate_on_submit():
        flash('You order has been successfully placed make an instant transfer now!')
        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(from_addr=my_email,
                                to_addrs=my_email,
                                msg=f"Subject:GNF ORDER\n\nA customer just placed an order\n"
                                    f"Customer Name:  {form.name.data}\n"
                                    f"Pick up type:   {form.type.data}\n"
                                    f"Contact no:  {form.num.data}\n"
                                    f"Location:  {form.location.data}\n"
                                    f"Account name:  {form.Account.data}\n"
                                    f"Goods:  {form.item.data}\n"
                                    f"Bill:   {form.Amount.data}\n"
                                )
    return render_template('delivery.html', form=form)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
