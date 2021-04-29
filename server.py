from flask import Flask
from critics import get_critics, pick_random_critic, individual_critic
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
        return pick_random_critic(id)

    @app.route('/critics/individual/', methods=['GET'])
    def get_individual_critic():
        return individual_critic(id)

    @app.route('/reviews/picks', methods=['GET'])
    def get_critics_picks():
        pass

    return app

if __name__ == "__main__":
    app = create_app()
    app.run(host="0.0.0.0", port=8000)