# Kids Tech School website
## 15.08 upload, base structure + register.
## 16.08 register fix, + authentiticated, +logout
## 17.08 login/logout fix, auto auth
## 18.08 lk for auth user with his main info
## 20.08 merge branch test -> master. Up: fix permission for CRM,info about students, profile lk /edit profile
## 21.09 update templates, something fix

# Django Functions:
## Registration:

###models.py
Пишем модель нашего объекта(Студента), наследуемся от User, у которого
уже есть некоторые нужные нам встроенные поля last_name,first_name,email,
username. Добавляем новые поля, которые отсутствуют в родительской моделе,
переопределим маг.метод __str__(без особой цели), далее в мета классе определим
как объект будет именован в ед. и мн. числе

    class Student(User):
        age = models.IntegerField(null=False)
        payment = models.BooleanField(default=False)

    def __str__(self):
        return self.username + self.last_name

    class Meta:
        verbose_name = 'Ученик'
        verbose_name_plural = 'Ученики'

###forms.py
Делаем форму для регистрации нашего объекта(студента), для этого наследуемся
от встроенного класса ModelForm, так как пароли не присутствуют в атрибутах
класса, и мы перед сохранением, будем проверять их на идентичность, создаем 2
переменных.
  Создаем мета класс, указывая model = Student, и поля которые необходимы для 
заполнения.
  Описываем функцию, которая будет проверять правильность ввода пароля,
если form.is_valid() имеет значение True. form.cleaned_data - это место, 
где хранятся все проверенные поля. 
Все поля хранятся в переменной data, в которой мы проведем проверку pas_1==pas_2,
если это не так вызывается исключение. Иначе возвращается пароль

