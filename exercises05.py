title = input("Digite o titulo")
htmlString = '''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>''' + title + '''</title>
  <style>
    body {
      width: 100%;
      height: 100%;
      background-color: yellow;
    }
    .divContainer {
      height: 100px;
      width: 100px;
      background-color: green;
    }
  </style>
</head>
<body class="container">

  <div class="divContainer"></div>

  <script>
    const bodyScript = document.querySelector(".container")
    const divContainer = document.querySelector(".divContainer")
    bodyScript.addEventListener("click", () => {
      divContainer.innerHTML = "Teste"
    });
  </script>

</body>
</html>'''

with open("/home/luiz/projetos/pythonExercises/index.html", 'a') as html:
    html.write(htmlString)