# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-04-12 14:18
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import microbot.validators
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Bot',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Date created')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Date updated')),
                ('token', models.CharField(db_index=True, help_text='Token provided by Telegram API https://core.telegram.org/bots', max_length=100, unique=True, validators=[microbot.validators.validate_token], verbose_name='Token')),
                ('enabled', models.BooleanField(default=True, help_text='Enable/disable bot', verbose_name='Enable')),
            ],
            options={
                'verbose_name': 'Bot',
                'verbose_name_plural': 'Bots',
            },
        ),
        migrations.CreateModel(
            name='Chat',
            fields=[
                ('id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('type', models.CharField(choices=[(b'private', 'Private'), (b'group', 'Group'), (b'supergroup', 'Supergroup'), (b'channel', 'Channel')], max_length=255)),
                ('title', models.CharField(blank=True, max_length=255, null=True)),
                ('username', models.CharField(blank=True, max_length=255, null=True)),
                ('first_name', models.CharField(blank=True, max_length=255, null=True)),
                ('last_name', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'verbose_name': 'Chat',
                'verbose_name_plural': 'Chats',
            },
        ),
        migrations.CreateModel(
            name='ChatState',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Date created')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Date updated')),
                ('context', models.TextField(blank=True, help_text='Context serialized to json when this state was set', null=True, verbose_name='Context')),
                ('chat', models.ForeignKey(help_text='Chat in Telegram API format. https://core.telegram.org/bots/api#chat', on_delete=django.db.models.deletion.CASCADE, related_name='chatstates', to='microbot.Chat', verbose_name='Chat')),
            ],
            options={
                'verbose_name': 'Chats States',
            },
        ),
        migrations.CreateModel(
            name='EnvironmentVar',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Date created')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Date updated')),
                ('key', models.CharField(help_text='Name of the variable', max_length=255, verbose_name='Key')),
                ('value', models.CharField(help_text='Value of the variable', max_length=255, verbose_name='Value')),
                ('bot', models.ForeignKey(help_text='Bot which variable is attached.', on_delete=django.db.models.deletion.CASCADE, related_name='env_vars', to='microbot.Bot', verbose_name='Bot')),
            ],
            options={
                'verbose_name': 'Environment Var',
                'verbose_name_plural': 'Environment Vars',
            },
        ),
        migrations.CreateModel(
            name='Handler',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Date created')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Date updated')),
                ('name', models.CharField(db_index=True, help_text='Name for the handler', max_length=100, verbose_name='Name')),
                ('pattern', models.CharField(help_text='Regular expression the Handler will be triggered. \n                               Using https://docs.python.org/2/library/re.html#regular-expression-syntax', max_length=255, validators=[microbot.validators.validate_pattern], verbose_name='Pattern')),
                ('enabled', models.BooleanField(default=True, help_text='Enable/disable handler', verbose_name='Enable')),
                ('priority', models.IntegerField(default=0, help_text='Set priority execution. Higher value higher priority', verbose_name='Priority')),
                ('bot', models.ForeignKey(help_text='Bot which Handler is attached to', on_delete=django.db.models.deletion.CASCADE, related_name='handlers', to='microbot.Bot', verbose_name='Bot')),
            ],
            options={
                'ordering': ['-priority'],
                'verbose_name': 'Handler',
                'verbose_name_plural': 'Handlers',
            },
        ),
        migrations.CreateModel(
            name='HeaderParam',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Date created')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Date updated')),
                ('key', models.CharField(help_text='Name of the parameter', max_length=255, verbose_name='Key')),
                ('value_template', models.CharField(help_text='Value template of the parameter. In jinja2 format. http://jinja.pocoo.org/', max_length=255, validators=[microbot.validators.validate_template], verbose_name='Value template')),
            ],
            options={
                'verbose_name': 'Header Parameter',
                'verbose_name_plural': 'Header Parameters',
            },
        ),
        migrations.CreateModel(
            name='Hook',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Date created')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Date updated')),
                ('name', models.CharField(db_index=True, help_text='Name of the hook', max_length=100, verbose_name='Name')),
                ('key', models.CharField(db_index=True, editable=False, help_text='Key generated to complete the Hook url. http://permabots.com/process/hook/{{key}}', max_length=30, unique=True)),
                ('enabled', models.BooleanField(default=True, help_text=b'Enable/disable hook', verbose_name='Enable')),
                ('bot', models.ForeignKey(help_text='Bot which Hook is attached', on_delete=django.db.models.deletion.CASCADE, related_name='hooks', to='microbot.Bot', verbose_name='Bot')),
            ],
            options={
                'verbose_name': 'Hook',
                'verbose_name_plural': 'Hooks',
            },
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Date created')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Date updated')),
                ('message_id', models.BigIntegerField(db_index=True, verbose_name='Id')),
                ('date', models.DateTimeField(verbose_name='Date')),
                ('text', models.TextField(blank=True, null=True, verbose_name='Text')),
                ('chat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='messages', to='microbot.Chat', verbose_name='Chat')),
            ],
            options={
                'ordering': ['-date'],
                'verbose_name': 'Message',
                'verbose_name_plural': 'Messages',
            },
        ),
        migrations.CreateModel(
            name='Recipient',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Date created')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Date updated')),
                ('chat_id', models.BigIntegerField(db_index=True, help_text='Chat identifier provided by Telegram API', verbose_name='Chat id')),
                ('name', models.CharField(db_index=True, help_text='Name of recipient', max_length=100, verbose_name='Name')),
                ('hook', models.ForeignKey(help_text='Hook which recipient is attached to', on_delete=django.db.models.deletion.CASCADE, related_name='recipients', to='microbot.Hook', verbose_name='Recipient')),
            ],
            options={
                'verbose_name': 'Recipient',
                'verbose_name_plural': 'Recipients',
            },
        ),
        migrations.CreateModel(
            name='Request',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Date created')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Date updated')),
                ('url_template', models.CharField(help_text='Url to request. A jinja2 template. http://jinja.pocoo.org/', max_length=255, validators=[microbot.validators.validate_template], verbose_name='Url template')),
                ('method', models.CharField(choices=[(b'Get', 'Get'), (b'Post', 'Post'), (b'Put', 'Put'), (b'Delete', 'Delete'), (b'Patch', 'Patch')], default=b'Get', help_text='Define Http method for the request', max_length=128, verbose_name='Method')),
                ('data', models.TextField(blank=True, help_text='Set POST/PUT/PATCH data in json format', null=True, verbose_name='Data of the request')),
            ],
            options={
                'verbose_name': 'Request',
                'verbose_name_plural': 'Requests',
            },
        ),
        migrations.CreateModel(
            name='Response',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Date created')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Date updated')),
                ('text_template', models.TextField(help_text='Template to generate text response. In jinja2 format. http://jinja.pocoo.org/', validators=[microbot.validators.validate_template, microbot.validators.validate_telegram_text_html], verbose_name='Text template')),
                ('keyboard_template', models.TextField(blank=True, help_text='Template to generate keyboard response. In jinja2 format. http://jinja.pocoo.org/', null=True, validators=[microbot.validators.validate_template, microbot.validators.validate_telegram_keyboard], verbose_name='Keyboard template')),
            ],
            options={
                'verbose_name': 'Response',
                'verbose_name_plural': 'Responses',
            },
        ),
        migrations.CreateModel(
            name='State',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Date created')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Date updated')),
                ('name', models.CharField(db_index=True, help_text='Name of the state', max_length=255, verbose_name='State name')),
                ('bot', models.ForeignKey(help_text='Bot which state is attached to', on_delete=django.db.models.deletion.CASCADE, related_name='states', to='microbot.Bot', verbose_name='Bot')),
            ],
            options={
                'verbose_name': 'State',
                'verbose_name_plural': 'States',
            },
        ),
        migrations.CreateModel(
            name='Update',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Date created')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Date updated')),
                ('update_id', models.BigIntegerField(db_index=True, verbose_name='Update Id')),
                ('bot', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='updates', to='microbot.Bot', verbose_name='Bot')),
                ('message', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='updates', to='microbot.Message', verbose_name='Message')),
            ],
            options={
                'verbose_name': 'Update',
                'verbose_name_plural': 'Updates',
            },
        ),
        migrations.CreateModel(
            name='UrlParam',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Date created')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Date updated')),
                ('key', models.CharField(help_text='Name of the parameter', max_length=255, verbose_name='Key')),
                ('value_template', models.CharField(help_text='Value template of the parameter. In jinja2 format. http://jinja.pocoo.org/', max_length=255, validators=[microbot.validators.validate_template], verbose_name='Value template')),
                ('request', models.ForeignKey(help_text='Request which this Url Parameter is attached to', on_delete=django.db.models.deletion.CASCADE, related_name='url_parameters', to='microbot.Request', verbose_name='Request')),
            ],
            options={
                'verbose_name': 'Url Parameter',
                'verbose_name_plural': 'Url Parameters',
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=255, verbose_name='First name')),
                ('last_name', models.CharField(blank=True, max_length=255, null=True, verbose_name='Last name')),
                ('username', models.CharField(blank=True, max_length=255, null=True, verbose_name='User name')),
            ],
            options={
                'verbose_name': 'User',
                'verbose_name_plural': 'Users',
            },
        ),
        migrations.AddField(
            model_name='message',
            name='forward_from',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='forwarded_from', to='microbot.User', verbose_name='Forward from'),
        ),
        migrations.AddField(
            model_name='message',
            name='from_user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='messages', to='microbot.User', verbose_name='User'),
        ),
        migrations.AddField(
            model_name='hook',
            name='response',
            field=models.OneToOneField(help_text='Template the hook uses to generate the response', on_delete=django.db.models.deletion.CASCADE, to='microbot.Response', verbose_name='Response'),
        ),
        migrations.AddField(
            model_name='headerparam',
            name='request',
            field=models.ForeignKey(help_text='Request which this Url Parameter is attached to', on_delete=django.db.models.deletion.CASCADE, related_name='header_parameters', to='microbot.Request', verbose_name='Request'),
        ),
        migrations.AddField(
            model_name='handler',
            name='request',
            field=models.OneToOneField(blank=True, help_text='Request the Handler processes', null=True, on_delete=django.db.models.deletion.SET_NULL, to='microbot.Request'),
        ),
        migrations.AddField(
            model_name='handler',
            name='response',
            field=models.OneToOneField(help_text='Template the handler uses to generate response', on_delete=django.db.models.deletion.CASCADE, to='microbot.Response'),
        ),
        migrations.AddField(
            model_name='handler',
            name='source_states',
            field=models.ManyToManyField(blank=True, help_text='Bot states the Handler needs to be to execute. Set none if any', related_name='source_handlers', to='microbot.State', verbose_name='Source States'),
        ),
        migrations.AddField(
            model_name='handler',
            name='target_state',
            field=models.ForeignKey(blank=True, help_text='This state will be set when handler ends processing', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='target_handlers', to='microbot.State', verbose_name='Target State'),
        ),
        migrations.AddField(
            model_name='chatstate',
            name='state',
            field=models.ForeignKey(help_text='State related to the chat', on_delete=django.db.models.deletion.CASCADE, related_name='chat', to='microbot.State', verbose_name='State'),
        ),
        migrations.AddField(
            model_name='bot',
            name='owner',
            field=models.ForeignKey(help_text='User who owns the bot', on_delete=django.db.models.deletion.CASCADE, related_name='bots', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='bot',
            name='user_api',
            field=models.OneToOneField(blank=True, help_text='Telegram API info. Automatically retrieved from Telegram', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='bot', to='microbot.User', verbose_name='Bot User'),
        ),
        migrations.AlterUniqueTogether(
            name='update',
            unique_together=set([('update_id', 'bot')]),
        ),
        migrations.AlterUniqueTogether(
            name='message',
            unique_together=set([('message_id', 'chat')]),
        ),
    ]