![image](https://user-images.githubusercontent.com/61281668/129646140-fa3b3553-aac6-4010-ae8f-de72bd204116.png)

    class StudentRegistrationForm(ModelForm):
        password_1 = CharField(max_length=20, min_length=6, widget=PasswordInput)  # Создаем поле ввода пароля
        password_2 = CharField(max_length=20, min_length=6, widget=PasswordInput)  # Повторное поле пароля

    class Meta:
        model = Student
        fields = ('username', 'first_name', 'last_name', 'email', 'age')

    def check_pass(self):
        data = self.cleaned_data
        if data['password_1'] != data['password_2']:
            raise ValidationError('Неверный повтор пароля')
        return data['password_1']


###views.py
Описываем вьюху для регистрации, она должна принимать request, который мы должны проверить,
POST или GET запрос пришел. В случае, если пришел запрос POST, мы указываем, что форма, которую
необходимо будет сгенерировать на странице является формой, которую мы описали в forms.py,
далее проводим проверку на валидность данных, и если все ОК, то мы создаем переменную, в которой
используем методм .save(commit=False)(где commit=False - означает, что джанго не будет сразу
сохранять эти данные в бд, это сделано для того, чтобы мы могли сохранить в моделе пароль, который
был проверен функцией. Далее модель сохраняется, возвращается рендер(запрос,страница перехода,словарь с
шаблонным именем, которому соответствует значение, которое можно использовать в HTML({{user_form.as_p}})

        def register(request):
            if request.method == 'POST':
                user_form = StudentRegistrationForm(request.POST)
                if user_form.is_valid():
                    new_user = user_form.save(commit=False)
                    new_user.set_password(user_form.cleaned_data['password_1'])
                    new_user.save()
                    return render(request, 'lk.html', {'new_user': new_user})
            else:
                user_form = UserRegistrationForm()12
            return render(request, 'register.html', {'user_form': user_form})


## Login ( default django form , django.contrib.auth.views LoginView)/ Logout

Создание дефолтной формы логина + crispy_form.
Используется дефолтная форма джанго, поэтому дополнительной формы не требуется

    ### urls.py


    from django.contrib.auth.views import LoginView
    from django.urls import path, include


    urlpatterns = [
        ...
        path('login/', LoginView.as_view(), name='login'),
        ...
    ]

В urls.py используем готовую вьюху

### template_login.html

        {% extends  'base.html' %}
        {% load crispy_forms_filters %}
        {% load crispy_forms_tags %}

        {% block main %}
            <div class="card">
                <div class="card-body">
                    <h4 class="card-title">Log in to your account</h4>

                    <form method="post">
                        {% csrf_token %}
                        {{ form|crispy }}
                        <button type="submit" class="btn btn-primary btn-block">Log in</button>
                    </form>
                </div>
            </div>
        {% endblock %}

Наследуем базовый шаблон, используем crispy_forms для дефолтного отображение с бутстрэпа
(!) Дефолтное расположение html , template/registration/login.html, либо явно прописываем его в urls.py

![image](https://user-images.githubusercontent.com/61281668/129646586-d4c7fb1f-4c20-4aee-ba8a-ad2d97d48c2a.png)/

    path('login/', LoginView.as_view(template_name='name.html'), name='login')

Для логаута хватает обычной вьюхи, с использованием встроенной функции

    def logout_from(request):
        print('Вышел')
        logout(request)
        return render(request, 'index.html')
Вьюху прописываем в юрл

### urls.py

    path('logout/', logout_from, name='logout')

Её можно забиндить на кнопку или ссылку, например так:

### lk.html
    <a href="{% url 'logout' %}">logout</a>

## Info about auth users
Способ для вытягивания информации об авторизованном пользователе
возможно не самый лучший способ, но первое, что пришло в голову
(может быть стоило использовать list_view)


В прошлой функции, которая рендерит в личный кабинет, внесены некоторые
поправки:
### Views
    def lk(request):
    a = request.user.username
    users = Student.objects.all()
    subs = TypeSubscribe.objects.all()
    if request.user.is_authenticated:
        active = Student.objects.filter(username=a)
        active_1 = active.get()
        context = {'users': users, 'subs': subs, 'active': active_1}
        return render(request, 'lk.html', context)
    else:
        return render(request, 'index.html')

Т.к по реквесту можно получить юзернейм пользователя, получаем его
и сохраняем в переменную, затем берем всех пользователей, которые
содержатся в моделе(студента) и тащим все данные из нее в query_set,
после проверяем, авторизован ли пользователь, если это так, 
то фильтруем всех студентов по юзернейму(получаем целевого пользователя)
сохраняем его и получаем из него все основные данные. Далее пихаем его 
в контекст, чтобы использовать в темплейте личного кабинета, для вывода
данных пользователя. Если же никто не авторизован, рендер не происходит,
в дальнейшем добавлю темплейт ошибки

### lk.html

    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>{{ active.first_name }}</title>
    </head>
    <body>
    <h1> IT'S LK</h1>
    <a href="{% url 'logout' %}">logout</a>
        <p>Name - {{ active.first_name }}</p>
        <P>Last name - {{ active.last_name }}</P>
        <p>Age - {{ active.age }}</p>
        <p>Balance - {{ active.balance }}</p>
        <p>Payment - {{ active.payment }}</p>
        <p>E-mail - {{ active.email }}</p>
        <p>Type of subs - {{ active.subs }}</p>
    </body>
    </html>

Тут особых пояснений не нужно, тащим данные из активного пользователя
с контекста, пока что выглядит вот так:

   ![image](https://user-images.githubusercontent.com/61281668/129892094-46594632-59cf-4dd9-b76c-e89df1c4caa0.png)


## 20.08 fix fun

    def to_crm(request):
    users = Student.objects.all()
    subs = TypeSubscribe.objects.all()
    context = {'users': users, 'subs': subs}
    if request.user.is_superuser:
        return render(request, 'CRM/CRM.html', context)
    else:
        return render(request, 'index.html')

Переход только в случае, если пользователь - суперюзер


## CRM ListView/DetailView

    class StudentList(ListView):
        model = Student
        context_object_name = 'StudentList'
        template_name = 'CRM/student_list.html'


    class StudentDetail(DetailView):
        model = Student
        context_object_name = 'students'
        template_name = 'CRM/student_detail.html'

Избавляет от лишней возни с получением всей информации с объектов и тд,
наследуемся от класса ListView, определяем модель, доступ к информации которой
нам будет необходим. Определяем контекст для темплейта, и имя темплейта, далее
будут темплейты.

DetailView, почти аналогично, только необходимо учесть, что в юрл, нужно передавать
pk какого-то конкретного объекта, чтобы можно было взглянуть на конкретно его данные,
что логично

## Куски темплейтов, для list/detail

    <body>
    {% for i in StudentList %}
        <p>Фамилия - {{ i.last_name}} {{ i.first_name }} - {{ i.age }} - {{ i.email }} - {{ i.balance }} - {{ i.subs }} - {{ i.last_login }}
        - {{ i.payment}}</p>
    {% endfor %}
    </body>

    <body>
        <P>Фамилия - {{ students.last_name }}</P>
        <P>Имя - {{ students.first_name }}</P>
        <P>Возраст - {{ students.age }}</P>
        <P>Оплата - {{ students.payment }}</P>
        <P>Подписка - {{ students.subs }}</P>
        <P>Баланс - {{ students.balance }}</P>
    </body>

Cоответственно лист перебираем, детейл обращаемся к конкретным атрибутам,
конкретного объекта

##urls.py (CRM)

    urlpatterns = [
    path('<int:pk>/', StudentDetail.as_view(), name='CRM'),
    path('students/', StudentList.as_view(), name='std_list'),
        ]


## Update lk, profile

    class UpdateProfile(UpdateView):
    model = Student
    fields = ['last_name', 'first_name', 'age', 'email']
    template_name = 'LK/edit_profile.html'
    success_url = 'success'


    def success_page(request):
        return render(request, 'LK/update_done.html')

Используется также дефолтная вью, передаем:модель,поля,темплейт и рендер перехода если все удачно.


