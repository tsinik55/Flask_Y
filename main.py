from flask import Flask, url_for, request

app = Flask(__name__)


@app.route('/')  # Это главная страница сайта
@app.route('/index')
def index():
    return 'Admiral<br><a href ="/slogan">slogan</a>'


@app.route('/poster')
def poster():
    return f"""<!DOCTYPE html>
    
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Poster</title>
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@4.6.2/dist/css/bootstrap.min.css" integrity="sha384-xOolHFLEh07PJGoPkLv1IbcEPTNtaed2xpHsD9ESMhqIYd0nLMwNLD69Npy4HI+N" crossorigin="anonymous">
    <link rel="stylesheet" type= "text/css" href="{url_for('static', filename='css/style.css')}">
</head>
<body>
<h1 class="red">Film poster</h1>

<img height ="429" width="417" src="{url_for('static', filename='images/admiral1.png')}"
alt="Здесь должна была быть картинка, но не нашлась">
<p>И крепка, как смерть, любовь</p>
<p class="text-primary">.text-primary</p>
<p class="text-secondary">.text-secondary</p>
<p class="text-success">.text-success</p>
<p class="text-danger">.text-danger</p>

<script src="https://cdn.jsdelivr.net/npm/jquery@3.5.1/dist/jquery.slim.min.js" integrity="sha384-DfXdz2htPH0lsSSs5nCTpuj/zy4C+OGpamoFVy38MVBnE+IbbVYUew+OrCXaRkfj" crossorigin="anonymous"></script>
<script src="https://cdn.jsdelivr.net/npm/bootstrap@4.6.2/dist/js/bootstrap.bundle.min.js" integrity="sha384-Fy6S3B9q64WdZWQUiU+q4/2Lc9npb8tCaSX9FK7E8HnRr0Jz8D6OP9dO5Vg3Q9ct" crossorigin="anonymous"></script>
</body>
</html>
"""


@app.route('/slogan')
def slogan():
    return 'какая то цитата<br><a href ="/">Назад</a>'


@app.route('/countdown')
def countdown():
    lst = [str(x) for x in range(10, 0, -1)]
    lst.append('Start!!!')
    return '<br>'.join(lst)


@app.route('/greeting/<username>')
def freeting(username):
    return f"""<!DOCTYPE html>

<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>{username}</title>
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@4.6.2/dist/css/bootstrap.min.css" integrity="sha384-xOolHFLEh07PJGoPkLv1IbcEPTNtaed2xpHsD9ESMhqIYd0nLMwNLD69Npy4HI+N" crossorigin="anonymous">
    <link rel="stylesheet" type= "text/css" href="{url_for('static', filename='css/style.css')}">
</head>
<body>
<h1 >Привет, {username}</h1>


<script src="https://cdn.jsdelivr.net/npm/jquery@3.5.1/dist/jquery.slim.min.js" integrity="sha384-DfXdz2htPH0lsSSs5nCTpuj/zy4C+OGpamoFVy38MVBnE+IbbVYUew+OrCXaRkfj" crossorigin="anonymous"></script>
<script src="https://cdn.jsdelivr.net/npm/bootstrap@4.6.2/dist/js/bootstrap.bundle.min.js" integrity="sha384-Fy6S3B9q64WdZWQUiU+q4/2Lc9npb8tCaSX9FK7E8HnRr0Jz8D6OP9dO5Vg3Q9ct" crossorigin="anonymous"></script>
</body>
</html>
"""


