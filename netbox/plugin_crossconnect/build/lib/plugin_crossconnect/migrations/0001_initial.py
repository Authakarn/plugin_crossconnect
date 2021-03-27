from django.db import migrations, models
import django.db.models.deletion

class Migration(migrations.Migration):
    initial = True

    operations = [
        migrations.CreateModel(
            name="plugin_crossconnect",
            fields=[
                ("id" , models.AutoField(auto_created=True,primary_key=True,serialize=False)),
                ("customer" , models.CharField(blank=True,max_length=50)),
                ("col2", models.CharField(blank=True,max_length=50)),
                ("col3", models.CharField(blank=True,max_length=50)),
            ]
        )
    ]