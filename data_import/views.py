import pandas as pd
from .models import Class, field, semester, day_of_week, period, code
from django.shortcuts import render
from .forms import ExcelUploadForm

def upload_excel(request):
    if request.method == 'POST' and request.FILES['excel_file']:
        excel_file = request.FILES['excel_file']
        
        # Excelファイルを読み込む
        df = pd.read_excel(excel_file)

        for _, row in df.iterrows():
            # クラス名と教師を取得
            class_instance = Class.objects.create(
                name=row['name'],
                teacher=row['teacher']
            )
            
            # フィールド（リスト形式）
            field_ids = map(int,str(row['field']).split(','))
            for field_id in field_ids:
                field_instance, created = field.objects.update_or_create(
                    field=field_id
                )

                class_instance.fields.add(field_instance)
            
            #semester（前期or後期）
            semester_ids = map(int,str(row['semester']).split(','))
            for semester_id in semester_ids:
                semester_instance, created = semester.objects.update_or_create(
                    semester=semester_id
                )

                class_instance.semester.add(semester_instance)

            # 曜日（リスト形式）
            day_of_week_ids = map(int,str(row['day_of_week']).split(','))
            for day_of_week_id in day_of_week_ids:
                day_of_week_instance, created = day_of_week.objects.update_or_create(
                    day_of_week=day_of_week_id
                )
                #class_instance.days_of_week.add(day_of_week_instance)
                class_instance.day_of_week.add(day_of_week_instance)

            # 時限（リスト形式）
            period_ids = map(int,str(row['period']).split(','))
            for period_id in period_ids:
                period_instance, created = period.objects.update_or_create(
                    period=period_id
                )

                class_instance.period.add(period_instance)

            # コード（整数）
            code_ids = map(int,str(row['code']).split(','))
            for code_id in code_ids:
                code_instance, created = code.objects.update_or_create(
                    code=code_id
                )

                class_instance.code.add(code_instance)

        return render(request, 'data_import/upload_success.html')

    return render(request, 'data_import/upload_excel.html', {'form': ExcelUploadForm()})
