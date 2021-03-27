from django.db import migrations, models
import django.db.models.deletion

class Migration(migrations.Migration):
    dependencies = [
        ('plugin_crossconnect','0001_initial'),
        ('tenancy','0001_initial'),
        ('circuits','0001_initial'),
    ]
    operations = [
        migrations.AlterField(
            model_name="plugin_crossconnect",
            name='customer',
            field=models.ForeignKey(to="tenancy.tenant",on_delete=models.PROTECT)
        ),
        migrations.RemoveField(
            model_name="plugin_crossconnect",
            name='col2',
        ),
        migrations.RemoveField(
            model_name="plugin_crossconnect",
            name='col3',
        ),
        migrations.AddField(
            model_name="plugin_crossconnect",
            name='routetypes',
            field=models.CharField(choices=[('0','Select Route Type'),('1','Short Route'),('2','Long Route')],default=0,max_length=1
        ),
        ),
        migrations.AddField(
            model_name="plugin_crossconnect",
            name='telconame',
            field=models.ForeignKey(to='circuits.provider',on_delete=models.PROTECT),
        )
    ]