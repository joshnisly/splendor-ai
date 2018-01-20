#!/usr/bin/env python3

import flask

import game
import game_cards

app = flask.Flask(__name__)

THE_GAME = game.SplendorGame()
THE_GAME.init_random()
THE_GAME.add_player(lambda: [], None)
THE_GAME.add_player(lambda: [], None)


@app.route('/', methods=['GET'])
def index():
    game_state = THE_GAME.get_game_state()
    return flask.render_template('index.html', **{
        'state': game_state,
        'colors': game_cards.COLOR_VALUES,
        'font_colors': game_cards.FONT_COLOR_VALUES
    })


if __name__ == '__main__':
    app.run(debug=True)
