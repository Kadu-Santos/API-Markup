# 🔰API MARKUP - API REST DJANGO

 1. [DESCRIÇÃO](#desc)
 2. [FERRAMENTAS](#fer)
 3. [TECNOLOGIAS](#tec)
 4. [PREPARANDO AMBIENTE](#ppa)
 5. [IMPLEMENTAÇÃO](#imp)
 6. [DEPLOY](#dp)
 7. [COMO USAR / END POINTS](#run)
 8. [LICENÇA DO PROJETO](LICENSE)
 ****

<div id='desc'></div>

## 📃Descrição do projeto

<p>A API em questão é uma solução simples para aplicações que desejam armazenar e gerenciar questões de múltipla escolha e puzzles com palavras bagunçadas. Ela oferece suporte a um conjunto de comandos HTTP que incluem GET, PUT, UPDATE e DELETE, permitindo que os usuários interajam com a API de maneira flexível e eficiente. Além de permitir o armazenamento de perguntas, alternativas e respostas com seus respectivos níveis de dificuldade. Isso possibilita a criação de aplicações, que podem ser adaptadas para atender às necessidades de diferentes públicos. Por fim, instalar o Insomnia para testar a API.</p>


<div id='fer'></div>

## 🔧Ferramentas

<p>Para iniciar o desenvolvimento da API, serão necessárias algumas ferramentas essenciais. Primeiramente, será preciso de um editor de código, como Visual Studio Code. Em seguida, será preciso instalar o Python, que é a linguagem de programação na qual a API será desenvolvida.</p>

#### Visual Studio Code v1.76

<ul>
    <li>Acesse o site oficial do Visual Studio Code em https://code.visualstudio.com/.</li>
    <li>Clique no botão "Download" na página inicial.</li>
    <li>Escolha o download apropriado para o seu sistema operacional (Windows, Mac ou Linux).</li>
    <li>Após o download, execute o arquivo de instalação e siga as instruções na tela.</li>
</ul>

#### Python 3

<ul>
    <li>Acesse o site oficial do Python em https://www.python.org/.</li>
    <li>Clique no botão "Downloads" na página inicial.</li>
    <li>Escolha o download apropriado para o seu sistema operacional (Windows, Mac ou Linux).</li>
    <li>Inicie o instalador do Python e siga as instruções na tela.</li>
    <li>Marque a opção "Add Python to PATH" para adicionar o Python ao PATH do sistema operacional, permitindo que ele seja acessado globalmente.</li>
    <li>Conclua a instalação e abra o terminal ou prompt de comando para verificar se o Python foi instalado corretamente, digitando "python --version".</li>
</ul>

#### Insomnia 2023.1

<ul>
    <li>Acesse o site oficial do Insomnia em https://insomnia.rest/.</li>
    <li>Clique no botão "Download" na página inicial.</li>
    <li>Escolha o download apropriado para o seu sistema operacional (Windows, Mac ou Linux).</li>
    <li>Após o download, execute o arquivo de instalação e siga as instruções na tela.</li>
</ul>

<div id='tec'></div>

## 📐Tecnologias

<p>No desenvolvimento dessa API foram utilizadas as seguintes tecnologias: </p>
<ul>
    <li>Framework API REST 3.14</li>
    <li>Django Frameork 4.1.7</li>
    <li><a href='https://github.com/'>Github</a></li>
    <li><a href='https://www.pythonanywhere.com/'>Pythonanywhere</a></li>
</ul>

<div id='ppa'></div>

## 💻Preparando Ambiente

<p>Para preparar o ambiente de desenvolvimento com o Visual Studio Code e instalar todas as dependencias do projeto, siga os passos abaixo:</p>
<ol>
    <li>Crie uma nova pasta para o projeto.</li>
    <li>Abra a pasta no Visual Studio Code.</li>
    <li>Instale as extenções Django e Python no Visual Code
        <ol>
            <li>Clique no ícone de extensões na barra lateral esquerda.</li>
            <li>Na barra de pesquisa, digite "Python" e selecione a extensão "Python" da Microsoft.</li>
            <li>Clique em "Install".</li>
            <li>Na barra de pesquisa, digite "Django" e selecione a extensão "Django" de Baptiste Darthenay.</li>
            <li>Clique em "Install".</li>
        </ol>
    </li>
    <li>Abra o terminal do Visual Studio Code clicando em 'Terminal' na parte superir da tela, 'Novo Terminal'.</li>
    <li>No terminal, digite o comando <code>python -m venv venv</code> para criar o ambiente virtual onde será instalado as dependencias do proheto.</li>
    <li>Em seguida, digite o comando <code>./venv/Scripts/Activate.ps1</code> para ativar o ambiente virtual (pode variar de acordo o sistema operacional).</li>
    <li>Após isso, deigite e comando <code>pip install django</code> para instalar o Django.</li>
    <li>Instale também o rest frameork com o comando <code>pip install djangorestframework</code>.</li>
    <li>Crie um projeto django com o comando <code>django-admin startproject nome_projeto . </code> Nessa implementação, chamarei de <code>config</code></li>
    <li>Digite <code>python manage.py migrate</code> no terminal para gravar informaçoes que o django cria altomaticamente para um bom funcionamento da aplicação.</li>
    <li>Por fim, com o projeto já criado, entre na pasta com o nome do projeto, procure por <code>settings.py</code> e o abra. Dentro desse arquivo:
        <ol>
            <li>Escreva <code>import os</code> logo abaixo de <code>from pathlib import Path</code></li>
            <li>Defina <code>ALLOWED_HOSTS</code> para <code>ALLOWED_HOSTS = ['*']</code></li>
            <li>Em <code>INSTALLED_APPS</code> adicione ao fim <code>'rest_framework',</code></li>
            <li>Em <code>LANGUAGE_CODE</code> defina <code>LANGUAGE_CODE = 'pt-br'</code></li>
            <li>Em seguida, defina <code>TIME_ZONE</code> para <code>TIME_ZONE = 'America/Sao_Paulo'</code></li>
            <li>Abaixo de <code>STATIC_URL = 'static/'</code> escreva <code>
STATIC_ROOT = os.path.join(BASE_DIR, 'static')</code></li>
        </ol>
     </li>
</ol>
<p>Após esses passos, o ambiente está pronto para iniciar o desenvolvimento, inclusive com cofigurações que facilitarão o deploy do projeto. Caso todos os paços tenha sido seguidos corretamente, você terá uma tela parecida com essa abaixo:</p>

<br>

<p align="center">
    <img src="imgs_tut\tela_de_referencia.png" width="550px" style="margin: auto;">
</p>

<br>

<div id='imp'></div>

## ⌨️Implementando projeto

<p>Para iniciar a implementaçõa, digite <code>python manage.py startapp nome_app</code> no terminal para criar uma nova aplicação dentro do django. Nessa implementação a aplicação está nomeada como <code>API</code>. Após criar o app, entre na pasta do projeto django (config), e abra o arquivo <code>settings.py</code> Dentro desse, procure por <code>INSTALLED_APPS</code> adicione ao fim o nome da aplicação que escolheu. <code>'API',</code></p>

<br>

<p align="center">
    <img src="imgs_tut\arvore_arquivos.png" width="270px" style="margin: auto;">
    <img src="imgs_tut\code_example.png" width="350px" style="margin: auto;">
</p>

<br>

#### 📌 Models

___

<p>Com a aplicação criada, entre na sua respectiva pasta, e edite o arquivo <code>models.py</code> Dentro desse aquivo serão definido as classes que representarão as tabelas no banco de dados. Ou seja, quando você cria um modelo, está criando uma classe Python que representa uma tabela no banco de dados. Cada atributo da classe representa uma coluna na tabela.</p> 

<p>Nesse projeto serão criadas duas tabelas, uma para questões de multipla escolha e putra para um puzzle, que conterá um enunciado, uma palavra, frase ou coamando com os termos fora de ordem, e uma resposta.</p> 

<p>Logo abaixo temos a definição da primeira classe "Pergunta", nela são definidos os campos: nivel, enunciado, alternativas A, B, C, e D, e a resposta. Temos também um metodo que será reponsável por retornar a pergunta da questão como uma representação em string da instância do modelo.</p>

<br>

```
 class Pergunta(models.Model):
        perguntaNivel = models.IntegerField()
        pergunta = models.CharField(max_length = 250)
        alternativa_a = models.CharField(max_length = 250)
        alternativa_b = models.CharField(max_length = 250)
        alternativa_c = models.CharField(max_length = 250)
        alternativa_d = models.CharField(max_length = 250)
        respost'a = models.CharField(max_length = 250)

    def __str__(self):
        return self.pergunta
```
<br>

<p>Aqui é definido a classe "Puzzle" com campos para definir: nivel, enunciado, uma palavra, frase ou coamando com os termos fora de ordem, e  resposta.</p>

<br>

```
    class Puzzle(models.Model):
        puzzleNivel = models.IntegerField()
        puzzleEnunciado = models.CharField(max_length = 250)
        puzzleComand = models.CharField(max_length = 250)
        puzzleResposta = models.CharField(max_length = 250)

        def __str__(self):
            return self.puzzleEnunciado
```

<br>

<p>Para que os modelos(tabelas) sejam adicionados ao banco de dados, digite o <code>python manage.py makemigrations nome_app</code> no terminal. Logo em seguida, digite <code>python manage.py migrate nome_app</code> Com isso as tebelas serão criadas no banco.</p>

<br>

<p align="center">
    <img src="imgs_tut\terminal_migrate.png" width="700px" style="margin: auto;">
</p>

<br>

#### 📌 Serializer

___

<p>Ainda dentro da pasta da aplicação, crie um arquivo chamado <code>serializer.py</code>. O Serializer usado para converter objetos, como as models do Django, e outras estruturas de dados, em tipos de dados nativos que possam ser facilmente renderizados em JSON, XML ou outros formatos de conteúdo.</p>

<p>No cabeçalho do arquivo será importado o "serializers" do "rest framework", classe reponsável por realizar a serialização dos models. Também serão importados os models "Pergunta" e "Puzzle" da aplicação.</p>

<br>

```
    from rest_framework import serializers
    from API.models import Pergunta, Puzzle
```

<br>

<p>Esse código é a definição de dois Serializers usando a biblioteca Rest_Framework do Django. Eles servem para transformar os dados de objetos "Pergunta" e "Puzzle" em um formato que pode ser transmitido pela internet (geralmente em formato JSON).</p>

<p>A classe "Meta" dentro de cada Serializer especifica qual modelo de banco de dados deve ser usado e quais campos devem ser incluídos na serialização (com o atributo "fields" definido como "all", significa que todos os campos do modelo serão incluídos).</p>

<br>

```
    class PerguntaSerializer(serializers.ModelSerializer):
        class Meta:
            model = Pergunta
            fields = '__all__'

    class PuzzleSerializer(serializers.ModelSerializer):
        class Meta:
            model = Puzzle
            fields = '__all__'
```

<br>

#### 📌 Views

___

<p>Ainda dentro da pasta da aplicação, abra o arquivo <code>views.py</code></p>

<p>As seguintes impotações são feitas para utilizar os "modelos" e as "classes serializadoras" criadas anteriormente. Também será importado o "viewsets", classe do Rest_Framework que permite gerenciar as operações de leitura, criação, atualização e exclusão de instâncias desses modelos na API.</p>

<br>

```
    from rest_framework import viewsets
    from API.models import Pergunta, Puzzle
    from API.serializer  import PerguntaSerializer, PuzzleSerializer
```

<br>

<p>No código abaico, definimos uma classe <code>PerguntaViewsetsque</code> herda de <code>viewsets.ModelViewSet</code> e definimos duas variáveis ​​de classe, <code>queryset</code> e <code>serializer_class</code>. Uma variável <code>queryset</code> define quais instâncias do modelo <code>Pergunta</code> serão usadas no <code>viewset</code>, enquanto uma variável <code>serializer_class</code> define qual classe serializadora será usada.</p>

<br>

```
    class PerguntaViewsets(viewsets.ModelViewSet):
        queryset = Pergunta.objects.all()
        serializer_class = PerguntaSerializer

    class PuzzleViewsets(viewsets.ModelViewSet):
        queryset = Puzzle.objects.all()
        serializer_class = PuzzleSerializer
```

<br>

<p>Com essas duas classes criadas, podemos usar as rotas padrão do Rest_Framework para acessar as instâncias do modelo Perguntae Puzzlena API, usando os métodos HTTP padrão como GET, POST, PUT e DELETE.</p>

<br>

#### 📌 Admin

___

<p>A área administrativa do Django é uma interface de administração gerada automaticamente que permite gerenciar os dados do banco de dados. Com ela, é possível adicionar, editar e excluir instâncias de modelos, além de executar outras tarefas administrativas, como gerenciar usuários e grupos.</p>
<p>Com isso em mente, abra o arquivo <code>admin.py</code> dentro da pasta da aplicação. Será adicionado as classes que foram criadas anteriormente, afim de que essas sejam exibidas na "área administrativa".</p>
<p>Importe as classes:</p>

<br>

```
    from django.contrib import admin
    from API.models import Pergunta, Puzzle
```

<br>

<p>A classe <code>Questao</code> herda da classe <code>admin.ModelAdmin</code> e define as configurações de exibição para o modelo <code>Pergunta</code>. O atributo <code>list_display</code> determina quais campos serão exibidos na lista de exibição do modelo, enquanto <code>list_display_links</code> define quais campos serão clicáveis para editar um objeto. Já <code>search_fields</code> especifica quais campos serão usados na busca de objetos.</p>

<br>

```
    class Questao(admin.ModelAdmin):
        list_display = ('id', 'perguntaNivel', 'pergunta', 'alternativa_a', 'alternativa_b', 'alternativa_c', 'alternativa_d', 'resposta')
        list_display_links = ('id', 'perguntaNivel', 'pergunta', 'alternativa_a', 'alternativa_b', 'alternativa_c', 'alternativa_d', 'resposta')
        search_fields = ('pergunta', 'perguntaNivel')
```

<br>

<p>De forma semelhante, a classe "GamePuzzle" define as configurações de exibição para o modelo "Puzzle".</p>

<br>

```
    class Questao(admin.ModelAdmin):
        list_display = ('id', 'perguntaNivel', 'pergunta', 'alternativa_a', 'alternativa_b', 'alternativa_c', 'alternativa_d', 'resposta')
        list_display_links = ('id', 'perguntaNivel', 'pergunta', 'alternativa_a', 'alternativa_b', 'alternativa_c', 'alternativa_d', 'resposta')
        search_fields = ('pergunta', 'perguntaNivel')
```

<br>

<p>Por fim, as funções <code>admin.site.register(Pergunta, Questao)</code> e <code>admin.site.register(Puzzle, GamePuzzle)</code> registram as classes <code>Questao</code> e <code>GamePuzzle</code> como responsáveis por exibir os modelos <code>Pergunta</code> e <code>Puzzle</code>, respectivamente, na área administrativa do Django.</p>

<br>

```
    admin.site.register(Pergunta, Questao)
    admin.site.register(Puzzle, GamePuzzle)
```

<br>

#### 📌 Urls

___

<p>Para finalizar a implementação, abra a pasta do projeto Django (definido anteriormente como <code>config</code>) e abra o arquivo chamdado <code>urls.py</code></p>
<p>Faça as seguintes impotações:</p>

<br>

```
    from django.contrib import admin
    from django.urls import path, include
    from rest_framework import routers
    from API.views import PerguntaViewsets, PuzzleViewsets
```

<br>

<p>No código abaixo será definindo as rotas (URLs) da API, utilizando a biblioteca <code>DefaultRouter</code> do Rest Framework. Primeiro, é criada uma instância do <code>DefaultRouter</code>. Em seguida, duas rotas são registradas utilizando o método <code>register</code>. As rotas são definidas para as viewssets <code>PerguntaViewsets</code> e <code>PuzzleViewsets</code>, que gerenciam as operações CRUD para os modelos <code>Pergunta</code> e <code>Puzzle</code>, respectivamente.</p>

<p>A seguir, o <code>urlpatterns</code> é definido para incluir a URL de administração padrão do Django e as rotas criadas pelo <code>DefaultRouter</code>. Qualquer solicitação de URL com a rota <code>pergunta</code> ou <code>puzzle</code> será roteada para um viewset correspondente, que gerenciará a solicitação e retornará uma resposta adequada.</p>

<br>

```
    router = routers.DefaultRouter()
    router.register(r'perguntas', PerguntaViewsets)
    router.register(r'puzzles', PuzzleViewsets)

    urlpatterns = [
        path('admin/', admin.site.urls),
        path('', include(router.urls)),
    ]
```

<br>

<p>📜 Após realizar os passos acima, vá ao terminal e digite <code>pip freeze > dependences.txt</code> Com isso será criado um arquivo de texto que conterá todas as dependencias do projeto. Esse arquivo será usado para instalar todas as dependecias do projeto no local onde será hospedado.</p>

<p>E assim finaliza a implementação da API, para ver seu funcionamento, basta digitar no terminal <code>python manage.py runserver</code></p>

<br>

<p align="center">
    <img src="imgs_tut\terminal_runserver.png" width="700px" style="margin: auto;">
</p>

<br>

<p>Abra o link gerado no terminal em seu navegador:</p>

<br>

<p align="center">
    <img src="imgs_tut\api_page.png" width="550px" style="margin: auto;">
</p>

<br>

<p>Nessa página será possivel realizar operações de GET, POST, PUT e DELETE. Nos tópico <a href="#run"> COMO USAR / END POINTS</a> será abordado com mais detalhes a utilização da API.</p>


<br>

<div id='dp'></div>

## 📟Deploy com Pythonanywhere

<p>Existem diversas plataformas gratuitas para hospedar uma aplicação django, no entanto, nesse tutorial será usado a plataforma Pythonanywhere. Para iniciar o processo de deploy, acesse <a href="https://www.pythonanywhere.com">https://www.pythonanywhere.com</a>, crie uma conta e confirme seu e-mail.</p>
<p>Após criar a conta, você terá a visão dessa tela abaixo:</p>

<br>

<p align="center">
    <img src="imgs_tut\home_pythonanywhere.png" width="550px" style="margin: auto;">
</p>

<br>

<p>Para realizar o upload do seu projeto na plataforma Pythonanywhere, é necessário que você possua uma conta no Github e um repositório com os arquivos do projeto. Caso ainda não possua esses requisitos, você pode criar uma conta no Github e criar um repositório com os arquivos do seu projeto.</p>

<p> Após ter sua conta no Github e um repositório com o projeto, acesse a página inicial da Pythonanywhere e clique no botão <code>$ Bash</code> em "new console". Isso abrirá uma nova página com um terminal.</p>

<br>

<p align="center">
    <img src="imgs_tut\terminal_pythonanywhere.png" width="550px" style="margin: auto;">
</p>

<br>

<p>Dentro do console, clone o seu projeto utilizando o comando <code>git clone "link_repositório"</code>. Com isso, os dados do seu projeto estarão hospedados na Pythonanywhere.</p>

<p>A seguir, é necessário criar um ambiente virtual dentro da plataforma. Para isso, utilize o comando: <code>python -m venv nome_ambiente</code></p>

<p>Após criar o ambiente virtual, é preciso ativá-lo utilizando o comando <code>source nome_ambiente/bin/activate</code>.</p>

<p>Em seguida, acesse a pasta do projeto que você clonou anteriormente utilizando o comando <code>cd nome_repositorio</code>. Utilize o comando <code>ls</code> para visualizar todos os arquivos da pasta.</p>

<p>Então, digite: <code>pip install -r dependences.txt</code> para instalar todas as dependencias do projeto.</p>

<p>Crie uma pasta pasta para armazenar os arquivos estáticos com o comando <code>mkdir static</code></p>

<p>Por fim, digite: <code>python manage.py collectstatic</code> para coletar arquivos estáticos (como folhas de estilo, imagens e scripts JavaScript) para a pasta 'static'.</p>

<br>

<p align="center">
    <img src="imgs_tut\terminal_comando_pythonanywhere.png" width="550px" style="margin: auto;">
</p>

<br>

<p>Volte à página inícial da pythonanywhere e vá até a gui "Web".</p>

<br>

<p align="center">
    <img src="imgs_tut\web_pythonanywhere.png" width="550px" style="margin: auto;">
</p>

<br>

<p>Selecione "Add a new app" e em seguide clique em "Next"</p>
<p>Aparecerá uma tela pedindo para selecionar um framework python, clique em "Manual Configuration"</p>
<p>Em seguida selecione a ultima versão do python e clique em "Next".</p>

<div id='run'></div>

## 💻Como Usar a API