@app.route('/nekrasov')
def nekrasov():
    return f"""
    <!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Постер</title>
        <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@4.6.2/dist/css/bootstrap.min.css" integrity="sha384-xOolHFLEh07PJGoPkLv1IbcEPTNtaed2xpHsD9ESMhqIYd0nLMwNLD69Npy4HI+N" crossorigin="anonymous">
    <link rel="stylesheet" type= "text/css" href="{url_for('static', filename='css/style.css')}">

    
</head>
<body>

<div class="container text-center">
  <div class="row">
    <div class="col">
  <h1>Постер к фильму</h1>
<img src="{url_for('static', filename='images/nekrasov.png')}"
alt="Здесь должна была быть картинка, но не нашлась">  
    </div>
    <div class="col">
<div class="p-3 mb-2 bg-primary text-white">.bg-primary</div>
<div class="p-3 mb-2 bg-secondary text-white">.bg-secondary</div>
<div class="p-3 mb-2 bg-success text-white">.bg-success</div>
<div class="p-3 mb-2 bg-danger text-white">.bg-danger</div>
<div class="p-3 mb-2 bg-warning text-dark">.bg-warning</div>    
    </div>
  </div>



<script src="https://cdn.jsdelivr.net/npm/jquery@3.5.1/dist/jquery.slim.min.js" integrity="sha384-DfXdz2htPH0lsSSs5nCTpuj/zy4C+OGpamoFVy38MVBnE+IbbVYUew+OrCXaRkfj" crossorigin="anonymous"></script>
<script src="https://cdn.jsdelivr.net/npm/bootstrap@4.6.2/dist/js/bootstrap.bundle.min.js" integrity="sha384-Fy6S3B9q64WdZWQUiU+q4/2Lc9npb8tCaSX9FK7E8HnRr0Jz8D6OP9dO5Vg3Q9ct" crossorigin="anonymous"></script>

</body>
</html>
"""


@app.route('/variants/<int:var>')
def variants(var):
    if var == 1:
        return f"""<!DOCTYPE html>
                <html lang="en">
                <head>
                    <meta charset="UTF-8">
                    <title>{var}</title>
                    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@4.6.2/dist/css/bootstrap.min.css" integrity="sha384-xOolHFLEh07PJGoPkLv1IbcEPTNtaed2xpHsD9ESMhqIYd0nLMwNLD69Npy4HI+N" crossorigin="anonymous">
                    <link rel="stylesheet" type= "text/css" href="{url_for('static', filename='css/style.css')}">
                </head>
                <body>
                <h1 >Привет, {var}</h1>
                <dl>
                  <dt>Режиссер:</dt>
                    <dd>Петр Точилин</dd>
                  <dt>В ролях:</dt>
                    <dd>Андрей Гайдулян</dd>
                    <dd>Алексей Гаврилов</dd>
                    <dd>Виталий Гогунский</dd>
                    <dd>Мария Кожевникова</dd>
                </dl>
                
                <script src="https://cdn.jsdelivr.net/npm/jquery@3.5.1/dist/jquery.slim.min.js" integrity="sha384-DfXdz2htPH0lsSSs5nCTpuj/zy4C+OGpamoFVy38MVBnE+IbbVYUew+OrCXaRkfj" crossorigin="anonymous"></script>
                <script src="https://cdn.jsdelivr.net/npm/bootstrap@4.6.2/dist/js/bootstrap.bundle.min.js" integrity="sha384-Fy6S3B9q64WdZWQUiU+q4/2Lc9npb8tCaSX9FK7E8HnRr0Jz8D6OP9dO5Vg3Q9ct" crossorigin="anonymous"></script>
                </body>
                </html>
"""
    elif var == 2:
        return f"""<!DOCTYPE html>
            <html lang="en">
            <head>
                <meta charset="UTF-8">
                <title>{var}</title>
                <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@4.6.2/dist/css/bootstrap.min.css" integrity="sha384-xOolHFLEh07PJGoPkLv1IbcEPTNtaed2xpHsD9ESMhqIYd0nLMwNLD69Npy4HI+N" crossorigin="anonymous">
                <link rel="stylesheet" type= "text/css" href="{url_for('static', filename='css/style.css')}">
            </head>
            <body>
            <h1 >Привет, {var}</h1>
            <ul>
             <li>Пункт 1.</li>
              <li>Пункт 2.
                <ul>
                  <li>Подпункт 2.1.</li>
                   <li>Подпункт 2.2.     
                    <ul>
                      <li>Подпункт 2.2.1.</li>
                      <li>Подпункт 2.2.2.</li>
                      </ul>
                   </li>          
                  <li>Подпункт 2.3.</li>
                </ul>
              </li>
             <li>Пункт 3.</li>
            </ul>
            
            <script src="https://cdn.jsdelivr.net/npm/jquery@3.5.1/dist/jquery.slim.min.js" integrity="sha384-DfXdz2htPH0lsSSs5nCTpuj/zy4C+OGpamoFVy38MVBnE+IbbVYUew+OrCXaRkfj" crossorigin="anonymous"></script>
            <script src="https://cdn.jsdelivr.net/npm/bootstrap@4.6.2/dist/js/bootstrap.bundle.min.js" integrity="sha384-Fy6S3B9q64WdZWQUiU+q4/2Lc9npb8tCaSX9FK7E8HnRr0Jz8D6OP9dO5Vg3Q9ct" crossorigin="anonymous"></script>
            </body>
            </html>
            """
    else:
        return " не знаю о чем вы"


