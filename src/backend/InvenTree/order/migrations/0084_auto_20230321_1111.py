# Generated by Django 3.2.18 on 2023-03-21 11:11

from django.db import migrations, models

from order.status_codes import ReturnOrderStatus


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0083_returnorderextraline'),
    ]

    operations = [
        migrations.AddField(
            model_name='returnorder',
            name='target_date',
            field=models.DateField(blank=True, help_text='Expected date for order delivery. Order will be overdue after this date.', null=True, verbose_name='Target Date'),
        ),
        migrations.AlterField(
            model_name='purchaseorder',
            name='target_date',
            field=models.DateField(blank=True, help_text='Expected date for order delivery. Order will be overdue after this date.', null=True, verbose_name='Target Date'),
        ),
        migrations.AlterField(
            model_name='returnorder',
            name='status',
            field=models.PositiveIntegerField(
                choices=ReturnOrderStatus.items(),
                default=ReturnOrderStatus.PENDING.value,
                help_text='Return order status', verbose_name='Status'
            ),
        ),
        migrations.AlterField(
            model_name='salesorder',
            name='target_date',
            field=models.DateField(blank=True, help_text='Expected date for order delivery. Order will be overdue after this date.', null=True, verbose_name='Target Date'),
        ),
    ]
