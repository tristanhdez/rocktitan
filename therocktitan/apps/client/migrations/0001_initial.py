# Generated by Django 4.0.4 on 2022-05-13 20:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Alternative_Keystone',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Champion',
            fields=[
                ('id', models.PositiveSmallIntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Difficulty',
            fields=[
                ('id', models.PositiveSmallIntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.PositiveSmallIntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=60)),
            ],
        ),
        migrations.CreateModel(
            name='Keystone',
            fields=[
                ('id', models.PositiveSmallIntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Path',
            fields=[
                ('id', models.PositiveSmallIntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('description', models.TextField(default='description')),
            ],
        ),
        migrations.CreateModel(
            name='Skill_Max',
            fields=[
                ('id', models.PositiveSmallIntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Slot_Rune_One',
            fields=[
                ('id', models.PositiveSmallIntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Slot_Rune_Three',
            fields=[
                ('id', models.PositiveSmallIntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Slot_Rune_Two',
            fields=[
                ('id', models.PositiveSmallIntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Slot_Shard_One',
            fields=[
                ('id', models.PositiveSmallIntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Slot_Shard_Three',
            fields=[
                ('id', models.PositiveSmallIntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Slot_Shard_Two',
            fields=[
                ('id', models.PositiveSmallIntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Update',
            fields=[
                ('id', models.PositiveSmallIntegerField(primary_key=True, serialize=False)),
                ('date', models.DateField()),
                ('comments', models.CharField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='Rune',
            fields=[
                ('id', models.PositiveSmallIntegerField(primary_key=True, serialize=False)),
                ('notes', models.TextField(blank=True)),
                ('keystone', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='client.keystone')),
                ('path', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='client.path')),
                ('slot_rune_one', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='client.slot_rune_one')),
                ('slot_rune_three', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='client.slot_rune_three')),
                ('slot_rune_two', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='client.slot_rune_two')),
                ('slot_shard_one', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='client.slot_shard_one')),
                ('slot_shard_three', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='client.slot_shard_three')),
                ('slot_shard_two', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='client.slot_shard_two')),
            ],
        ),
        migrations.CreateModel(
            name='Matchup',
            fields=[
                ('id', models.PositiveSmallIntegerField(primary_key=True, serialize=False)),
                ('comments', models.TextField()),
                ('notes', models.TextField(blank=True)),
                ('alternative_keystone', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='client.alternative_keystone')),
                ('champions', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='client.champion')),
                ('difficulty', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='client.difficulty')),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='client.item')),
                ('rune', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='client.keystone')),
                ('skill_max', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='client.skill_max')),
                ('slot_rune_one', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='client.slot_rune_one')),
                ('slot_rune_three', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='client.slot_rune_three')),
                ('slot_rune_two', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='client.slot_rune_two')),
            ],
        ),
        migrations.AddField(
            model_name='alternative_keystone',
            name='alternative_keystone',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='client.keystone'),
        ),
    ]