@app.route('/slideshow')  # карусель
def slideshow():
    return f"""<!DOCTYPE html>

    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>Постер</title>
        <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@4.6.2/dist/css/bootstrap.min.css" integrity="sha384-xOolHFLEh07PJGoPkLv1IbcEPTNtaed2xpHsD9ESMhqIYd0nLMwNLD69Npy4HI+N" crossorigin="anonymous">
        <link rel="stylesheet" type= "text/css" href="{url_for('static', filename='css/style.css')}">
    </head>
    <body>
    
    <div class="container">
  <div class="row">
    <div class="col">
     <div id="carouselExampleControlsNoTouching" class="carousel slide" data-touch="false" data-interval="false">
  <div class="carousel-inner">
    <div class="carousel-item active">
      <img src="{url_for('static', filename='images/foni4.png')}" class="d-block w-100" alt="...">
    </div>
    <div class="carousel-item">
      <img src="{url_for('static', filename='images/foni1.png')}" class="d-block w-100" alt="...">
    </div>
    <div class="carousel-item">
      <img src="{url_for('static', filename='images/foni3.png')}" class="d-block w-100" alt="...">
    </div>
  </div>
  <a class="carousel-control-prev" href="#carouselExampleControlsNoTouching" role="button" data-slide="prev">
    <span class="carousel-control-prev-icon" aria-hidden="true"></span>
    <span class="sr-only">Previous</span>
  </a>
  <a class="carousel-control-next" href="#carouselExampleControlsNoTouching" role="button" data-slide="next">
    <span class="carousel-control-next-icon" aria-hidden="true"></span>
    <span class="sr-only">Next</span>
  </a>
</div>
    </div>
    <div class="col-6">
 <div id="carouselExampleControls" class="carousel slide" data-ride="carousel">
  <div class="carousel-inner">
    <div class="carousel-item active">
      <img src="{url_for('static', filename='images/foni1.png')}" class="d-block w-100" alt="Здесь должна была быть картинка, но не нашлась">
    </div>
    <div class="carousel-item">
      <img src="{url_for('static', filename='images/foni2.png')}" class="d-block w-100" alt="Здесь должна была быть картинка, но не нашлась">
    </div>
    <div class="carousel-item">
      <img src="{url_for('static', filename='images/foni3.png')}" class="d-block w-100" alt="Здесь должна была быть картинка, но не нашлась">
    </div>
  </div>
  <a class="carousel-control-prev" href="#carouselExampleControls" role="button" data-slide="prev">
    <span class="carousel-control-prev-icon" aria-hidden="true"></span>
    <span class="sr-only">Предыдущий</span>
  </a>
  <a class="carousel-control-next" href="#carouselExampleControls" role="button" data-slide="next">
    <span class="carousel-control-next-icon" aria-hidden="true"></span>
    <span class="sr-only">Следующий</span>
  </a>
</div>
    </div>
    <div class="col">
<div id="carouselExampleIndicators" class="carousel slide" data-ride="carousel">
  <ol class="carousel-indicators">
    <li data-target="#carouselExampleIndicators" data-slide-to="0" class="active"></li>
    <li data-target="#carouselExampleIndicators" data-slide-to="1"></li>
    <li data-target="#carouselExampleIndicators" data-slide-to="2"></li>
  </ol>
  <div class="carousel-inner">
    <div class="carousel-item active">
      <img src="{url_for('static', filename='images/foni3.png')}" class="d-block w-100" alt="...">
    </div>
    <div class="carousel-item">
      <img src="{url_for('static', filename='images/foni4.png')}" class="d-block w-100" alt="...">
    </div>
    <div class="carousel-item">
      <img src="{url_for('static', filename='images/foni2.png')}" class="d-block w-100" alt="...">
    </div>
  </div>
  <a class="carousel-control-prev" href="#carouselExampleIndicators" role="button" data-slide="prev">
    <span class="carousel-control-prev-icon" aria-hidden="true"></span>
    <span class="sr-only">Previous</span>
  </a>
  <a class="carousel-control-next" href="#carouselExampleIndicators" role="button" data-slide="next">
    <span class="carousel-control-next-icon" aria-hidden="true"></span>
    <span class="sr-only">Next</span>
  </a>
</div>
    </div>
  </div>
  
    
    
    


    <script src="https://cdn.jsdelivr.net/npm/jquery@3.5.1/dist/jquery.slim.min.js" integrity="sha384-DfXdz2htPH0lsSSs5nCTpuj/zy4C+OGpamoFVy38MVBnE+IbbVYUew+OrCXaRkfj" crossorigin="anonymous"></script>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@4.6.2/dist/js/bootstrap.bundle.min.js" integrity="sha384-Fy6S3B9q64WdZWQUiU+q4/2Lc9npb8tCaSX9FK7E8HnRr0Jz8D6OP9dO5Vg3Q9ct" crossorigin="anonymous"></script>
    </body>
    </html>
    """


