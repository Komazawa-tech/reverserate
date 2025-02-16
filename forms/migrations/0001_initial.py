# Generated by Django 5.1.2 on 2024-11-23 03:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BaseClass',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('credit', models.CharField(choices=[('A', 'A:履修即単位'), ('B', 'B:楽にとれる'), ('C', 'C:それなりに厳しい'), ('D', 'D:時間を返せ')], max_length=1, verbose_name='単位期待度')),
                ('score', models.CharField(choices=[('A', 'A:「S」が押し寄せる'), ('B', 'B:「A」は普通にとれる'), ('C', 'C:「B」がやっと'), ('D', 'D:「C」しかこない')], max_length=1, verbose_name='得点期待度')),
                ('homework', models.CharField(choices=[('A', 'A:手持ち無沙汰'), ('B', 'B:少しはある'), ('C', 'C:割と大変'), ('D', 'D:殺す気ですか')], max_length=1, verbose_name='課題量')),
                ('explanation', models.CharField(choices=[('A', 'A:分かりやすい'), ('B', 'B:まあ分かる'), ('C', 'C:分かりにくい'), ('D', 'D:理解不能')], max_length=1, verbose_name='説明')),
                ('passion', models.CharField(choices=[('A', 'A:あふれんばかり'), ('B', 'B:まあある'), ('C', 'C:ないとは言わない'), ('D', 'D:一切ない')], max_length=1, verbose_name='講義への熱意')),
                ('recommend', models.CharField(choices=[('A', 'A:是非取るべき'), ('B', 'B:取る価値あり'), ('C', 'C:取る価値なし'), ('D', 'D:取ると後悔する')], max_length=1, verbose_name='講義のオススメ度')),
                ('good_comment', models.TextField(max_length=400, verbose_name='良い点')),
                ('bad_comment', models.TextField(max_length=400, verbose_name='悪い点')),
                ('other_comment', models.TextField(blank=True, max_length=400, null=True, verbose_name='その他')),
            ],
        ),
    ]
