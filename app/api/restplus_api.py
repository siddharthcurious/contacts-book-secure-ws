from flask_restplus import Api

api = Api(
    version='0.0.1',
    title='Contacts Book Application',
    description='Python Flask Restplus powered APIs',
    contact_url=None,
    contact_email="sandhyalalkumar@gmail.com",
    security=None,
    doc='/',
    default_mediatype='application/json',
    catch_all_404s=False,
    serve_challenge_on_401=False,
    )