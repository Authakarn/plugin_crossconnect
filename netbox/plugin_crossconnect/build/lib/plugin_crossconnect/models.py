from django.db import models
from utilities.querysets import RestrictedQuerySet
#from extras.models import ChangeLoggedModel

class plugin_crossconnect(models.Model):
     #customer = models.ForeignKey(to="dcim.Tenants",on_delete=models.DO_NOTHING,)
     circuitid = models.CharField(max_length=20,null=True)
     customer = models.ForeignKey(to="tenancy.tenant",on_delete=models.PROTECT)
     ROUTE_TYPES = (
          ('0','Select Route Type'),
          ('1','Short Route'),
          ('2','Long Route'),     
     )
     TERMINATION = (
          ('0','Select Terminal'),
          ('1','Telco'),
          ('2','Customer'),
          ('3','SNT'),
     )
     routetypes = models.CharField(max_length=1,choices=ROUTE_TYPES,default=0)
     telconame = models.ForeignKey(to='circuits.provider',on_delete=models.PROTECT)
     telcocid = models.CharField(max_length=20,null=True)
     terminationa = models.CharField(max_length=1,choices=TERMINATION,default=0)
     terminationatelcorownumber = models.CharField(max_length=10,null=True)
     terminationarackunit = models.CharField(max_length=50,null=True)
     terminationaportnumber = models.CharField(max_length=50,null=True)
     terminationb = models.CharField(max_length=1,choices=TERMINATION,default=0)
     terminationbtelcorownumber = models.CharField(max_length=10,null=True)
     terminationbrackunit = models.CharField(max_length=50,null=True)
     terminationbportnumber = models.CharField(max_length=50,null=True)
     connectortype = models.CharField(max_length=10,null=True)
     cabletype = models.CharField(max_length=5,null=True)
     description = models.CharField(max_length=250,null=True)
     
     objects = RestrictedQuerySet.as_manager()

     
#      def __str__(self):
#         return self.customer

# class plugin_crossconnect(models.Model):
#     name = models.CharField(max_length=50)
#     sound = models.CharField(max_length=50)



# class plugin_crossconnect(models.Model):
#     customer = models.CharField(max_length=50