from argparse import ArgumentParser

import uvicorn

from depositpredictor.api import app


def start_api():
    uvicorn.run(app, host="0.0.0.0", port=8085)

if __name__ == "__main__":

    parser = ArgumentParser(description="Bank Deposit Predictor")
    parser.add_argument("command", choices=["run"])

    args = parser.parse_args()

    if args.command == "run":
        start_api()
