from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired, URL
from flask_ckeditor import CKEditorField


class DeliveryForm(FlaskForm):
    name = StringField("Name", validators=[DataRequired()])
    type = StringField("Delivery/Pickup", validators=[DataRequired()])
    num = StringField("Contact Number", validators=[DataRequired()])
    location = StringField("Location: If you're Picking your goods up leave this space empty")
    Account = StringField("The name on the account you're making the "
                          "transaction from, This is for Confirmation purposes", validators=[DataRequired()])
    item = CKEditorField("List of all items you wish to purchase we understand any way its inputted",
                         validators=[DataRequired()])
    Amount = StringField("Total Amount in NGN", validators=[DataRequired()])
    submit = SubmitField("Make an order now")
