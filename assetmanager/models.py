from django.db import models
from administration.choices import *
from administration.models import baseModel
from members.models import members
from loans.models import Loans
from administration.models import Branch


# Create your models here.


class loanAsset(baseModel):
    loan = models.ForeignKey(Loans, on_delete=models.CASCADE)
    name = models.CharField(max_length=50, null=True)
    description = models.TextField(null=True)
    expiry_date = models.DateField(null=True,blank=True)
    inspection_date = models.DateField(null=True,blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, null=True)
    value = models.IntegerField(null=True)

    class Meta:
        db_table = "loan_asset"

    def __str__(self):
    	return f"{self.loan.lendee.names}'s {self.name}"
 


class assetDocument(baseModel):
    upload_date = models.DateField(auto_now_add=True)
    document_name = models.CharField(max_length=200, null=True, blank=True)
    file = models.FileField(upload_to='assetdocuments/',null=True)
    proof_of = models.ForeignKey(loanAsset, on_delete=models.CASCADE)
    
    class Meta:
        db_table = "asset_document"
        
    def __str__(self):
        return self.document_name
    
		
	