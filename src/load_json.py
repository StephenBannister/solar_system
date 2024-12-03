import json, logging

def load_json_data(filename):
    ''' helper function to open and read JSON files. Returns the content.
    '''
    try:
        with open(filename, "r") as file:
            return json.load(file)
    except FileNotFoundError as e:
        logging.error(f"The file '{filename}' was not found.")
        raise e
    except json.JSONDecodeError as e:
        logging.error(f"The file '{filename}' does not contain valid JSON.")
        raise e
    except Exception as e:
        logging.error(f"An unexpected error occurred: {e}")
        raise e