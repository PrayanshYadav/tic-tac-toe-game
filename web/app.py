
from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = "tic_tac_toe_secret_key"

WINNING_COMBINATIONS = [
    [0, 1, 2],
    [3, 4, 5],
    [6, 7, 8],
    [0, 3, 6],
    [1, 4, 7],
    [2, 5, 8],
    [0, 4, 8],
    [2, 4, 6]
]


@app.route("/", methods=["GET", "POST"])
def home():

    if "board" not in session:
        session["board"] = [""] * 9
        session["current_player"] = "X"
        session["winner"] = ""
        session["draw"] = False
        session["game_over"] = False

    if request.method == "POST":

        position = request.form.get("position", type=int)
        board = session["board"]

        if (
            not session["game_over"]
            and position is not None
            and 0 <= position < 9
            and board[position] == ""
        ):

            board[position] = session["current_player"]
            session["board"] = board

            winner = ""

            for combination in WINNING_COMBINATIONS:
                if all(board[i] == session["current_player"]
                       for i in combination):
                    winner = session["current_player"]
                    break

            if winner:
                session["winner"] = winner
                session["game_over"] = True

            elif all(cell != "" for cell in board):
                session["draw"] = True
                session["game_over"] = True

            else:
                session["current_player"] = (
                    "O" if session["current_player"] == "X" else "X"
                )

    return render_template(
        "index.html",
        board=session["board"],
        current_player=session["current_player"],
        winner=session["winner"],
        draw=session["draw"],
        game_over=session["game_over"]
    )


@app.route("/restart", methods=["POST"])
def restart():
    session.clear()
    return redirect(url_for("home"))


if __name__ == "__main__":
    app.run(debug=True)
