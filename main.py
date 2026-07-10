from flask import Flask
from controllers.users_controller import user_bp
from controllers.bank_account_controller import bank_bp
from controllers.transaction_controller import transaction_bp
app = Flask(__name__)

app.register_blueprint(user_bp)
app.register_blueprint(bank_bp)
app.register_blueprint(transaction_bp)

if __name__ == '__main__':
    app.run(debug=True)
    