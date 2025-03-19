import json
import logging


def write_to_file(path: str, data):
    try:
        with open(path, "w") as json_file:
            json.dump(data, json_file, indent=4)
        logging.log(level=1, msg=f"Data successfully written to {path}")
    except IOError as e:
        logging.error(f"I/O error: {e}")
    except Exception as e:
        logging.error(f"Unexpected error: {e}")
