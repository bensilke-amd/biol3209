import requests
from dnarecords.models import Sequence
from utils import SequenceCreator



example_type = 'ENSG00000157764'

class EnsemblSequenceCreator(SequenceCreator):
    # Class to use the http://rest.ensembl.org endpoints and create sequence objects easily from ids.
    server = "http://rest.ensembl.org"
    get_ext = "/archive/id/"
    headers={ "Content-Type" : "application/json"}


    def get(self, operation):
        r = requests.get(self.server+self.get_ext, headers=self.headers)
        return r.json()

    # comparative genomics