@app.route('/form_sample', methods=['GET', 'POST'])
def form_sample():
    if request.method == 'GET':
        return f"""<!DOCTYPE html>

        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <title>Form Example</title>
            <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@4.6.2/dist/css/bootstrap.min.css" integrity="sha384-xOolHFLEh07PJGoPkLv1IbcEPTNtaed2xpHsD9ESMhqIYd0nLMwNLD69Npy4HI+N" crossorigin="anonymous">
            <link rel="stylesheet" type= "text/css" href="{url_for('static', filename='css/style.css')}">
        </head>
        <body>
        <h1> Registration Form </h1>
         <div class="container">
         <form class="login_form" method="post">
         
         <input type="text" class="form-control" name="fname"  placeholder="First name">
          <input type="text" class="form-control" name="sname"  placeholder="Last name"><br>
          <input type="email" class="form-control" name="email" placeholder="name@example.com">
          <input type="password" class="form-control" name="password" placeholder="Password">
          <div class="form-group">
          <label form="classSelect">Select your education</label>
          <select class= "form-control" id="classSelect" name="profession">
                <option selected>High School</option>
                <option>Middle School</option>
          </div>
         <button class="btn btn-primary" type="submit">Submit</button>
          </form>
        
        </select>
        </div>
        <! -- Radio button - Gender selection ->
        <div class = "form group">
            <label for="form-check">Select your gender</label> 
            <div class="form-check">
                <input class = "form-check-input" type = "radio" name="sex" id="male" value="male" checked>
                <label class = "form-check-label" type = for "male">Male</label>
            </div>
            <div class="form-check">
                <input class = "form-check-input" type = "radio" name="sex" id="female" value="female" checked>
                <label class = "form-check-label" type = for "female">Female</label>
            </div>
        </div>
        <! -- End og gender selection -- >
        <! -- Text block -- >
        <div>
            <label for="Information</label>
            <textarea class="form-control" id="about" name="about" rows="3"</textarea>
        </div><br>
        <! -- End of text block -- >
        <! -- Checkbox -- >
        <div>
            
        
        
        
        
            
        
        <script src="https://cdn.jsdelivr.net/npm/jquery@3.5.1/dist/jquery.slim.min.js" integrity="sha384-DfXdz2htPH0lsSSs5nCTpuj/zy4C+OGpamoFVy38MVBnE+IbbVYUew+OrCXaRkfj" crossorigin="anonymous"></script>
        <script src="https://cdn.jsdelivr.net/npm/bootstrap@4.6.2/dist/js/bootstrap.bundle.min.js" integrity="sha384-Fy6S3B9q64WdZWQUiU+q4/2Lc9npb8tCaSX9FK7E8HnRr0Jz8D6OP9dO5Vg3Q9ct" crossorigin="anonymous"></script>
        </body>
        </html>
        """
    elif request.method == 'POST':
        print(request.form['fname'])
        print(request.form['sname'])
        print(request.form['email'])
        print(request.form['password"'])
        return 'The form is sent'


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)
