import imaplib
import email
from email.header import decode_header
import webbrowser
import os
from openai import OpenAI
import json

debug_use_website = True

# account credentials
username = "kamel4061@outlook.com"
password = "1qaz@WSXparola12"
# use your email provider's IMAP server, you can look for your provider's IMAP server on Google
# or check this page: https://www.systoolsgroup.com/imap/
# for office 365, it's this:
imap_server = "outlook.office365.com"

def clean(text):
    # clean text for creating a folder
    return "".join(c if c.isalnum() else "_" for c in text)

# create an IMAP4 class with SSL 
imap = imaplib.IMAP4_SSL(imap_server)
# authenticate
imap.login(username, password)

status, messages = imap.select("INBOX")
# number of top emails to fetch
#DON'T GRAB MORE MESSAGES THAN THERE ARE,IT WILL ERROR OUT
N = 1
# total number of emails
messages = int(messages[0])

#text to print
final_message = "test"

email_from = "yes"
email_subject = "yes"
email_body = "yes"


def Call(): 
    for i in range(messages, messages-N, -1):
        # fetch the email message by ID
        res, msg = imap.fetch(str(i), "(RFC822)")
        for response in msg:
            if isinstance(response, tuple):
                # parse a bytes email into a message object
                msg = email.message_from_bytes(response[1])
                # decode the email subject
                subject, encoding = decode_header(msg["Subject"])[0]
                if isinstance(subject, bytes):
                    # if it's a bytes, decode to str
                    subject = subject.decode(encoding)
                # decode email sender
                From, encoding = decode_header(msg.get("From"))[0]
                if isinstance(From, bytes):
                    From = From.decode(encoding)
                print("Subject:", subject)
                email_subject = subject

                print("From:", From)
                email_from = From
                # if the email message is multipart
                if msg.is_multipart():
                    # iterate over email parts
                    for part in msg.walk():
                        # extract content type of email
                        content_type = part.get_content_type()
                        content_disposition = str(part.get("Content-Disposition"))
                        try:
                            # get the email body
                            body = part.get_payload(decode=True).decode()
                        except:
                            pass
                        if content_type == "text/plain" and "attachment" not in content_disposition:
                            # print text/plain emails and skip attachments
                            print(body)
                        elif "attachment" in content_disposition:
                            # download attachment
                            filename = part.get_filename()
                            if filename:
                                folder_name = clean(subject)
                                if not os.path.isdir(folder_name):
                                    # make a folder for this email (named after the subject)
                                    os.mkdir(folder_name)
                                filepath = os.path.join(folder_name, filename)
                                # download attachment and save it
                                open(filepath, "wb").write(part.get_payload(decode=True))
                else:
                    # extract content type of email
                    content_type = msg.get_content_type()
                    # get the email body
                    body = msg.get_payload(decode=True).decode()
                    if content_type == "text/plain":
                        # print only text email parts
                        print(body)
                        email_body = body

            #create client object

def Do_AI():
    client = OpenAI(
        # Defaults to os.environ.get("OPENAI_API_KEY")
        api_key =  "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"
    )

    #get response

    Call()

    chat_completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": "Tell me if the mail is a phishing email with the following syntax : Phishing email : Yes/No + percentage of certainty" + email_subject + " " + email_from + " " + email_body}]
    )

    final_message = chat_completion.choices[0].message.content;
    print(final_message)
    return "Is the last email a scam?(Y/N + percentage of certainty) " + final_message
    #return(chat_completion.choices[0].message.content)         

#Call()
    


if(debug_use_website):
    #flask stuff
    from flask import Flask,render_template
    app = Flask(__name__)

    @app.route("/")
    def index():
        return render_template("template.html")

    @app.route('/my-link/')
    def my_link():
        print ("I got clicked!")

        return Do_AI()

    if __name__ == '__main__':
        app.run(debug=True)