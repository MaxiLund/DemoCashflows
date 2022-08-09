from generic_app.models import *
import pandas as pd

class CashflowUploadFile(UploadModelMixin, Model):
    
    id = AutoField(primary_key=True)
    upload_file = FileField()
    
    def update(self):
        df = pd.read_excel(self.upload_file)
        for index, row in df.iterrows():
            cashflow = Cashflow(amount=row['amount'], currency=row['currency'])
            cashflow.save()
