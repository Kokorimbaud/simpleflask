from flask import Flask
from critics import get_critics, pick_random_critic, random_critic, the_one_critic


def create_app():
    app = Flask("test")

    @app.route("/")
    def home():
        return "yay!"

    @app.route('/critics/', methods=["GET"])
    def all_critics():
        return get_critics()

    @app.route('/critics/random/', methods=["GET"])
    def random_critic():
        return pick_random_critic()[0]

    @app.route('/critics/individual/', methods=['GET'])
    def get_individual_critic():
        return random_critic()

    @app.route('/critics/stephen-holden/', methods=['GET'])
    def get_stephen_holden():
        return the_one_critic()

    return app


if __name__ == "__main__":
    app = create_app()
    app.run(host="0.0.0.0", port=8000)