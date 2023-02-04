# from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def index(request):
    HTML_CODE = '''
      <!DOCTYPE html>
    <html lang="ru">
    <head>
      <title>Дама сдавала багаж | С.Маршак</title>
      <style>
        body {
          background: #8fbc8f;
          font-family: sans-serif;
        }
        footer, #top-nav {
          background: #893f45;
        }
        .nav-item {
          display: inline-block;
          font-size: 20px;
        }
        .active a {
          color: white;
        }
        .negative {
          color: white;
          background: black;
        }
        #footer-inner {
          font-size: 30px;
        }
      </style>
    </head>
    <body>
      <header>
        <nav id="top-nav">
          <ul>
            <li class="nav-item active">
              <a href="/">Главная страница</a>
            </li>
            <li class="nav-item">
              <a href="about/">О сайте</a>
            </li>
          </ul>
        </nav>
      </header>
      <main>
        <p class="negative">
          Дама сдавала багаж:
        </p>
        <ul>
          <li>Диван,</li>
          <li>Чемодан,</li>
          <li>Саквояж...</li>
        </ul>
      </main>
      <footer>
        <div id="footer-inner">
          Текст в подвале
        </div>
      </footer>
    </body>
    </html>
    '''
    return HttpResponse(HTML_CODE)


def group_posts(request, slug):
    return HttpResponse(f'Посты, отфильтрованные по группам: {slug}')
