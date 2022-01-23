import google.cloud.dialogflow_v2 as dialogflow

from proto import Message
from google.oauth2 import service_account
from lib.env import CONFIG

DIALOGFLOW_PROJECT_ID = CONFIG['DIALOGFLOW_PROJECT_ID']
DIALOGFLOW_LANGUAGE_CODE = CONFIG['DIALOGFLOW_LANGUAGE_CODE']
SESSION_ID = CONFIG['DIALOGFLOW_SESSION_ID']
SERVICE_ACCOUNT_FILE = CONFIG['DIALOGFLOW_SERVICE_ACCOUNT_FILE']+'.json'
CREDENTIALS = service_account.Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE)

def send_request(body):
    session_client = dialogflow.SessionsClient(credentials=CREDENTIALS)
    session = session_client.session_path(DIALOGFLOW_PROJECT_ID, SESSION_ID)
    text_input = dialogflow.types.TextInput(text=(body), language_code=DIALOGFLOW_LANGUAGE_CODE)
    query_input = dialogflow.types.QueryInput(text=text_input)
    response = session_client.detect_intent(session=session, query_input=query_input)
    json_response = Message.to_dict(response)
    return json_response
