title = input("Digite o titulo: ")
userName = input("Digite o seu nome para aparecer no corpo do arquivo: ")
textInput = input("Digite o seu texto para ser exibido no espaço: ")
htmlString = '''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>''' + title + '''</title>
  <style>
    body {
      display: flex;
      flex-direction: column;
      height: 100vh;
      background: url("https://klondikelubricants.com/wp-content/uploads/2015/06/The-best-top-desktop-space-wallpapers-0n-hd-space-wallpaper-horse-head-nebula.jpeg") no-repeat center;
      background-size: cover;
      align-items: center;
      justify-content: center;
    }
    .instructions {
      margin-bottom: 36px;
      color: #fff;
    }
    .containers {
      display: flex;
      flex-direction: row;
      justify-content: center;
      align-items: center;
      height: 200px;
      width: 100%;
    }
    .divContainer {
      display: flex;
      justify-content: center;
      align-items: center;
      width: 100%;
      max-width: 700px;
      margin: 10px auto;
      padding: 32px;
      background-color: #f4ede8;
    }
    .divContainerTwo {
      flex: 1;
      display: flex;
      justify-content: center;
      align-items: center;
      height: 100px;
      background-color: red;
    }
  </style>
</head>
<body class="container">

  <div class="instructions">
    <h1>Bem vindo, ''' + userName + '''</h1>
    <h1>Clique em qualquer lugar da página para exibir seu texto</h1>
  </div>
  <div class="containers">
    <div class="divContainer"></div>
  </div>

  <script>
    const bodyScript = document.querySelector(".container")
    const divContainer = document.querySelector(".divContainer")
    const divContainerTwo = document.querySelector(".divContainerTwo")
    bodyScript.addEventListener("click", () => {
      divContainer.innerHTML = "''' + textInput + '''"
    });
  </script>

</body>
</html>'''

with open("/home/luiz/projetos/pythonExercises/index.html", 'w') as html:
    html.write(htmlString)