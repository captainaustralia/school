# Kids Tech School website
## 15.08 upload, base structure + register.
## 16.08 register fix, + authentiticated, +logout
## 17.09 login/logout fix, auto auth

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

