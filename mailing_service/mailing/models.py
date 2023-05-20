from django.db import models



class Client(models.Model):
    phone_number = models.CharField(max_length=12, verbose_name='Номер телефона')
    operator_code = models.CharField(max_length=10, verbose_name='Код оператора')
    tag = models.CharField(max_length=100, verbose_name='Классификация')
    timezone = models.CharField(max_length=100, verbose_name='Часовой пояс')


class Mailing(models.Model):
    start_time = models.DateTimeField(verbose_name='Время старта')
    message_text = models.TextField(verbose_name='Текст сообщения')
    client_filter_operator_code = models.CharField(max_length=20, verbose_name='Код оператора')
    client_filter_tag = models.CharField(max_length=100, verbose_name='Классификация')
    end_time = models.DateTimeField(verbose_name='Дата окончания рассылки')


class Message(models.Model):
    creation_time = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=100)
    mailing = models.ForeignKey(Mailing, on_delete=models.CASCADE, related_name='messages')
    client = models.ForeignKey(Client, on_delete=models.CASCADE)