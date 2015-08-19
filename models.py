from django.db import models

class Ban(models.Model):
    ban_id = models.AutoField(primary_key=True)
    server_id = models.ForeignKey(Server)
    ban_ip = models.CharField(max_length=255)
    ban_name = models.CharField(max_length=2048)
    ban_uid = models.CharField(max_length=255)
    ban_timestamp = models.IntegerField() # timestamp?
    ban_length = models.IntegerField() # ban length in seconds?
    ban_invoker_client_id = models.ForeignKey(Client)
    ban_invoker_uid = models.CharField(max_length=40)
    ban_invoker_name = models.CharField(max_length=255)
    ban_reason = models.CharField(max_length=255)
    ban_enforcements = models.IntegerField()
    ban_hash = models.CharField(max_length=255)

class Binding(models.Model):
    binding_id = models.AutoField(primary_key=True)
    ip = models.CharField(max_length=20)
    type = models.IntegerField()

class ChannelProperty(models.Model):
    server_id = models.ForeignKey(Server)
    ident = models.CharField(max_length=100)
    value = models.CharField(max_length=255)

    class Meta:
        db_table = 'channel_properties'

class ChannelPermission(models.Model):
    server_id = models.ForeignKey(Server)
    id1 = models.IntegerField()

class Channel(models.Model):
    channel_id = models.AutoField(primary_key=True)
    channel_parent_id = models.ForeignKey(Channel)
    server_id = models.ForeignKey(Server)

class ClientProperty(models.Model):
    server_id = models.ForeignKey(Server)
    id = models.ForeignKey(Client)
    ident = models.CharField(max_length=100)
    value = models.CharField(max_length=255)

    class Meta:
        db_table = 'client_properties'

class Client(models.Model):
    client_id = models.AutoField(primary_key=True)
    server_id = models.ForeignKey(Server)
    client_unique_id = models.CharField(max_length=40)
    client_nickname = models.CharField(max_length=100)
    client_login_name = models.CharField(max_length=20)
    client_login_password = models.CharField(max_length=40)
    client_lastconnected = models.IntegerField() # timestamp?
    client_totalconnections = models.IntegerField()
    client_month_upload = models.IntegerField()
    client_month_download = models.IntegerField()
    client_total_download = models.IntegerField()
    client_total_download = models.IntegerField()
    client_lastip = models.CharField(max_length=20)

class Complain(models.Model):
    server_id = models.ForeignKey(Server)
    complain_from_client_id = models.ForeignKey(Client)
    complain_to_client_id = models.ForeignKey(Client)
    complain_message = models.CharField(max_length=255)
    complain_timestamp = models.IntegerField() # timestamp?
    complain_hash = models.CharField(max_length=255)

class Message(models.Model):
    message_id = models.AutoField(primary_key=True)
    server_id = models.ForeignKey(Server)
    message_from_client_id = models.ForeignKey(Client)
    message_from_client_uid = models.CharField(max_length=40)
    message_to_client_id = models.ForeignKey(Client)
    message_subject = models.CharField(max_length=255)
    message_msg = models.TextField()
    message_timestamp = models.PositiveIntegerField() # timestamp?
    message_flag_read = models.BooleanField() # integer? bool?
class ServerProperty(models.Model):
    server_id = models.ForeignKey(Server)
    id = models.ForeignKey(Server)
    ident = models.CharField(max_length=100)
    value = models.CharField(max_length=255)

class Server(models.Model):
    server_id = models.AutoField(primary_key=True)
    server_port = models.IntegerField()
    server_autostart = models.IntegerField()
    server_machine_id = models.CharField(max_length=50)
    server_month_upload = models.IntegerField()
    server_month_download = models.IntegerField()
    server_total_upload = models.IntegerField()
    server_total_download = models.IntegerField()

class Token(models.Model):
    server_id = models.ForeignKey(Server)
    token_key = models.CharField(max_length=50)
    token_type = models.IntegerField()
    token_id1 = models.PositiveIntegerField()
    token_id2 = models.PositiveIntegerField()
    token_created = models.IntegerField() # timestamp?
    token_description = models.CharField(max_length=255)
    token_customset = models.TextField()
    token_from_client_id = models.ForeignKey(Client)
