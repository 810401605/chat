from django.db import migrations, models

class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ChatSession',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('input_text', models.TextField()),
                ('response_text', models.TextField()),
                ('user', models.ForeignKey(on_delete=models.CASCADE, related_name='chat_sessions', to='auth.User')),
            ],
        ),
    ]
