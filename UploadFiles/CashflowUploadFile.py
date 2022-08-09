from generic_app.models import *

class CashflowUploadFile(UploadModelMixin, Model):
    
    id = AutoField(primary_key=True)
    upload_file = FileField()
    
    def update(self):
        # TODO specify what you want to do once the model has been saved
        pass
