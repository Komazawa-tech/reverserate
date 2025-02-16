from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic import TemplateView, ListView
from django.urls import reverse
from django.db.models import Q

from data_import .models import Class, Answer, field, semester, day_of_week, period, code, Group
from .forms import BaseClassForm

class IndexView(TemplateView):
    template_name = 'forms/class_index.html'

    def get(self, request, *args, **kwargs):
        # URLパラメータから class_name を取得
        class_name = request.GET.get('class_name', '')

        # class_name が指定されていれば、SearchResultView へリダイレクト
        if class_name:
            # 例: forms/result/?class_name=class_name にリダイレクト
            redirect_url = reverse('forms:searchresult') + f'?class_name={class_name}'
            return redirect(redirect_url)

        # class_name が無い場合は通常通りテンプレートを表示
        return super().get(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        return render(request, self.template_name)

class SearchResultView(ListView):
    template_name = 'forms/search_result.html'
    model = Class

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['group_id'] = self.kwargs.get('group_id')
        
        context['semester_choices'] = semester.SEMESTER_CHOICES
        context['selected_semesters'] = self.request.GET.getlist("class_semester")
        
        context['period_choices'] = period.PERIOD_CHOICES
        context['selected_period'] = self.request.GET.getlist("class_period")

        context['day_of_week_choices'] = day_of_week.DAY_OF_WEEK_CHOICES
        context['selected_day_of_week']  = self.request.GET.getlist("class_day_of_week")
        
        context['field_choices'] = field.FIELD_CHOICES
        context['selected_field'] = self.request.GET.getlist("class_field")

        
        return context
    

    def get_queryset(self):
        query_name = self.request.GET.get("class_name", "").strip()
        query_teacher = self.request.GET.get("class_teacher", "").strip()
        query_semester = self.request.GET.getlist("class_semester")
        query_period = self.request.GET.getlist("class_period")
        query_day_of_week = self.request.GET.getlist("class_day_of_week")
        query_field = self.request.GET.getlist("class_field")
        query_code = self.request.GET.getlist("class_code")
        
        filters = Q()
        
        if query_name:
            filters &= Q(name__icontains=query_name)
        
        if query_teacher:
            filters &= Q(teacher__icontains=query_teacher)
        
        if query_semester:
            query_semester = [int(s) for s in query_semester ]
            filters &= Q(semester__semester__in=query_semester)
        
        if query_period:
            query_period = [int(s) for s in query_period ]
            filters &= Q(period__period__in = query_period)
        
        if query_day_of_week:
            query_day_of_week = [int(s) for s in query_day_of_week]
            filters &= Q(day_of_week__day_of_week__in = query_day_of_week)

        if query_field:
            query_field = [int(s) for s in query_field]
            filters &= Q(field__field__in = query_field)
        
        if query_code:
            try:
                query_code = [int(s) for s in query_code if s.strip().isdigit()]
                if query_code:
                    filters &=Q(code__code__in = query_code)
            except ValueError:
                pass
        


        return Class.objects.filter(filters) if filters else Class.objects.filter(field__isnull=True)


    
    

class ClassDetailView(TemplateView):
    template_name = "forms/class_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        class_id = self.kwargs.get('id')

        class_instance= get_object_or_404(Class, id=class_id)

        field_ids = class_instance.field.values_list('field', flat=True)
        field_dict = dict(field.FIELD_CHOICES)
        field_names= [field_dict.get(f,"None") for f in field_ids]

        day_of_week_ids = class_instance.day_of_week.values_list('day_of_week', flat=True)
        day_of_week_dict = dict(day_of_week.DAY_OF_WEEK_CHOICES)
        day_of_week_names = [day_of_week_dict.get(f,"None") for f in day_of_week_ids]

        context = {
            'name' : class_instance.name,
            'teacher': class_instance.teacher,
            'field':field_names,
            'day_of_week':day_of_week_names,
        }

        context['form'] = BaseClassForm()

        return context

    def post(self, request, *args, **kwargs):
        form = BaseClassForm(request.POST)
        class_id = self.kwargs.get('id')
        group_id = self.kwargs.get('group_id')
        class_instance = get_object_or_404(Class, id=class_id)
        group_instance = get_object_or_404(Group, id = group_id)

        if form.is_valid():
            Answer.objects.create(
                Class=class_instance,
                group=group_instance,
                credit=form.cleaned_data['credit'],
                score=form.cleaned_data['score'],
                homework=form.cleaned_data['homework'],
                explanation=form.cleaned_data['explanation'],
                passion=form.cleaned_data['passion'],
                recommend=form.cleaned_data['recommend'],
                GoodComment=form.cleaned_data['GoodComment'],
                BadComment=form.cleaned_data['BadComment'],
                OtherComment=form.cleaned_data.get('OtherComment', '')
            )
            return redirect('forms:searchresult')  # テスト用ページにリダイレクト

        # フォームにエラーがある場合、エラー情報を含めてレンダリング
        context = {'class': class_instance, 'form': form}
        return self.render_to_response(context)



        