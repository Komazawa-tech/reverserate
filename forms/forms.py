from django import forms

class HelloForm(forms.Form):
    name = forms.CharField(label='name')
    mail = forms.CharField(label='mail')
    age  = forms.IntegerField(label='age')

class BaseClassForm(forms.Form):
    credit = forms.ChoiceField(
        choices=[
            ('','--- 選択してください ---'),
            ('A','A:履修即単位'),
            ('B','B:楽にとれる'),
            ('C','C:それなりに厳しい'),
            ('D','D:時間を返せ'),
        ],
        required=True,
        widget=forms.Select,
        label= '単位期待度'
    )

    score = forms.ChoiceField(
        choices=[
            ('','--- 選択してください ---'),
            ('A','A:「S」が押し寄せる'),
            ('B','B:「A」は普通にとれる'),
            ('C','C:「B」がやっと'),
            ('D','D:「C」しかこない'),
        ],
        required=True,
        widget=forms.Select,
        label='得点期待度'
    )

    
    homework = forms.ChoiceField(
        choices=[
            ('','--- 選択してください ---'),
            ('A','A:手持ち無沙汰'),
            ('B','B:少しはある'),
            ('C','C:割と大変'),
            ('D','D:殺す気ですか'),
        ],
        required=True,
        widget=forms.Select,
        label='課題量'
    )

    explanation = forms.ChoiceField(
        choices=[
            ('','--- 選択してください ---'),
            ('A','A:分かりやすい'),
            ('B','B:まあ分かる'),
            ('C','C:分かりにくい'),
            ('D','D:理解不能'),
        ],
        required=True,
        widget=forms.Select,
        label='説明'
    )

    passion = forms.ChoiceField(
        choices=[
            ('','--- 選択してください ---'),
            ('A','A:あふれんばかり'),
            ('B','B:まあある'),
            ('C','C:ないとは言わない'),
            ('D','D:一切ない'),
        ],
        required=True,
        widget=forms.Select,
        label='講義への熱意'
    )

    
    recommend = forms.ChoiceField(
        choices=[
            ('','--- 選択してください ---'),
            ('A','A:是非取るべき'),
            ('B','B:取る価値あり'),
            ('C','C:取る価値なし'),
            ('D','D:取ると後悔する'),
        ],
        required=True,
        widget=forms.Select,
        label= '講義のオススメ度'
        )
    
    GoodComment =forms.CharField(
        required= True,
        max_length=400,
        label='良い点',
        widget=forms.Textarea(
            attrs={
            'rows':5,
            'cols':60,
            'placeholder':'良かった点を記入してください 例:レジュメが見やすい、ユーモアたっぷり、質問しやすい、優しい、○○したい人はオススメなど'
            }
        )
    )
    
    BadComment =forms.CharField(
        required= True,
        max_length=400,
        label='悪い点',
        widget=forms.Textarea(
            attrs={
            'rows':5,
            'cols':60,
            'placeholder':'悪かった点を教えてください 例:予習が必要、試験がムズイ、説明が分かりにくい、毎回レポートあり、難しい、ハイブリッド（大噓）'
            }
        )
    )

    OtherComment =forms.CharField(
        required= False,
        max_length=400,
        label='その他',
        widget=forms.Textarea(
            attrs={
            'rows':5,
            'cols':60,
            'placeholder':'その他の意見や先生について教えてください 例:穴場授業、出席皆無、PC必須、教員がかっこいいorかわいい、先生の名言”インデントしない奴は死んだほうがいい”'
            }
        )
    )
    
class GroupCode (forms.Form):
    ClubCode = forms.CharField(
        required=False,
        max_length = 5,
        label = "組織コード"
    )


    
