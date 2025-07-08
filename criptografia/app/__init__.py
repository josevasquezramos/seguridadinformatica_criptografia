from flask import Flask

def create_app():
    app = Flask(__name__)

    from app.routes import (
        home,
        cifra_flujo,
        simetrico_bloque,
        mochila,
        exponencial,
        hash,
        firma,
        certificados,
        cuantica,
        blockchain,
    )

    app.register_blueprint(home.bp)
    app.register_blueprint(cifra_flujo.bp)
    app.register_blueprint(simetrico_bloque.bp)
    app.register_blueprint(mochila.bp)
    app.register_blueprint(exponencial.bp)
    app.register_blueprint(hash.bp)
    app.register_blueprint(firma.bp)
    app.register_blueprint(certificados.bp)
    app.register_blueprint(cuantica.bp)
    app.register_blueprint(blockchain.bp)

    return app
